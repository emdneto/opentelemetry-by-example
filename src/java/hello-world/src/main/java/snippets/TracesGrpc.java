package snippets;

import io.opentelemetry.api.GlobalOpenTelemetry;
import io.opentelemetry.api.common.Attributes;
import io.opentelemetry.api.trace.Span;
import io.opentelemetry.api.trace.Tracer;
import io.opentelemetry.exporter.otlp.trace.OtlpGrpcSpanExporter;
import io.opentelemetry.sdk.OpenTelemetrySdk;
import io.opentelemetry.sdk.resources.Resource;
import io.opentelemetry.sdk.trace.SdkTracerProvider;
import io.opentelemetry.sdk.trace.export.SimpleSpanProcessor;
import io.opentelemetry.semconv.ResourceAttributes;

public class TracesGrpc {
  private static final String SERVICE_NAME = "java.hello-world.TracesGrpc";

  public static void main(String[] args) throws InterruptedException {
    OtlpGrpcSpanExporter spanExporter =
        OtlpGrpcSpanExporter.builder().setEndpoint("http://localhost:4317").build();

    // Builds the Tracer Provider with span processor and resource attribute
    SdkTracerProvider tracerProvider =
        SdkTracerProvider.builder()
            .addSpanProcessor(SimpleSpanProcessor.create(spanExporter))
            .setResource(
                Resource.create(Attributes.of(ResourceAttributes.SERVICE_NAME, SERVICE_NAME)))
            .build();

    // Sets and registers the Tracer Provider as Global
    OpenTelemetrySdk.builder().setTracerProvider(tracerProvider).buildAndRegisterGlobal();

    // Creates the tracer
    Tracer tracer = GlobalOpenTelemetry.getTracer(SERVICE_NAME);

    // Creates a span, set its attributes and finishes it
    Span span = tracer.spanBuilder("HelloWorldSpanGrpc").startSpan();
    span.setAttribute("foo", "grpc");
    span.end();

    //  Print something to console
    System.out.println("Hello, World!");

    // Waits for things to settle and shuts the Trace Provider down right before finishing the app
    Thread.sleep(2000);
    tracerProvider.shutdown();
  }
}
