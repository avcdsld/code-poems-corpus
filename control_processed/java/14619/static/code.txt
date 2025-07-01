@PostMapping(value = "/v1/tickets", consumes = MediaType.APPLICATION_FORM_URLENCODED_VALUE)
    public ResponseEntity<String> createTicketGrantingTicket(@RequestBody(required=false) final MultiValueMap<String, String> requestBody,
                                                             final HttpServletRequest request) {
        try {
            val tgtId = createTicketGrantingTicketForRequest(requestBody, request);
            return createResponseEntityForTicket(request, tgtId);
        } catch (final AuthenticationException e) {
            return RestResourceUtils.createResponseEntityForAuthnFailure(e, request, applicationContext);
        } catch (final BadRestRequestException e) {
            LOGGER.error(e.getMessage(), e);
            return new ResponseEntity<>(e.getMessage(), HttpStatus.BAD_REQUEST);
        } catch (final Exception e) {
            LOGGER.error(e.getMessage(), e);
            return new ResponseEntity<>(e.getMessage(), HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }