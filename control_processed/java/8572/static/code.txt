public static void setCronSetting(String cronSettingPath) {
		try {
			crontabSetting = new Setting(cronSettingPath, Setting.DEFAULT_CHARSET, false);
		} catch (SettingRuntimeException | NoResourceException e) {
			// ignore setting file parse error and no config error
		}
	}