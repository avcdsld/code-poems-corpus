function queryBat (queue, cb) {
  const res = []

  queue.forEach(item => {
    const { selector, single, fields, component } = item
    // selector 的容器节点
    /* eslint-disable */
    const container = (
      component !== null ?
        (Nerv.findDOMNode(component) || document) :
        document
    )
    /* eslint-enable */

    // 特殊处理 ---- 选自己
    let selectSelf = false
    if (container !== document) {
      const $nodeList = container.parentNode.querySelectorAll(selector)
      for (let i = 0, len = $nodeList.length; i < len; ++i) {
        if (container === $nodeList[i]) {
          selectSelf = true
          break
        }
      }
    }

    if (single) {
      const el = selectSelf === true ? container : container.querySelector(selector)
      res.push(filter(fields, el, selector))
    } else {
      const $children = container.querySelectorAll(selector)
      const children = []
      selectSelf === true && children.push(container)
      for (let i = 0, len = $children.length; i < len; ++i) {
        children.push($children[i])
      }
      res.push(children.map(dom => filter(fields, dom)))
    }
  })
  cb(res)
}