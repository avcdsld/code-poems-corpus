function drawDataPointsValueHighlights(data) {
            showCrossHairComponentsWithLabels(true);

            // Draw line perpendicular to y-axis
            highlightCrossHairContainer.selectAll('line.highlight-y-line')
              .attr('stroke', nameColorMap[data.name])
              .attr('class', 'highlight-y-line')
              .attr('x1', (xScale(data.x) - areaScale(data.y)))
              .attr('x2', 0)
              .attr('y1', yScale(data.y))
              .attr('y2', yScale(data.y));


            // Draw line perpendicular to x-axis
            highlightCrossHairContainer.selectAll('line.highlight-x-line')
              .attr('stroke', nameColorMap[data.name])
              .attr('class', 'highlight-x-line')
              .attr('x1', xScale(data.x))
              .attr('x2', xScale(data.x))
              .attr('y1', (yScale(data.y) + areaScale(data.y)))
              .attr('y2', chartHeight);

            // Draw data label for y value
            highlightCrossHairLabelsContainer.selectAll('text.highlight-y-legend')
              .attr('text-anchor', 'middle')
              .attr('fill', nameColorMap[data.name])
              .attr('class', 'highlight-y-legend')
              .attr('y', (yScale(data.y) + (areaScale(data.y) / 2)))
              .attr('x', highlightTextLegendOffset)
              .text(`${d3Format.format(yAxisFormat)(data.y)}`);

            // Draw data label for x value
            highlightCrossHairLabelsContainer.selectAll('text.highlight-x-legend')
              .attr('text-anchor', 'middle')
              .attr('fill', nameColorMap[data.name])
              .attr('class', 'highlight-x-legend')
              .attr('transform', `translate(0, ${chartHeight - highlightTextLegendOffset})`)
              .attr('x', (xScale(data.x) - (areaScale(data.y) / 2)))
              .text(`${d3Format.format(xAxisFormat)(data.x)}`);
        }