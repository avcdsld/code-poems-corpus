async function combineLocales(localesPath) {
  const localesFiles = await fs.readdir(localesPath);
  const jsonFiles = localesFiles.filter((fileName) =>
    fileName.endsWith('.json'),
  );

  return jsonFiles.reduce(async (promise, file) => {
    const accumulator = await promise;
    const localeCode = path
      .basename(file)
      .split('.')
      .shift();
    const fileContents = JSON.parse(
      await fs.readFile(path.resolve(localesPath, file), 'utf-8'),
    );
    accumulator[localeCode] = fileContents;
    return accumulator;
  }, Promise.resolve({}));
}