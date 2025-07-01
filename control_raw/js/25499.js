function writeApplicationFileForMultipleApplications(application) {
  const applicationBaseName = application[GENERATOR_NAME].baseName;
  checkPath(applicationBaseName);
  createFolderIfNeeded(applicationBaseName);
  writeConfigFile(application, path.join(applicationBaseName, '.yo-rc.json'));
}