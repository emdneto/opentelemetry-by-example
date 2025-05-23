from snippet_test_utils import SnippetTestBase


class Snippet(SnippetTestBase):
    def test_snippet_manual(self):
        spans = self.get_spans("snippet-manual")
        self.assertEqual(len(spans), 1)
        self.assert_span(
            spans[0],
            span_name="GET",
            kind="SPAN_KIND_CLIENT",
            attributes={
                "http.method": "GET",
                "http.status_code": 200,
                "http.url": "https://www.example.org/",
            },
        )

    def test_snippet_zerocode(self):
        spans = self.get_spans("snippet-zerocode")
        self.assertEqual(len(spans), 1)
        self.assert_span(
            spans[0],
            span_name="GET",
            kind="SPAN_KIND_CLIENT",
            attributes={
                "http.method": "GET",
                "http.status_code": 200,
                "http.url": "https://www.example.org/",
            },
        )

    def test_snippet_zerocode_stable_semconv(self):
        spans = self.get_spans("snippet-zerocode-stable-semconv")
        self.assertEqual(len(spans), 1)
        self.assert_span(
            spans[0],
            span_name="GET",
            kind="SPAN_KIND_CLIENT",
            attributes={
                "http.request.method": "GET",
                "http.response.status_code": 200,
                "url.full": "https://www.example.org/",
                "network.protocol.version": "1.1",
                "network.peer.address": "www.example.org",
                "server.address": "www.example.org",
            },
        )
