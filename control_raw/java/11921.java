@RequirePOST
    public HttpResponse doAct(StaplerRequest req) throws ServletException, IOException {
        Jenkins.getInstance().checkPermission(Jenkins.ADMINISTER);

        if(req.hasParameter("n")) {
            // we'll shut up
            disable(true);
            return HttpResponses.redirectViaContextPath("/manage");
        }

        return new HttpRedirect("confirm");
    }