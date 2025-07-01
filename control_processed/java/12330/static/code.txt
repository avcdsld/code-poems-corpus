public void doSignup( StaplerRequest req, StaplerResponse rsp ) throws IOException, ServletException {
        if (getSecurityRealm().allowsSignup()) {
            req.getView(getSecurityRealm(), "signup.jelly").forward(req, rsp);
            return;
        }
        req.getView(SecurityRealm.class, "signup.jelly").forward(req, rsp);
    }