function isOOB (cb) {
  User.listByRoles('authority', function (err, users) {
    if (err) { return cb(err) }
    // return true if there are no authority users
    return cb(null, !users || !users.length)
  })
}