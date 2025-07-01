function weekFormat() {

  const format = function(d) {
    return formatWeekYear(d) + "w" + formatWeek(d);
  };

  format.parse = function parse(dateString) {
    const matchedDate = dateString.match(/^(\d{4})w(\d{2})$/);
    return matchedDate ? getDateFromWeek(matchedDate[1], matchedDate[2]) : null;
  };

  const formatWeekYear = function(d) {
    if (!(d instanceof Date)) d = new Date(+d);
    return new Date(+d + ((4 - (d.getUTCDay() || 7)) * 86400000)).getUTCFullYear();
  };

  const formatWeek = function(d) {
    if (!(d instanceof Date)) d = new Date(+d);
    const quote = new Date(+d + ((4 - (d.getUTCDay() || 7)) * 86400000));
    const week = Math.ceil(((quote.getTime() - quote.setUTCMonth(0, 1)) / 86400000 + 1) / 7);
    return week < 10 ? "0" + week : week;
  };

  const getDateFromWeek = function(p1, p2) {
    const week = parseInt(p2);
    const year = p1;
    const startDateOfYear = new Date(); // always 4th of January (according to standard ISO 8601)
    startDateOfYear.setUTCFullYear(year);
    startDateOfYear.setUTCMonth(0);
    startDateOfYear.setUTCDate(4);
    const startDayOfWeek = startDateOfYear.getUTCDay() || 7;
    const dayOfWeek = 1; // Monday === 1
    const dayOfYear = week * 7 + dayOfWeek - (startDayOfWeek + 4);

    let date = formats["year"].data.parse(year);
    date = new Date(date.getTime() + dayOfYear * 24 * 60 * 60 * 1000);

    return date;
  };

  return format;

}