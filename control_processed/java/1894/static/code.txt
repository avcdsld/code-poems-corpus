public static List<CharSequence> unescapeCsvFields(CharSequence value) {
        List<CharSequence> unescaped = new ArrayList<CharSequence>(2);
        StringBuilder current = InternalThreadLocalMap.get().stringBuilder();
        boolean quoted = false;
        int last = value.length() - 1;
        for (int i = 0; i <= last; i++) {
            char c = value.charAt(i);
            if (quoted) {
                switch (c) {
                    case DOUBLE_QUOTE:
                        if (i == last) {
                            // Add the last field and return
                            unescaped.add(current.toString());
                            return unescaped;
                        }
                        char next = value.charAt(++i);
                        if (next == DOUBLE_QUOTE) {
                            // 2 double-quotes should be unescaped to one
                            current.append(DOUBLE_QUOTE);
                            break;
                        }
                        if (next == COMMA) {
                            // This is the end of a field. Let's start to parse the next field.
                            quoted = false;
                            unescaped.add(current.toString());
                            current.setLength(0);
                            break;
                        }
                        // double-quote followed by other character is invalid
                        throw newInvalidEscapedCsvFieldException(value, i - 1);
                    default:
                        current.append(c);
                }
            } else {
                switch (c) {
                    case COMMA:
                        // Start to parse the next field
                        unescaped.add(current.toString());
                        current.setLength(0);
                        break;
                    case DOUBLE_QUOTE:
                        if (current.length() == 0) {
                            quoted = true;
                            break;
                        }
                        // double-quote appears without being enclosed with double-quotes
                        // fall through
                    case LINE_FEED:
                        // fall through
                    case CARRIAGE_RETURN:
                        // special characters appears without being enclosed with double-quotes
                        throw newInvalidEscapedCsvFieldException(value, i);
                    default:
                        current.append(c);
                }
            }
        }
        if (quoted) {
            throw newInvalidEscapedCsvFieldException(value, last);
        }
        unescaped.add(current.toString());
        return unescaped;
    }