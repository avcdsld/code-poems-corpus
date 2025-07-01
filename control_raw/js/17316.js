function buildScales(){
            xScale = d3Scale.scaleBand()
                .domain(data.map(getKey))
                .rangeRound([0, chartWidth])
                .paddingInner(0);

            yScale = d3Scale.scaleLinear()
                .domain([0, d3Array.max(data, getValue)])
                .rangeRound([chartHeight, 0]);
        }