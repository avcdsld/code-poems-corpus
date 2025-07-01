function updateLinkSetOnLoad(linkSet, load) {
      // console.log('update linkset on load ' + load.name);
      // snapshot(linkSet.loader);

      console.assert(load.status == 'loaded' || load.status == 'linked', 'loaded or linked');

      linkSet.loadingCount--;

      if (linkSet.loadingCount > 0)
        return;

      // adjusted for spec bug https://bugs.ecmascript.org/show_bug.cgi?id=2995
      var startingLoad = linkSet.startingLoad;

      // non-executing link variation for loader tracing
      // on the server. Not in spec.
      /***/
      if (linkSet.loader.loaderObj.execute === false) {
        var loads = [].concat(linkSet.loads);
        for (var i = 0, l = loads.length; i < l; i++) {
          var load = loads[i];
          load.module = load.kind == 'dynamic' ? {
            module: _newModule({})
          } : {
            name: load.name,
            module: _newModule({}),
            evaluated: true
          };
          load.status = 'linked';
          finishLoad(linkSet.loader, load);
        }
        return linkSet.resolve(startingLoad);
      }
      /***/

      var abrupt = doLink(linkSet);

      if (abrupt)
        return;

      console.assert(linkSet.loads.length == 0, 'loads cleared');

      linkSet.resolve(startingLoad);
    }