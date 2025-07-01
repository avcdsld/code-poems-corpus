protected String callRestEndpointForMultifactor(final Principal principal, final Service resolvedService) {
        val restTemplate = new RestTemplate();
        val restEndpoint = casProperties.getAuthn().getMfa().getRestEndpoint();
        val entity = new RestEndpointEntity(principal.getId(), resolvedService.getId());
        val responseEntity = restTemplate.postForEntity(restEndpoint, entity, String.class);
        if (responseEntity.getStatusCode() == HttpStatus.OK) {
            return responseEntity.getBody();
        }
        return null;
    }