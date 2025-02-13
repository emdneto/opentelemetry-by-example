import unittest
import requests
import time
from typing import Any, Callable

TelemetryItemT = dict[str, Any]


def get_telemetry_from_backend() -> dict[str, Any]:
    url = "http://localhost:8080/telemetry"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def retry_with_backoff(
    fetch: Callable[[], list[TelemetryItemT]],
    retries: int = 6,
    backoff_factor: float = 1.25,
) -> list[TelemetryItemT]:
    for attempt in range(1, retries + 1):
        items = fetch()
        if items:
            return items
        sleep_time = backoff_factor ** attempt
        print(f"No data found. Retrying... (Attempt {attempt}/{retries}) Waiting {sleep_time:.2f}s")
        time.sleep(sleep_time)
    raise TimeoutError(f"Unable to get items after {retries} retries.")


def filter_by_service_name(items: list[TelemetryItemT], service_name: str) -> list[TelemetryItemT]:
    return [
        item for item in items
        if item.get("resource", {}).get("attributes", {}).get("service.name") == service_name
    ]


def get_telemetry(
    signal: str,
    service_name: str,
    retries: int = 5,
    backoff_factor: float = 1.25
) -> list[TelemetryItemT]:

    def fetch() -> list[TelemetryItemT]:
        data = get_telemetry_from_backend()
        return filter_by_service_name(data.get(signal, []), service_name)

    return retry_with_backoff(
        fetch=fetch,
        retries=retries,
        backoff_factor=backoff_factor,
    )

class SnippetTestBase(unittest.TestCase):
    """
    Base test class providing helper methods for retrieving spans, metrics,
    and logs, and asserting their properties. This is installed by default
    in all envirioments.
    """

    def get_spans(self, service_name: str) -> list[TelemetryItemT]:
        return get_telemetry("traces", service_name)

    def get_metrics(self, service_name: str) -> list[TelemetryItemT]:
        return get_telemetry("metrics", service_name)

    def get_logs(self, service_name: str) -> list[TelemetryItemT]:
        return get_telemetry("logs", service_name)

    def assert_span(
        self,
        span: TelemetryItemT,
        span_name: str,
        kind: str,
        scope_name: str | None = None,
        attributes: dict[str, Any] | None = None,
    ) -> None:
        self.assertEqual(
            span.get("name"),
            span_name,
            f"Span '{span_name}' not found in telemetry data."
        )

        self.assertIn(
            kind,
            span.get("kind", ""),
            f"Span kind mismatch. Expected '{kind}', got '{span.get('kind')}'."
        )

        if scope_name is not None:
            scope = span.get("scope", {})
            self.assertEqual(
                scope.get("name", ""),
                scope_name,
                f"Scope name mismatch. Expected '{scope_name}', got '{scope.get('name')}'."
            )

        if attributes is not None:
            self.assert_attributes_strict(span.get("attributes", {}), attributes)

    def assert_attributes_strict(
        self,
        actual_attrs: dict[str, Any],
        expected_attrs: dict[str, Any]
    ) -> None:
        for key, value in expected_attrs.items():
            self.assertIn(
                key,
                actual_attrs,
                f"Attribute '{key}' not found in {actual_attrs}."
            )
            self.assertEqual(
                actual_attrs[key],
                value,
                f"Attribute '{key}' value mismatch. Expected '{value}', got '{actual_attrs[key]}'."
            )

    def assert_attributes_present(
        self,
        actual_attrs: dict[str, Any],
        expected_keys: list[str]
    ) -> None:
        for key in expected_keys:
            self.assertIn(
                key,
                actual_attrs,
                f"Attribute '{key}' not found. Existing attributes: {list(actual_attrs.keys())}"
            )
