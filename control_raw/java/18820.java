@Override
    protected ImageWritable doTransform(ImageWritable image, Random random) {
        if (image == null) {
            return null;
        }
        Mat mat = converter.convert(image.getFrame());
        int top = random != null ? random.nextInt(cropTop + 1) : cropTop;
        int left = random != null ? random.nextInt(cropLeft + 1) : cropLeft;
        int bottom = random != null ? random.nextInt(cropBottom + 1) : cropBottom;
        int right = random != null ? random.nextInt(cropRight + 1) : cropRight;

        y = Math.min(top, mat.rows() - 1);
        x = Math.min(left, mat.cols() - 1);
        int h = Math.max(1, mat.rows() - bottom - y);
        int w = Math.max(1, mat.cols() - right - x);
        Mat result = mat.apply(new Rect(x, y, w, h));

        return new ImageWritable(converter.convert(result));
    }