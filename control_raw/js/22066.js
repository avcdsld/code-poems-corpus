function renderEjs(filename, data, element, callback) {
  $.get(filename)
    .done(function(htmlTmpl) {
      element.html(ejs.render(htmlTmpl, data));
    })
    .fail(function(error) {
      console.log('failed to get html template ' + filename + ': ' + JSON.stringify(error));
      alert('failed to fetch html template ' + filename);
    })
    .always(function () {
      if (typeof callback === 'function') callback();
      resizeApp();
    });
}