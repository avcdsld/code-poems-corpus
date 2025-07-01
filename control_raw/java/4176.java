public static void logEnvironmentInfo(Logger log, String componentName, String[] commandLineArgs) {
		if (log.isInfoEnabled()) {
			RevisionInformation rev = getRevisionInformation();
			String version = getVersion();
			
			String jvmVersion = getJvmVersion();
			String[] options = getJvmStartupOptionsArray();
			
			String javaHome = System.getenv("JAVA_HOME");
			
			long maxHeapMegabytes = getMaxJvmHeapMemory() >>> 20;
			
			log.info("--------------------------------------------------------------------------------");
			log.info(" Starting " + componentName + " (Version: " + version + ", "
					+ "Rev:" + rev.commitId + ", " + "Date:" + rev.commitDate + ")");
			log.info(" OS current user: " + System.getProperty("user.name"));
			log.info(" Current Hadoop/Kerberos user: " + getHadoopUser());
			log.info(" JVM: " + jvmVersion);
			log.info(" Maximum heap size: " + maxHeapMegabytes + " MiBytes");
			log.info(" JAVA_HOME: " + (javaHome == null ? "(not set)" : javaHome));

			String hadoopVersionString = getHadoopVersionString();
			if (hadoopVersionString != null) {
				log.info(" Hadoop version: " + hadoopVersionString);
			} else {
				log.info(" No Hadoop Dependency available");
			}

			if (options.length == 0) {
				log.info(" JVM Options: (none)");
			}
			else {
				log.info(" JVM Options:");
				for (String s: options) {
					log.info("    " + s);
				}
			}

			if (commandLineArgs == null || commandLineArgs.length == 0) {
				log.info(" Program Arguments: (none)");
			}
			else {
				log.info(" Program Arguments:");
				for (String s: commandLineArgs) {
					log.info("    " + s);
				}
			}

			log.info(" Classpath: " + System.getProperty("java.class.path"));

			log.info("--------------------------------------------------------------------------------");
		}
	}