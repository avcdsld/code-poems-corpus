public static String captchaChar(int length, boolean caseSensitivity) {
        StringBuilder sb       = new StringBuilder();
        Random        rand     = new Random();// 随机用以下三个随机生成器
        Random        randdata = new Random();
        int           data     = 0;
        for (int i = 0; i < length; i++) {
            int index = rand.nextInt(caseSensitivity ? 3 : 2);
            // 目的是随机选择生成数字，大小写字母
            switch (index) {
                case 0:
                    data = randdata.nextInt(10);// 仅仅会生成0~9, 0~9的ASCII为48~57
                    sb.append(data);
                    break;
                case 1:
                    data = randdata.nextInt(26) + 97;// 保证只会产生ASCII为97~122(a-z)之间的整数,
                    sb.append((char) data);
                    break;
                case 2: // caseSensitivity为true的时候, 才会有大写字母
                    data = randdata.nextInt(26) + 65;// 保证只会产生ASCII为65~90(A~Z)之间的整数
                    sb.append((char) data);
                    break;
                default:
                    break;
            }
        }
        return sb.toString();
    }