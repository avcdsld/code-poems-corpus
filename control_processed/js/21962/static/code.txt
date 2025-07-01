function (worldWindow, layersPanel, timeSeriesPlayer) {
        var thisServersPanel = this;

        this.wwd = worldWindow;
        this.layersPanel = layersPanel;
        this.timeSeriesPlayer = timeSeriesPlayer;

        this.idCounter = 1;

        this.legends = {};

        $("#addServerBox").find("button").on("click", function (e) {
            thisServersPanel.onAddServerButton(e);
        });

        $("#addServerText").on("keypress", function (e) {
            thisServersPanel.onAddServerTextKeyPress($(this), e);
        });
    }