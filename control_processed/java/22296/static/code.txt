private void initFromSPIServiceLoader() {

        String property = System.getProperty("druid.load.spifilter.skip");
        if (property != null) {
            return;
        }

        ServiceLoader<Filter> druidAutoFilterLoader = ServiceLoader.load(Filter.class);

        for (Filter autoFilter : druidAutoFilterLoader) {
            AutoLoad autoLoad = autoFilter.getClass().getAnnotation(AutoLoad.class);
            if (autoLoad != null && autoLoad.value()) {
                if (LOG.isInfoEnabled()) {
                    LOG.info("load filter from spi :" + autoFilter.getClass().getName());
                }
                addFilter(autoFilter);
            }
        }
    }