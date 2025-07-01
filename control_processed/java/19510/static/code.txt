public FunctionHandle resolveFunction(Session session, QualifiedName name, List<TypeSignatureProvider> parameterTypes)
    {
        // TODO Actually use session
        // Session will be used to provide information about the order of function namespaces to through resolving the function.
        // This is likely to be in terms of SQL path. Currently we still don't have support multiple function namespaces, nor
        // SQL path. As a result, session is not used here. We still add this to distinguish the two versions of resolveFunction
        // while the refactoring is on-going.
        return staticFunctionNamespace.resolveFunction(name, parameterTypes);
    }