public <T> Future<T> actAsync(final FileCallable<T> callable) throws IOException, InterruptedException {
        try {
            DelegatingCallable<T,IOException> wrapper = new FileCallableWrapper<>(callable);
            for (FileCallableWrapperFactory factory : ExtensionList.lookup(FileCallableWrapperFactory.class)) {
                wrapper = factory.wrap(wrapper);
            }
            return (channel!=null ? channel : localChannel)
                .callAsync(wrapper);
        } catch (IOException e) {
            // wrap it into a new IOException so that we get the caller's stack trace as well.
            throw new IOException("remote file operation failed",e);
        }
    }