function isLeapYear (date) {
  var year
  var currentDate = date ? XEUtils.toStringDate(date) : new Date()
  if (isDate(currentDate)) {
    year = currentDate.getFullYear()
    return (year % 4 === 0) && (year % 100 !== 0 || year % 400 === 0)
  }
  return false
}