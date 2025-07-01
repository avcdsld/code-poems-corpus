@Override
    protected ImageWritable doTransform(ImageWritable image, Random random) {
        if (image == null) {
            return null;
        }
        Mat mat = (Mat) converter.convert(image.getFrame());

        Mat result = new Mat();

        try {
            cvtColor(mat, result, conversionCode);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        return new ImageWritable(converter.convert(result));
    }