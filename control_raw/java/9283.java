public static FlatMessage[] messagePartition(FlatMessage flatMessage, Integer partitionsNum, String pkHashConfigs) {
        if (partitionsNum == null) {
            partitionsNum = 1;
        }
        FlatMessage[] partitionMessages = new FlatMessage[partitionsNum];

        if (flatMessage.getIsDdl()) {
            partitionMessages[0] = flatMessage;
        } else {
            if (flatMessage.getData() != null && !flatMessage.getData().isEmpty()) {
                String database = flatMessage.getDatabase();
                String table = flatMessage.getTable();
                HashMode hashMode = getPartitionHashColumns(database + "." + table, pkHashConfigs);
                if (hashMode == null) {
                    // 如果都没有匹配，发送到第一个分区
                    partitionMessages[0] = flatMessage;
                } else if (hashMode.tableHash) {
                    int hashCode = table.hashCode();
                    int pkHash = Math.abs(hashCode) % partitionsNum;
                    // math.abs可能返回负值，这里再取反，把出现负值的数据还是写到固定的分区，仍然可以保证消费顺序
                    pkHash = Math.abs(pkHash);
                    partitionMessages[pkHash] = flatMessage;
                } else {
                    List<String> pkNames = hashMode.pkNames;
                    if (hashMode.autoPkHash) {
                        pkNames = flatMessage.getPkNames();
                    }

                    int idx = 0;
                    for (Map<String, String> row : flatMessage.getData()) {
                        int hashCode = database.hashCode();
                        for (String pkName : pkNames) {
                            String value = row.get(pkName);
                            if (value == null) {
                                value = "";
                            }
                            hashCode = hashCode ^ value.hashCode();
                        }

                        int pkHash = Math.abs(hashCode) % partitionsNum;
                        // math.abs可能返回负值，这里再取反，把出现负值的数据还是写到固定的分区，仍然可以保证消费顺序
                        pkHash = Math.abs(pkHash);

                        FlatMessage flatMessageTmp = partitionMessages[pkHash];
                        if (flatMessageTmp == null) {
                            flatMessageTmp = new FlatMessage(flatMessage.getId());
                            partitionMessages[pkHash] = flatMessageTmp;
                            flatMessageTmp.setDatabase(flatMessage.getDatabase());
                            flatMessageTmp.setTable(flatMessage.getTable());
                            flatMessageTmp.setIsDdl(flatMessage.getIsDdl());
                            flatMessageTmp.setType(flatMessage.getType());
                            flatMessageTmp.setSql(flatMessage.getSql());
                            flatMessageTmp.setSqlType(flatMessage.getSqlType());
                            flatMessageTmp.setMysqlType(flatMessage.getMysqlType());
                            flatMessageTmp.setEs(flatMessage.getEs());
                            flatMessageTmp.setTs(flatMessage.getTs());
                        }
                        List<Map<String, String>> data = flatMessageTmp.getData();
                        if (data == null) {
                            data = new ArrayList<>();
                            flatMessageTmp.setData(data);
                        }
                        data.add(row);
                        if (flatMessage.getOld() != null && !flatMessage.getOld().isEmpty()) {
                            List<Map<String, String>> old = flatMessageTmp.getOld();
                            if (old == null) {
                                old = new ArrayList<>();
                                flatMessageTmp.setOld(old);
                            }
                            old.add(flatMessage.getOld().get(idx));
                        }
                        idx++;
                    }
                }
            } else {
                // 针对stmt/mixed binlog格式的query事件
                partitionMessages[0] = flatMessage;
            }
        }
        return partitionMessages;
    }