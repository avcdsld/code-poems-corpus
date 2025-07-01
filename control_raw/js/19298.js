function parseDuration(durationString) {
  if (durationString === null || typeof durationString === 'undefined') {
    return -1;
  }
  // Some VAST doesn't have an HH:MM:SS duration format but instead jus the number of seconds
  if (util.isNumeric(durationString)) {
    return parseInt(durationString);
  }

  const durationComponents = durationString.split(':');
  if (durationComponents.length !== 3) {
    return -1;
  }

  const secondsAndMS = durationComponents[2].split('.');
  let seconds = parseInt(secondsAndMS[0]);
  if (secondsAndMS.length === 2) {
    seconds += parseFloat(`0.${secondsAndMS[1]}`);
  }

  const minutes = parseInt(durationComponents[1] * 60);
  const hours = parseInt(durationComponents[0] * 60 * 60);

  if (
    isNaN(hours) ||
    isNaN(minutes) ||
    isNaN(seconds) ||
    minutes > 60 * 60 ||
    seconds > 60
  ) {
    return -1;
  }
  return hours + minutes + seconds;
}