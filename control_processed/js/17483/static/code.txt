function buildScales() {
            const decidedRange = isReverse ? [chartWidth, 0] : [0, chartWidth];

            xScale = d3Scale.scaleLinear()
                .domain([0, Math.max(ranges[0], markers[0], measures[0])])
                .rangeRound(decidedRange)
                .nice();

            // Derive width scales from x scales
            barWidth = bulletWidth(xScale);

            // set up opacity scale based on ranges and measures
            rangeOpacityScale = ranges.map((d, i) => startMaxRangeOpacity - (i * rangeOpacifyDiff)).reverse();
            measureOpacityScale = ranges.map((d, i) => 0.9 - (i * measureOpacifyDiff)).reverse();

            // initialize range and measure bars and marker line colors
            rangeColor = colorSchema[0];
            measureColor = colorSchema[1];
        }