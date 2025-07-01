public static void displayByteArray(byte[] record) {
        int i;
        for (i = 0; i < record.length - 1; i++) {
            if (i % 16 == 0) {
                System.out.println();
            }
            System.out.print(Integer.toHexString(record[i] >> 4 & 0x0F));
            System.out.print(Integer.toHexString(record[i] & 0x0F));
            System.out.print(",");
        }
        System.out.print(Integer.toHexString(record[i] >> 4 & 0x0F));
        System.out.print(Integer.toHexString(record[i] & 0x0F));
        System.out.println();
    }