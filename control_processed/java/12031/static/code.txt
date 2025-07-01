private byte[] verifyMagic(byte[] payload) {
        int payloadLen = payload.length-MAGIC.length;
        if (payloadLen<0)   return null;    // obviously broken

        for (int i=0; i<MAGIC.length; i++) {
            if (payload[payloadLen+i]!=MAGIC[i])
                return null;    // broken
        }
        byte[] truncated = new byte[payloadLen];
        System.arraycopy(payload,0,truncated,0,truncated.length);
        return truncated;
    }