function forEachUp(domEle, fn$$1) {
    while (domEle != null) {
      fn$$1(domEle);
      domEle = domEle.parentNode;
    }
  }