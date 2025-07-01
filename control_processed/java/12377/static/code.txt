public BeanConfiguration addAbstractBean(String name) {
        BeanConfiguration bc = new DefaultBeanConfiguration(name);
        bc.setAbstract(true);
        registerBeanConfiguration(name, bc);

        return bc;
    }