from opentelemetry import trace

tracer = trace.get_tracer(__name__, attributes={"domain": "foo"})

with tracer.start_as_current_span("all-instrumentation-install") as span:
    span.set_attribute("foo", "bar")
    span.add_event("event in span")
    print("Hello world")
