@Override
    public Map<String, Double> accuracy(List<String> questions) {
        Map<String, Double> accuracy = new HashMap<>();
        Counter<String> right = new Counter<>();
        String analogyType = "";
        for (String s : questions) {
            if (s.startsWith(":")) {
                double correct = right.getCount(CORRECT);
                double wrong = right.getCount(WRONG);
                if (analogyType.isEmpty()) {
                    analogyType = s;
                    continue;
                }
                double accuracyRet = 100.0 * correct / (correct + wrong);
                accuracy.put(analogyType, accuracyRet);
                analogyType = s;
                right.clear();
            } else {
                String[] split = s.split(" ");
                List<String> positive = Arrays.asList(split[1], split[2]);
                List<String> negative = Arrays.asList(split[0]);
                String predicted = split[3];
                String w = wordsNearest(positive, negative, 1).iterator().next();
                if (predicted.equals(w))
                    right.incrementCount(CORRECT, 1.0f);
                else
                    right.incrementCount(WRONG, 1.0f);

            }
        }
        if (!analogyType.isEmpty()) {
            double correct = right.getCount(CORRECT);
            double wrong = right.getCount(WRONG);
            double accuracyRet = 100.0 * correct / (correct + wrong);
            accuracy.put(analogyType, accuracyRet);
        }
        return accuracy;
    }