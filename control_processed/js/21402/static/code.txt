function format(string) {
        var args = Array.prototype.slice.call(arguments, 1);
        return string.replace(/{(\d+)}/g, function (match, n) {
            return typeof args[n] != 'undefined' ? args[n] : match;
        });
    }