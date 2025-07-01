public SDVariable constant(String name, float value) {
        try(MemoryWorkspace ws = Nd4j.getMemoryManager().scopeOutOfWorkspaces()) {
            return constant(name, Nd4j.scalar(value));
        }
    }