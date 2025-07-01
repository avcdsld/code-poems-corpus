public static UserExecutorConfiguration of(ExecutorType type, int num) {
        ArgumentUtils.check("type", type).notNull();
        UserExecutorConfiguration configuration = of(type);
        configuration.type = type;
        switch (type) {
            case FIXED:
                configuration.nThreads = num;
                break;
            case SCHEDULED:
                configuration.corePoolSize = num;
                break;
            case WORK_STEALING:
                configuration.parallelism = num;
                break;
            default:
        }
        return configuration;
    }