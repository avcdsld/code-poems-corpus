function buildContainerGroups() {
            let container = svg
              .append('g')
                .classed('container-group', true);

            container
              .append('g')
                .classed('chart-group', true);
            container
              .append('g')
                .classed('legend-group', true);
        }