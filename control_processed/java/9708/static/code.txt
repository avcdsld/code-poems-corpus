public MasterSlaveServersConfig setMasterAddress(String masterAddress) {
        if (masterAddress != null) {
            this.masterAddress = URIBuilder.create(masterAddress);
        }
        return this;
    }