public static Map<String, Integer> getKeywordCounts(String[] keywordArray)
    {
        Map<String, Integer> counts = new HashMap<String, Integer>();

        Integer counter;
        for (int i = 0; i < keywordArray.length; ++i)
        {
            counter = counts.get(keywordArray[i]);
            if (counter == null)
            {
                counter = 0;
            }
            counts.put(keywordArray[i], ++counter); //增加词频
        }

        return counts;
    }