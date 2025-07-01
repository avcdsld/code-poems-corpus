function kruskal(weightFn) {
    weightFn = weightFn || function (edge) {
      return 1;
    };

    var _this$byGroup = this.byGroup(),
        nodes = _this$byGroup.nodes,
        edges = _this$byGroup.edges;

    var numNodes = nodes.length;
    var forest = new Array(numNodes);
    var A = nodes; // assumes byGroup() creates new collections that can be safely mutated

    var findSetIndex = function findSetIndex(ele) {
      for (var i = 0; i < forest.length; i++) {
        var eles = forest[i];

        if (eles.has(ele)) {
          return i;
        }
      }
    }; // start with one forest per node


    for (var i = 0; i < numNodes; i++) {
      forest[i] = this.spawn(nodes[i]);
    }

    var S = edges.sort(function (a, b) {
      return weightFn(a) - weightFn(b);
    });

    for (var _i = 0; _i < S.length; _i++) {
      var edge = S[_i];
      var u = edge.source()[0];
      var v = edge.target()[0];
      var setUIndex = findSetIndex(u);
      var setVIndex = findSetIndex(v);
      var setU = forest[setUIndex];
      var setV = forest[setVIndex];

      if (setUIndex !== setVIndex) {
        A.merge(edge); // combine forests for u and v

        setU.merge(setV);
        forest.splice(setVIndex, 1);
      }
    }

    return A;
  }