function save_options() {
  var showChangeLog = document.getElementById('show_changelog').checked;
  chrome.storage.sync.set({
    showChangeLog: showChangeLog
  }, function () {
    // Update status to let user know options were saved.
    var status = document.getElementById('status');
    status.textContent = 'Options saved.';
    setTimeout(function () {
      status.textContent = '';
    }, 750);
  });
}