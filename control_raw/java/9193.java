public List<IRequestDumpable> createRequestDumpers(DumpConfig config, HttpServerExchange exchange) {

        RequestDumperFactory factory = new RequestDumperFactory();
        List<IRequestDumpable> dumpers = new ArrayList<>();
        for(String dumperNames: requestDumpers) {
            IRequestDumpable dumper = factory.create(dumperNames, config, exchange);
            dumpers.add(dumper);
        }
        return dumpers;
    }