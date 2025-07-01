function ensureDirExists (name) {
  try {
    fs.mkdirSync(path.join(__dirname, name));
  } catch (e) {
    if (e.code !== 'EEXIST') {
      console.log("Error ensuring that node_modules exists");
      process.exit(1);
    }
  }
}