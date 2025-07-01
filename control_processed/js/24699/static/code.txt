function stroke (from, to, template, init = true) {
    return `${init === true ? 'M' : 'L'}${Math.floor(template[from].x)},${Math.floor(template[from].y)} L${Math.floor(template[to].x)},${Math.floor(template[to].y)}`
  }