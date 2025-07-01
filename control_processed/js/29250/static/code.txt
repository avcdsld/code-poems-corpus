function () {

        var constraints = {
            url: function (value) {
                if (validate.isEmpty(value)) {
                    return {
                        presence: {
                            message: 'is required'
                        }
                    };
                }

                if (!(/^https?\:\/\//).test(value)) {
                    return {
                        format: 'must contain a VALID URL (http(s)://...)'
                    }
                }

                return null;
            },
            phoneNumber: function (value) {

                if (validate.isEmpty(value)) {
                    return {
                        presence: {
                            message: 'is required'
                        }
                    };
                }

                return null;
            }
        };

        let error = validate(options, constraints);
        if (error) {
            var msg = "";
            for (var k in error) {
                msg += error[k] + "; ";
            }
            throw new Error(msg);
        }
    }