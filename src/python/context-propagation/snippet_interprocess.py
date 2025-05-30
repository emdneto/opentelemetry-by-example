# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "opentelemetry-api",
#     "opentelemetry-exporter-otlp-proto-grpc",
#     "opentelemetry-sdk",
#     "requests",
#     "flask",
# ]
# ///

# --8<-- [start:code]
import time
import threading
from typing import Any

import requests
from flask import Flask, jsonify, request
from opentelemetry import trace, propagate
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter,
)

resource = Resource.create(
    {"service.name": "context-propagation-interprocess"}
)
provider = TracerProvider(resource=resource)
trace.set_tracer_provider(provider)

provider.add_span_processor(
    BatchSpanProcessor(
        OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
    )
)

tracer = trace.get_tracer(__name__)

app = Flask(__name__)


@app.route("/api/data", methods=["GET"])
def get_data():
    # Extract context from incoming request headers
    ctx = propagate.extract(request.headers)

    # Start span with extracted context as parent
    with tracer.start_as_current_span("server_operation", context=ctx) as span:
        span.set_attribute("server.endpoint", "/api/data")
        span.add_event("Processing request on server")

        result = {"message": "Hello from server", "data": [1, 2, 3]}

        span.add_event("Request processed successfully")
        return jsonify(result)


def start_server():
    app.run(host="localhost", port=5001, debug=False, use_reloader=False)


def make_http_request() -> dict[str, Any]:
    with tracer.start_as_current_span("client_operation") as span:
        span.set_attribute("client.operation", "fetch_data")
        span.add_event("Making HTTP request")

        headers = {"Content-Type": "application/json"}

        # Inject current span context into headers
        propagate.inject(headers)

        try:
            # Make HTTP request with propagated context
            response = requests.get(
                "http://localhost:5001/api/data", headers=headers
            )

            span.set_attribute("http.status_code", response.status_code)
            span.add_event("HTTP request completed")

            return response.json()
        except Exception as e:
            span.add_event("HTTP request failed", {"error": str(e)})
            return {"error": str(e)}


server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()
time.sleep(2)  # Wait for server to start
make_http_request()
# --8<-- [end:code]
