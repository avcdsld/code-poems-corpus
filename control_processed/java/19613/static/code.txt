public List<PlanFragment> getAllFragments()
    {
        ImmutableList.Builder<PlanFragment> fragments = ImmutableList.builder();

        fragments.add(getFragment());
        for (SubPlan child : getChildren()) {
            fragments.addAll(child.getAllFragments());
        }

        return fragments.build();
    }