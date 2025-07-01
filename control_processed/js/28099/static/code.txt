function formatTime(time) {
  let date = new Date(time);

  return (date.getFullYear() + '-' +
    zeroPad(date.getMonth() + 1) + '-' +
    zeroPad(date.getDate()) + ' ' +
    zeroPad(date.getHours()) + ':' +
    zeroPad(date.getMinutes()) + ':' +
    zeroPad(date.getSeconds()));

  function zeroPad(num) {
    return ('0' + num).slice(-2)
  }
}