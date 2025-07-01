function authenticateClient (req, res, next) {
  Client.authenticate(req, function (err, client) {
    if (err) { return next(err) }
    req.client = client
    next()
  })
}