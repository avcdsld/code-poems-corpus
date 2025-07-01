@SneakyThrows
    public static void printAsciiArt(final PrintStream out, final String asciiArt, final String additional) {
        out.println(ANSI_CYAN);
        if (StringUtils.isNotBlank(additional)) {
            out.println(FigletFont.convertOneLine(asciiArt));
            out.println(additional);
        } else {
            out.print(FigletFont.convertOneLine(asciiArt));
        }
        out.println(ANSI_RESET);
    }