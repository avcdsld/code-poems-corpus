public static <T, R> Callable<R> andThen(Callable<T> callable, Function<T, R> resultHandler){
        return () -> resultHandler.apply(callable.call());
    }