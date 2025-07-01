function onDocumentClick(event) {
        var element = event.target;
        if (element && element.hasAttribute('data-brackets-id')) {
            MessageBroker.send({"tagId": element.getAttribute('data-brackets-id')});
        }
    }