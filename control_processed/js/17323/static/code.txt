function buildAxis(){
            let minor, major;

            if (xAxisFormat === 'custom' && typeof xAxisCustomFormat === 'string') {
                minor = {
                    tick: xTicks,
                    format: d3TimeFormat.timeFormat(xAxisCustomFormat)
                };
            } else {
                ({minor, major} = timeAxisHelper.getTimeSeriesAxis(data, width, xAxisFormat));
            }

            xAxis = d3Axis.axisBottom(xScale)
                .ticks(minor.tick)
                .tickSize(10, 0)
                .tickPadding([tickPadding])
                .tickFormat(minor.format);
        }