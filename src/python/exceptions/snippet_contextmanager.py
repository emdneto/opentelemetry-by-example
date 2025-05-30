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
from opentelemetry.trace import Status, StatusCode

# Creates a resource and adds it to the tracer provider
resource = Resource.create({"service.name": "recording-exceptions-contextmanager"})
provider = TracerProvider(resource=resource)
trace.set_tracer_provider(provider)

# Adds span processor with the OTLP exporter to the tracer provider
provider.add_span_processor(
    BatchSpanProcessor(
        OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
    )
)

tracer = trace.get_tracer(__name__)

# Simulates an operation that fail to demonstrate how to record exceptions
with tracer.start_as_current_span("risky_operation_grpc") as span:
    try:
        raise ValueError("Something went wrong in gRPC operation!")
    except Exception as e:
        pass
# --8<-- [end:code]
