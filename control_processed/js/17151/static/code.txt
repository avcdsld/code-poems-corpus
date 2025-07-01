function (e) {
    if (e.type === 'touchstart') {
      // 触发了 touch 事件
      TouchHandler.touches += 1;
    } else if (['touchmove', 'touchend', 'touchcancel'].indexOf(e.type) > -1) {
      // touch 事件结束 500ms 后解除对鼠标事件的阻止
      setTimeout(function () {
        if (TouchHandler.touches) {
          TouchHandler.touches -= 1;
        }
      }, 500);
    }
  }