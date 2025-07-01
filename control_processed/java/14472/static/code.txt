public void put(final Ticket ticket, final Ticket encodedTicket) {
        val metadata = this.ticketCatalog.find(ticket);
        val values = buildTableAttributeValuesMapFromTicket(ticket, encodedTicket);
        LOGGER.debug("Adding ticket id [{}] with attribute values [{}]", encodedTicket.getId(), values);
        val putItemRequest = new PutItemRequest(metadata.getProperties().getStorageName(), values);
        LOGGER.debug("Submitting put request [{}] for ticket id [{}]", putItemRequest, encodedTicket.getId());
        val putItemResult = amazonDynamoDBClient.putItem(putItemRequest);
        LOGGER.debug("Ticket added with result [{}]", putItemResult);
        getAll();
    }