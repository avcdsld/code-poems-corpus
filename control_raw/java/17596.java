public static double iou(DetectedObject o1, DetectedObject o2) {
        double x1min  = o1.getCenterX() - o1.getWidth() / 2;
        double x1max  = o1.getCenterX() + o1.getWidth() / 2;
        double y1min  = o1.getCenterY() - o1.getHeight() / 2;
        double y1max  = o1.getCenterY() + o1.getHeight() / 2;

        double x2min  = o2.getCenterX() - o2.getWidth() / 2;
        double x2max  = o2.getCenterX() + o2.getWidth() / 2;
        double y2min  = o2.getCenterY() - o2.getHeight() / 2;
        double y2max  = o2.getCenterY() + o2.getHeight() / 2;

        double ow = overlap(x1min, x1max, x2min, x2max);
        double oh = overlap(y1min, y1max, y2min, y2max);

        double intersection = ow * oh;
        double union = o1.getWidth() * o1.getHeight() + o2.getWidth() * o2.getHeight() - intersection;
        return intersection / union;
    }