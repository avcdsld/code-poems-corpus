function() {
            var err = null, status = parseInt(res.statusCode, 10);
            if (status > 399) { // Unsuccessful HTTP status? Then pass an error to the callback
                var match = data.match(/^\{"message": "(.+)"\}/i);
                err = new error.DiscogsError(status, ((match && match[1]) ? match[1] : null));
            }
            callback(err, data, rateLimit);
        }