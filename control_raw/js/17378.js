function handleClick(e) {
            let { closestPoint } = getPointProps(e);
            let d = getPointData(closestPoint);

            handleClickAnimation(d);

            dispatcher.call('customClick', e, d, d3Selection.mouse(e), [chartWidth, chartHeight]);
        }