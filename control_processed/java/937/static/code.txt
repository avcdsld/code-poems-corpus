public static ValueCreator byStaticMethodInvocation(final Class<?> compatibleType, final String methodName)
    {
        return new ValueCreator()
        {
            public Object createValue(Class<?> type, String value)
            {
                Object v = null;
                if (compatibleType.isAssignableFrom(type))
                {
                    try
                    {
                        Method m = type.getMethod(methodName, String.class);
                        return m.invoke(null, value);
                    }
                    catch (NoSuchMethodException e)
                    {
                        // ignore
                    }
                    catch (Exception e)
                    {
                        throw new IllegalArgumentException(String.format("could not invoke %s#%s to create an obejct from %s", type.toString(), methodName, value));
                    }
                }
                return v;
            }
        };
    }