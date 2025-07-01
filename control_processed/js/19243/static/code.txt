function(component, propertyName) {
      function handleProp(prop) {
        idx = ICAL.helpers.binsearchInsert(
          result,
          prop,
          compareTime
        );

        // ordered insert
        result.splice(idx, 0, prop);
      }

      var result = [];
      var props = component.getAllProperties(propertyName);
      var len = props.length;
      var i = 0;
      var prop;

      var idx;

      for (; i < len; i++) {
        props[i].getValues().forEach(handleProp);
      }

      return result;
    }