protected boolean doesStartingTimeAllowServiceAccess() {
        if (this.startingDateTime != null) {
            val st = DateTimeUtils.zonedDateTimeOf(this.startingDateTime);
            if (st != null) {
                val now = ZonedDateTime.now(ZoneOffset.UTC);
                if (now.isBefore(st)) {
                    LOGGER.warn("Service access not allowed because it starts at [{}]. Zoned now is [{}]", this.startingDateTime, now);
                    return false;
                }
            } else {
                val stLocal = DateTimeUtils.localDateTimeOf(this.startingDateTime);
                if (stLocal != null) {
                    val now = LocalDateTime.now(ZoneOffset.UTC);
                    if (now.isBefore(stLocal)) {
                        LOGGER.warn("Service access not allowed because it starts at [{}]. Local now is [{}]", this.startingDateTime, now);
                        return false;
                    }
                }
            }
        }
        return true;
    }