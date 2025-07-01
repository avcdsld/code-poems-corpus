function bestInitialLayout(areas, params) {
        var initial = greedyLayout(areas, params);
        var loss = params.lossFunction || lossFunction;

        // greedylayout is sufficient for all 2/3 circle cases. try out
        // constrained MDS for higher order problems, take its output
        // if it outperforms. (greedy is aesthetically better on 2/3 circles
        // since it axis aligns)
        if (areas.length >= 8) {
            var constrained  = constrainedMDSLayout(areas, params),
                constrainedLoss = loss(constrained, areas),
                greedyLoss = loss(initial, areas);

            if (constrainedLoss + 1e-8 < greedyLoss) {
                initial = constrained;
            }
        }
        return initial;
    }