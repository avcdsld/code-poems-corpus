function(id, chunkIdx) {
            var fileState = handler._getFileState(id);

            if (fileState) {
                delete fileState.temp.cachedChunks[chunkIdx];
            }
        }