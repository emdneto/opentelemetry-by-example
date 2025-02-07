import base64


def parse_telemetry(data):
    return {
        "metrics": parse_metric_requests(data.get("metric_requests", [])),
        "traces": parse_trace_requests(data.get("trace_requests", [])),
        "logs": parse_log_requests(data.get("log_requests", [])),
    }


def parse_metric_requests(metric_requests):
    return metric_requests


def parse_trace_requests(trace_requests):
    traces = []
    for request in trace_requests:
        pbreq = request.get("pbreq", {})
        resource_spans = pbreq.get("resourceSpans", [])

        for resource_span in resource_spans:
            resource = resource_span.get("resource", {})
            resource_attributes = parse_attributes(resource.get("attributes", []))
            scope_spans = resource_span.get("scopeSpans", [])

            for scope_span in scope_spans:
                scope = scope_span.get("scope", {})
                spans = scope_span.get("spans", [])

                for span in spans:
                    traces.append(
                        {
                            "trace_id": decode_base64(span.get("traceId")),
                            "span_id": decode_base64(span.get("spanId")),
                            "parent_id": decode_base64(span.get("parentSpanId")),
                            "name": span.get("name"),
                            "kind": span.get("kind"),
                            "start_time": span.get("startTimeUnixNano"),
                            "end_time": span.get("endTimeUnixNano"),
                            "attributes": parse_attributes(span.get("attributes", [])),
                            "resource": {"attributes": resource_attributes},
                            "events": span.get("events", []),
                            "links": span.get("links", []),
                            "scope": scope,
                        }
                    )
    return traces


def parse_log_requests(log_requests):
    """Placeholder function for log requests."""
    return log_requests  # Customize as needed based on your log structure


def parse_attributes(attributes):
    parsed_attributes = {}
    for attr in attributes:
        key = attr.get("key")
        value = parse_value(attr.get("value", {}))
        parsed_attributes[key] = value
    return parsed_attributes


def parse_value(value):
    if "stringValue" in value:
        return value["stringValue"]
    elif "intValue" in value:
        return int(value["intValue"])
    elif "doubleValue" in value:
        return float(value["doubleValue"])
    elif "boolValue" in value:
        return bool(value["boolValue"])
    return None


def decode_base64(encoded: str) -> str:
    try:
        return base64.b64decode(encoded).hex()
    except Exception:
        return encoded
