public void error(String format, Object... args) throws IOException, ServletException {
        error(String.format(format,args));
    }