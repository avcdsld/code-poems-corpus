function (worldWindow) {

        var self = this;

        /**
         * The WorldWindow associated with this annotation controller.
         * @type {WorldWindow}
         */
        this.worldWindow = worldWindow;

        // Store the loaded annotation so we may read/modify
        // its settings
        this.currentAnnotation = null;

        // Store DOM slider elements
        this.opacitySlider = $("#opacitySlider");
        this.scaleSlider = $("#scaleSlider");
        this.cornerSlider = $("#cornerSlider");
        this.leadWidthSlider = $("#leadWidthSlider");
        this.leadHeightSlider = $("#leadHeightSlider");
        this.backgroundR = $("#bgR");
        this.backgroundG = $("#bgG");
        this.backgroundB = $("#bgB");
        this.textR = $("#textR");
        this.textG = $("#textG");
        this.textB = $("#textB");

        // Store DOM spinner elements for the insets
        this.spinnerLeft = $("#spinnerLeft");
        this.spinnerRight = $("#spinnerRight");
        this.spinnerTop = $("#spinnerTop");
        this.spinnerBottom = $("#spinnerBottom");

        // Store DOM input elements
        this.text = $("#annotationText");

        // Store DOM label elements
        this.bgColorLabel = $("#bgColor");
        this.textColorLabel = $("#textColor");
        this.opacityLabel = $("#opacity");
        this.scaleLabel = $("#scale");
        this.cornerRadiusLabel = $("#cornerRadius");
        this.leaderGapLabel = $("#leadSize");

        // Create an event for the textbox so that we may update the
        // annotation's label as the textbox contents change
        this.text.on('input', function (e) {
            self.currentAnnotation.text = this.value;
            self.worldWindow.redraw();
        });

        this.opacitySlider.slider({
            value: 0,
            min: 0,
            max: 1,
            step: 0.1,
            animate: true,
            slide: function (event, ui) {
                $("#opacity").html(ui.value);
                self.currentAnnotation.attributes.opacity = ui.value;
            }
        });

        this.scaleSlider.slider({
            value: 1,
            min: 0.70,
            max: 2,
            step: 0.1,
            animate: true,
            slide: function (event, ui) {
                $("#scale").html(ui.value);
                self.currentAnnotation.attributes.scale = ui.value;
            }
        });

        this.cornerSlider.slider({
            value: 1,
            min: 0,
            max: 30,
            step: 1,
            animate: true,
            slide: function (event, ui) {
                $("#cornerRadius").html(ui.value);
                self.currentAnnotation.attributes.cornerRadius = ui.value;
            }
        });

        // Width value of the lead (arrow)
        this.leadWidthSlider.slider({
            //value: 40,
            min: 0,
            max: 70,
            step: 1,
            animate: true,
            slide: function (event, ui) {
                self.changeLeadSize(
                    self.leadWidthSlider.slider('value'),
                    self.leadHeightSlider.slider('value'));
            }
        });

        // Length value of the lead (arrow)
        this.leadHeightSlider.slider({
            //value: 30,
            min: 0,
            max: 100,
            animate: true,
            slide: function (event, ui) {
                self.changeLeadSize(
                    self.leadWidthSlider.slider('value'),
                    self.leadHeightSlider.slider('value'));
            }
        });

        // Red value of the background color
        this.backgroundR.slider({
            value: 0,
            min: 0,
            max: 255,
            step: 1,
            animate: true,
            slide: function (event, ui) {
                self.changeBackgroundColor(
                    self.backgroundR.slider('value'),
                    self.backgroundG.slider('value'),
                    self.backgroundB.slider('value'));
            }
        });

        // Green value of the background color
        this.backgroundG.slider({
            value: 0,
            min: 0,
            max: 255,
            animate: true,
            slide: function (event, ui) {
                self.changeBackgroundColor(
                    self.backgroundR.slider('value'),
                    self.backgroundG.slider('value'),
                    self.backgroundB.slider('value'));
            }
        });

        // Blue value of the background color
        this.backgroundB.slider({
            value: 0,
            min: 0,
            max: 255,
            animate: true,
            slide: function (event, ui) {
                self.changeBackgroundColor(
                    self.backgroundR.slider('value'),
                    self.backgroundG.slider('value'),
                    self.backgroundB.slider('value'));
            }
        });

        // Red value of the text color
        this.textR.slider({
            value: 0,
            min: 0,
            max: 255,
            animate: true,
            slide: function (event, ui) {
                self.changeTextColor(
                    self.textR.slider('value'),
                    self.textG.slider('value'),
                    self.textB.slider('value'));
            }
        });

        // Green value of the text color
        this.textG.slider({
            value: 0,
            min: 0,
            max: 255,
            animate: true,
            slide: function (event, ui) {
                self.changeTextColor(
                    self.textR.slider('value'),
                    self.textG.slider('value'),
                    self.textB.slider('value'));
            }
        });

        // Blue value of the text color
        this.textB.slider({
            value: 0,
            min: 0,
            max: 255,
            animate: true,
            slide: function (event, ui) {
                self.changeTextColor(
                    self.textR.slider('value'),
                    self.textG.slider('value'),
                    self.textB.slider('value'));
            }
        });

        // Left inset spinner
        this.spinnerLeft.spinner({
            min: 0,
            max: 100,
            spin: function (event, ui) {
                var insets = self.currentAnnotation.attributes.insets.clone();
                insets.left = ui.value;
                self.currentAnnotation.attributes.insets = insets;
                self.worldWindow.redraw();
            }
        });

        // Right inset spinner
        this.spinnerRight.spinner({
            min: 0,
            max: 100,
            spin: function (event, ui) {
                var insets = self.currentAnnotation.attributes.insets.clone();
                insets.right = ui.value;
                self.currentAnnotation.attributes.insets = insets;
                self.worldWindow.redraw();
            }
        });

        // Top inset spinner
        this.spinnerTop.spinner({
            min: 0,
            max: 100,
            spin: function (event, ui) {
                var insets = self.currentAnnotation.attributes.insets.clone();
                insets.top = ui.value;
                self.currentAnnotation.attributes.insets = insets;
                self.worldWindow.redraw();
            }
        });

        // Bottom inset spinner
        this.spinnerBottom.spinner({
            min: 0,
            max: 100,
            spin: function (event, ui) {
                var insets = self.currentAnnotation.attributes.insets.clone();
                insets.bottom = ui.value;
                self.currentAnnotation.attributes.insets = insets;
                self.worldWindow.redraw();
            }
        });
    }