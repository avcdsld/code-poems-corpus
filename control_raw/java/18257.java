public static int[] getOutputSize(INDArray inputData, int[] kernel, int[] strides, int[] padding,
                                      ConvolutionMode convolutionMode, int[] dilation) {
        // FIXME: int cast
        int inH = (int) inputData.size(2);
        int inW = (int) inputData.size(3);

        //Determine the effective kernel size, accounting for dilation
        //http://deeplearning.net/software/theano/tutorial/conv_arithmetic.html#dilated-convolutions
        int[] eKernel = effectiveKernelSize(kernel, dilation);
        boolean atrous = (eKernel == kernel);

        int[] inShape = new int[]{inH, inW};
        validateShapes(inputData, eKernel, strides, padding, convolutionMode, dilation, inShape, atrous);

        if (convolutionMode == ConvolutionMode.Same) {

            int outH = (int) Math.ceil(inH / ((double) strides[0]));
            int outW = (int) Math.ceil(inW / ((double) strides[1]));

            return new int[]{outH, outW};
        }

        int hOut = (inH - eKernel[0] + 2 * padding[0]) / strides[0] + 1;
        int wOut = (inW - eKernel[1] + 2 * padding[1]) / strides[1] + 1;

        return new int[]{hOut, wOut};
    }