@Override
    public long size() {
        try {
            val response = getSearchResultResponse();
            if (LdapUtils.containsResultEntry(response)) {
                return response.getResult().getEntries()
                    .stream()
                    .map(this.ldapServiceMapper::mapToRegisteredService)
                    .filter(Objects::nonNull).count();
            }
        } catch (final LdapException e) {
            LOGGER.error(e.getMessage(), e);
        }
        return 0;
    }