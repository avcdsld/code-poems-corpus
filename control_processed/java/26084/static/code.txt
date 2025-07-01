public ExternalStorageLocation getExternalStorageLocation(String path, String operation, String type) {
        try {
            ExternalPayloadStorage.Operation payloadOperation = ExternalPayloadStorage.Operation.valueOf(StringUtils.upperCase(operation));
            ExternalPayloadStorage.PayloadType payloadType = ExternalPayloadStorage.PayloadType.valueOf(StringUtils.upperCase(type));
            return executionService.getExternalStorageLocation(payloadOperation, payloadType, path);
        } catch (Exception e) {
            // FIXME: for backwards compatibility
            LOGGER.error("Invalid input - Operation: {}, PayloadType: {}, defaulting to WRITE/TASK_OUTPUT", operation, type);
            return executionService.getExternalStorageLocation(ExternalPayloadStorage.Operation.WRITE, ExternalPayloadStorage.PayloadType.TASK_OUTPUT, path);
        }
    }