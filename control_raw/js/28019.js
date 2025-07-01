function writeYamlFile(file, data) {
  return new Promise((resolve, reject) => {
    writeFile(file, toYaml(data))
      .then(resolve)
      .catch(reject);
  });
}