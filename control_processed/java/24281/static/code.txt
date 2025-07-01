private void addAttributes(ConfiguratorRegistration configuratorRegistration, String group) {
        // if group == null; group = "DEFAULT_GROUP"
        if (StringUtils.isNotEmpty(group)) {
            configuratorRegistration.setGroup(group);
        }

    }