function () {
    var data = this.data;
    var els;

    // If objects not defined, intersect with everything.
    els = data.objects
      ? this.el.sceneEl.querySelectorAll(data.objects)
      : this.el.sceneEl.querySelectorAll('*');
    this.objects = this.flattenObject3DMaps(els);
    this.dirty = false;
  }