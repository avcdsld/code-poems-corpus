function (texture) {
        var pixels = texture.pixels;
        var width = texture.width;
        var height = texture.height;

        function fetchPixel(x, y, rg) {
            x = Math.max(Math.min(x, width - 1), 0);
            y = Math.max(Math.min(y, height - 1), 0);
            var idx = (y * (width - 1) + x) * 4;
            if (pixels[idx + 3] === 0) {
                return false;
            }
            rg[0] = pixels[idx];
            rg[1] = pixels[idx + 1];
            return true;
        }

        function addPixel(a, b, out) {
            out[0] = a[0] + b[0];
            out[1] = a[1] + b[1];
        }

        var center = [], left = [], right = [], top = [], bottom = [];
        var weight = 0;
        for (var y = 0; y < height; y++) {
            for (var x = 0; x < width; x++) {
                var idx = (y * (width - 1) + x) * 4;
                if (pixels[idx + 3] === 0) {
                    weight = center[0] = center[1] = 0;
                    if (fetchPixel(x - 1, y, left)) {
                        weight++; addPixel(left, center, center);
                    }
                    if (fetchPixel(x + 1, y, right)) {
                        weight++; addPixel(right, center, center);
                    }
                    if (fetchPixel(x, y - 1, top)) {
                        weight++; addPixel(top, center, center);
                    }
                    if (fetchPixel(x, y + 1, bottom)) {
                        weight++; addPixel(bottom, center, center);
                    }
                    center[0] /= weight;
                    center[1] /= weight;
                    // PENDING If overwrite. bilinear interpolation.
                    pixels[idx] = center[0];
                    pixels[idx + 1] = center[1];
                }
                pixels[idx + 3] = 1;
            }
        }
    }