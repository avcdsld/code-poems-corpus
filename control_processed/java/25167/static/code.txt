protected final void skipIndex(final int skippedCharIndex) {
        _bufferedString.addChar();
        if (_skipped.length == 0 || _skipped[_skipped.length - 1] != -1) {
            _skipped = Arrays.copyOf(_skipped, Math.max(_skipped.length + 1, 1));
        }

        _skipped[_skippedWriteIndex] = skippedCharIndex;
        _skippedWriteIndex++;
    }