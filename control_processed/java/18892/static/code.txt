protected void initCudaContextForThread(Long threadId) {

        // we set device to be used prior to stream creation

        nativeOps.setDevice(getDeviceId());

        CudaContext context = new CudaContext();
        context.initHandle();
        context.initOldStream();
        context.initStream();
        context.associateHandle();
        //contextPool.put(threadId, context);
    }