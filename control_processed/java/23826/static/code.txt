public static synchronized Registry getRegistry(RegistryConfig registryConfig) {
        if (ALL_REGISTRIES.size() > 3) { // 超过3次 是不是配错了？
            if (LOGGER.isWarnEnabled()) {
                LOGGER.warn("Size of registry is greater than 3, Please check it!");
            }
        }
        try {
            // 注意：RegistryConfig重写了equals方法，如果多个RegistryConfig属性一样，则认为是一个对象
            Registry registry = ALL_REGISTRIES.get(registryConfig);
            if (registry == null) {
                ExtensionClass<Registry> ext = ExtensionLoaderFactory.getExtensionLoader(Registry.class)
                    .getExtensionClass(registryConfig.getProtocol());
                if (ext == null) {
                    throw ExceptionUtils.buildRuntime("registry.protocol", registryConfig.getProtocol(),
                        "Unsupported protocol of registry config !");
                }
                registry = ext.getExtInstance(new Class[] { RegistryConfig.class }, new Object[] { registryConfig });
                ALL_REGISTRIES.put(registryConfig, registry);
            }
            return registry;
        } catch (SofaRpcRuntimeException e) {
            throw e;
        } catch (Throwable e) {
            throw new SofaRpcRuntimeException(e.getMessage(), e);
        }
    }