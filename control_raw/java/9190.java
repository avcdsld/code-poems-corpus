private static Object typeCast(String str) {
        if (str == null || str.equals("")) {
            return null;
        }
        // Try to cast to boolean true
        for (String trueString : trueArray) {
            if (trueString.equals(str)) {
                return true;
            }
        }
        // Try to cast to boolean false
        for (String falseString : falseArray) {
            if (falseString.equals(str)) {
                return false;
            }
        }
        // Strings that cannot cast to int or double are treated as string
        try {
            return Integer.parseInt(str);
        } catch (Exception e1) {
            try {
                return Double.parseDouble(str);
            } catch (Exception e2) {
                return str;
            }
        }
    }