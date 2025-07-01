function makeCallbackButton (labelIndex) {
        return function () {
            if (modalWindow) {
                modalWindow.removeEventListener('unload', onUnload, false);
                modalWindow.close();
            }
          // checking if prompt
            var promptInput = modalDocument.getElementById('prompt-input');
            var response;
            if (promptInput) {
                response = {
                    input1: promptInput.value,
                    buttonIndex: labelIndex
                };
            }
            response = response || labelIndex;
            callback(response);
        };
    }