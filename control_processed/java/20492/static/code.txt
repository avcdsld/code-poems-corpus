private static boolean startsWith(char[] array, char[] prefix) {
        if (prefix == null) {
            return true;
        }

        if (array == null) {
            return false;
        }

        int length = prefix.length;
        if (array.length < length) {
            return false;
        }

        for (int i = 0; i < length; i++) {
            if (prefix[i] != array[i]) {
                return false;
            }
        }

        return true;
    }