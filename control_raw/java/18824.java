public static INDArray fromNpyBase64(String base64) {
        byte[] bytes = Base64.decodeBase64(base64);
        return Nd4j.createNpyFromByteArray(bytes);
    }