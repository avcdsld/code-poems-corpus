function updateVersion(file, content, version) {
    const prev = /id="branch-cordova-sdk"[\s]*version="\d+\.\d+\.\d+"/gim;
    const next = `id="branch-cordova-sdk"\n  version="${version}"`;

    try {
      if (isFileXml(file)) {
        content = content.replace(prev, next);
      } else {
        isChange = content.version !== version;
        content.version = version;
      }
    } catch (e) {
      throw new Error(
        `BRANCH SDK: update to update npm version with file ${file}`
      );
    }
    return content;
  }