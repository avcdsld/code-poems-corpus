@Singleton
    @Requires(classes = HibernateValidator.class)
    ValidatorFactory validatorFactory(Optional<Environment> environment) {
        Configuration validatorConfiguration = Validation.byDefaultProvider()
            .configure();

        messageInterpolator.ifPresent(validatorConfiguration::messageInterpolator);
        traversableResolver.ifPresent(validatorConfiguration::traversableResolver);
        constraintValidatorFactory.ifPresent(validatorConfiguration::constraintValidatorFactory);
        parameterNameProvider.ifPresent(validatorConfiguration::parameterNameProvider);

        if (ignoreXmlConfiguration) {
            validatorConfiguration.ignoreXmlConfiguration();
        }
        environment.ifPresent(env -> {
            Optional<Properties> config = env.getProperty("hibernate.validator", Properties.class);
            config.ifPresent(properties -> {
                for (Map.Entry<Object, Object> entry : properties.entrySet()) {
                    Object value = entry.getValue();
                    if (value != null) {
                        validatorConfiguration.addProperty(
                            "hibernate.validator." + entry.getKey(),
                            value.toString()
                        );
                    }
                }
            });
        });
        return validatorConfiguration.buildValidatorFactory();
    }