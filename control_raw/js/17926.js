function observeRoot(widget, attributes, callback, skipSetState) {
    attributes.forEach(attribute => {
        Object.defineProperty(widget.el, attribute, {
            get() {
                return widget.state[attribute];
            },
            set(value) {
                if (!skipSetState) {
                    widget.setState(attribute, value);
                }
                if (callback) {
                    callback(value);
                }
            }
        });
    });
}