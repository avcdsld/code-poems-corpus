int numChildren(int streamId) {
        State state = state(streamId);
        return state == null ? 0 : state.children.size();
    }