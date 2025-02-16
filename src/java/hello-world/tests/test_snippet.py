from snippet_test_utils import SnippetTestBase


class BaseTestCase(SnippetTestBase):
    def test_snippet_grpc(self):
        spans = self.get_spans("java.hello-world.TracesGrpc")
        self.assertEqual(len(spans), 1)
        self.assert_span(
            spans[0],
            span_name="HelloWorldSpanGrpc",
            kind="INTERNAL",
            attributes={"foo": "grpc"},
        )
