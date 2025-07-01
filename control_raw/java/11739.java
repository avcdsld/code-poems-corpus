@Exported
    @QuickSilver
    public RunT getLastBuild() {
        SortedMap<Integer, ? extends RunT> runs = _getRuns();

        if (runs.isEmpty())
            return null;
        return runs.get(runs.firstKey());
    }