function processTypeUserAttrs(typeUserAttr, values) {
    const advField = []
    const attrTypeMap = {
      array: selectUserAttrs,
      string: inputUserAttrs,
      number: numberAttribute,
      boolean: (attr, attrData) =>
        boolAttribute(attr, { ...attrData, [attr]: values[attr] }, { first: attrData.label }),
    }

    for (const attribute in typeUserAttr) {
      if (typeUserAttr.hasOwnProperty(attribute)) {
        const attrValType = userAttrType(attribute, typeUserAttr[attribute])
        const orig = mi18n.get(attribute)
        const tUA = typeUserAttr[attribute]
        const origValue = tUA.value || ''
        tUA.value = values[attribute] || tUA.value || ''

        if (tUA.label) {
          i18n[attribute] = Array.isArray(tUA.label) ? mi18n.get(...tUA.label) || tUA.label[0] : tUA.label
        }

        if (attrTypeMap[attrValType]) {
          advField.push(attrTypeMap[attrValType](attribute, tUA))
        }

        i18n[attribute] = orig
        tUA.value = origValue
      }
    }

    return advField.join('')
  }