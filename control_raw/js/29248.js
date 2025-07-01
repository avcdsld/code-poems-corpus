function () {

        var constraints = {
            callTo: function (value) {

                if (validate.isEmpty(value)) {
                    return {
                        presence: {
                            message: 'is required'
                        }
                    };
                }
                if (!(/^\+\d{1,3}\d{3,}$/).test(value)) {
                    return {
                        format: 'must not contain invalid callTo phone number'
                    };
                }

                return null;
            },
            callFrom: function (value) {

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
            // TODO should this be rejected by promise instead?

            var msg = "";
            for (var k in error) {
                msg += error[k] + "; ";
            }
            throw new Error(msg);
        }
    }