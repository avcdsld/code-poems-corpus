function sendClientConsoleMessage(ws, message) {
  var msg = JSON.stringify({
    custom: {
      console: message
    }
  });
  ws.write(msg);
}