private String readAttributeAsFixedLengthString(Attribute attribute, int bufferSize)
            throws UnsupportedKerasConfigurationException {
        synchronized (Hdf5Archive.LOCK_OBJECT) {
            VarLenType vl = attribute.getVarLenType();
            byte[] attrBuffer = new byte[bufferSize];
            BytePointer attrPointer = new BytePointer(attrBuffer);
            attribute.read(vl, attrPointer);
            attrPointer.get(attrBuffer);
            vl.deallocate();
            return new String(attrBuffer);
        }
    }