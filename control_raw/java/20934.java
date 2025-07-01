protected ExtensionHttpSessions getExtensionHttpSessions() {
		if(extensionHttpSessions==null){
			extensionHttpSessions = Control.getSingleton().getExtensionLoader().getExtension(ExtensionHttpSessions.class);
		}
		return extensionHttpSessions;
		
	}