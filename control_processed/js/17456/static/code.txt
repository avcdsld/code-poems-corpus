function centerInlineLegendOnSVG() {
            let legendGroupSize = svg.select('g.legend-container-group').node().getBoundingClientRect().width + getLineElementMargin();
            let emptySpace = width - legendGroupSize;
            let newXPosition = (emptySpace/2);

            if (emptySpace > 0) {
                svg.select('g.legend-container-group')
                    .attr('transform', `translate(${newXPosition},0)`)
            }
        }