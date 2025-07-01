private Double fetchQualityValue(Iterable<CodeQuality> qualityIterable, String param) {
    Double paramValue = null;
    Iterator<CodeQuality> qualityIterator = qualityIterable.iterator();

    if (!qualityIterator.hasNext()) {
      return paramValue;
    }

    CodeQuality codeQuality = qualityIterator.next();
    for (CodeQualityMetric codeQualityMetric : codeQuality.getMetrics()) {
      if (codeQualityMetric.getName().equals(param)) {
        paramValue = Double.valueOf(codeQualityMetric.getValue());
        break;
      }
    }

    return paramValue;
  }