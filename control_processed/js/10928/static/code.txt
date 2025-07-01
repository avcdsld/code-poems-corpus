async function mergePr(prNo, branchName) {
  logger.debug(`mergePr(${prNo}, ${branchName})`);
  // Used for "automerge" feature
  try {
    const pr = await getPr(prNo);
    if (!pr) {
      throw Object.assign(new Error('not-found'), { statusCode: 404 });
    }
    await api.post(
      `./rest/api/1.0/projects/${config.projectKey}/repos/${
        config.repositorySlug
      }/pull-requests/${prNo}/merge?version=${pr.version}`
    );
    await getPr(prNo, true);
  } catch (err) {
    if (err.statusCode === 404) {
      throw new Error('not-found');
    } else if (err.statusCode === 409) {
      throw new Error('repository-changed');
    } else {
      logger.warn({ err }, `Failed to merge PR`);
      return false;
    }
  }

  logger.debug({ pr: prNo }, 'PR merged');
  // Delete branch
  await deleteBranch(branchName);
  return true;
}