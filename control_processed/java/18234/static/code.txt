@Override
    public NDArrayMessage doGetUpdate(int index) {
        byte[] key = ByteBuffer.allocate(4).putInt(index).array();
        try {
            UnsafeBuffer unsafeBuffer = new UnsafeBuffer(db.get(key));
            return NDArrayMessage.fromBuffer(unsafeBuffer, 0);
        } catch (RocksDBException e) {
            throw new RuntimeException(e);
        }
    }