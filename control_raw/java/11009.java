public static InputStream skip(InputStream in, long size) throws IOException {
        DataInputStream di = new DataInputStream(in);

        while (size>0) {
            int chunk = (int)Math.min(SKIP_BUFFER.length,size);
            di.readFully(SKIP_BUFFER,0,chunk);
            size -= chunk;
        }

        return in;
    }