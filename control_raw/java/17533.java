public int getTopNCorrectCount() {
        if (confusion == null)
            return 0;
        if (topN <= 1) {
            int nClasses = confusion().getClasses().size();
            int countCorrect = 0;
            for (int i = 0; i < nClasses; i++) {
                countCorrect += confusion().getCount(i, i);
            }
            return countCorrect;
        }
        return topNCorrectCount;
    }