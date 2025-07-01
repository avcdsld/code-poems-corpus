function checkPartition(obj) {
  var count = 0
  Object.keys(obj).forEach(key=> {
    if (obj[key] === '*String') count += 1
    if (obj[key] === '*Number') count += 1
  })
  return count === 1
}