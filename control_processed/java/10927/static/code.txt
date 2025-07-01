public @NonNull List<PluginWrapper.PluginDisableResult> disablePlugins(@NonNull PluginWrapper.PluginDisableStrategy strategy, @NonNull List<String> plugins) throws IOException {
        // Where we store the results of each plugin disablement
        List<PluginWrapper.PluginDisableResult> results = new ArrayList<>(plugins.size());

        // Disable all plugins passed
        for (String pluginName : plugins) {
            PluginWrapper plugin = this.getPlugin(pluginName);

            if (plugin == null) {
                results.add(new PluginWrapper.PluginDisableResult(pluginName, PluginWrapper.PluginDisableStatus.NO_SUCH_PLUGIN, Messages.PluginWrapper_NoSuchPlugin(pluginName)));
            } else {
                results.add(plugin.disable(strategy));
            }
        }

        return results;
    }