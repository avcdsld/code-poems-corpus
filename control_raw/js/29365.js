function createDom(str) {
    var name = FRAGMENT_REG.test(str) && RegExp.$1;
    if (!(name in CONTAINERS)) {
      name = '*';
    }
    var container = CONTAINERS[name];
    str = str.replace(/(^\s*)|(\s*$)/g, '');
    container.innerHTML = '' + str;
    var dom = container.childNodes[0];
    container.removeChild(dom);
    return dom;
  }