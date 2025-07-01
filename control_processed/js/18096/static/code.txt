function formatTimezoneOffset (minutes) {
  let sign = simpleSign(negateExceptForZero(minutes))
  minutes = Math.abs(minutes)
  let hours = Math.floor(minutes / 60)
  minutes -= hours * 60
  let strHours = String(hours)
  let strMinutes = String(minutes)
  if (strHours.length < 2) strHours = '0' + strHours
  if (strMinutes.length < 2) strMinutes = '0' + strMinutes
  return (sign === -1 ? '-' : '+') + strHours + strMinutes
}