private <T extends Describable<T>>
    Descriptor<T> findDescriptor(String shortClassName, Collection<? extends Descriptor<T>> descriptors) {
        String name = '.'+shortClassName;
        for (Descriptor<T> d : descriptors) {
            if(d.clazz.getName().endsWith(name))
                return d;
        }
        return null;
    }