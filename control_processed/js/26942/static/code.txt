function _handleReadMultipleRegisters(requestBuffer, vector, unitID, callback) {
    var address = requestBuffer.readUInt16BE(2);
    var length = requestBuffer.readUInt16BE(4);

    if (_errorRequestBufferLength(requestBuffer)) {
        return;
    }

    // build answer
    var responseBuffer = Buffer.alloc(3 + length * 2 + 2);
    try {
        responseBuffer.writeUInt8(length * 2, 2);
    }
    catch (err) {
        callback(err);
        return;
    }

    var callbackInvoked = false;
    var cbCount = 0;
    var buildCb = function(i) {
        return function(err, value) {
            if (err) {
                if (!callbackInvoked) {
                    callbackInvoked = true;
                    callback(err);
                }

                return;
            }

            cbCount = cbCount + 1;

            responseBuffer.writeUInt16BE(value, 3 + i * 2);

            if (cbCount === length && !callbackInvoked) {
                modbusSerialDebug({ action: "FC3 response", responseBuffer: responseBuffer });

                callbackInvoked = true;
                callback(null, responseBuffer);
            }
        };
    };

    if (length === 0)
        callback({
            modbusErrorCode: 0x02, // Illegal address
            msg: "Invalid length"
        });

    // read registers
    function tryAndHandlePromiseOrValue(i, values) {
        var cb = buildCb(i);
        try {
            var promiseOrValue = values[i];
            _handlePromiseOrValue(promiseOrValue, cb);
        }
        catch (err) {
            cb(err);
        }
    }

    if (vector.getMultipleHoldingRegisters && length > 1) {

        if (vector.getMultipleHoldingRegisters.length === 4) {
            vector.getMultipleHoldingRegisters(address, length, unitID, function(err, values) {
                if (!err && values.length !== length) {
                    var error = new Error("Requested address length and response length do not match");
                    callback(error);
                    throw error;
                } else {
                    for (var i = 0; i < length; i++) {
                        var cb = buildCb(i);
                        try {
                            cb(err, values[i]);
                        }
                        catch (ex) {
                            cb(ex);
                        }
                    }
                }
            });
        } else {
            var values = vector.getMultipleHoldingRegisters(address, length, unitID);
            if (values.length === length) {
                for (i = 0; i < length; i++) {
                    tryAndHandlePromiseOrValue(i, values);
                }
            } else {
                var error = new Error("Requested address length and response length do not match");
                callback(error);
                throw error;
            }
        }

    }
    else if (vector.getHoldingRegister) {
        for (var i = 0; i < length; i++) {
            var cb = buildCb(i);
            try {
                if (vector.getHoldingRegister.length === 3) {
                    vector.getHoldingRegister(address + i, unitID, cb);
                } else {
                    var promiseOrValue = vector.getHoldingRegister(address + i, unitID);
                    _handlePromiseOrValue(promiseOrValue, cb);
                }
            }
            catch (err) {
                cb(err);
            }
        }
    }


}