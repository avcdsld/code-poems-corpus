public void addProviderListener(ConsumerConfig consumerConfig, ProviderInfoListener listener) {
        if (listener != null) {
            RegistryUtils.initOrAddList(providerListenerMap, consumerConfig, listener);
        }
    }