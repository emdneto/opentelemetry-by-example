import requests
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter,
)

# Creates a resource and adds it to the tracer provider
resource = Resource.create({"service.name": "snippet-manual"})
provider = TracerProvider(resource=resource)
trace.set_tracer_provider(provider)

# Adds span processor with the OTLP exporter to the tracer provider
provider.add_span_processor(
    BatchSpanProcessor(
        OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
    )
)

# You can optionally pass a custom TracerProvider to instrument().
RequestsInstrumentor().instrument()
response = requests.get(url="https://www.example.org/")
