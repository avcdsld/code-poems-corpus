private Page<CollectorItem> removeJobUrlAndInstanceUrl(Page<CollectorItem> collectorItems) {
        for (CollectorItem cItem : collectorItems) {
            if(cItem.getOptions().containsKey("jobUrl")) cItem.getOptions().remove("jobUrl");
            if(cItem.getOptions().containsKey("instanceUrl")) cItem.getOptions().remove("instanceUrl");
        }
        return collectorItems;
    }