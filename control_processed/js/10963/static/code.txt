async function createPr(
  branchName,
  title,
  description,
  labels,
  useDefaultBranch = true
) {
  // labels is not supported in Bitbucket: https://bitbucket.org/site/master/issues/11976/ability-to-add-labels-to-pull-requests-bb

  const base = useDefaultBranch ? config.defaultBranch : config.baseBranch;

  logger.debug({ repository: config.repository, title, base }, 'Creating PR');

  const body = {
    title,
    description,
    source: {
      branch: {
        name: branchName,
      },
    },
    destination: {
      branch: {
        name: base,
      },
    },
    close_source_branch: true,
  };

  const prInfo = (await api.post(
    `/2.0/repositories/${config.repository}/pullrequests`,
    { body }
  )).body;
  const pr = { number: prInfo.id, displayNumber: `Pull Request #${prInfo.id}` };
  // istanbul ignore if
  if (config.prList) {
    config.prList.push(pr);
  }
  return pr;
}