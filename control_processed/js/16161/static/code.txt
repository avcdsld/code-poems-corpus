function extend (Vue) {
  if (!Vue.prototype.hasOwnProperty('$i18n')) {
    // $FlowFixMe
    Object.defineProperty(Vue.prototype, '$i18n', {
      get () { return this._i18n }
    });
  }

  Vue.prototype.$t = function (key, ...values) {
    const i18n = this.$i18n;
    return i18n._t(key, i18n.locale, i18n._getMessages(), this, ...values)
  };

  Vue.prototype.$tc = function (key, choice, ...values) {
    const i18n = this.$i18n;
    return i18n._tc(key, i18n.locale, i18n._getMessages(), this, choice, ...values)
  };

  Vue.prototype.$te = function (key, locale) {
    const i18n = this.$i18n;
    return i18n._te(key, i18n.locale, i18n._getMessages(), locale)
  };

  Vue.prototype.$d = function (value, ...args) {
    return this.$i18n.d(value, ...args)
  };

  Vue.prototype.$n = function (value, ...args) {
    return this.$i18n.n(value, ...args)
  };
}