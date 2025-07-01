public static INDArray toOutcomeMatrix(int[] index, long numOutcomes) {
        INDArray ret = Nd4j.create(index.length, numOutcomes);
        for (int i = 0; i < ret.rows(); i++) {
            int[] nums = new int[(int) numOutcomes];
            nums[index[i]] = 1;
            ret.putRow(i, NDArrayUtil.toNDArray(nums));
        }

        return ret;
    }