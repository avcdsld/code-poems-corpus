function storeOptions() {
    var showTomster = this.checked;

    chrome.storage.sync.set({
      options: { showTomster: showTomster }
    }, function optionsSaved() {
      console.log("saved!");
    });
  }