public static KV<String, Forest> remove(String key) {
        KV<String, Forest> kv = AMBIGUITY.get(key);
        if (kv != null && kv.getV() != null) {
            kv.getV().clear();
        }
        MyStaticValue.ENV.remove(key);
        return AMBIGUITY.remove(key);
    }