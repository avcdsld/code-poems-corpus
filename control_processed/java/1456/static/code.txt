public Object current() {
        assert ctx.executor().inEventLoop();
        PendingWrite write = head;
        if (write == null) {
            return null;
        }
        return write.msg;
    }