function () {
    if (!currentInst) {
      return;
    }

    var $dialog = currentInst.$dialog;

    var $dialogTitle = $dialog.children('.mdui-dialog-title');
    var $dialogContent = $dialog.children('.mdui-dialog-content');
    var $dialogActions = $dialog.children('.mdui-dialog-actions');

    // 调整 dialog 的 top 和 height 值
    $dialog.height('');
    $dialogContent.height('');

    var dialogHeight = $dialog.height();
    $dialog.css({
      top: (($window.height() - dialogHeight) / 2) + 'px',
      height: dialogHeight + 'px',
    });

    // 调整 mdui-dialog-content 的高度
    $dialogContent.height(dialogHeight - ($dialogTitle.height() || 0) - ($dialogActions.height() || 0));
  }