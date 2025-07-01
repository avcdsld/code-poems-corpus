static void convertToCipherStrings(Iterable<String> cipherSuites, StringBuilder cipherBuilder,
                                       StringBuilder cipherTLSv13Builder, boolean boringSSL) {
        for (String c: cipherSuites) {
            if (c == null) {
                break;
            }

            String converted = toOpenSsl(c, boringSSL);
            if (converted == null) {
                converted = c;
            }

            if (!OpenSsl.isCipherSuiteAvailable(converted)) {
                throw new IllegalArgumentException("unsupported cipher suite: " + c + '(' + converted + ')');
            }

            if (SslUtils.isTLSv13Cipher(converted) || SslUtils.isTLSv13Cipher(c)) {
                cipherTLSv13Builder.append(converted);
                cipherTLSv13Builder.append(':');
            } else {
                cipherBuilder.append(converted);
                cipherBuilder.append(':');
            }
        }

        if (cipherBuilder.length() == 0 && cipherTLSv13Builder.length() == 0) {
            throw new IllegalArgumentException("empty cipher suites");
        }
        if (cipherBuilder.length() > 0) {
            cipherBuilder.setLength(cipherBuilder.length() - 1);
        }
        if (cipherTLSv13Builder.length() > 0) {
            cipherTLSv13Builder.setLength(cipherTLSv13Builder.length() - 1);
        }
    }