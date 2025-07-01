async function abandonPr(prNo) {
  logger.debug(`abandonPr(prNo)(${prNo})`);
  const azureApiGit = await azureApi.gitApi();
  await azureApiGit.updatePullRequest(
    {
      status: 2,
    },
    config.repoId,
    prNo
  );
}