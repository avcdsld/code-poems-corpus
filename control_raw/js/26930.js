function(path, options) {
    var modbus = this;

    // options
    options = options || {};

    // disable auto open, as we handle the open
    options.autoOpen = false;

    // internal buffer
    this._buffer = Buffer.from("");
    this._id = 0;
    this._cmd = 0;
    this._length = 0;

    // create the SerialPort
    this._client = new SerialPort(path, options);

    // register the port data event
    this._client.on("data", function(data) {

        // add new data to buffer
        modbus._buffer = Buffer.concat([modbus._buffer, data]);

        modbusSerialDebug({ action: "receive serial ascii port", data: data, buffer: modbus._buffer });
        modbusSerialDebug(JSON.stringify({ action: "receive serial ascii port strings", data: data, buffer: modbus._buffer }));

        // check buffer for start delimiter
        var sdIndex = modbus._buffer.indexOf(0x3A); // ascii for ':'
        if(sdIndex === -1) {
            // if not there, reset the buffer and return
            modbus._buffer = Buffer.from("");
            return;
        }
        // if there is data before the start delimiter, remove it
        if(sdIndex > 0) {
            modbus._buffer = modbus._buffer.slice(sdIndex);
        }
        // do we have the complete message (i.e. are the end delimiters there)
        if(modbus._buffer.includes("\r\n", 1, "ascii") === true) {
            // check there is no excess data after end delimiters
            var edIndex = modbus._buffer.indexOf(0x0A); // ascii for '\n'
            if(edIndex !== modbus._buffer.length - 1) {
                // if there is, remove it
                modbus._buffer = modbus._buffer.slice(0, edIndex + 1);
            }

            // we have what looks like a complete ascii encoded response message, so decode
            var _data = _asciiDecodeResponseBuffer(modbus._buffer);
            modbusSerialDebug({ action: "got EOM", data: _data, buffer: modbus._buffer });
            if(_data !== null) {

                // check if this is the data we are waiting for
                if (_checkData(modbus, _data)) {
                    modbusSerialDebug({ action: "emit data serial ascii port", data: data, buffer: modbus._buffer });
                    modbusSerialDebug(JSON.stringify({ action: "emit data serial ascii port strings", data: data, buffer: modbus._buffer }));
                    // emit a data signal
                    modbus.emit("data", _data);
                }
            }
            // reset the buffer now its been used
            modbus._buffer = Buffer.from("");
        } else {
            // otherwise just wait for more data to arrive
        }
    });

    /**
     * Check if port is open.
     *
     * @returns {boolean}
     */
    Object.defineProperty(this, "isOpen", {
        enumerable: true,
        get: function() {
            return this._client.isOpen;
        }
    });

    EventEmitter.call(this);
}