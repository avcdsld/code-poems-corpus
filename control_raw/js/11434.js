async function tryTemplateShorthand(templateName: string) {
  if (templateName.match(FILE_PROTOCOL) || templateName.match(HTTP_PROTOCOL)) {
    return templateName;
  }
  try {
    const reactNativeTemplatePackage = `react-native-template-${templateName}`;
    const response = await fetch(
      `https://registry.yarnpkg.com/${reactNativeTemplatePackage}/latest`,
    );

    if (JSON.parse(response).name) {
      return reactNativeTemplatePackage;
    }
  } catch (e) {
    // we expect this to fail when `file://` protocol or regular module is passed
  }
  return templateName;
}