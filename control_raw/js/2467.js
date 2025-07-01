function listShortcuts(blocks, filePath) {
    var parser = parsers.getForFile(filePath);

    if (!parser) {
        return Immutable.List();
    }

    return blocks
        .map(function(block) {
            return block.getShortcuts();
        })
        .filter(function(shortcuts) {
            return (
                shortcuts &&
                shortcuts.acceptParser(parser.getName())
            );
        });
}