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
    and logs, and asserting their properties.
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

# import unittest
# import requests
# import time
# from typing import Any, TypedDict, TypeVar, Callable

# def get_telemetry_from_backend():
#     url = "http://localhost:8080/telemetry"
#     response = requests.get(url)
#     response.raise_for_status()
#     return response.json()

# T = TypeVar("T")

# def retry_with_backoff(
#     fetch: Callable[[], list[T]],
#     retries: int = 5,
#     backoff_factor: float = 1.25,
#     not_found_msg: str = "No items found. Retrying..."
# ) -> list[T]:
#     attempt = 0
#     while attempt < retries:
#         items = fetch()
#         if items:
#             return items
#         attempt += 1
#         sleep_time = backoff_factor ** attempt
#         print(f"{not_found_msg} (Attempt {attempt}/{retries}) Waiting {sleep_time:.2f}s")
#         time.sleep(sleep_time)

#     raise TimeoutError(f"Unable to get items after {retries} retries.")

# def filter_by_service_name(items: list[T], service_name: str) -> list[T]:
#     return [
#         item for item in items
#         if item.get("resource", {}).get("attributes", {}).get("service.name") == service_name
#     ]


# def get_spans_from_backend(
#     service_name: str,
#     retries: int = 5,
#     backoff_factor: float = 1.25
# ) -> list[T]:

#     def fetch_spans() -> list[T]:
#         data = get_telemetry_from_backend()
#         return filter_by_service_name(data.get("traces", []), service_name)

#     return retry_with_backoff(
#         fetch=fetch_spans,
#         retries=retries,
#         backoff_factor=backoff_factor,
#         not_found_msg=f"No spans found for service '{service_name}'. Retrying..."
#     )

# def get_metrics_from_backend(
#     service_name: str,
#     retries: int = 5,
#     backoff_factor: float = 1.25
# ) -> list[T]:

#     def fetch_metrics() -> list[T]:
#         data = get_telemetry_from_backend()
#         return filter_by_service_name(data.get("metrics", []), service_name)

#     return retry_with_backoff(
#         fetch=fetch_metrics,
#         retries=retries,
#         backoff_factor=backoff_factor,
#         not_found_msg=f"No metrics found for service '{service_name}'. Retrying..."
#     )

# def get_logs_from_backend(
#     service_name: str,
#     retries: int = 5,
#     backoff_factor: float = 1.25
# ) -> list[T]:

#     def fetch_logs() -> list[T]:
#         data = get_telemetry_from_backend()
#         return filter_by_service_name(data.get("logs", []), service_name)

#     return retry_with_backoff(
#         fetch=fetch_logs,
#         retries=retries,
#         backoff_factor=backoff_factor,
#         not_found_msg=f"No logs found for service '{service_name}'. Retrying..."
#     )
# class SnippetTestBase(unittest.TestCase):
#     """
#     Base test class providing helper methods for retrieving spans, metrics,
#     and logs, and asserting their properties.
#     """

#     def get_spans(self, service_name: str) -> list[T]:
#         return get_spans_from_backend(service_name)

#     def get_metrics(self, service_name: str) -> list[T]:
#         return get_metrics_from_backend(service_name)

#     def get_logs(self, service_name: str) -> list[T]:
#         return get_logs_from_backend(service_name)

#     def assert_span(
#         self,
#         span: T,
#         span_name: str,
#         kind: str,
#         scope_name: str | None = None,
#         attributes: dict[str, Any] | None = None,
#     ) -> None:
#         self.assertEqual(
#             span.get("name"),
#             span_name,
#             f"Span '{span_name}' not found in telemetry data."
#         )

#         self.assertIn(
#             kind,
#             span.get("kind", ""),
#             f"Span kind mismatch. Expected '{kind}', got '{span.get('kind')}'."
#         )

#         if scope_name is not None:
#             scope = span.get("scope", {})
#             name = scope.get("name", "")
#             self.assertEqual(
#                 name,
#                 scope_name,
#                 f"Scope name mismatch. Expected '{scope_name}', got '{span.get('scope', {}).get('name')}'."
#             )

#         if attributes is not None:
#             self.assert_attributes_strict(span.get("attributes", {}), attributes)

#     def assert_attributes_strict(
#         self,
#         actual_attrs: dict[str, Any],
#         expected_attrs: dict[str, Any]
#     ) -> None:
#         """
#         Test all expected attributes strict match by key/value.
#         """
#         for key, value in expected_attrs.items():
#             self.assertIn(
#                 key,
#                 actual_attrs,
#                 f"Attribute '{key}' not found in {actual_attrs}."
#             )
#             self.assertEqual(
#                 actual_attrs[key],
#                 value,
#                 f"Attribute '{key}' value mismatch. "
#                 f"Expected '{value}', got '{actual_attrs[key]}'."
#             )

#     def assert_attributes_present(
#         self,
#         actual_attrs: dict[str, Any],
#         expected_keys: list[str]
#     ) -> None:
#         """
#         Test that all specified attribute keys exist
#         """
#         for key in expected_keys:
#             self.assertIn(
#                 key,
#                 actual_attrs,
#                 f"Attribute '{key}' not found. "
#                 f"Existing attributes: {list(actual_attrs.keys())}"
#             )
