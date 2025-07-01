public static CharsetDecoder decoder(Charset charset, CodingErrorAction malformedInputAction,
                                         CodingErrorAction unmappableCharacterAction) {
        checkNotNull(charset, "charset");
        CharsetDecoder d = charset.newDecoder();
        d.onMalformedInput(malformedInputAction).onUnmappableCharacter(unmappableCharacterAction);
        return d;
    }