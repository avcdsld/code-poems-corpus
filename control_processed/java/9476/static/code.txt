@Override
    public void sync(List<Dml> dmls) {
        if (dmls == null || dmls.isEmpty()) {
            return;
        }
        try {
            rdbSyncService.sync(mappingConfigCache, dmls, envProperties);
            rdbMirrorDbSyncService.sync(dmls);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }