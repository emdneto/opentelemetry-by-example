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
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter,
)
import time

resource = Resource.create({"service.name": "context-propagation-intraprocess"})
provider = TracerProvider(resource=resource)
trace.set_tracer_provider(provider)

provider.add_span_processor(
    BatchSpanProcessor(
        OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
    )
)

tracer = trace.get_tracer(__name__)

def fetch_data(item_id: str) -> dict:
    with tracer.start_as_current_span("fetch_data") as span:
        span.set_attribute("item.id", item_id)
        time.sleep(0.1)
        with tracer.start_as_current_span("fetch_data_inner") as inner_span:
            inner_span.set_attribute("inner.operation", "fetching")
            time.sleep(0.05)
        return {"id": item_id, "data": "example"}

def validate_data(data: dict) -> bool:
    with tracer.start_as_current_span("validate_data") as span:
        span.set_attribute("validation.result", True)
        time.sleep(0.05)
        with tracer.start_as_current_span("validate_data_inner") as inner_span:
            inner_span.set_attribute("inner.operation", "validating")
            time.sleep(0.02)
        return True

def process_request(request_id: str) -> dict:
    """Parent function - creates root span"""
    with tracer.start_as_current_span("process_request") as span:
        span.set_attribute("request.id", request_id)

        # These calls automatically create child spans
        data = fetch_data(request_id)
        is_valid = validate_data(data)

        if is_valid:
            span.set_attribute("status", "success")
            return {"status": "processed", "data": data}
        else:
            span.set_attribute("status", "failed")
            return {"status": "failed"}

process_request("req-001")
process_request("req-002")
# --8<-- [end:code]
