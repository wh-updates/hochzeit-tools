(function () {
  // Blume, Saison (von, bis Monat), Farben
  var F = [
    ['Tulpen', 3, 5, ['weiss', 'rosa', 'rot', 'gelb']], ['Ranunkeln', 3, 5, ['weiss', 'rosa', 'rot', 'gelb']], ['Narzissen', 3, 4, ['gelb', 'weiss']], ['Flieder', 4, 5, ['blau', 'weiss']], ['Anemonen', 11, 4, ['weiss', 'rosa', 'rot', 'blau']],
    ['Pfingstrosen', 5, 6, ['weiss', 'rosa', 'rot']], ['Rosen', 5, 10, ['weiss', 'rosa', 'rot', 'gelb']], ['Rittersporn', 6, 8, ['blau', 'weiss']], ['Lavendel', 6, 8, ['blau']], ['Schleierkraut', 6, 9, ['weiss']],
    ['Sonnenblumen', 7, 9, ['gelb']], ['Dahlien', 7, 10, ['weiss', 'rosa', 'rot', 'gelb']], ['Hortensien', 6, 10, ['weiss', 'rosa', 'blau', 'gruen']], ['Zinnien', 7, 9, ['rosa', 'rot', 'gelb']], ['Ziergräser', 7, 10, ['gruen', 'gelb']],
    ['Chrysanthemen', 9, 11, ['weiss', 'gelb', 'rot']], ['Beerenzweige', 9, 12, ['rot']], ['Amaryllis', 11, 2, ['rot', 'weiss', 'rosa']], ['Christrosen', 12, 3, ['weiss', 'gruen']], ['Nelken', 1, 12, ['weiss', 'rosa', 'rot']], ['Eukalyptus', 1, 12, ['gruen']], ['Tannengrün', 11, 2, ['gruen']]
  ];
  var MN = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'], $ = function (id) { return document.getElementById(id); };
  var TIP = { rund: 'Ein runder Strauß mit zwei bis drei Blumensorten wirkt ruhig und klassisch und lässt sich gut tragen.', wild: 'Lockere Sträuße mit Gräsern und Wildblumen passen zu Natur, Strand und Wiese. Ein Band aus Leinen oder Seide rundet ab.', wasserfall: 'Fließende Sträuße brauchen Blüten mit längeren Trieben oder Grün. Sie wirken besonders auf Treppen und vor Kirchen- oder Hallenräumen.', minimal: 'Wenige große Blüten wie Pfingstrosen, Dahlien oder Hortensien brauchen kaum Beiwerk. Dafür muss die Qualität der einzelnen Blüte stimmen.' };
  $('month').innerHTML = MN.map(function (m, i) { return '<option value="' + (i + 1) + '">' + m + '</option>'; }).join('');
  var st = HT.load('strauss', { m: String(new Date().getMonth() + 2 > 12 ? 1 : new Date().getMonth() + 2), c: 'weiss', s: 'rund' }); $('month').value = st.m; $('color').value = st.c; $('style').value = st.s;
  function inSeason(f, m) { return f[1] <= f[2] ? (m >= f[1] && m <= f[2]) : (m >= f[1] || m <= f[2]); }
  function render() {
    st = { m: $('month').value, c: $('color').value, s: $('style').value }; HT.save('strauss', st);
    var m = +st.m, main = F.filter(function (f) { return inSeason(f, m) && f[3].indexOf(st.c) >= 0 && f[0] !== 'Eukalyptus' && f[0] !== 'Tannengrün' && f[0] !== 'Ziergräser'; }),
      green = F.filter(function (f) { return inSeason(f, m) && f[3].indexOf('gruen') >= 0 && (f[0] === 'Eukalyptus' || f[0] === 'Tannengrün' || f[0] === 'Ziergräser' || f[0] === 'Christrosen'); });
    var other = F.filter(function (f) { return inSeason(f, m) && f[3].indexOf(st.c) < 0 && green.indexOf(f) < 0 && f[0] !== 'Eukalyptus'; });
    $('res').innerHTML = '<h3>Hauptblumen in ' + MN[m - 1] + '</h3><p>' + (main.length ? main.map(function (f) { return '<span class="pill">' + f[0] + '</span>'; }).join(' ') : 'In dieser Farbe gibt es in diesem Monat wenig Saisonware. Fragt eure Floristin nach Alternativen oder nach Farbtönen daneben.') + '</p>' +
      '<h3>Grün und Beiwerk</h3><p>' + (green.length ? green.map(function (f) { return '<span class="pill">' + f[0] + '</span>'; }).join(' ') : 'Eukalyptus ist fast das ganze Jahr verfügbar.') + '</p>' +
      (other.length ? '<h3>Weitere Saisonblumen in anderen Farben</h3><p>' + other.map(function (f) { return '<span class="pill">' + f[0] + '</span>'; }).join(' ') + '</p>' : '');
    $('tip').textContent = TIP[st.s];
  }
  ['month', 'color', 'style'].forEach(function (id) { $(id).addEventListener('change', render); }); render();
})();
