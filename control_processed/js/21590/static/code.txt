function nextColor(pos, start, finish) {
    var r = [], i, e, from, to
    for (i = 0; i < 6; i++) {
      from = Math.min(15, parseInt(start.charAt(i),  16))
      to   = Math.min(15, parseInt(finish.charAt(i), 16))
      e = Math.floor((to - from) * pos + from)
      e = e > 15 ? 15 : e < 0 ? 0 : e
      r[i] = e.toString(16)
    }
    return '#' + r.join('')
  }