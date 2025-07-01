function (runOptions) {
        var dimension = cliUtils.dimension(),
            options = {
                depth: 25,

                maxArrayLength: 100, // only supported in Node v6.1.0 and up: https://github.com/nodejs/node/pull/6334

                colors: !cliUtils.noTTY(runOptions.color),

                // note that similar dimension calculation is in utils.wrapper
                // only supported in Node v6.3.0 and above: https://github.com/nodejs/node/pull/7499
                breakLength: ((dimension.exists && (dimension.width > 20)) ? dimension.width : 60) - 16
            };

        return function (item) {
            return inspect(item, options);
        };
    }