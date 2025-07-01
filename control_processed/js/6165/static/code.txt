function getRelativePath(filepath, baseDir) {
    const absolutePath = path.isAbsolute(filepath)
        ? filepath
        : path.resolve(filepath);

    if (baseDir) {
        if (!path.isAbsolute(baseDir)) {
            throw new Error(`baseDir should be an absolute path: ${baseDir}`);
        }
        return path.relative(baseDir, absolutePath);
    }
    return absolutePath.replace(/^\//u, "");

}