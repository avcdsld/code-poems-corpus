function processRelease (argv, gyp, defaultVersion, defaultRelease) {
  var version = (semver.valid(argv[0]) && argv[0]) || gyp.opts.target || defaultVersion
    , versionSemver = semver.parse(version)
    , overrideDistUrl = gyp.opts['dist-url'] || gyp.opts.disturl
    , isDefaultVersion
    , name
    , distBaseUrl
    , baseUrl
    , libUrl32
    , libUrl64
    , tarballUrl
    , canGetHeaders

  if (!versionSemver) {
    // not a valid semver string, nothing we can do
    return { version: version }
  }
  // flatten version into String
  version = versionSemver.version

  // defaultVersion should come from process.version so ought to be valid semver
  isDefaultVersion = version === semver.parse(defaultVersion).version

  // can't use process.release if we're using --target=x.y.z
  if (!isDefaultVersion)
    defaultRelease = null

  if (defaultRelease) {
    // v3 onward, has process.release
    name = defaultRelease.name
  } else {
    // old node or alternative --target=
    // semver.satisfies() doesn't like prerelease tags so test major directly
    name = 'node'
  }

  // check for the nvm.sh standard mirror env variables
  if (!overrideDistUrl && process.env.NODEJS_ORG_MIRROR)
    overrideDistUrl = process.env.NODEJS_ORG_MIRROR

  if (overrideDistUrl)
    log.verbose('download', 'using dist-url', overrideDistUrl)

  if (overrideDistUrl)
    distBaseUrl = overrideDistUrl.replace(/\/+$/, '')
  else
    distBaseUrl = 'https://nodejs.org/dist'
  distBaseUrl += '/v' + version + '/'

  // new style, based on process.release so we have a lot of the data we need
  if (defaultRelease && defaultRelease.headersUrl && !overrideDistUrl) {
    baseUrl = url.resolve(defaultRelease.headersUrl, './')
    libUrl32 = resolveLibUrl(name, defaultRelease.libUrl || baseUrl || distBaseUrl, 'x86', versionSemver.major)
    libUrl64 = resolveLibUrl(name, defaultRelease.libUrl || baseUrl || distBaseUrl, 'x64', versionSemver.major)
    tarballUrl = defaultRelease.headersUrl
  } else {
    // older versions without process.release are captured here and we have to make
    // a lot of assumptions, additionally if you --target=x.y.z then we can't use the
    // current process.release
    baseUrl = distBaseUrl
    libUrl32 = resolveLibUrl(name, baseUrl, 'x86', versionSemver.major)
    libUrl64 = resolveLibUrl(name, baseUrl, 'x64', versionSemver.major)

    // making the bold assumption that anything with a version number >3.0.0 will
    // have a *-headers.tar.gz file in its dist location, even some frankenstein
    // custom version
    canGetHeaders = semver.satisfies(versionSemver, headersTarballRange)
    tarballUrl = url.resolve(baseUrl, name + '-v' + version + (canGetHeaders ? '-headers' : '') + '.tar.gz')
  }

  return {
    version: version,
    semver: versionSemver,
    name: name,
    baseUrl: baseUrl,
    tarballUrl: tarballUrl,
    shasumsUrl: url.resolve(baseUrl, 'SHASUMS256.txt'),
    versionDir: (name !== 'node' ? name + '-' : '') + version,
    libUrl32: libUrl32,
    libUrl64: libUrl64,
    libPath32: normalizePath(path.relative(url.parse(baseUrl).path, url.parse(libUrl32).path)),
    libPath64: normalizePath(path.relative(url.parse(baseUrl).path, url.parse(libUrl64).path))
  }
}