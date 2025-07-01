@Nullable
    public static String replaceMacro( @CheckForNull String s, @Nonnull Map<String,String> properties) {
        return replaceMacro(s, new VariableResolver.ByMap<>(properties));
    }