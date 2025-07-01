public int removeScriptsFromDir (File dir) {
		logger.debug("Removing scripts from dir: " + dir.getAbsolutePath());
		trackedDirs.remove(dir);
		int removedScripts = 0;
		
		for (ScriptType type : this.getScriptTypes()) {
			
			
			File locDir = new File(dir, type.getName());
			if (locDir.exists()) {
				// Loop through all of the known scripts and templates 
				// removing any from this directory
				for (ScriptWrapper sw : this.getScripts(type)) {
					if (isSavedInDir(sw, locDir)) {
						this.removeScript(sw);
						removedScripts++;
					}
				}
				for (ScriptWrapper sw : this.getTemplates(type)) {
					if (isSavedInDir(sw, locDir)) {
						this.removeTemplate(sw);
						removedScripts++;
					}
				}
			}
		}
		return removedScripts;
	}