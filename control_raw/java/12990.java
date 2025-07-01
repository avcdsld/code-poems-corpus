private static Point getEllipseIntersection(Shape shape,
                                                Line2D.Double line) {
        double angle = Math.atan2(line.y2 - line.y1,
                                  line.x2 - line.x1);
        double x = shape.getBounds2D().getWidth() / 2 * Math.cos(angle) + shape.getBounds2D().getCenterX();
        double y = shape.getBounds2D().getHeight() / 2 * Math.sin(angle) + shape.getBounds2D().getCenterY();
        Point p = new Point();
        p.setLocation(x,
                      y);
        return p;
    }