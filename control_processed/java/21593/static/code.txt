private static Object delegateChains(final Class<?> type) {
        final ReturnsEmptyValues returnsEmptyValues = new ReturnsEmptyValues();
        Object result = returnsEmptyValues.returnValueFor(type);

        if (result == null) {
            Class<?> emptyValueForClass = type;
            while (emptyValueForClass != null && result == null) {
                final Class<?>[] classes = emptyValueForClass.getInterfaces();
                for (Class<?> clazz : classes) {
                    result = returnsEmptyValues.returnValueFor(clazz);
                    if (result != null) {
                        break;
                    }
                }
                emptyValueForClass = emptyValueForClass.getSuperclass();
            }
        }

        if (result == null) {
            result = new ReturnsMoreEmptyValues().returnValueFor(type);
        }

        return result;
    }