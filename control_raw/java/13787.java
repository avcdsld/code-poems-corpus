@JsonIgnore
    protected static IPersonAttributeDao getAttributeRepository() {
        val repositories = ApplicationContextProvider.getAttributeRepository();
        return repositories.orElse(null);
    }