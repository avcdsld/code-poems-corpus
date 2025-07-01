public final List<Pair<String, Double>> predict(Collection<String> context)
    {
        return predict(context.toArray(new String[0]));
    }