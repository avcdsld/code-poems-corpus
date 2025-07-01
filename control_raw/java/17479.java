public void setLayerMaskArrays(INDArray featuresMaskArray, INDArray labelsMaskArray) {
        if (featuresMaskArray != null) {

            // FIXME: int cast
            //New approach: use feedForwardMaskArray method
            feedForwardMaskArray(featuresMaskArray, MaskState.Active, (int) featuresMaskArray.size(0));


            /*
            //feedforward layers below a RNN layer: need the input (features) mask array
            //Reason: even if the time series input is zero padded, the output from the dense layers are
            // non-zero (i.e., activationFunction(0*weights + bias) != 0 in general)
            //This assumes that the time series input is masked - i.e., values are 0 at the padded time steps,
            // so we don't need to do anything for the recurrent layer
            
            //Now, if mask array is 2d -> need to reshape to 1d (column vector) in the exact same order
            // as is done for 3d -> 2d time series reshaping
            INDArray reshapedFeaturesMask = TimeSeriesUtils.reshapeTimeSeriesMaskToVector(featuresMaskArray);
            
            for( int i=0; i<layers.length-1; i++ ){
                Type t = layers[i].type();
                if( t == Type.CONVOLUTIONAL || t == Type.FEED_FORWARD ){
                    layers[i].setMaskArray(reshapedFeaturesMask);
                } else if( t == Type.RECURRENT ) break;
            
            }
            */
        }
        if (labelsMaskArray != null) {
            if (!(getOutputLayer() instanceof IOutputLayer))
                return;
            layers[layers.length - 1].setMaskArray(labelsMaskArray);
        }
    }