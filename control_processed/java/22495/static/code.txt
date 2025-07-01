private StringBuffer getArgsString(Object[] args) {
        StringBuffer buffer = new StringBuffer();
        String prefix = "args ";
        for (int i = 0; i < args.length; i++) {
            if (args.length > 1) {
                buffer.append(prefix + (i + 1));
            }
            buffer.append("\r\t");
            buffer.append(getResultString(args[i]));
            buffer.append("\n");
        }
        return buffer;
    }