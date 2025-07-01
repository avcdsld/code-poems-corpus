public static OptimizationConfiguration fromYaml(String json) {
        try {
            return JsonMapper.getYamlMapper().readValue(json, OptimizationConfiguration.class);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }