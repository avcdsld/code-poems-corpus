async function getPkgReleases({ lookupName: repo, lookupType }) {
  let versions;
  const cachedResult = await renovateCache.get(
    cacheNamespace,
    getCacheKey(repo, lookupType || 'tags')
  );
  // istanbul ignore if
  if (cachedResult) {
    return cachedResult;
  }
  try {
    if (lookupType === 'releases') {
      const url = `https://api.github.com/repos/${repo}/releases?per_page=100`;
      versions = (await ghGot(url, { paginate: true })).body.map(
        o => o.tag_name
      );
    } else {
      // tag
      const url = `https://api.github.com/repos/${repo}/tags?per_page=100`;
      versions = (await ghGot(url, {
        paginate: true,
      })).body.map(o => o.name);
    }
  } catch (err) {
    logger.info({ repo, err }, 'Error retrieving from github');
  }
  if (!versions) {
    return null;
  }
  const dependency = {
    sourceUrl: 'https://github.com/' + repo,
  };
  dependency.releases = versions.map(version => ({
    version,
    gitRef: version,
  }));
  const cacheMinutes = 10;
  await renovateCache.set(
    cacheNamespace,
    getCacheKey(repo, lookupType),
    dependency,
    cacheMinutes
  );
  return dependency;
}