@Override
    public CollectorItem createCollectorItemSelectOptions(CollectorItem item, Map<String, Object> allOptions, Map<String, Object> uniqueOptions) {
        Collector collector =  collectorRepository.findOne(item.getCollectorId());
        Map<String,Object> uniqueFieldsFromCollector = collector.getUniqueFields();
        List<CollectorItem> existing = customRepositoryQuery.findCollectorItemsBySubsetOptions(
                item.getCollectorId(), allOptions, uniqueOptions,uniqueFieldsFromCollector);

        if (!CollectionUtils.isEmpty(existing)) {
            CollectorItem existingItem = existing.get(0);
            existingItem.getOptions().putAll(item.getOptions());
            return collectorItemRepository.save(existingItem);
        }
        return collectorItemRepository.save(item);
    }