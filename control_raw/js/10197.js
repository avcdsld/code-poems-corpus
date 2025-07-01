function completeProcess(messages) {
  var html = outputHTMLString(messages);
  var file = new Blob([html], {type: 'text/html'});
  var url = URL.createObjectURL(file);

  var a = document.getElementById('button');
  a.className = 'download';
  a.innerHTML = 'Download';
  a.href = url;
  a.download = "snap-it.html";
}