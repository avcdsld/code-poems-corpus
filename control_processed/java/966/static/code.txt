protected BaseFeatureData selectFeatures(IDataSet dataSet)
    {
        ChiSquareFeatureExtractor chiSquareFeatureExtractor = new ChiSquareFeatureExtractor();

        logger.start("使用卡方检测选择特征中...");
        //FeatureStats对象包含文档中所有特征及其统计信息
        BaseFeatureData featureData = chiSquareFeatureExtractor.extractBasicFeatureData(dataSet); //执行统计

        //我们传入这些统计信息到特征选择算法中，得到特征与其分值
        Map<Integer, Double> selectedFeatures = chiSquareFeatureExtractor.chi_square(featureData);

        //从统计数据中删掉无用的特征并重建特征映射表
        int[][] featureCategoryJointCount = new int[selectedFeatures.size()][];
        featureData.wordIdTrie = new BinTrie<Integer>();
        String[] wordIdArray = dataSet.getLexicon().getWordIdArray();
        int p = -1;
        for (Integer feature : selectedFeatures.keySet())
        {
            featureCategoryJointCount[++p] = featureData.featureCategoryJointCount[feature];
            featureData.wordIdTrie.put(wordIdArray[feature], p);
        }
        logger.finish(",选中特征数:%d / %d = %.2f%%\n", featureCategoryJointCount.length,
                      featureData.featureCategoryJointCount.length,
                      featureCategoryJointCount.length / (double)featureData.featureCategoryJointCount.length * 100.);
        featureData.featureCategoryJointCount = featureCategoryJointCount;

        return featureData;
    }