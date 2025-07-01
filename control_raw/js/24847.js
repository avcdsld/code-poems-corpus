function blockTicks (d) {
    const k = (d.end - d.start) / d.len
    return range(0, d.len, conf.ticks.spacing).map((v, i) => {
      return {
        angle: v * k + d.start,
        label: displayLabel(v, i)
      }
    })
  }