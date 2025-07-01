private String buildPosition(String journalName, Long position, Long timestamp) {
        StringBuilder masterBuilder = new StringBuilder();
        if (StringUtils.isNotEmpty(journalName) || position != null || timestamp != null) {
            masterBuilder.append('{');
            if (StringUtils.isNotEmpty(journalName)) {
                masterBuilder.append("\"journalName\":\"").append(journalName).append("\"");
            }

            if (position != null) {
                if (masterBuilder.length() > 1) {
                    masterBuilder.append(",");
                }
                masterBuilder.append("\"position\":").append(position);
            }

            if (timestamp != null) {
                if (masterBuilder.length() > 1) {
                    masterBuilder.append(",");
                }
                masterBuilder.append("\"timestamp\":").append(timestamp);
            }
            masterBuilder.append('}');
            return masterBuilder.toString();
        } else {
            return null;
        }
    }