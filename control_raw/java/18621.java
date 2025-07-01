protected void initializeHelper(DataType dataType){
        String backend = Nd4j.getExecutioner().getEnvironmentInformation().getProperty("backend");
        if("CUDA".equalsIgnoreCase(backend)) {
            try {
                helper = Class.forName("org.deeplearning4j.nn.layers.dropout.CudnnDropoutHelper")
                        .asSubclass(DropoutHelper.class).getConstructor(DataType.class).newInstance(dataType);
                log.debug("CudnnDropoutHelper successfully initialized");
                if (!helper.checkSupported()) {
                    helper = null;
                }
            } catch (Throwable t) {
                if (!(t instanceof ClassNotFoundException)) {
                    log.warn("Could not initialize CudnnDropoutHelper", t);
                }
                //Unlike other layers, don't warn here about CuDNN not found - if the user has any other layers that can
                // benefit from them cudnn, they will get a warning from those
            }
        }
        initializedHelper = true;
    }