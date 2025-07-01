function readFilePaths(files) {
    const locations = [];
    for (let i = 0; i < files.length; i++) {
      const file = files[i];
      const location = path.join(__dirname, "../../../", file);
      locations.push(location);
    }
    return locations;
  }