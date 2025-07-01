public static ModelAndView produceErrorView(final String view, final Exception e) {
        return new ModelAndView(view, CollectionUtils.wrap("rootCauseException", e));
    }