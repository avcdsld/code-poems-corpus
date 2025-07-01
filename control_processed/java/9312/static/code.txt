private Long findTransactionBeginPosition(ErosaConnection mysqlConnection, final EntryPosition entryPosition)
                                                                                                                 throws IOException {
        // 针对开始的第一条为非Begin记录，需要从该binlog扫描
        final java.util.concurrent.atomic.AtomicLong preTransactionStartPosition = new java.util.concurrent.atomic.AtomicLong(0L);
        mysqlConnection.reconnect();
        mysqlConnection.seek(entryPosition.getJournalName(), 4L, entryPosition.getGtid(), new SinkFunction<LogEvent>() {

            private LogPosition lastPosition;

            public boolean sink(LogEvent event) {
                try {
                    CanalEntry.Entry entry = parseAndProfilingIfNecessary(event, true);
                    if (entry == null) {
                        return true;
                    }

                    // 直接查询第一条业务数据，确认是否为事务Begin
                    // 记录一下transaction begin position
                    if (entry.getEntryType() == CanalEntry.EntryType.TRANSACTIONBEGIN
                        && entry.getHeader().getLogfileOffset() < entryPosition.getPosition()) {
                        preTransactionStartPosition.set(entry.getHeader().getLogfileOffset());
                    }

                    if (entry.getHeader().getLogfileOffset() >= entryPosition.getPosition()) {
                        return false;// 退出
                    }

                    lastPosition = buildLastPosition(entry);
                } catch (Exception e) {
                    processSinkError(e, lastPosition, entryPosition.getJournalName(), entryPosition.getPosition());
                    return false;
                }

                return running;
            }
        });

        // 判断一下找到的最接近position的事务头的位置
        if (preTransactionStartPosition.get() > entryPosition.getPosition()) {
            logger.error("preTransactionEndPosition greater than startPosition from zk or localconf, maybe lost data");
            throw new CanalParseException("preTransactionStartPosition greater than startPosition from zk or localconf, maybe lost data");
        }
        return preTransactionStartPosition.get();
    }