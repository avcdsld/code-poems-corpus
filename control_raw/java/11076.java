protected void respond(StaplerResponse rsp, String html) throws IOException, ServletException {
        rsp.setContentType("text/html;charset=UTF-8");
        rsp.getWriter().print(html);
    }