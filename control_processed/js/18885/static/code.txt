function getModules(directory, logger, local) {
    logger(`Getting modules @ ${directory.path}`);
    if (directory.barrel) {
        // If theres a barrel then use that as it *should* contain descendant modules.
        logger(`Found existing barrel @ ${directory.barrel.path}`);
        return [directory.barrel];
    }
    const files = [].concat(directory.files);
    if (!local) {
        directory.directories.forEach((childDirectory) => {
            // Recurse.
            files.push(...getModules(childDirectory, logger, local));
        });
    }
    // Only return files that look like TypeScript modules.
    return files.filter((file) => file.name.match(utilities_1.isTypeScriptFile));
}