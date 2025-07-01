function _parseModbusBuffer(requestBuffer, vector, serverUnitID, sockWriter) {
    var cb;

    // Check requestBuffer length
    if (!requestBuffer || requestBuffer.length < MBAP_LEN) {
        modbusSerialDebug("wrong size of request Buffer " + requestBuffer.length);
        return;
    }

    var unitID = requestBuffer[0];
    var functionCode = requestBuffer[1];
    var crc = requestBuffer[requestBuffer.length - 2] + requestBuffer[requestBuffer.length - 1] * 0x100;

    // if crc is bad, ignore message
    if (crc !== crc16(requestBuffer.slice(0, -2))) {
        modbusSerialDebug("wrong CRC of request Buffer");
        return;
    }

    // if crc is bad, ignore message
    if (serverUnitID !== 255 && serverUnitID !== unitID) {
        modbusSerialDebug("wrong unitID");
        return;
    }

    modbusSerialDebug("request for function code " + functionCode);
    cb = _callbackFactory(unitID, functionCode, sockWriter);

    switch (parseInt(functionCode)) {
        case 1:
        case 2:
            handlers.readCoilsOrInputDiscretes(requestBuffer, vector, unitID, cb, functionCode);
            break;
        case 3:
            handlers.readMultipleRegisters(requestBuffer, vector, unitID, cb);
            break;
        case 4:
            handlers.readInputRegisters(requestBuffer, vector, unitID, cb);
            break;
        case 5:
            handlers.writeCoil(requestBuffer, vector, unitID, cb);
            break;
        case 6:
            handlers.writeSingleRegister(requestBuffer, vector, unitID, cb);
            break;
        case 15:
            handlers.forceMultipleCoils(requestBuffer, vector, unitID, cb);
            break;
        case 16:
            handlers.writeMultipleRegisters(requestBuffer, vector, unitID, cb);
            break;
        case 43:
            handlers.handleMEI(requestBuffer, vector, unitID, cb);
            break;
        default:
            var errorCode = 0x01; // illegal function

            // set an error response
            functionCode = parseInt(functionCode) | 0x80;
            var responseBuffer = Buffer.alloc(3 + 2);
            responseBuffer.writeUInt8(errorCode, 2);

            modbusSerialDebug({
                error: "Illegal function",
                functionCode: functionCode
            });

            cb({ modbusErrorCode: errorCode }, responseBuffer);
    }
}