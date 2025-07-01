public ProviderGroup addAll(Collection<ProviderInfo> providerInfos) {
        if (CommonUtils.isEmpty(providerInfos)) {
            return this;
        }
        ConcurrentHashSet<ProviderInfo> tmp = new ConcurrentHashSet<ProviderInfo>(this.providerInfos);
        tmp.addAll(providerInfos); // 排重
        this.providerInfos = new ArrayList<ProviderInfo>(tmp);
        return this;
    }