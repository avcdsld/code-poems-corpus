private Object put(String name, Class<?> beanClass, boolean isSingleton) {
        BeanDefine beanDefine = this.createBeanDefine(beanClass, isSingleton);

        if (pool.put(name, beanDefine) != null) {
            log.warn("Duplicated Bean: {}", name);
        }

        // add interface、put to pool
        Class<?>[] interfaces = beanClass.getInterfaces();
        if (interfaces.length > 0) {
            for (Class<?> interfaceClazz : interfaces) {
                if (null != this.getBean(interfaceClazz)) {
                    break;
                }
                this.put(interfaceClazz.getName(), beanDefine);
            }
        }

        return Objects.requireNonNull(beanDefine).getBean();
    }