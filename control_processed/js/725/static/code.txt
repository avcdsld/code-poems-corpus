function mapExec(array, func) {
  for (var i = 0; i < array.length; ++i) {
    func.call(this, array[i], i);
  }
}