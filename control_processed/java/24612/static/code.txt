public static boolean isThereJobCallbackProperty(final Props props,
      final JobCallbackStatusEnum status) {

    if (props == null || status == null) {
      throw new NullPointerException("One of the argument is null");
    }

    final String jobCallBackUrl = firstJobcallbackPropertyMap.get(status);
    return props.containsKey(jobCallBackUrl);
  }