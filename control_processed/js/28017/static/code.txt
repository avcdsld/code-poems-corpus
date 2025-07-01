async function assignLangToWebpackConfig(config, lang) {
  let langSpecificConfig = config;

  if (lang) {
    langSpecificConfig.lang = lang; // Make sure only ONE language config is set per Webpack build instance.
  }

  let langSpecificWebpackConfig = await createWebpackConfig(langSpecificConfig);

  if (langSpecificConfig.webpackStats) {
    langSpecificWebpackConfig.profile = true;
    langSpecificWebpackConfig.parallelism = 1;
  }

  webpackConfigs.push(langSpecificWebpackConfig);
}