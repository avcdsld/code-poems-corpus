public SDVariable sru(String baseName, SRUConfiguration configuration) {
        return new SRU(sd, configuration).outputVariables(baseName)[0];
    }