public StaticInfo readStatic() throws IOException {

        List<Pair<UIStaticInfoRecord, Table>> out = new ArrayList<>();
        boolean allStaticRead = false;
        try (RandomAccessFile f = new RandomAccessFile(file, "r"); FileChannel fc = f.getChannel()) {
            f.seek(0);
            while (!allStaticRead) {

                //read 2 header ints
                int lengthHeader = f.readInt();
                int lengthContent = f.readInt();

                //Read header
                ByteBuffer bb = ByteBuffer.allocate(lengthHeader);
                f.getChannel().read(bb);
                bb.flip();      //Flip for reading
                UIStaticInfoRecord r = UIStaticInfoRecord.getRootAsUIStaticInfoRecord(bb);

                //Read content
                bb = ByteBuffer.allocate(lengthContent);
                f.getChannel().read(bb);
                bb.flip();      //Flip for reading

                byte infoType = r.infoType();
                Table t;
                switch (infoType) {
                    case UIInfoType.GRAPH_STRUCTURE:
                        t = UIGraphStructure.getRootAsUIGraphStructure(bb);
                        break;
                    case UIInfoType.SYTEM_INFO:
                        t = UISystemInfo.getRootAsUISystemInfo(bb);
                        break;
                    case UIInfoType.START_EVENTS:
                        t = null;
                        break;
                    default:
                        throw new RuntimeException("Unknown UI static info type: " + r.infoType());
                }

                //TODO do we need to close file here?

                out.add(new Pair<>(r, t));
                long pointer = f.getFilePointer();
                long length = f.length();
                {
                    log.trace("File pointer = {}, file length = {}", pointer, length);
                    if (infoType == UIInfoType.START_EVENTS || pointer >= length) {
                        allStaticRead = true;
                    }
                }
            }
            StaticInfo s = new StaticInfo(out, f.getFilePointer());
            return s;
        }
    }