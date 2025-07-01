public SingleLogoutService getSingleLogoutService(final String binding) {
        return getSingleLogoutServices().stream().filter(acs -> acs.getBinding().equalsIgnoreCase(binding)).findFirst().orElse(null);
    }