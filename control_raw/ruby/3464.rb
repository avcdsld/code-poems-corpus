def string_visible_contains(element, value)
      contains = {
        target: value,
        substring: true,
        insensitive: true
      }

      {
        typeArray: [element],
        onlyVisible: true,
        name: contains,
        label: contains,
        value: contains
      }
    end