function whenDocumentReady(callback, doc) {
  if (!isDocumentReady(doc)) {
    var checkReady = function() {
      if (doc.readyState === 'complete' ||
          doc.readyState === requiredReadyState) {
        doc.removeEventListener(READY_EVENT, checkReady);
        whenDocumentReady(callback, doc);
      }
    };
    doc.addEventListener(READY_EVENT, checkReady);
  } else if (callback) {
    callback();
  }
}