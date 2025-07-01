@Singleton
    @Primary
    @Requires(classes = JaegerTracer.Builder.class)
    Tracer jaegerTracer(JaegerTracer.Builder tracerBuilder) {
        Tracer tracer = tracerBuilder.build();
        if (!GlobalTracer.isRegistered()) {
            GlobalTracer.register(tracer);
        }
        return tracer;
    }