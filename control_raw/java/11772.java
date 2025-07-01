@Deprecated
    @CheckForNull
    public Computer getComputer() {
        for( Computer c : Jenkins.getInstance().getComputers() )
            if(c.getChannel()==channel)
                return c;
        return null;
    }