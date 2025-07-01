public static String getStringValue(String primaryKey) {
        String val = (String) CFG.get(primaryKey);
        if (val == null) {
            throw new SofaRpcRuntimeException("Not Found Key: " + primaryKey);
        } else {
            return val;
        }
    }