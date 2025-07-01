public static String resolve(String originalHost) {
        String currentHost = originalHost;
        if (isLocalOrIp(currentHost)) {
            return originalHost;
        }
        try {
            String targetHost = null;
            do {
                Attributes attrs = getDirContext().getAttributes(currentHost, new String[]{A_RECORD_TYPE, CNAME_RECORD_TYPE});
                Attribute attr = attrs.get(A_RECORD_TYPE);
                if (attr != null) {
                    targetHost = attr.get().toString();
                }
                attr = attrs.get(CNAME_RECORD_TYPE);
                if (attr != null) {
                    currentHost = attr.get().toString();
                } else {
                    targetHost = currentHost;
                }

            } while (targetHost == null);
            return targetHost;
        } catch (NamingException e) {
            logger.warn("Cannot resolve eureka server address {}; returning original value {}", currentHost, originalHost, e);
            return originalHost;
        }
    }