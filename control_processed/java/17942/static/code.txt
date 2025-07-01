protected <T extends TokenBase> List<T> createTokenList(String text) {

        if (!split) {
            return createTokenList(0, text);
        }

        List<Integer> splitPositions = getSplitPositions(text);

        if (splitPositions.isEmpty()) {
            return createTokenList(0, text);
        }

        ArrayList<T> result = new ArrayList<>();

        int offset = 0;

        for (int position : splitPositions) {
            result.addAll(this.<T>createTokenList(offset, text.substring(offset, position + 1)));
            offset = position + 1;
        }

        if (offset < text.length()) {
            result.addAll(this.<T>createTokenList(offset, text.substring(offset)));
        }

        return result;
    }