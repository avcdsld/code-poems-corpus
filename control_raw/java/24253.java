public static String getStringValue(String primaryKey, String secondaryKey) {
        String val = (String) CFG.get(primaryKey);
        if (val == null) {
            val = (String) CFG.get(secondaryKey);
            if (val == null) {
                throw new SofaRpcRuntimeException("Not found key: " + primaryKey + "/" + secondaryKey);
            } else {
                return val;
            }
        } else {
            return val;
        }
    }