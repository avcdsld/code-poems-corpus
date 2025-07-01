function checkCssSupported() {
  // First, check if the 'perspective' CSS property or a vendor-prefixed
  // variant is available.
  var perspectiveProperty = prefixProperty('perspective');
  var el = document.createElement('div');
  var supported = typeof el.style[perspectiveProperty] !== 'undefined';

  // Certain versions of Chrome disable 3D transforms even though the CSS
  // property exists. In those cases, we use the following media query,
  // which only succeeds if the feature is indeed enabled.
  if (supported && perspectiveProperty === 'WebkitPerspective') {
    var id = '__marzipano_test_css3d_support__';
    var st = document.createElement('style');
    st.textContent = '@media(-webkit-transform-3d){#' + id + '{height: 3px;})';
    document.getElementsByTagName('head')[0].appendChild(st);
    el.id = id;
    document.body.appendChild(el);
    // The offsetHeight seems to be different than 3 at some zoom levels on
    // Chrome (and maybe other browsers). Test for > 0 instead.
    supported = el.offsetHeight > 0;
    st.parentNode.removeChild(st);
    el.parentNode.removeChild(el);
  }

  return supported;
}