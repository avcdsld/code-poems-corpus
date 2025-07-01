public String determineUrl() {
		if (StringUtils.hasText(this.url)) {
			return this.url;
		}
		String databaseName = determineDatabaseName();
		String url = (databaseName != null)
				? this.embeddedDatabaseConnection.getUrl(databaseName) : null;
		if (!StringUtils.hasText(url)) {
			throw new DataSourceBeanCreationException(
					"Failed to determine suitable jdbc url", this,
					this.embeddedDatabaseConnection);
		}
		return url;
	}