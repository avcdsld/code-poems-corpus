async function getBranchStatusCheck(branchName, context) {
  logger.debug(`getBranchStatusCheck(${branchName}, context=${context})`);

  const branchCommit = await config.storage.getBranchCommit(branchName);

  try {
    const states = await utils.accumulateValues(
      `./rest/build-status/1.0/commits/${branchCommit}`
    );

    for (const state of states) {
      if (state.key === context) {
        switch (state.state) {
          case 'SUCCESSFUL':
            return 'success';
          case 'INPROGRESS':
            return 'pending';
          case 'FAILED':
          default:
            return 'failure';
        }
      }
    }
  } catch (err) {
    logger.warn({ err }, `Failed to check branch status`);
  }
  return null;
}