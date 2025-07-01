function drawSlices() {
            // Not ideal, we need to figure out how to call exit for nested elements
            if (slices) {
                svg.selectAll('g.arc').remove();
            }

            slices = svg.select('.chart-group')
                .selectAll('g.arc')
                .data(layout(data));

            let newSlices = slices.enter()
                .append('g')
                  .each(storeAngle)
                  .each(reduceOuterRadius)
                  .classed('arc', true)
                  .append('path');

            if (isAnimated) {
                newSlices.merge(slices)
                    .attr('fill', getSliceFill)
                    .on('mouseover', function(d) {
                        handleMouseOver(this, d, chartWidth, chartHeight);
                    })
                    .on('mousemove', function(d) {
                        handleMouseMove(this, d, chartWidth, chartHeight);
                    })
                    .on('mouseout', function(d) {
                        handleMouseOut(this, d, chartWidth, chartHeight);
                    })
                    .on('click', function(d) {
                        handleClick(this, d, chartWidth, chartHeight);
                    })
                    .transition()
                    .ease(ease)
                    .duration(pieDrawingTransitionDuration)
                    .attrTween('d', tweenLoading);
            } else {
                newSlices.merge(slices)
                    .attr('fill', getSliceFill)
                    .attr('d', shape)
                    .on('mouseover', function(d) {
                        handleMouseOver(this, d, chartWidth, chartHeight);
                    })
                    .on('mousemove', function(d) {
                        handleMouseMove(this, d, chartWidth, chartHeight);
                    })
                    .on('mouseout', function(d) {
                        handleMouseOut(this, d, chartWidth, chartHeight);
                    })
                    .on('click', function(d) {
                        handleClick(this, d, chartWidth, chartHeight);
                    });
            }

            slices.exit().remove();
        }