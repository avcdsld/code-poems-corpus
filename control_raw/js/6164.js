function convertPathToPosix(filepath) {
    const normalizedFilepath = path.normalize(filepath);
    const posixFilepath = normalizedFilepath.replace(/\\/gu, "/");

    return posixFilepath;
}