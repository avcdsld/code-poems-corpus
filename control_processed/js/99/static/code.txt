async function changesToRelease () {
  const lastCommitWasRelease = new RegExp(`^Bump v[0-9.]*(-beta[0-9.]*)?(-nightly[0-9.]*)?$`, 'g')
  const lastCommit = await GitProcess.exec(['log', '-n', '1', `--pretty=format:'%s'`], gitDir)
  return !lastCommitWasRelease.test(lastCommit.stdout)
}