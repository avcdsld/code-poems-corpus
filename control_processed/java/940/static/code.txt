public static List<NR> viterbiComputeSimply(List<EnumItem<NR>> roleTagList)
    {
        return Viterbi.computeEnumSimply(roleTagList, PersonDictionary.transformMatrixDictionary);
    }