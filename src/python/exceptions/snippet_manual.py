# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "opentelemetry-api",
#     "opentelemetry-exporter-otlp-proto-grpc",
#     "opentelemetry-sdk",
# ]
# ///

# --8<-- [start:code]
from opentelemetry import trace
from opentelemetry.trace import StatusCode
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter,
)

# Creates a resource and adds it to the tracer provider
resource = Resource.create({"service.name": "recording-exceptions-manual"})
provider = TracerProvider(resource=resource)
trace.set_tracer_provider(provider)

# Adds span processor with the OTLP exporter to the tracer provider
provider.add_span_processor(
    BatchSpanProcessor(
        OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
    )
)

tracer = trace.get_tracer(__name__)


def process_order(
    order_id: str,
    amount: float,
    will_fail: bool = False,
) -> str:
    """
    Processes an order. If will_fail=True, simulates a downstream exception.
    Returns "OK" on success; on failure, it raises the exception.
    """
    with tracer.start_as_current_span("process_order") as span:
        span.set_attribute("order.id", order_id)
        span.set_attribute("order.amount", amount)
        span.add_event("Begin processing order")

        try:
            # deterministic “failure”
            if will_fail:
                raise ConnectionError("Simulated payment failure")

            # success path
            span.add_event("Payment succeeded")
            return "OK"

        except Exception as exc:
            # record and mark error
            span.record_exception(
                exc,
                {
                    "error.type": type(exc).__name__,
                    "error.stage": "payment processing",
                },
            )
            span.set_status(StatusCode.ERROR, f"Payment error: {exc}")
            return f"Failed to process order {order_id}: {exc}"


# deterministic runs:
process_order("ORD-1001", 120.0, will_fail=False)
process_order("ORD-1002", 55.5, will_fail=True)

# --8<-- [end:code]
