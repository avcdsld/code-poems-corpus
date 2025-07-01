public WordVectorModel train(String trainFileName, String modelFileName)
    {
        Config settings = new Config();
        settings.setInputFile(trainFileName);
        settings.setLayer1Size(layerSize);
        settings.setUseContinuousBagOfWords(type == NeuralNetworkType.CBOW);
        settings.setUseHierarchicalSoftmax(useHierarchicalSoftmax);
        settings.setNegative(negativeSamples);
        settings.setNumThreads(numThreads);
        settings.setAlpha(initialLearningRate == null ? type.getDefaultInitialLearningRate() : initialLearningRate);
        settings.setSample(downSampleRate);
        settings.setWindow(windowSize);
        settings.setIter(iterations);
        settings.setMinCount(minFrequency);
        settings.setOutputFile(modelFileName);
        Word2VecTraining model = new Word2VecTraining(settings);
        final long timeStart = System.currentTimeMillis();
//        if (callback == null)
//        {
//            callback = new TrainingCallback()
//            {
//                public void corpusLoading(float percent)
//                {
//                    System.out.printf("\r加载训练语料：%.2f%%", percent);
//                }
//
//                public void corpusLoaded(int vocWords, int trainWords, int totalWords)
//                {
//                    System.out.println();
//                    System.out.printf("词表大小：%d\n", vocWords);
//                    System.out.printf("训练词数：%d\n", trainWords);
//                    System.out.printf("语料词数：%d\n", totalWords);
//                }
//
//                public void training(float alpha, float progress)
//                {
//                    System.out.printf("\r学习率：%.6f  进度：%.2f%%", alpha, progress);
//                    long timeNow = System.currentTimeMillis();
//                    long costTime = timeNow - timeStart + 1;
//                    progress /= 100;
//                    String etd = Utility.humanTime((long) (costTime / progress * (1.f - progress)));
//                    if (etd.length() > 0) System.out.printf("  剩余时间：%s", etd);
//                    System.out.flush();
//                }
//            };
//        }
        settings.setCallback(callback);

        try
        {
            model.trainModel();
            System.out.println();
            System.out.printf("训练结束，一共耗时：%s\n", Utility.humanTime(System.currentTimeMillis() - timeStart));
            return new WordVectorModel(modelFileName);
        }
        catch (IOException e)
        {
            logger.warning("训练过程中发生IO异常\n" + TextUtility.exceptionToString(e));
        }

        return null;
    }