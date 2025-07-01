function getReturnContext(state) {
    let context = state.tryContext;

    while (context) {
        if (context.hasFinalizer && context.position !== "finally") {
            return context;
        }
        context = context.upper;
    }

    return state;
}