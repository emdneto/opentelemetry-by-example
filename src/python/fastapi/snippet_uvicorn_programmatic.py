# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "fastapi",
#     "opentelemetry-api",
#     "opentelemetry-sdk",
#     "opentelemetry-distro",
#     "opentelemetry-instrumentation",
#     "opentelemetry-exporter-otlp",
#     "uvicorn",
#     "opentelemetry-instrumentation-fastapi",
#     "opentelemetry-instrumentation-asgi",
#     "opentelemetry-util-http",
#     "opentelemetry-semantic-conventions",
# ]
# ///

# --8<-- [start:code]
from opentelemetry.instrumentation import auto_instrumentation
auto_instrumentation.initialize() # Need to initialize first before importing FastAPI

from fastapi import FastAPI
import uvicorn
import requests
from opentelemetry.trace import get_tracer

tracer = get_tracer(__name__)

app = FastAPI()

@app.get("/foobar")
async def root():
    with tracer.start_as_current_span("foobar_span") as span:
        span.set_attribute("endpoint", "/foobar")
        span.add_event("Handling request to /foobar")
        # Simulate some processing
        requests.get("http://httpbin.org/get?hello=world")
    return {"message": "Hello World"}

uvicorn.run(app, host="0.0.0.0", port=3000)
# --8<-- [end:code]
