public static RedissonRxClient createRx() {
        Config config = new Config();
        config.useSingleServer().setAddress("redis://127.0.0.1:6379");
        return createRx(config);
    }