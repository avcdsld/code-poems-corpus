private static Point getIntersection(Shape shape,
                                         Line2D.Double line) {
        if (shape instanceof Ellipse2D) {
            return getEllipseIntersection(shape,
                                          line);
        } else if (shape instanceof Rectangle2D || shape instanceof Path2D) {
            return getShapeIntersection(shape,
                                        line);
        } else {
            // something strange
            return null;
        }
    }