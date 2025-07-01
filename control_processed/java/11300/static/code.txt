public void setValue(String name, int value) {
        byte[] data = new byte[4];
        data[0] = (byte) (value & 0xff);
        data[1] = (byte) ((value >> 8) & 0xff);
        data[2] = (byte) ((value >> 16) & 0xff);
        data[3] = (byte) ((value >> 24) & 0xff);

        check(Advapi32.INSTANCE.RegSetValueEx(handle, name, 0, WINNT.REG_DWORD, data, data.length));
    }