static void verifyItemDoesNotAlreadyExist(@Nonnull ItemGroup<?> parent, @Nonnull String newName, @CheckForNull Item variant) throws IllegalArgumentException, Failure {
        Item existing;
        try (ACLContext ctxt = ACL.as(ACL.SYSTEM)) {
            existing = parent.getItem(newName);
        }
        if (existing != null && existing != variant) {
            if (existing.hasPermission(Item.DISCOVER)) {
                String prefix = parent.getFullName();
                throw new IllegalArgumentException((prefix.isEmpty() ? "" : prefix + "/") + newName + " already exists");
            } else {
                // Cannot hide its existence, so at least be as vague as possible.
                throw new Failure("");
            }
        }
    }