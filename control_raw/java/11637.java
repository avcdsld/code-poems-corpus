public void doLogout(StaplerRequest req, StaplerResponse rsp) throws IOException, ServletException {
        HttpSession session = req.getSession(false);
        if(session!=null)
            session.invalidate();
        Authentication auth = SecurityContextHolder.getContext().getAuthentication();
        SecurityContextHolder.clearContext();

        // reset remember-me cookie
        Cookie cookie = new Cookie(ACEGI_SECURITY_HASHED_REMEMBER_ME_COOKIE_KEY,"");
        cookie.setMaxAge(0);
        cookie.setSecure(req.isSecure());
        cookie.setHttpOnly(true);
        cookie.setPath(req.getContextPath().length()>0 ? req.getContextPath() : "/");
        rsp.addCookie(cookie);

        rsp.sendRedirect2(getPostLogOutUrl(req,auth));
    }