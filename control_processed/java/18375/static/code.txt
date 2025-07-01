@Override
    public void tagLocation(DataBuffer buffer, Location location) {
        if (location == Location.HOST)
            AtomicAllocator.getInstance().getAllocationPoint(buffer).tickHostWrite();
        else if (location == Location.DEVICE)
            AtomicAllocator.getInstance().getAllocationPoint(buffer).tickDeviceWrite();
        else if (location == Location.EVERYWHERE) {
            AtomicAllocator.getInstance().getAllocationPoint(buffer).tickDeviceWrite();
            AtomicAllocator.getInstance().getAllocationPoint(buffer).tickHostRead();
        }
    }