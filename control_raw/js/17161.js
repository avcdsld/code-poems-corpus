function Tab(selector, opts) {
    var _this = this;

    _this.$tab = $(selector).eq(0);
    if (!_this.$tab.length) {
      return;
    }

    // 已通过自定义属性实例化过，不再重复实例化
    var oldInst = _this.$tab.data('mdui.tab');
    if (oldInst) {
      return oldInst;
    }

    _this.options = $.extend({}, DEFAULT, (opts || {}));
    _this.$tabs = _this.$tab.children('a');
    _this.$indicator = $('<div class="mdui-tab-indicator"></div>').appendTo(_this.$tab);
    _this.activeIndex = false; // 为 false 时表示没有激活的选项卡，或不存在选项卡

    // 根据 url hash 获取默认激活的选项卡
    var hash = location.hash;
    if (hash) {
      _this.$tabs.each(function (i, tab) {
        if ($(tab).attr('href') === hash) {
          _this.activeIndex = i;
          return false;
        }
      });
    }

    // 含 mdui-tab-active 的元素默认激活
    if (_this.activeIndex === false) {
      _this.$tabs.each(function (i, tab) {
        if ($(tab).hasClass('mdui-tab-active')) {
          _this.activeIndex = i;
          return false;
        }
      });
    }

    // 存在选项卡时，默认激活第一个选项卡
    if (_this.$tabs.length && _this.activeIndex === false) {
      _this.activeIndex = 0;
    }

    // 设置激活状态选项卡
    _this._setActive();

    // 监听窗口大小变化事件，调整指示器位置
    $window.on('resize', $.throttle(function () {
      _this._setIndicatorPosition();
    }, 100));

    // 监听点击选项卡事件
    _this.$tabs.each(function (i, tab) {
      _this._bindTabEvent(tab);
    });
  }