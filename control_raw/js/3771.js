function waitForAll(promises, failOnReject, timeout) {
        var masterDeferred = new $.Deferred(),
            results = [],
            count = 0,
            sawRejects = false;

        if (!promises || promises.length === 0) {
            masterDeferred.resolve();
            return masterDeferred.promise();
        }

        // set defaults if needed
        failOnReject = (failOnReject === undefined) ? false : true;

        if (timeout !== undefined) {
            withTimeout(masterDeferred, timeout);
        }

        promises.forEach(function (promise) {
            promise
                .fail(function (err) {
                    sawRejects = true;
                })
                .done(function (result) {
                    results.push(result);
                })
                .always(function () {
                    count++;
                    if (count === promises.length) {
                        if (failOnReject && sawRejects) {
                            masterDeferred.reject();
                        } else {
                            masterDeferred.resolve(results);
                        }
                    }
                });
        });

        return masterDeferred.promise();
    }