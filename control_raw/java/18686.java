public void build(Trie trie) {
        ProgressLog.begin("building " + (compact ? "compact" : "sparse") + " trie");
        baseBuffer = IntBuffer.allocate(BASE_CHECK_INITIAL_SIZE);
        baseBuffer.put(0, 1);
        checkBuffer = IntBuffer.allocate(BASE_CHECK_INITIAL_SIZE);
        tailBuffer = CharBuffer.allocate(TAIL_INITIAL_SIZE);
        add(-1, 0, trie.getRoot());
        reportUtilizationRate();
        ProgressLog.end();
    }