public List<PluginWrapper> getPlugins(Class<? extends Plugin> pluginSuperclass) {
        List<PluginWrapper> result = new ArrayList<>();
        for (PluginWrapper p : getPlugins()) {
            if(pluginSuperclass.isInstance(p.getPlugin()))
                result.add(p);
        }
        return Collections.unmodifiableList(result);
    }