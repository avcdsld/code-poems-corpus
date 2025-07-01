function (e) {
            if (e.keyCode === KeyEvent.DOM_VK_ESCAPE) {
                this.props.actions.cancelRename();
            } else if (e.keyCode === KeyEvent.DOM_VK_RETURN) {
                this.props.actions.performRename();
            }
        }