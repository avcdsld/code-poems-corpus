function init() {
  'use strict';

  var wheel = document.querySelector('#wheel > svg');
  var cdn = document.querySelector('.mdl-gen__cdn .mdl-gen__cdn-link');
  var mc = new MaterialCustomizer(wheel, cdn);

  // Workaround for IE.
  var dl = document.querySelector('#download');
  dl.addEventListener('click', function() {
    if (window.navigator.msSaveBlob) {
      window.navigator.msSaveBlob(this.blob, 'material.min.css');
    }
  }.bind(mc));

  // Hook up GA event
  dl.addEventListener('click', function() {
    ga('send', {
      hitType: 'event',
      eventCategory: 'customizer',
      eventAction: 'download',
      eventLabel: mc.getSelectedPrimary() + '-' + mc.getSelectedSecondary()
    });
  });

  var clickCtr = 0;
  cdn.addEventListener('click', function() {
    var selection = window.getSelection();
    selection.removeAllRanges();

    var range = document.createRange();
    if (clickCtr === 0) {
      var link = cdn.querySelectorAll('.token.attr-value')[1];
      range.setStart(link, 2);
      range.setEnd(link, 3);
    } else {
      range.setStart(cdn, 1);
      range.setEnd(cdn, 2);
    }

    selection.addRange(range);
    clickCtr = (clickCtr + 1) % 2;
  });

  // Prevent browser's selection handling
  cdn.addEventListener('mouseup', function(ev) {
    ev.preventDefault();
  });
  cdn.addEventListener('mousedown', function(ev) {
    ev.preventDefault();
  });

  document.addEventListener('mouseup', function() {
    if (window.getSelection().toString().indexOf('.min.css') !== -1) {
      ga('send', {
        hitType: 'event',
        eventCategory: 'customizer',
        eventAction: 'copy',
        eventLabel: mc.getSelectedPrimary() + '-' + mc.getSelectedSecondary()
      });
    }
  });

  // Download template
  var req = new XMLHttpRequest();
  req.onload = function() {
    mc.template = this.responseText;
    mc.highlightField('Indigo');
    mc.highlightField('Pink');
    window.requestAnimationFrame(function() {
      mc.updateCDN();
      mc.updateStylesheet();
    });
  };
  req.open('get', '../material.min.css.template', true);
  req.send();
}