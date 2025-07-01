function _setTimeIfInRange(clock, timeToSet, stopTime) {
  stopTime = defaultValue(stopTime, clock.stopTime);

  if (JulianDate.lessThan(timeToSet, clock.startTime)) {
    clock.currentTime = clock.startTime.clone();
  } else if (JulianDate.greaterThan(timeToSet, stopTime)) {
    clock.currentTime = stopTime.clone();
  } else {
    clock.currentTime = timeToSet.clone();
  }
}