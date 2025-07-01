protected List<MessageDescriptor> getWarnings(final ResponseEntity<?> authenticationResponse) {
        val messageDescriptors = new ArrayList<MessageDescriptor>();

        val passwordExpirationDate = authenticationResponse.getHeaders().getFirstZonedDateTime("X-CAS-PasswordExpirationDate");
        if (passwordExpirationDate != null) {
            val days = Duration.between(Instant.now(), passwordExpirationDate).toDays();
            messageDescriptors.add(new PasswordExpiringWarningMessageDescriptor(null, days));
        }

        val warnings = authenticationResponse.getHeaders().get("X-CAS-Warning");
        if (warnings != null) {
            warnings.stream()
                .map(DefaultMessageDescriptor::new)
                .forEach(messageDescriptors::add);
        }

        return messageDescriptors;
    }