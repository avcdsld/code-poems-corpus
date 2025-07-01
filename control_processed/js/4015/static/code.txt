function enableDebugger() {
        try {
            _nodeConnection.domains.base.enableDebugger();
        } catch (e) {
            window.alert("Failed trying to enable Node debugger: " + e.message);
        }
    }