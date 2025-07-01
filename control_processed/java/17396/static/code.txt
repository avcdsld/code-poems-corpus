public Deque<Integer> getCrossoverPoints() {
        Collections.shuffle(parameterIndexes);
        List<Integer> crossoverPointLists =
                        parameterIndexes.subList(0, rng.nextInt(maxCrossovers - minCrossovers) + minCrossovers);
        Collections.sort(crossoverPointLists);
        Deque<Integer> crossoverPoints = new ArrayDeque<Integer>(crossoverPointLists);
        crossoverPoints.add(Integer.MAX_VALUE);

        return crossoverPoints;
    }