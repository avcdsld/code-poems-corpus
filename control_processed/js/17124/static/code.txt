function Dialog(selector, opts) {
    var _this = this;

    // 对话框元素
    _this.$dialog = $(selector).eq(0);
    if (!_this.$dialog.length) {
      return;
    }

    // 已通过 data 属性实例化过，不再重复实例化
    var oldInst = _this.$dialog.data('mdui.dialog');
    if (oldInst) {
      return oldInst;
    }

    // 如果对话框元素没有在当前文档中，则需要添加
    if (!$.contains(document.body, _this.$dialog[0])) {
      _this.append = true;
      $('body').append(_this.$dialog);
    }

    _this.options = $.extend({}, DEFAULT, (opts || {}));
    _this.state = 'closed';

    // 绑定取消按钮事件
    _this.$dialog.find('[mdui-dialog-cancel]').each(function () {
      $(this).on('click', function () {
        componentEvent('cancel', 'dialog', _this, _this.$dialog);
        if (_this.options.closeOnCancel) {
          _this.close();
        }
      });
    });

    // 绑定确认按钮事件
    _this.$dialog.find('[mdui-dialog-confirm]').each(function () {
      $(this).on('click', function () {
        componentEvent('confirm', 'dialog', _this, _this.$dialog);
        if (_this.options.closeOnConfirm) {
          _this.close();
        }
      });
    });

    // 绑定关闭按钮事件
    _this.$dialog.find('[mdui-dialog-close]').each(function () {
      $(this).on('click', function () {
        _this.close();
      });
    });
  }