public static void init() {
        String tracerClassName = System.getProperty(OPENTRACING_TRACER_CLASS_NAME);
        Preconditions.checkNotNull(tracerClassName, "Can not find opentracing tracer implementation class via system property `%s`", OPENTRACING_TRACER_CLASS_NAME);
        try {
            init((Tracer) Class.forName(tracerClassName).newInstance());
        } catch (final ReflectiveOperationException ex) {
            throw new ShardingException("Initialize opentracing tracer class failure.", ex);
        }
    }