@SneakyThrows
    public void commitAll(final String message) {
        this.gitInstance.add().addFilepattern(".").call();
        this.gitInstance.commit()
            .setMessage(message)
            .setAll(true)
            .setAuthor("CAS", "cas@apereo.org")
            .call();
    }