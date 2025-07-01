public User createAccountWithHashedPassword(String userName, String hashedPassword) throws IOException {
        if (!PASSWORD_ENCODER.isPasswordHashed(hashedPassword)) {
            throw new IllegalArgumentException("this method should only be called with a pre-hashed password");
        }
        User user = User.getById(userName, true);
        user.addProperty(Details.fromHashedPassword(hashedPassword));
        SecurityListener.fireUserCreated(user.getId());
        return user;
    }