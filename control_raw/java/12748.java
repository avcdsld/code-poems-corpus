@JsonIgnore
    public String getId() {
        if (instanceId != null && !instanceId.isEmpty()) {
            return instanceId;
        } else if (dataCenterInfo instanceof UniqueIdentifier) {
            String uniqueId = ((UniqueIdentifier) dataCenterInfo).getId();
            if (uniqueId != null && !uniqueId.isEmpty()) {
                return uniqueId;
            }
        }
        return hostName;
    }