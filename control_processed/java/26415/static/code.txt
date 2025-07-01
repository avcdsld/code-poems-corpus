public Blade after(@NonNull String path, @NonNull RouteHandler handler) {
        this.routeMatcher.addRoute(path, handler, HttpMethod.AFTER);
        return this;
    }