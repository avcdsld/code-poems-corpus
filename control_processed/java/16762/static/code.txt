public static float[] getFloatData(INDArray buf) {
        if (buf.data().dataType() != DataType.FLOAT)
            throw new IllegalArgumentException("Float data must be obtained from a float buffer");

        if (buf.data().allocationMode() == DataBuffer.AllocationMode.HEAP) {
            return buf.data().asFloat();
        } else {
            float[] ret = new float[(int) buf.length()];
            INDArray linear = buf.reshape(-1);

            for (int i = 0; i < buf.length(); i++)
                ret[i] = linear.getFloat(i);
            return ret;
        }
    }