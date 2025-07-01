function highlight(code) {
  return new Promise((resolve, reject) => {
    pygmentize({ lang: 'html', format: 'html' }, code, function (err, result) {
      if (err) {
        console.log(err);
        reject(err);
      } else {
        resolve(result.toString());
      };
    });
  });
}