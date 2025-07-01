public static HystrixCollapserProperties.Setter initializeCollapserProperties(List<HystrixProperty> properties) {
        return initializeProperties(HystrixCollapserProperties.Setter(), properties, COLLAPSER_PROP_MAP, "collapser");
    }