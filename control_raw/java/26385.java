public static String hashPassword(String plaintext) {
        String salt = BCrypt.gensalt(workload);
        return BCrypt.hashpw(plaintext, salt);
    }