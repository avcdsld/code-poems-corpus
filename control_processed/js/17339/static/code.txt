function drawEndMarker(){
            if (circle) {
                svg.selectAll('.sparkline-circle').remove();
            }

            circle = svg.selectAll('.chart-group')
              .append('circle')
                .attr('class', 'sparkline-circle')
                .attr('cx', xScale(data[data.length - 1].date))
                .attr('cy', yScale(data[data.length - 1].value))
                .attr('r', markerSize);
        }