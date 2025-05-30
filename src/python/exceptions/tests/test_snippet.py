from snippet_test_utils import SnippetTestBase


class BaseTestCase(SnippetTestBase):
    def test_snippet_manual(self):
        spans = self.get_spans("recording-exceptions-manual")
        # We should have 2 spans - one successful and one failed
        self.assertEqual(len(spans), 2)

        # Find successful span - should have order.id = "ORD-1001"
        successful_span = next(
            span
            for span in spans
            if span.get("attributes", {}).get("order.id") == "ORD-1001"
        )
        self.assert_span(
            successful_span,
            span_name="process_order",
            kind="INTERNAL",
            attributes={"order.id": "ORD-1001", "order.amount": 120.0},
        )
        # Check that status is OK
        print(successful_span)
        self.assertEqual(successful_span.get("status", {}).get("code"), None)

        # Find failed span - should have order.id = "ORD-1002"
        failed_span = next(
            span
            for span in spans
            if span.get("attributes", {}).get("order.id") == "ORD-1002"
        )
        self.assert_span(
            failed_span,
            span_name="process_order",
            kind="INTERNAL",
            attributes={"order.id": "ORD-1002", "order.amount": 55.5},
        )
        # Check that status is ERROR
        self.assertEqual(
            failed_span.get("status", {}).get("code"), "STATUS_CODE_ERROR"
        )
        self.assertIn(
            "Payment error:", failed_span.get("status", {}).get("message", "")
        )

        # Check for exception events with additional attributes
        events = failed_span.get("events", [])
        exception_events = [
            event for event in events if event.get("name") == "exception"
        ]
        self.assertGreaterEqual(
            len(exception_events),
            1,
            "Should have at least one exception event",
        )

        exception_event = exception_events[0]
        exception_attributes = exception_event.get("attributes", {})

        # Verify standard exception attributes
        self.assertIn("exception.message", exception_attributes)
        self.assertIn("exception.type", exception_attributes)
        self.assertIn("exception.stacktrace", exception_attributes)

        # Verify additional custom attributes from snippet_manual.py
        self.assertEqual(
            "ConnectionError", exception_attributes.get("error.type")
        )
        self.assertEqual(
            "payment processing", exception_attributes.get("error.stage")
        )
