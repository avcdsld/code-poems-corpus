public Query addParameters(Object... values) {
        for (Object v : values) {
            if (v instanceof String) {
                addParameter((String) v);
            } else if (v instanceof Integer) {
                addParameter((Integer) v);
            } else if (v instanceof Long) {
                addParameter((Long) v);
            } else if(v instanceof Double) {
                addParameter((Double) v);
            } else if (v instanceof Boolean) {
                addParameter((Boolean) v);
            } else if (v instanceof Date) {
                addParameter((Date) v);
            } else if (v instanceof Timestamp) {
                addParameter((Timestamp) v);
            } else {
                throw new IllegalArgumentException(
                        "Type " + v.getClass().getName() + " is not supported by automatic property assignment");
            }
        }

        return this;
    }