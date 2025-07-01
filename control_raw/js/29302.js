function FileKeyInfo(file) {
  this.file = file

  this.getKeyInfo = function(key, prefix) {
    prefix = prefix || ''
    prefix = prefix ? prefix + ':' : prefix
    return "<" + prefix + "X509Data></" + prefix + "X509Data>"
  }

  this.getKey = function(keyInfo) {
    return fs.readFileSync(this.file)
  }
}