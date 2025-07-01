function(userId, filterId) {
        if (!this.filters[userId] || !this.filters[userId][filterId]) {
            return null;
        }
        return this.filters[userId][filterId];
    }