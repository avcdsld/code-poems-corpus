@Override
    public String getEscapedValue(String value, boolean toQuote) {
        // Escape special characters
        StringBuilder buf = new StringBuilder(value.length());
        int idx = 0;
        int ch;

        while (idx < value.length()) {
            ch = value.charAt(idx++);
            if (ch == 0) {
                buf.append("\\0");

            } else if (ch == 92) { // backslash
                buf.append("\\\\");

            } else if (ch == 124) { // vertical bar
                // 124 = "|" = AbstractSerializationStream.RPC_SEPARATOR_CHAR
                buf.append("\\!");

            } else if ((ch >= 0xD800) && (ch < 0xFFFF)) {
                buf.append(String.format("\\u%04x", ch));

            } else {
                buf.append((char) ch);
            }
        }

        return buf.toString();
    }