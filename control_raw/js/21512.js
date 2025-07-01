function showType(ts, cm, pos) {
    ts.request(cm, "type", function(error, data) {
      if (error) return showError(ts, cm, error);
      if (ts.options.typeTip) {
        var tip = ts.options.typeTip(data);
      } else {
        var tip = elt("span", null, elt("strong", null, data.type || "not found"));
        if (data.doc)
          tip.appendChild(document.createTextNode(" — " + data.doc));
        if (data.url) {
          tip.appendChild(document.createTextNode(" "));
          var link = elt("a", null, "[docs]");
          link.target = '_blank';
          tip.appendChild(link).href = data.url;
        }
      }
      tempTooltip(cm, tip);
    }, pos);
  }