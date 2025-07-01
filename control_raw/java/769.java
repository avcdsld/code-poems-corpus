public static List<NS> viterbiCompute(List<EnumItem<NS>> roleTagList)
    {
        return Viterbi.computeEnum(roleTagList, PlaceDictionary.transformMatrixDictionary);
    }