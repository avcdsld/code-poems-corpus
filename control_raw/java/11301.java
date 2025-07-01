public boolean valueExists(String name) {
        IntByReference pType, lpcbData;
        byte[] lpData = new byte[1];

        pType = new IntByReference();
        lpcbData = new IntByReference();

        OUTER:
        while(true) {
            int r = Advapi32.INSTANCE.RegQueryValueEx(handle, name, null, pType, lpData, lpcbData);
            switch(r) {
            case WINERROR.ERROR_MORE_DATA:
                lpData = new byte[lpcbData.getValue()];
                continue OUTER;
            case WINERROR.ERROR_FILE_NOT_FOUND:
                return false;
            case WINERROR.ERROR_SUCCESS:
                return true;
            default:
                throw new JnaException(r);
            }
        }
    }