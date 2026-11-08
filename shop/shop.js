(function () {
  var L = window.SHOP_LINKS || {};
  document.querySelectorAll('a.buy').forEach(function (a) {
    var url = L[a.getAttribute('data-product')];
    if (url) { a.href = url; a.textContent = 'Jetzt kaufen'; a.removeAttribute('aria-disabled'); a.rel = 'nofollow'; }
  });
})();
