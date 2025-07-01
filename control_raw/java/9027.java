public void dumpRequest(Map<String, Object> result) {
        if(!dumpConfig.isRequestEnabled()) { return; }

        Map<String, Object> requestResult = new LinkedHashMap<>();
        for(IRequestDumpable dumper: dumperFactory.createRequestDumpers(dumpConfig, exchange)) {
            if(dumper.isApplicableForRequest()){
                dumper.dumpRequest(requestResult);
            }
        }
        result.put(DumpConstants.REQUEST, requestResult);
    }