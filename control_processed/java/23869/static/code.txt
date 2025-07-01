public static Cluster getCluster(ConsumerBootstrap consumerBootstrap) {
        try {
            ConsumerConfig consumerConfig = consumerBootstrap.getConsumerConfig();
            ExtensionClass<Cluster> ext = ExtensionLoaderFactory.getExtensionLoader(Cluster.class)
                .getExtensionClass(consumerConfig.getCluster());
            if (ext == null) {
                throw ExceptionUtils.buildRuntime("consumer.cluster",
                    consumerConfig.getCluster(), "Unsupported cluster of client!");
            }
            return ext.getExtInstance(new Class[] { ConsumerBootstrap.class },
                new Object[] { consumerBootstrap });
        } catch (SofaRpcRuntimeException e) {
            throw e;
        } catch (Throwable e) {
            throw new SofaRpcRuntimeException(e.getMessage(), e);
        }
    }