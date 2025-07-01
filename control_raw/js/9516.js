function handleClientStreaming(call, handler, metadata) {
  var stream = new ServerReadableStream(call, metadata, handler.deserialize);
  stream.on('error', function(error) {
    handleError(call, error);
  });
  stream.waitForCancel();
  handler.func(stream, function(err, value, trailer, flags) {
    stream.terminate();
    if (err) {
      if (trailer) {
        err.metadata = trailer;
      }
      handleError(call, err);
    } else {
      sendUnaryResponse(call, value, handler.serialize, trailer, flags);
    }
  });
}