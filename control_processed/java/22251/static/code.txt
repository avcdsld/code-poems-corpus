@SuppressWarnings("WeakerAccess")
    @Internal
    protected final Optional findBeanForMethodArgument(BeanResolutionContext resolutionContext, BeanContext context, MethodInjectionPoint injectionPoint, Argument argument) {
        return resolveBeanWithGenericsFromMethodArgument(resolutionContext, injectionPoint, argument, (beanType, qualifier) ->
                ((DefaultBeanContext) context).findBean(resolutionContext, beanType, qualifier)
        );
    }