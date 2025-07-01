public void evaluate(DataSetIterator iterator, Map<String,IEvaluation> variableEvals){
        Map<String,Integer> map = new HashMap<>();
        Map<String,List<IEvaluation>> variableEvalsList = new HashMap<>();
        for(String s : variableEvals.keySet()){
            map.put(s, 0);  //Only 1 possible output here with DataSetIterator
            variableEvalsList.put(s, Collections.singletonList(variableEvals.get(s)));
        }
        evaluate(new MultiDataSetIteratorAdapter(iterator), variableEvalsList, map);
    }