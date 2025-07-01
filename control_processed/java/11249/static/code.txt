@SuppressWarnings("unchecked")
    @WithBridgeMethods(List.class)
    public @Nonnull
    RunList getBuilds() {
        return RunList.fromJobs((Iterable) Jenkins.get().
                allItems(Job.class)).filter((Predicate<Run<?, ?>>) r -> r instanceof AbstractBuild && relatedTo((AbstractBuild<?, ?>) r));
    }