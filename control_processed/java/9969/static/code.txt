public static PostgreSQLCommandPacket newInstance(
            final PostgreSQLCommandPacketType commandPacketType, final PostgreSQLPacketPayload payload, final int connectionId) throws SQLException {
        switch (commandPacketType) {
            case QUERY:
                return new PostgreSQLComQueryPacket(payload);
            case PARSE:
                return new PostgreSQLComParsePacket(payload);
            case BIND:
                return new PostgreSQLComBindPacket(payload, connectionId);
            case DESCRIBE:
                return new PostgreSQLComDescribePacket(payload);
            case EXECUTE:
                return new PostgreSQLComExecutePacket(payload);
            case SYNC:
                return new PostgreSQLComSyncPacket(payload);
            case TERMINATE:
                return new PostgreSQLComTerminationPacket(payload);
            default:
                return new PostgreSQLUnsupportedCommandPacket(commandPacketType.getValue());
        }
    }