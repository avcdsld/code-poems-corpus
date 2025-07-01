function (type) {
      var items = this.elm_result.children;
      var index = 0;
      for (var i = 0; i < items.length; i++) {
        if (items[i].className == 'ok') {
          items[i].className = '';
          if (type == 'up') index = i - 1;
          else index = i + 1;
          break;
        };
      };
      if (items[index]) items[index].className = 'ok';
    }