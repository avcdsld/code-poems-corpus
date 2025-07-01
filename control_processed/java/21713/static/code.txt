@SuppressWarnings({"cast", "unchecked"})
    public static <E> Weigher<? super Iterable<E>> iterable() {
        return (Weigher<Iterable<E>>) (Weigher<?>) IterableWeigher.INSTANCE;
    }