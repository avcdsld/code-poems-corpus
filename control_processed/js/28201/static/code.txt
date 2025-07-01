function($super, properties, data, orientation, colorScheme, exportMode) {
            this.timeUtils = Splunk.JSCharting.TimeUtils;
            this.exportMode = exportMode;
            $super(properties, data, orientation, colorScheme);
        }