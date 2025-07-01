@SuppressWarnings("unchecked")
    public static Message[] messagePartition(Message message, Integer partitionsNum, String pkHashConfigs) {
        if (partitionsNum == null) {
            partitionsNum = 1;
        }
        Message[] partitionMessages = new Message[partitionsNum];
        List<Entry>[] partitionEntries = new List[partitionsNum];
        for (int i = 0; i < partitionsNum; i++) {
            partitionEntries[i] = new ArrayList<>();
        }

        List<CanalEntry.Entry> entries;
        if (message.isRaw()) {
            List<ByteString> rawEntries = message.getRawEntries();
            entries = new ArrayList<>(rawEntries.size());
            for (ByteString byteString : rawEntries) {
                Entry entry;
                try {
                    entry = Entry.parseFrom(byteString);
                } catch (InvalidProtocolBufferException e) {
                    throw new RuntimeException(e);
                }
                entries.add(entry);
            }
        } else {
            entries = message.getEntries();
        }

        for (Entry entry : entries) {
            CanalEntry.RowChange rowChange;
            try {
                rowChange = CanalEntry.RowChange.parseFrom(entry.getStoreValue());
            } catch (Exception e) {
                throw new RuntimeException(e.getMessage(), e);
            }

            if (rowChange.getIsDdl()) {
                partitionEntries[0].add(entry);
            } else {
                if (rowChange.getRowDatasList() != null && !rowChange.getRowDatasList().isEmpty()) {
                    String database = entry.getHeader().getSchemaName();
                    String table = entry.getHeader().getTableName();
                    HashMode hashMode = getPartitionHashColumns(database + "." + table, pkHashConfigs);
                    if (hashMode == null) {
                        // 如果都没有匹配，发送到第一个分区
                        partitionEntries[0].add(entry);
                    } else if (hashMode.tableHash) {
                        int hashCode = table.hashCode();
                        int pkHash = Math.abs(hashCode) % partitionsNum;
                        pkHash = Math.abs(pkHash);
                        // tableHash not need split entry message
                        partitionEntries[pkHash].add(entry);
                    } else {
                        for (CanalEntry.RowData rowData : rowChange.getRowDatasList()) {
                            int hashCode = database.hashCode();
                            if (hashMode.autoPkHash) {
                                // isEmpty use default pkNames
                                for (CanalEntry.Column column : rowData.getAfterColumnsList()) {
                                    if (column.getIsKey()) {
                                        hashCode = hashCode ^ column.getValue().hashCode();
                                    }
                                }
                            } else {
                                for (CanalEntry.Column column : rowData.getAfterColumnsList()) {
                                    if (checkPkNamesHasContain(hashMode.pkNames, column.getName())) {
                                        hashCode = hashCode ^ column.getValue().hashCode();
                                    }
                                }
                            }

                            int pkHash = Math.abs(hashCode) % partitionsNum;
                            pkHash = Math.abs(pkHash);
                            // build new entry
                            Entry.Builder builder = Entry.newBuilder(entry);
                            RowChange.Builder rowChangeBuilder = RowChange.newBuilder(rowChange);
                            rowChangeBuilder.clearRowDatas();
                            rowChangeBuilder.addRowDatas(rowData);
                            builder.clearStoreValue();
                            builder.setStoreValue(rowChangeBuilder.build().toByteString());
                            partitionEntries[pkHash].add(builder.build());
                        }
                    }
                } else {
                    // 针对stmt/mixed binlog格式的query事件
                    partitionEntries[0].add(entry);
                }
            }
        }

        for (int i = 0; i < partitionsNum; i++) {
            List<Entry> entriesTmp = partitionEntries[i];
            if (!entriesTmp.isEmpty()) {
                partitionMessages[i] = new Message(message.getId(), entriesTmp);
            }
        }

        return partitionMessages;
    }