private boolean loadBaseAndCheck(String path)
    {
        try
        {
            DataInputStream in = new DataInputStream(new BufferedInputStream(IOAdapter == null ?
                                                                                     new FileInputStream(path) :
                    IOAdapter.open(path)
            ));
            size = in.readInt();
            base = new int[size + 65535];   // 多留一些，防止越界
            check = new int[size + 65535];
            for (int i = 0; i < size; i++)
            {
                base[i] = in.readInt();
                check[i] = in.readInt();
            }
        }
        catch (Exception e)
        {
            return false;
        }
        return true;
    }