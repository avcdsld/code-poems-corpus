function resolveFileToURL(output, filePath) {
    // Convert /test.png -> test.png
    filePath = LocationUtils.toAbsolute(filePath, '', '');

    var page = output.getPage(filePath);

    // if file is a page, return correct .html url
    if (page) {
        filePath = fileToURL(output, filePath);
    }

    return LocationUtils.normalize(filePath);
}