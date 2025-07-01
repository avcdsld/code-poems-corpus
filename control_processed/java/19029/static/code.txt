public static String readString(DataInput in) throws IOException {
        int length = WritableUtils.readVInt(in);
        byte[] bytes = new byte[length];
        in.readFully(bytes, 0, length);
        return decode(bytes);
    }