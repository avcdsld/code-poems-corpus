public double gMeasure(EvaluationAveraging averaging) {
        int nClasses = confusion().getClasses().size();
        if (averaging == EvaluationAveraging.Macro) {
            double macroGMeasure = 0.0;
            for (int i = 0; i < nClasses; i++) {
                macroGMeasure += gMeasure(i);
            }
            macroGMeasure /= nClasses;
            return macroGMeasure;
        } else if (averaging == EvaluationAveraging.Micro) {
            long tpCount = 0;
            long fpCount = 0;
            long fnCount = 0;
            for (int i = 0; i < nClasses; i++) {
                tpCount += truePositives.getCount(i);
                fpCount += falsePositives.getCount(i);
                fnCount += falseNegatives.getCount(i);
            }
            double precision = EvaluationUtils.precision(tpCount, fpCount, DEFAULT_EDGE_VALUE);
            double recall = EvaluationUtils.recall(tpCount, fnCount, DEFAULT_EDGE_VALUE);
            return EvaluationUtils.gMeasure(precision, recall);
        } else {
            throw new UnsupportedOperationException("Unknown averaging approach: " + averaging);
        }
    }