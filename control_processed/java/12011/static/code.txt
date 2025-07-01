@Nonnull
    public UserDetails loadUserByUsername(String idOrFullName) throws UsernameNotFoundException, DataAccessException, ExecutionException {
        Boolean exists = existenceCache.getIfPresent(idOrFullName);
        if(exists != null && !exists) {
            throw new UsernameNotFoundException(String.format("\"%s\" does not exist", idOrFullName));
        } else {
            try {
                return detailsCache.get(idOrFullName, new Retriever(idOrFullName));
            } catch (ExecutionException | UncheckedExecutionException e) {
                if (e.getCause() instanceof UsernameNotFoundException) {
                    throw ((UsernameNotFoundException)e.getCause());
                } else if (e.getCause() instanceof DataAccessException) {
                    throw ((DataAccessException)e.getCause());
                } else {
                    throw e;
                }
            }
        }
    }