function (translationId, interpolateParams, Interpolator, sanitizeStrategy) {
      // Start with the fallbackLanguage with index 0
      return resolveForFallbackLanguageInstant((startFallbackIteration > 0 ? startFallbackIteration : fallbackIndex), translationId, interpolateParams, Interpolator, sanitizeStrategy);
    }