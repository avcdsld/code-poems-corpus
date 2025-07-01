public void setAdminAddress(@CheckForNull String adminAddress) {
        String address = Util.nullify(adminAddress);
        if(address != null && address.startsWith("\"") && address.endsWith("\"")) {
            // some users apparently quote the whole thing. Don't know why
            // anyone does this, but it's a machine's job to forgive human mistake
            address = address.substring(1,address.length()-1);
        }
        this.adminAddress = address;
        save();
    }