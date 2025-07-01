public static void main(final String[] args) throws ParseException {
    final CommandLineParser parser = new DefaultParser();

    if (parser.parse(createHelpOptions(), args, true).hasOption(HELP_KEY)) {
      new HelpFormatter().printHelp(EncryptionCLI.class.getSimpleName(), createOptions(), true);
      return;
    }

    final CommandLine line = parser.parse(createOptions(), args);

    final String passphraseKey = line.getOptionValue(PASSPHRASE_KEY);
    final String plainText = line.getOptionValue(PLAINTEXT_KEY);
    final String version = line.getOptionValue(VERSION_KEY);

    final ICrypto crypto = new Crypto();
    final String cipheredText = crypto
        .encrypt(plainText, passphraseKey, Version.fromVerString(version));
    System.out.println(cipheredText);
  }