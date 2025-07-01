function(req, res, next) {
                if (req.headers.accept && req.headers.accept.startsWith('text/html')) {
                  req.url = '/index.html'; // eslint-disable-line no-param-reassign
                }
                next();
              }