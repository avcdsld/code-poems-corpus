function drawDataPoints() {
            let circles = svg.select('.chart-group')
                .attr('clip-path', `url(#${maskingRectangleId})`)
                .selectAll('circle')
                .data(dataPoints)
                .enter();

            if (isAnimated) {
                circles
                    .append('circle')
                    .attr('class', 'data-point data-point-highlighter')
                    .transition()
                    .delay(delay)
                    .duration(duration)
                    .ease(ease)
                    .style('stroke', (d) => nameColorMap[d.name])
                    .attr('fill', (d) => (
                        hasHollowCircles ? hollowColor : nameColorMap[d.name]
                    ))
                    .attr('fill-opacity', circleOpacity)
                    .attr('r', (d) => areaScale(d.y))
                    .attr('cx', (d) => xScale(d.x))
                    .attr('cy', (d) => yScale(d.y))
                    .style('cursor', 'pointer');
            } else {
                circles
                    .append('circle')
                    .attr('class', 'point')
                    .attr('class', 'data-point-highlighter')
                    .style('stroke', (d) => nameColorMap[d.name])
                    .attr('fill', (d) => (
                        hasHollowCircles ? hollowColor : nameColorMap[d.name]
                    ))
                    .attr('fill-opacity', circleOpacity)
                    .attr('r', (d) => areaScale(d.y))
                    .attr('cx', (d) => xScale(d.x))
                    .attr('cy', (d) => yScale(d.y))
                    .style('cursor', 'pointer');
            }
        }