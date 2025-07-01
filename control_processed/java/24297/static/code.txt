static void parseMethodInfo(Map<String, Object> methodParameters, String method, String valueStr) {
        int idxSplit = valueStr.indexOf('#'); // "#"被认为是MethodSpecial配置的标志
        if (idxSplit < 0) {
            return;
        }

        int idxLeft = valueStr.indexOf('[');
        int idxRight = valueStr.indexOf(']');

        String parameters = valueStr.substring(idxLeft + 1, idxRight);
        String[] kvs = parameters.split("@");
        if (kvs.length > 0) {
            Map<String, String> tmp = new HashMap<String, String>();
            for (String kvp : kvs) {
                String[] kv = kvp.split("#");
                if (kv.length == 2) {
                    tmp.put(kv[0], kv[1]);
                }
            }
            // timeout特殊处理
            String timeout = getValue(tmp, ATTR_TIMEOUT, KEY_TIMEOUT,
                TIMEOUT);
            if (timeout != null) {
                removeOldKeys(tmp, ATTR_TIMEOUT, KEY_TIMEOUT, TIMEOUT);
                try {
                    methodParameters.put("." + method + "." + ATTR_TIMEOUT,
                        Integer.parseInt(timeout));
                } catch (Exception e) {
                    LOGGER.error("method timeout is invalid : {}", timeout);
                }
            }
            // 其它就存起来
            for (Map.Entry<String, String> entry : tmp.entrySet()) {
                methodParameters.put("." + method + "." + entry.getKey(), entry.getValue());
            }
        }
    }