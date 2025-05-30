from snippet_test_utils import SnippetTestBase


class BaseTestCase(SnippetTestBase):
    def test_traces_grpc(self):
        spans = self.get_spans("hello-world-otlp-grpc")
        self.assertEqual(len(spans), 1)
        self.assert_span(
            spans[0],
            span_name="HelloWorldSpanGrpc",
            kind="INTERNAL",
            attributes={"foo": "grpc"},
        )

    def test_traces_http(self):
        spans = self.get_spans("hello-world-otlp-http")
        self.assertEqual(len(spans), 1)
        self.assert_span(
            spans[0],
            span_name="HelloWorldSpanHttp",
            kind="INTERNAL",
            attributes={"foo": "http"},
        )

    def test_metrics_grpc(self):
        metrics = self.get_metrics("hello-world-otlp-grpc")
        # We expect 3 different metric types: counter, histogram, and up-down counter
        self.assertEqual(len(metrics), 3)

        # Check for the presence of our specific metrics
        metric_names = [metric.get("name", "") for metric in metrics]
        self.assertIn("hello_requests_total", metric_names)
        self.assertIn("hello_request_duration_seconds", metric_names)
        self.assertIn("hello_active_users", metric_names)

    def test_metrics_http(self):
        metrics = self.get_metrics("hello-world-otlp-http")
        self.assertEqual(len(metrics), 3)

        metric_names = [metric.get("name", "") for metric in metrics]
        self.assertIn("hello_requests_total", metric_names)
        self.assertIn("hello_request_duration_seconds", metric_names)
        self.assertIn("hello_active_users", metric_names)
