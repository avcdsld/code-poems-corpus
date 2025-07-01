public String getAttr(String key) {
        String val = (String) dynamicAttrs.get(key);
        return val == null ? staticAttrs.get(key) : val;
    }