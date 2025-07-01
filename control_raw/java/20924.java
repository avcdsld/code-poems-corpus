public static void loadedPlugin(AbstractPlugin plugin) {
        if (!isPluginLoadedImpl(plugin)) {
            checkPluginId(plugin);
            getLoadedPlugins().add(plugin);
            mapLoadedPlugins.put(plugin.getId(), plugin);
            Collections.sort(loadedPlugins, riskComparator);
        }
    }