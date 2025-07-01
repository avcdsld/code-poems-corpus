private boolean check(File fingerprintFile, TaskListener listener) {
        try {
            Fingerprint fp = loadFingerprint(fingerprintFile);
            if (fp == null || !fp.isAlive()) {
                listener.getLogger().println("deleting obsolete " + fingerprintFile);
                fingerprintFile.delete();
                return true;
            } else {
                // get the fingerprint in the official map so have the changes visible to Jenkins
                // otherwise the mutation made in FingerprintMap can override our trimming.
                fp = getFingerprint(fp);
                return fp.trim();
            }
        } catch (IOException e) {
            Functions.printStackTrace(e, listener.error("Failed to process " + fingerprintFile));
            return false;
        }
    }