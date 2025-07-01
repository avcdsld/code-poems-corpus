function() {
        return Promise.all([
            this._loadAccountData(),
            this._loadSyncData(),
        ]).then(([accountData, syncData]) => {
            console.log(
                `LocalIndexedDBStoreBackend: loaded initial data`,
            );
            this._syncAccumulator.accumulate({
                next_batch: syncData.nextBatch,
                rooms: syncData.roomsData,
                groups: syncData.groupsData,
                account_data: {
                    events: accountData,
                },
            });
        });
    }