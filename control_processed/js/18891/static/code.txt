function walkTree(directory, callback) {
    callback(directory);
    directory.directories.forEach(childDirectory => walkTree(childDirectory, callback));
}