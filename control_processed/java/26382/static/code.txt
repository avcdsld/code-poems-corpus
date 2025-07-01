public static Validation<Integer> range(int min, int max) {
        return greaterThan(min).and(lowerThan(max));
    }