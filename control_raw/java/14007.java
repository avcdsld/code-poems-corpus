protected String digestEncodedPassword(final String encodedPassword, final Map<String, Object> values) {
        val hashService = new DefaultHashService();
        if (StringUtils.isNotBlank(this.staticSalt)) {
            hashService.setPrivateSalt(ByteSource.Util.bytes(this.staticSalt));
        }
        hashService.setHashAlgorithmName(this.algorithmName);

        if (values.containsKey(this.numberOfIterationsFieldName)) {
            val longAsStr = values.get(this.numberOfIterationsFieldName).toString();
            hashService.setHashIterations(Integer.parseInt(longAsStr));
        } else {
            hashService.setHashIterations(this.numberOfIterations);
        }

        if (!values.containsKey(this.saltFieldName)) {
            throw new IllegalArgumentException("Specified field name for salt does not exist in the results");
        }

        val dynaSalt = values.get(this.saltFieldName).toString();
        val request = new HashRequest.Builder()
            .setSalt(dynaSalt)
            .setSource(encodedPassword)
            .build();
        return hashService.computeHash(request).toHex();
    }