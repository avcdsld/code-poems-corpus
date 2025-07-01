function verifyPasswordsEnabled (req, res, next) {
  if (!settings.providers.password) {
    return next(new PasswordsDisabledError())
  } else {
    return next()
  }
}