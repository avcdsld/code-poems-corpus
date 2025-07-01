public void readFields(DataInput in) throws IOException {
        int newLength = WritableUtils.readVInt(in);
        setCapacity(newLength, false);
        in.readFully(bytes, 0, newLength);
        length = newLength;
    }