function runTypedoc() {
  const typeSource = apiType === 'node' ? tempNodeSourcePath : sourceFile;
  const command = `${repoPath}/node_modules/.bin/typedoc ${typeSource} \
  --out ${docPath} \
  --readme ${tempHomePath} \
  --options ${__dirname}/typedoc.js \
  --theme ${__dirname}/theme`;

  console.log('Running command:\n', command);
  return exec(command);
}