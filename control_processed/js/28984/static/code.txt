function respondWithCode(res, code, message) {
            /* eslint-disable */
            res._headers = {};
            res._headerNames = {};
            res.statusCode = code;
            /* eslint-enable */
            res.setHeader('Content-Type', 'text/plain; charset=UTF-8');
            res.setHeader('Content-Length', Buffer.byteLength(message));
            res.setHeader('X-Content-Type-Options', 'nosniff');
            res.end(message);
        }