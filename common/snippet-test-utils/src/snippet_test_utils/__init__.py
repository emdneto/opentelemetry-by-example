import unittest
import requests
import time
from typing import List, Dict, Any, Optional


def get_telemetry_from_sink() -> dict[str, list[dict[str, Any]]]:
    url = "http://localhost:8080/telemetry"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_telemetry(
    signal: str, service_name: str, retries: int = 5, backoff_factor: float = 1.25
):
    attempt = 0
    telemetry = []
    while attempt < retries:
        data = get_telemetry_from_sink()
        telemetry = [
            telemetry
            for telemetry in data.get(signal, [])
            if telemetry.get("resource", {}).get("attributes", {}).get("service.name")
            == service_name
        ]

        if telemetry:
            return telemetry

        attempt += 1
        sleep_time = backoff_factor**attempt
        print(
            f"No telemetry found for service '{service_name}'. Retrying in {sleep_time:.2f} seconds..."
        )
        time.sleep(sleep_time)
    raise TimeoutError(
        f"Unable to retrieve {signal} for service '{service_name}' after {retries} retries."
    )


class SnippetTestBase(unittest.TestCase):
    def get_spans(self, service_name: str):
        return get_telemetry("traces", service_name)

    def get_metrics(self, service_name: str):
        return get_telemetry("metrics", service_name)

    def get_logs(self, service_name: str):
        return get_telemetry("logs", service_name)

    def assert_span(
        self, span: dict[str, Any], span_name: str, attributes: dict[str, Any] | None = None
    ):
        self.assertEqual(
            span.get("name"),
            span_name,
            f"Span '{span_name}' not found in telemetry data.",
        )
        self.assertDictEqual(span.get("attributes", {}), attributes)
