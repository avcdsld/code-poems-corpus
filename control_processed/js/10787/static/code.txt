function leavingDocumentOut(e) {
        if (qq.safari()) {
            return e.x < 0 || e.y < 0;
        }

        return e.x === 0 && e.y === 0;
    }