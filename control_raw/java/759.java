int searchVocab(String word)
    {
        if (word == null) return -1;
        Integer pos = vocabIndexMap.get(word);
        return pos == null ? -1 : pos.intValue();
    }