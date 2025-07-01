public CompositeByteBuf discardReadComponents() {
        ensureAccessible();
        final int readerIndex = readerIndex();
        if (readerIndex == 0) {
            return this;
        }

        // Discard everything if (readerIndex = writerIndex = capacity).
        int writerIndex = writerIndex();
        if (readerIndex == writerIndex && writerIndex == capacity()) {
            for (int i = 0, size = componentCount; i < size; i++) {
                components[i].free();
            }
            lastAccessed = null;
            clearComps();
            setIndex(0, 0);
            adjustMarkers(readerIndex);
            return this;
        }

        // Remove read components.
        int firstComponentId = 0;
        Component c = null;
        for (int size = componentCount; firstComponentId < size; firstComponentId++) {
            c = components[firstComponentId];
            if (c.endOffset > readerIndex) {
                break;
            }
            c.free();
        }
        if (firstComponentId == 0) {
            return this; // Nothing to discard
        }
        Component la = lastAccessed;
        if (la != null && la.endOffset <= readerIndex) {
            lastAccessed = null;
        }
        removeCompRange(0, firstComponentId);

        // Update indexes and markers.
        int offset = c.offset;
        updateComponentOffsets(0);
        setIndex(readerIndex - offset, writerIndex - offset);
        adjustMarkers(offset);
        return this;
    }