private static ASN1Sequence getAltnameSequence(final byte[] sanValue) {
        try (val bInput = new ByteArrayInputStream(sanValue);
             val input = new ASN1InputStream(bInput)) {
            return ASN1Sequence.getInstance(input.readObject());
        } catch (final IOException e) {
            LOGGER.error("An error has occurred while reading the subject alternative name value", e);
        }
        return null;
    }