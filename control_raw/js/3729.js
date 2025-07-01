function _measureText(text) {
        var measuringElement = $("<span />", { css : { "position" : "absolute", "top" : "-200px", "left" : "-1000px", "visibility" : "hidden", "white-space": "pre" } }).appendTo("body");
        measuringElement.text("pW" + text);
        var width = measuringElement.width();
        measuringElement.remove();
        return width;
    }