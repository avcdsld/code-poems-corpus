function(eventTags, logger) {
    if (eventTags && eventTags.hasOwnProperty(VALUE_EVENT_METRIC_NAME)) {
      var rawValue = eventTags[VALUE_EVENT_METRIC_NAME];
      var parsedEventValue = parseFloat(rawValue);
      if (isNaN(parsedEventValue)) {
        logger.log(LOG_LEVEL.INFO, sprintf(LOG_MESSAGES.FAILED_TO_PARSE_VALUE, MODULE_NAME, rawValue));
        return null;
      }
      logger.log(LOG_LEVEL.INFO, sprintf(LOG_MESSAGES.PARSED_NUMERIC_VALUE, MODULE_NAME, parsedEventValue));
      return parsedEventValue;
    }
    return null;
  }