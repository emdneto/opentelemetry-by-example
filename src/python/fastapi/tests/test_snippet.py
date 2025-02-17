from snippet_test_utils import SnippetTestBase


class Snippet(SnippetTestBase):
    def test_snippet_zero_code(self):
        spans = self.get_spans("fastapi-uvicorn-zero-code")
        self.assertEqual(len(spans), 3)

        internal_http_send_span = spans[0]
        internal_http_send_response_span = spans[1]
        server_span = spans[2]

        self.assert_span(
            internal_http_send_span,
            span_name="GET /foobar http send",
            kind="INTERNAL",
            attributes={
                "http.status_code": 200,
            },
        )

        self.assert_span(
            internal_http_send_response_span,
            span_name="GET /foobar http send",
            kind="INTERNAL",
            attributes={
                "asgi.event.type": "http.response.body",
            },
        )

        self.assert_span(
            server_span,
            span_name="GET /foobar",
            kind="SERVER",
            scope_name="opentelemetry.instrumentation.fastapi",
            attributes={
                "http.method": "GET",
                "http.status_code": 200,
                "http.target": "/foobar",
                "http.scheme": "http",
            },
        )

        # present_attributes = [
        #     "net.host.name",
        #     "net.peer.port",
        #     "http.user_agent",
        #     "net.peer.ip",
        # ]

        # strict_match_attributes = {
        #     "http.method": "GET",
        #     "http.server_name": "127.0.0.1",
        #     "http.scheme": "http",
        #     "http.host": "localhost:5001",
        #     "net.host.port": 5001,
        #     "http.target": "/rolldice",
        #     "http.flavor": "1.1",
        #     "http.route": "/rolldice",
        #     "http.status_code": 200,
        # }

        # span = spans[0]
        # self.assert_span(
        #     span,
        #     span_name="GET /rolldice",
        #     kind="SERVER",
        #     scope_name="opentelemetry.instrumentation.flask",
        #     attributes=strict_match_attributes,
        # )
        # self.assert_attributes_present(
        #     span.get("attributes", {}), present_attributes
        # )

        # error_attributes = {
        #     "http.method": "GET",
        #     "http.status_code": 404,
        # }

        # span_error = spans[1]
        # self.assert_span(
        #     span_error,
        #     span_name="GET /404",
        #     kind="SERVER",
        #     attributes=error_attributes,
        # )
