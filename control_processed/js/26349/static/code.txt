function(pluginResult, payloadString) {
    var payload = JSON.parse(payloadString),
        ndefObjectAsString = JSON.stringify(decode(b64toArray(payload.data)));
    pluginResult.callbackOk(ndefObjectAsString, true);
}