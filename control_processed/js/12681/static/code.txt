function cpu(callback) {

  return new Promise((resolve) => {
    process.nextTick(() => {
      getCpu().then(result => {
        if (callback) { callback(result); }
        resolve(result);
      });
    });
  });
}