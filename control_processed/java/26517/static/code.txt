public static byte[] encrypt3DES2Base64(byte[] data, byte[] key) {
        try {
            return Base64.getEncoder().encode(encrypt3DES(data, key));
        } catch (Exception e) {
            return null;
        }
    }