async function _handleReadDeviceIdentification(requestBuffer, vector, unitID, callback) {
    const PDULenMax = 253;
    const MEI14HeaderLen = 6;
    const stringLengthMax = PDULenMax - MEI14HeaderLen - 2;

    if(!vector.readDeviceIdentification) {
        callback({ modbusErrorCode: 0x01 });
        return;
    }

    var readDeviceIDCode = requestBuffer.readUInt8(3);
    var objectID = requestBuffer.readUInt8(4);

    // Basic request parameters checks
    switch(readDeviceIDCode) {
        case 0x01:
            if(objectID > 0x02 || (objectID > 0x06 && objectID < 0x80))
                objectID = 0x00;
            break;

        case 0x02:
            if(objectID >= 0x80 || (objectID > 0x06 && objectID < 0x80))
                objectID = 0x00;
            break;

        case 0x03:
            if(objectID > 0x06 && objectID < 0x80)
                objectID = 0x00;
            break;

        case 0x04:
            if(objectID > 0x06 && objectID < 0x80) {
                callback({ modbusErrorCode: 0x02 });
                return;
            }
            break;

        default:
            callback({ modbusErrorCode: 0x03 });
            return;
    }

    // Filling mandatory basic device identification objects
    var objects = {
        0x00: "undefined",
        0x01: "undefined",
        0x02: "undefined"
    };

    const pkg = require("../package.json");
    if(pkg) {
        if(pkg.author)
            objects[0x00] = pkg.author;
        if(pkg.name)
            objects[0x01] = pkg.name;
        if(pkg.version)
            objects[0x02] = pkg.version;
    }

    var promiseOrValue = vector.readDeviceIdentification(unitID);
    try {
        var userObjects = await new Promise((resolve, reject) => {
            _handlePromiseOrValue(promiseOrValue, (err, value) => {
                if(err)
                    reject(err);
                else
                    resolve(value);
            });
        });
    }
    catch(error) {
        callback(error);
        return;
    }

    for(var o of Object.keys(userObjects)) {
        const i = parseInt(o);
        if(!isNaN(i) && i >= 0 && i <= 255)
            objects[i] = userObjects[o];
    }

    // Checking the existence of the requested objectID
    if(!objects[objectID]) {
        if(readDeviceIDCode === 0x04) {
            callback({ modbusErrorCode: 0x02 });
            return;
        }

        objectID = 0x00;
    }

    var ids = [];
    var totalLength = 2 + MEI14HeaderLen + 2; // UnitID + FC + MEI14Header + CRC
    var lastID = 0;
    var conformityLevel = 0x81;

    var supportedIDs = Object.keys(objects);

    // Filtering of objects and Conformity level determination
    for(var id of supportedIDs) {
        id = parseInt(id);

        if(isNaN(id))
            continue;

        // Enforcing valid object IDs from the user
        if(id < 0x00 || (id > 0x06 && id < 0x80) || id > 0xFF) {
            callback({ modbusErrorCode: 0x04 });
            throw new Error("Invalid Object ID provided for Read Device Identification: " + id);
        }

        if(id > 0x02)
            conformityLevel = 0x82;
        if(id > 0x80)
            conformityLevel = 0x83;

        // Starting from requested object ID
        if(objectID > id)
            continue;

        // Enforcing maximum string length
        if(objects[id].length > stringLengthMax) {
            callback({ modbusErrorCode: 0x04 });
            throw new Error("Read Device Identification string size can be maximum " + stringLengthMax);
        }

        if(lastID !== 0)
            continue;

        if(objects[id].length + 2 > PDULenMax - totalLength) {
            if(lastID === 0)
                lastID = id;
        }
        else {
            totalLength += objects[id].length + 2;
            ids.push(id);

            // Requested a single object
            if(readDeviceIDCode === 0x04)
                break;
        }
    }

    ids.sort((a, b) => parseInt(a) - parseInt(b));
    var responseBuffer = Buffer.alloc(totalLength);

    var i = 2;
    i = responseBuffer.writeUInt8(14, i);                                   // MEI type
    i = responseBuffer.writeUInt8(readDeviceIDCode, i);
    i = responseBuffer.writeUInt8(conformityLevel, i);
    if(lastID === 0)                                                        // More follows
        i = responseBuffer.writeUInt8(0x00, i);
    else
        i = responseBuffer.writeUInt8(0xFF, i);

    i = responseBuffer.writeUInt8(lastID, i);                               // Next Object Id
    i = responseBuffer.writeUInt8(ids.length, i);                           // Number of objects

    for(id of ids) {
        i = responseBuffer.writeUInt8(id, i);                               // Object id
        i = responseBuffer.writeUInt8(objects[id].length, i);               // Object length
        i += responseBuffer.write(objects[id], i, objects[id].length);      // Object value
    }

    callback(null, responseBuffer);
}