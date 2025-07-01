function IndexHandler(req, res, next, local = false) {
            const parsedUrl = url.parse(req.url);
            if (!parsedUrl.pathname.startsWith(self.localFilesystemUrl) &&
                parsedUrl.pathname !== '/favicon.ico'
            ) {
                /** @type {Asset} */
                const indexFile = self.assetBundle.getIndexFile();
                if (local) {
                    createStreamProtocolResponse(indexFile.getFile(), res, () => {
                    });
                } else {
                    send(req, encodeURIComponent(indexFile.getFile())).pipe(res);
                }
            } else {
                next();
            }
        }