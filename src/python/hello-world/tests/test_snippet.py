from snippet_test_utils import SnippetTestBase


class BaseTestCase(SnippetTestBase):
    def test_snippet_grpc(self):
        spans = self.get_spans("hello-world-otlp-grpc")
        self.assertEqual(len(spans), 1)
        self.assert_span(
            spans[0],
            span_name="HelloWorldSpanGrpc",
            kind="INTERNAL",
            attributes={"foo": "grpc"},
        )

    def test_snippet_http(self):
        spans = self.get_spans("hello-world-otlp-http")
        self.assertEqual(len(spans), 1)
        self.assert_span(
            spans[0],
            span_name="HelloWorldSpanHttp",
            kind="INTERNAL",
            attributes={"foo": "http"},
        )
