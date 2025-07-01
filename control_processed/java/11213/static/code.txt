public EnvVars overrideAll(Map<String,String> all) {
        for (Map.Entry<String, String> e : all.entrySet()) {
            override(e.getKey(),e.getValue());
        }
        return this;
    }