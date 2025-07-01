public OpentsdbEvent convert(ServiceMetricEvent serviceMetricEvent)
  {
    String metric = serviceMetricEvent.getMetric();
    if (!metricMap.containsKey(metric)) {
      return null;
    }

    long timestamp = serviceMetricEvent.getCreatedTime().getMillis() / 1000L;
    Number value = serviceMetricEvent.getValue();

    Map<String, Object> tags = new HashMap<>();
    String service = serviceMetricEvent.getService().replace(':', '_');
    String host = serviceMetricEvent.getHost().replace(':', '_');
    tags.put("service", service);
    tags.put("host", host);

    Map<String, Object> userDims = serviceMetricEvent.getUserDims();
    for (String dim : metricMap.get(metric)) {
      if (userDims.containsKey(dim)) {
        Object dimValue = userDims.get(dim);
        if (dimValue instanceof String) {
          dimValue = ((String) dimValue).replace(':', '_');
        }
        tags.put(dim, dimValue);
      }
    }

    return new OpentsdbEvent(sanitize(metric), timestamp, value, tags);
  }