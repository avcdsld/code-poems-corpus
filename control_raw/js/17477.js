function handleMouseMove(e){
            let [xPosition, yPosition] = d3Selection.mouse(e),
                xPositionOffset = -margin.left, //Arbitrary number, will love to know how to assess it
                dataPoint = getNearestDataPoint(xPosition + xPositionOffset),
                dataPointXPosition;

            if (dataPoint) {
                dataPointXPosition = xScale(new Date(dataPoint.date));
                // More verticalMarker to that datapoint
                moveVerticalMarker(dataPointXPosition);
                // Add data points highlighting
                highlightDataPoints(dataPoint);
                // Emit event with xPosition for tooltip or similar feature
                dispatcher.call('customMouseMove', e, dataPoint, topicColorMap, dataPointXPosition, yPosition);
            }
        }