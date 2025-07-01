public void doDescription(StaplerRequest req, StaplerResponse rsp)
            throws IOException {
        if (req.getMethod().equals("GET")) {
            //read
            rsp.setContentType("text/plain;charset=UTF-8");
            rsp.getWriter().write(Util.fixNull(this.getDescription()));
            return;
        }
        if (req.getMethod().equals("POST")) {
            checkPermission(CONFIGURE);

            // submission
            if (req.getParameter("description") != null) {
                this.setDescription(req.getParameter("description"));
                rsp.sendError(SC_NO_CONTENT);
                return;
            }
        }

        // huh?
        rsp.sendError(SC_BAD_REQUEST);
    }