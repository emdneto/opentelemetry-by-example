from snippet_test_utils import SnippetTestBase


class Snippet(SnippetTestBase):
    def test_snippet(self):
        spans = self.get_spans("snippet")
        self.assertEqual(len(spans), 1)
        self.assert_span(
            spans[0],
            span_name="all-instrumentation-install",
            kind="SPAN_KIND_INTERNAL",
            attributes={"foo": "bar"},
            scope_name="snippet",
            scope_attributes={"domain": "foo"},
        )
        self.assertEqual(spans[0]["events"][0]["name"], "event in span")
