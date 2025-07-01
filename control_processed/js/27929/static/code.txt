function() {
      var _vm = this;
      var _h = _vm.$createElement;
      var _c = _vm._self._c || _h;
      return _c(
        _vm.tag,
        {
          tag: "component",
          class: [
            _vm.breakpointClasses,
            _vm.col || (_vm.breakpointClasses.length === 0 && !_vm.cols)
              ? "col"
              : "",
            _vm.cols ? "col-" + _vm.cols : "",
            _vm.offset ? "offset-" + _vm.offset : "",
            _vm.order ? "order-" + _vm.order : "",
            _vm.alignSelf ? "align-self-" + _vm.alignSelf : ""
          ]
        },
        [_vm._t("default")],
        2
      )
    }