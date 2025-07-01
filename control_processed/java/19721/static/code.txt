public synchronized ListenableFuture<?> reserve(long bytes)
    {
        checkArgument(bytes >= 0, "bytes is negative");

        if ((currentBytes + bytes) >= maxBytes) {
            throw exceededLocalLimit(succinctBytes(maxBytes));
        }
        currentBytes += bytes;

        return NOT_BLOCKED;
    }