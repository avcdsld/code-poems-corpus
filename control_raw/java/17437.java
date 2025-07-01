@Override
    public void setParamTable(Map<String, INDArray> paramTable) {
        Map<String, INDArray> currParamTable = paramTable();
        if (!currParamTable.keySet().equals(paramTable.keySet())) {
            throw new IllegalArgumentException("Cannot set param table: parameter keys do not match.\n" + "Current: "
                    + currParamTable.keySet() + "\nTo set: " + paramTable.keySet());
        }

        for (String s : paramTable.keySet()) {
            INDArray curr = currParamTable.get(s);
            INDArray toSet = paramTable.get(s);
            if (!Arrays.equals(curr.shape(), toSet.shape())) {
                throw new IllegalArgumentException("Cannot set parameter table: parameter \"" + s + "\" shapes "
                        + "do not match. Current = " + Arrays.toString(curr.shape()) + ", to set = "
                        + Arrays.toString(toSet.shape()));
            }
        }

        //Now that we've checked ALL params (to avoid leaving net in half-modified state)
        for (String s : paramTable.keySet()) {
            INDArray curr = currParamTable.get(s);
            INDArray toSet = paramTable.get(s);
            curr.assign(toSet);
        }
    }