function _cmdCloseServer(path, cba) {
    var pathKey = getPathKey(path);
    if (_servers[pathKey]) {
        var serverToClose = _servers[pathKey];
        delete _servers[pathKey];
        serverToClose.close();
        return true;
    }
    return false;
}