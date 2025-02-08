from flask import Flask, jsonify
from oteltest.sink import GrpcSink
from oteltest.sink.handler import AccumulatingHandler
import threading
import logging
from sink.utils import parse_telemetry

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

handler = AccumulatingHandler()

app = Flask(__name__)


@app.route("/telemetry", methods=["GET"])
def get_telemetry():
    try:
        # return _handler.telemetry_to_json(), 200
        return parse_telemetry(handler.telemetry.to_dict()), 200
    except Exception as e:
        _logger.error(f"Error retrieving telemetry data: {e}", exc_info=True)
        return jsonify({"error": str(e)}), 500


def run_sink():
    threading.Thread(
        target=app.run, kwargs={"host": "0.0.0.0", "port": 8080}, daemon=False
    ).start()
    sink = GrpcSink(handler, _logger, port=4319)
    sink.start()
    sink.wait_for_termination()
