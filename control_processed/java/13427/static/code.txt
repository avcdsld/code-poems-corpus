public void map(final UserResource user, final Principal p,
                    final Credential credential) {
        user.setUserName(p.getId());
        if (credential instanceof UsernamePasswordCredential) {
            user.setPassword(UsernamePasswordCredential.class.cast(credential).getPassword());
        }
        user.setActive(Boolean.TRUE);

        user.setNickName(getPrincipalAttributeValue(p, "nickName"));
        user.setDisplayName(getPrincipalAttributeValue(p, "displayName"));

        val name = new Name(getPrincipalAttributeValue(p, "formattedName"),
            getPrincipalAttributeValue(p, "familyName"),
            getPrincipalAttributeValue(p, "middleName"),
            getPrincipalAttributeValue(p, "givenName"),
            getPrincipalAttributeValue(p, "honorificPrefix"),
            getPrincipalAttributeValue(p, "honorificSuffix"));
        user.setName(name);

        val entry = new Entry(getPrincipalAttributeValue(p, "mail"), "primary");
        user.setEmails(CollectionUtils.wrap(entry));

        val entry2 = new Entry(getPrincipalAttributeValue(p, "phoneNumber"), "primary");
        user.setPhoneNumbers(CollectionUtils.wrap(entry2));
    }