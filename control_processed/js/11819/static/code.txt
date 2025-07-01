function(ev) {
        var text = this.clipboardModel.get('text');

        if (!supportWindowClipboardData) {
            (ev.originalEvent || ev).clipboardData.setData('text/plain', text);
        }

        ev.preventDefault();
    }