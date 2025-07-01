async function createPr(
  branchName,
  title,
  body,
  labels,
  useDefaultBranch,
  statusCheckVerify
) {
  const base = useDefaultBranch ? config.defaultBranch : config.baseBranch;
  // Include the repository owner to handle forkMode and regular mode
  const head = `${config.repository.split('/')[0]}:${branchName}`;
  const options = {
    body: {
      title,
      head,
      base,
      body,
    },
  };
  // istanbul ignore if
  if (config.forkToken) {
    options.token = config.forkToken;
    options.body.maintainer_can_modify = true;
  }
  logger.debug({ title, head, base }, 'Creating PR');
  const pr = (await get.post(
    `repos/${config.parentRepo || config.repository}/pulls`,
    options
  )).body;
  logger.debug({ branch: branchName, pr: pr.number }, 'PR created');
  // istanbul ignore if
  if (config.prList) {
    config.prList.push(pr);
  }
  pr.displayNumber = `Pull Request #${pr.number}`;
  pr.branchName = branchName;
  await addLabels(pr.number, labels);
  if (statusCheckVerify) {
    logger.debug('Setting statusCheckVerify');
    await setBranchStatus(
      branchName,
      `${appSlug}/verify`,
      `${appName} verified pull request`,
      'success',
      urls.homepage
    );
  }
  return pr;
}