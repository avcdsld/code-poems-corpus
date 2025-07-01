public DecoderResult decode(boolean[][] image, Map<DecodeHintType,?> hints)
      throws ChecksumException, FormatException {
    return decode(BitMatrix.parse(image), hints);
  }