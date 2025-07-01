function drawHourLabels() {
            let hourLabelsGroup = svg.select('.hour-labels-group');

            hourLabels = svg.select('.hour-labels-group').selectAll('.hour-label')
                .data(hoursHuman);

            hourLabels.enter()
              .append('text')
                .text((label) => label)
                .attr('y', 0)
                .attr('x', (d, i) => i * boxSize)
                .style('text-anchor', 'middle')
                .style('dominant-baseline', 'central')
                .attr('class', 'hour-label');

            hourLabelsGroup.attr('transform', `translate(${boxSize / 2}, -${hourLabelHeight})`);
        }