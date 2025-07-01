function copyTimeFromDateToDate(date1, date2) {
  date2.setHours(date1.getHours());
  date2.setMinutes(date1.getMinutes());
  date2.setSeconds(date1.getSeconds());
  date2.setMilliseconds(date1.getMilliseconds());
}