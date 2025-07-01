function _restoreOverriddenDefault(name, state) {
        if (state.overridden[name]) {
            var language = getLanguage(state.overridden[name]);
            language[state.add](name);
            delete state.overridden[name];
        }
    }