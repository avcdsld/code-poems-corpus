function() {
      var _vm = this;
      var _h = _vm.$createElement;
      var _c = _vm._self._c || _h;
      return _c(
        "button",
        {
          staticClass: "btn",
          class: [
            _vm.themeClass,
            _vm.sizeClass,
            _vm.pill ? "btn-pill" : "",
            _vm.squared ? "btn-squared" : "",
            _vm.blockLevel ? "btn-block" : "",
            _vm.active ? "active" : ""
          ],
          attrs: { disabled: this.disabled, "aria-pressed": this.active },
          on: { click: _vm.handleClick }
        },
        [_vm._t("default", [_vm._v("Button")])],
        2
      )
    }