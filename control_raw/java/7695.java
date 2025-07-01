public static Db use(DataSource ds, String driverClassName) {
		return new Db(ds, DialectFactory.newDialect(driverClassName));
	}