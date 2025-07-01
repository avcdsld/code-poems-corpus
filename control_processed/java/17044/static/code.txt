@Override
    public MultiDataSet next() {
        if (throwable != null)
            throw throwable;

        if (hasDepleted.get())
            return null;

        MultiDataSet temp = nextElement;
        nextElement = null;
        return temp;
    }