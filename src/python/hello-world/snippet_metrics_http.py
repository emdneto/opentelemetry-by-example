# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "opentelemetry-api",
#     "opentelemetry-exporter-otlp-proto-grpc",
#     "opentelemetry-exporter-otlp-proto-http",
#     "opentelemetry-sdk",
# ]
# ///
# --8<-- [start:code]
import time
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter

# Creates a resource and adds it to the meter provider
resource = Resource.create({"service.name": "hello-world-otlp-http"})
metric_reader = PeriodicExportingMetricReader(
    exporter=OTLPMetricExporter(endpoint="http://localhost:4318/v1/metrics"),
    export_interval_millis=1000,  # Export every 1 second for demo
)
provider = MeterProvider(resource=resource, metric_readers=[metric_reader])
metrics.set_meter_provider(provider)

meter = metrics.get_meter(__name__)

# Create different metric instruments
request_counter = meter.create_counter(
    name="hello_requests_total",
    description="Total number of hello requests",
    unit="1",
)

response_time_histogram = meter.create_histogram(
    name="hello_request_duration_seconds",
    description="Hello request duration in seconds",
    unit="s",
)

active_users_gauge = meter.create_up_down_counter(
    name="hello_active_users",
    description="Number of active users",
    unit="1",
)

request_counter.add(1, {"method": "POST", "endpoint": "/hello", "transport": "http"})
response_time_histogram.record(0.1, {"method": "POST", "endpoint": "/hello", "transport": "http"})
active_users_gauge.add(1, {"region": "us-west", "transport": "http"})
# --8<-- [end:code]
