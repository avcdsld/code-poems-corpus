public static String identifyDriver(String nameContainsProductInfo) {
		if (StrUtil.isBlank(nameContainsProductInfo)) {
			return null;
		}
		// 全部转为小写，忽略大小写
		nameContainsProductInfo = StrUtil.cleanBlank(nameContainsProductInfo.toLowerCase());

		String driver = null;
		if (nameContainsProductInfo.contains("mysql")) {
			driver = ClassLoaderUtil.isPresent(DRIVER_MYSQL_V6) ? DRIVER_MYSQL_V6 : DRIVER_MYSQL;
		} else if (nameContainsProductInfo.contains("oracle")) {
			driver = ClassLoaderUtil.isPresent(DRIVER_ORACLE) ? DRIVER_ORACLE : DRIVER_ORACLE_OLD;
		} else if (nameContainsProductInfo.contains("postgresql")) {
			driver = DRIVER_POSTGRESQL;
		} else if (nameContainsProductInfo.contains("sqlite")) {
			driver = DRIVER_SQLLITE3;
		} else if (nameContainsProductInfo.contains("sqlserver")) {
			driver = DRIVER_SQLSERVER;
		} else if (nameContainsProductInfo.contains("hive")) {
			driver = DRIVER_HIVE;
		} else if (nameContainsProductInfo.contains("h2")) {
			driver = DRIVER_H2;
		} else if (nameContainsProductInfo.startsWith("jdbc:derby://")) {
			// Derby数据库网络连接方式
			driver = DRIVER_DERBY;
		} else if (nameContainsProductInfo.contains("derby")) {
			// 嵌入式Derby数据库
			driver = DRIVER_DERBY_EMBEDDED;
		} else if (nameContainsProductInfo.contains("hsqldb")) {
			// HSQLDB
			driver = DRIVER_HSQLDB;
		} else if (nameContainsProductInfo.contains("dm")) {
			// 达梦7
			driver = DRIVER_DM7;
		}

		return driver;
	}