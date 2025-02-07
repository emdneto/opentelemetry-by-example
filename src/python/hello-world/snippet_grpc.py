from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

# Creates a resource and adds it to the tracer provider
resource = Resource.create({"service.name": "hello-world-otlp-grpc"})
provider = TracerProvider(resource=resource)
trace.set_tracer_provider(provider)

# Adds span processor with the OTLP exporter to the tracer provider
provider.add_span_processor(SimpleSpanProcessor(OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)))

tracer = trace.get_tracer(__name__, attributes={"scope": "foo"})

# Starts and sets an attribute to a span
with tracer.start_as_current_span("HelloWorldSpanGrpc") as span:
    span.set_attribute("foo", "grpc")
    print("Hello world")
