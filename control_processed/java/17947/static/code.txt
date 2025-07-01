@Override
    public void destroyWorkspace(MemoryWorkspace workspace) {
        if (workspace == null || workspace instanceof DummyWorkspace)
            return;

        //workspace.destroyWorkspace();
        backingMap.get().remove(workspace.getId());
    }