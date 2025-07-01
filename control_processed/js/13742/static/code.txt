function() {

      var elementFilter = this.options.filterElements
      var forceContext = this.options.forceContext
      return getText(this.node)
      /**
       * Gets aggregate text of a node without resorting
       * to broken innerText/textContent
       */
      function getText(node, txt) {

        if (node.nodeType === 3) {
          return [node.data]
        }

        if (elementFilter && !elementFilter(node)) {
          return []
        }

        var txt = ['']
        var i = 0
        if (node = node.firstChild) do {

          if (node.nodeType === 3) {
            txt[i] += node.data
            continue
          }

          var innerText = getText(node)
          if (
            forceContext &&
            node.nodeType === 1 &&
            (forceContext === true || forceContext(node))
          ) {
            txt[++i] = innerText
            txt[++i] = ''
          } else {
            if (typeof innerText[0] === 'string') {
              // Bridge nested text-node data so that they're
              // not considered their own contexts:
              // I.e. ['some', ['thing']] -> ['something']
              txt[i] += innerText.shift()
            }
            if (innerText.length) {
              txt[++i] = innerText
              txt[++i] = ''
            }
          }
        } while (node = node.nextSibling)
        return txt
      }
      
    }