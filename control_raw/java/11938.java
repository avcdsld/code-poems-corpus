public void reportAsHeaders(HttpServletResponse rsp) {
        rsp.addHeader("X-You-Are-Authenticated-As",authentication.getName());
        if (REPORT_GROUP_HEADERS) {
            for (GrantedAuthority auth : authentication.getAuthorities()) {
                rsp.addHeader("X-You-Are-In-Group",auth.getAuthority());
            }
        } else {
            rsp.addHeader("X-You-Are-In-Group-Disabled", "JENKINS-39402: use -Dhudson.security.AccessDeniedException2.REPORT_GROUP_HEADERS=true or use /whoAmI to diagnose");
        }
        rsp.addHeader("X-Required-Permission", permission.getId());
        for (Permission p=permission.impliedBy; p!=null; p=p.impliedBy) {
            rsp.addHeader("X-Permission-Implied-By", p.getId());
        }
    }