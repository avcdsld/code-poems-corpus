void breakLinks(final OtpErlangObject reason) {
        final Link[] l = links.clearLinks();

        if (l != null) {
            final int len = l.length;

            for (int i = 0; i < len; i++) {
                exit(1, l[i].remote(), reason);
            }
        }
    }