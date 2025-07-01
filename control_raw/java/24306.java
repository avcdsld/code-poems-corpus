public static List<Field> getAllFields(Class clazz) {
        List<Field> all = new ArrayList<Field>();
        for (Class<?> c = clazz; c != Object.class && c != null; c = c.getSuperclass()) {
            Field[] fields = c.getDeclaredFields(); // 所有方法，不包含父类
            for (Field field : fields) {
                int mod = field.getModifiers();
                // 过滤static 和 transient，支持final
                if (Modifier.isStatic(mod) || Modifier.isTransient(mod)) {
                    continue;
                }
                field.setAccessible(true); // 不管private还是protect都可以
                all.add(field);
            }
        }
        return all;
    }