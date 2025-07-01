function(ip, options) {
    var self = this;
    this.ip = ip;
    this.openFlag = false;
    this.callback = null;

    // options
    if (typeof options === "undefined") options = {};
    this.port = options.port || TELNET_PORT; // telnet server port

    // internal buffer
    this._buffer = Buffer.alloc(0);
    this._id = 0;
    this._cmd = 0;
    this._length = 0;

    // handle callback - call a callback function only once, for the first event
    // it will triger
    var handleCallback = function(had_error) {
        if (self.callback) {
            self.callback(had_error);
            self.callback = null;
        }
    };

    // create a socket
    this._client = new net.Socket();
    if (options.timeout) this._client.setTimeout(options.timeout);

    // register the port data event
    this._client.on("data", function onData(data) {
        // add data to buffer
        self._buffer = Buffer.concat([self._buffer, data]);

        // check if buffer include a complete modbus answer
        var expectedLength = self._length;
        var bufferLength = self._buffer.length;
        modbusSerialDebug(
            "on data expected length:" +
                expectedLength +
                " buffer length:" +
                bufferLength
        );

        modbusSerialDebug({
            action: "receive tcp telnet port",
            data: data,
            buffer: self._buffer
        });
        modbusSerialDebug(
            JSON.stringify({
                action: "receive tcp telnet port strings",
                data: data,
                buffer: self._buffer
            })
        );

        // check data length
        if (expectedLength < 6 || bufferLength < EXCEPTION_LENGTH) return;

        // loop and check length-sized buffer chunks
        var maxOffset = bufferLength - EXCEPTION_LENGTH;
        for (var i = 0; i <= maxOffset; i++) {
            var unitId = self._buffer[i];
            var functionCode = self._buffer[i + 1];

            if (unitId !== self._id) continue;

            if (
                functionCode === self._cmd &&
                i + expectedLength <= bufferLength
            ) {
                self._emitData(i, expectedLength);
                return;
            }
            if (
                functionCode === (0x80 | self._cmd) &&
                i + EXCEPTION_LENGTH <= bufferLength
            ) {
                self._emitData(i, EXCEPTION_LENGTH);
                return;
            }

            // frame header matches, but still missing bytes pending
            if (functionCode === (0x7f & self._cmd)) break;
        }
    });

    this._client.on("connect", function() {
        self.openFlag = true;
        handleCallback();
    });

    this._client.on("close", function(had_error) {
        self.openFlag = false;
        handleCallback(had_error);
    });

    this._client.on("error", function(had_error) {
        self.openFlag = false;
        handleCallback(had_error);
    });

    this._client.on("timeout", function() {
        self.openFlag = false;
        modbusSerialDebug("TelnetPort port: TimedOut");
        handleCallback(new Error("TelnetPort Connection Timed Out."));
    });

    /**
     * Check if port is open.
     *
     * @returns {boolean}
     */
    Object.defineProperty(this, "isOpen", {
        enumerable: true,
        get: function() {
            return this.openFlag;
        }
    });

    EventEmitter.call(this);
}