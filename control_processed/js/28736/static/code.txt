function loadConfig(path) {
  try {
    var configJSON = JSON.parse(fs.readFileSync(process.cwd() + "/" + path));
    console.log("Config file detected: " + path)
    return configJSON;
  }
  catch(e) {
    console.log("Config file: " + e.toString())
  }
}