function load(path) {
  return io.read(path).then(data => {
    let zip = new Zip;
    return zip.z_.loadAsync(data).then(() => zip);
  });
}