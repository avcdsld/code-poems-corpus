public static String getLayerNameFromConfig(Map<String, Object> layerConfig,
                                                KerasLayerConfiguration conf)
            throws InvalidKerasConfigurationException {
        Map<String, Object> innerConfig = KerasLayerUtils.getInnerLayerConfigFromConfig(layerConfig, conf);
        if (!innerConfig.containsKey(conf.getLAYER_FIELD_NAME()))
            throw new InvalidKerasConfigurationException("Field " + conf.getLAYER_FIELD_NAME()
                    + " missing from layer config");
        return (String) innerConfig.get(conf.getLAYER_FIELD_NAME());
    }