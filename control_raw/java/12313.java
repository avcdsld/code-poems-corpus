public static void checkGoodName(String name) throws Failure {
        if(name==null || name.length()==0)
            throw new Failure(Messages.Hudson_NoName());

        if(".".equals(name.trim()))
            throw new Failure(Messages.Jenkins_NotAllowedName("."));
        if("..".equals(name.trim()))
            throw new Failure(Messages.Jenkins_NotAllowedName(".."));
        for( int i=0; i<name.length(); i++ ) {
            char ch = name.charAt(i);
            if(Character.isISOControl(ch)) {
                throw new Failure(Messages.Hudson_ControlCodeNotAllowed(toPrintableName(name)));
            }
            if("?*/\\%!@#$^&|<>[]:;".indexOf(ch)!=-1)
                throw new Failure(Messages.Hudson_UnsafeChar(ch));
        }

        // looks good
    }