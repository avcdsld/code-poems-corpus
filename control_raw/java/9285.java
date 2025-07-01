public void seek(String binlogfilename, Long binlogPosition, String gtid, SinkFunction func) throws IOException {
        updateSettings();
        loadBinlogChecksum();
        sendBinlogDump(binlogfilename, binlogPosition);
        DirectLogFetcher fetcher = new DirectLogFetcher(connector.getReceiveBufferSize());
        fetcher.start(connector.getChannel());
        LogDecoder decoder = new LogDecoder();
        decoder.handle(LogEvent.ROTATE_EVENT);
        decoder.handle(LogEvent.FORMAT_DESCRIPTION_EVENT);
        decoder.handle(LogEvent.QUERY_EVENT);
        decoder.handle(LogEvent.XID_EVENT);
        LogContext context = new LogContext();
        // 若entry position存在gtid，则使用传入的gtid作为gtidSet
        // 拼接的标准,否则同时开启gtid和tsdb时，会导致丢失gtid
        // 而当源端数据库gtid 有purged时会有如下类似报错
        // 'errno = 1236, sqlstate = HY000 errmsg = The slave is connecting
        // using CHANGE MASTER TO MASTER_AUTO_POSITION = 1 ...
        if (StringUtils.isNotEmpty(gtid)) {
            decoder.handle(LogEvent.GTID_LOG_EVENT);
            context.setGtidSet(MysqlGTIDSet.parse(gtid));
        }
        context.setFormatDescription(new FormatDescriptionLogEvent(4, binlogChecksum));
        while (fetcher.fetch()) {
            accumulateReceivedBytes(fetcher.limit());
            LogEvent event = null;
            event = decoder.decode(fetcher, context);

            if (event == null) {
                throw new CanalParseException("parse failed");
            }

            if (!func.sink(event)) {
                break;
            }
        }
    }