async function inferUserDocsDirectory (cwd) {
  const paths = await globby([
    '**/.vuepress/config.js',
    '!node_modules'
  ], {
    cwd,
    dot: true
  })
  const siteConfigPath = paths && paths[0]
  if (siteConfigPath) {
    return path.resolve(
      cwd,
      siteConfigPath.replace('.vuepress/config.js', '')
    )
  }
  return null
}