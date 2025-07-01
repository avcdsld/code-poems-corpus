function() {
      var _vm = this;
      var _h = _vm.$createElement;
      var _c = _vm._self._c || _h;
      return _c(
        "label",
        {
          class: [
            "custom-control",
            "custom-radio",
            _vm.inline ? "custom-control-inline" : "",
            _vm.computedStateClass
          ]
        },
        [
          _c("input", {
            directives: [
              {
                name: "model",
                rawName: "v-model",
                value: _vm.computedLocalChecked,
                expression: "computedLocalChecked"
              }
            ],
            ref: "check",
            class: ["custom-control-input", _vm.computedStateClass],
            attrs: {
              type: "radio",
              autocomplete: "off",
              "aria-required": _vm.required ? "true" : null,
              id: _vm.computedID,
              name: _vm.name,
              disabled: _vm.disabled,
              required: _vm.name && _vm.required
            },
            domProps: {
              value: _vm.value,
              checked: _vm._q(_vm.computedLocalChecked, _vm.value)
            },
            on: {
              change: [
                function($event) {
                  _vm.computedLocalChecked = _vm.value;
                },
                _vm.handleChange
              ]
            }
          }),
          _vm._v(" "),
          _c("label", {
            staticClass: "custom-control-label",
            attrs: { for: _vm.computedID, "aria-hidden": "true" }
          }),
          _vm._v(" "),
          _c(
            "span",
            { class: ["custom-control-description"] },
            [_vm._t("default")],
            2
          )
        ]
      )
    }