public static IndexMaps createIndices(String conllPath, boolean labeled, boolean lowercased, String clusterFile) throws IOException
    {
        HashMap<String, Integer> wordMap = new HashMap<String, Integer>();
        HashMap<Integer, Integer> labels = new HashMap<Integer, Integer>();
        HashMap<String, Integer> clusterMap = new HashMap<String, Integer>();
        HashMap<Integer, Integer> cluster4Map = new HashMap<Integer, Integer>();
        HashMap<Integer, Integer> cluster6Map = new HashMap<Integer, Integer>();

        String rootString = "ROOT";

        wordMap.put("ROOT", 0);
        labels.put(0, 0);

        // 所有label的id必须从零开始并且连续
        BufferedReader reader = new BufferedReader(new FileReader(conllPath));
        String line;
        while ((line = reader.readLine()) != null)
        {
            String[] args = line.trim().split("\t");
            if (args.length > 7)
            {
                String label = args[7];
                int head = Integer.parseInt(args[6]);
                if (head == 0)
                    rootString = label;

                if (!labeled)
                    label = "~";
                else if (label.equals("_"))
                    label = "-";

                if (!wordMap.containsKey(label))
                {
                    labels.put(wordMap.size(), labels.size());
                    wordMap.put(label, wordMap.size());
                }
            }
        }

        reader = new BufferedReader(new FileReader(conllPath));
        while ((line = reader.readLine()) != null)
        {
            String[] cells = line.trim().split("\t");
            if (cells.length > 7)
            {
                String pos = cells[3];
                if (!wordMap.containsKey(pos))
                {
                    wordMap.put(pos, wordMap.size());
                }
            }
        }

        if (clusterFile.length() > 0)
        {
            reader = new BufferedReader(new FileReader(clusterFile));
            while ((line = reader.readLine()) != null)
            {
                String[] cells = line.trim().split("\t");
                if (cells.length > 2)
                {
                    String cluster = cells[0];
                    String word = cells[1];
                    String prefix4 = cluster.substring(0, Math.min(4, cluster.length()));
                    String prefix6 = cluster.substring(0, Math.min(6, cluster.length()));
                    int clusterId = wordMap.size();

                    if (!wordMap.containsKey(cluster))
                    {
                        clusterMap.put(word, wordMap.size());
                        wordMap.put(cluster, wordMap.size());
                    }
                    else
                    {
                        clusterId = wordMap.get(cluster);
                        clusterMap.put(word, clusterId);
                    }

                    int pref4Id = wordMap.size();
                    if (!wordMap.containsKey(prefix4))
                    {
                        wordMap.put(prefix4, wordMap.size());
                    }
                    else
                    {
                        pref4Id = wordMap.get(prefix4);
                    }

                    int pref6Id = wordMap.size();
                    if (!wordMap.containsKey(prefix6))
                    {
                        wordMap.put(prefix6, wordMap.size());
                    }
                    else
                    {
                        pref6Id = wordMap.get(prefix6);
                    }

                    cluster4Map.put(clusterId, pref4Id);
                    cluster6Map.put(clusterId, pref6Id);
                }
            }
        }

        reader = new BufferedReader(new FileReader(conllPath));
        while ((line = reader.readLine()) != null)
        {
            String[] cells = line.trim().split("\t");
            if (cells.length > 7)
            {
                String word = cells[1];
                if (lowercased)
                    word = word.toLowerCase();
                if (!wordMap.containsKey(word))
                {
                    wordMap.put(word, wordMap.size());
                }
            }
        }

        return new IndexMaps(wordMap, labels, rootString, cluster4Map, cluster6Map, clusterMap);
    }