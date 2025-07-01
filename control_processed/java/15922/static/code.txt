private boolean isClientChannelClosed(Throwable cause) {
        if (cause instanceof ClosedChannelException ||
                cause instanceof Errors.NativeIoException) {
            LOG.error("ZuulFilterChainHandler::isClientChannelClosed - IO Exception");
            return true;
        }
        return false;
    }