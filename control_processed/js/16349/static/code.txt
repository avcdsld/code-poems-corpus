function (ui, done) {
        var port = ui.options.get("port");
        var listenHost = ui.options.get("listen", "localhost");
        ui.bs.utils.portscanner.findAPortNotInUse(port, port + 100, {
            host: listenHost,
            timeout: 1000
        }, function (err, port) {
            if (err) {
                return done(err);
            }
            done(null, {
                options: {
                    port: port
                }
            });
        });
    }