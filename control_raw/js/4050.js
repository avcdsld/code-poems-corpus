function _0xColorToHex(color, convertToStr) {
        var hexColor = tinycolor(color.replace("0x", "#"));
        hexColor._format = "0x";

        if (convertToStr) {
            return hexColor.toString();
        }
        return hexColor;
    }