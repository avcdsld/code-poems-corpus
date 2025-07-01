function getTooltipPosition([mouseX, mouseY]) {
            let tooltipX, tooltipY;

            // show tooltip to the right
            if ((mouseX - tooltipWidth) < 0) {
                // Tooltip on the right
                tooltipX = tooltipWidth - 185;
            } else {
                // Tooltip on the left
                tooltipX = -205
            }

            if (mouseY) {
                tooltipY = tooltipOffset.y;
                // tooltipY = mouseY + tooltipOffset.y;
            } else {
                tooltipY = tooltipOffset.y;
            }

            return [tooltipX, tooltipY];
        }