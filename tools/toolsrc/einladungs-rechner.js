(function () {
  var $ = function (id) { return document.getElementById(id); }, ids = ['g', 'h', 'res', 'wd', 'std', 'ck', 'porto'];
  var st = HT.load('einladung', { g: '60', h: '35', res: '10', wd: '', std: '1', ck: '1,50', porto: '0,95' });
  ids.forEach(function (k) { if (st[k] !== undefined) $(k).value = st[k]; });
  function eur(n) { return n.toLocaleString('de-DE', { style: 'currency', currency: 'EUR' }); }
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function fd(d) { return pad(d.getDate()) + '.' + pad(d.getMonth() + 1) + '.' + d.getFullYear(); }
  function calc() {
    ids.forEach(function (k) { st[k] = $(k).value; }); HT.save('einladung', st);
    var g = Math.max(0, Math.round(HT.num(st.g))), h = Math.max(0, Math.round(HT.num(st.h))), r = Math.max(0, HT.num(st.res));
    if (h > g) h = g;
    var n = Math.ceil(h * (1 + r / 100)), mal = st.std === '1' ? 2 : 1, ck = HT.num(st.ck), po = HT.num(st.porto);
    var cards = n * mal, costK = cards * ck, costP = h * mal * po;
    $('sum').innerHTML = 'Ihr braucht etwa <b>' + n + ' Einladungen</b> für ' + h + ' Haushalte' + (mal === 2 ? ' (und ebenso viele Save-the-Dates, zusammen ' + cards + ' Karten)' : '') + '.';
    $('rows').innerHTML = [['Karten und Umschläge (inkl. Reserve)', eur(costK)], ['Porto (ohne Reserve)', eur(costP)], ['Gesamt', eur(costK + costP)], ['Pro Haushalt', h ? eur((costK + costP) / h) : '–']].map(function (x) { return '<tr><th scope="row" style="text-align:left">' + x[0] + '</th><td class="num"><b>' + x[1] + '</b></td></tr>'; }).join('');
    var v = st.wd, rows = [];
    if (/^\d{4}-\d{2}-\d{2}$/.test(v)) {
      var w = new Date(v + 'T12:00:00'), back = function (days) { var d = new Date(w.getTime()); d.setDate(d.getDate() - days); return fd(d); };
      if (mal === 2) rows.push([back(270) + ' bis ' + back(180), 'Save-the-Date verschicken']);
      rows.push([back(30 * 5) + ' bis ' + back(30 * 3), 'Einladungen gestalten, drucken und verschicken']);
      rows.push([back(56), 'Rückmeldefrist setzen']);
      rows.push([back(42), 'Fehlende Antworten nachfassen']);
      rows.push([back(21), 'Endgültige Gästezahl an Location und Catering melden']);
    } else rows.push(['–', 'Bitte Hochzeitsdatum eintragen, dann erscheint der Zeitplan.']);
    $('plan').innerHTML = rows.map(function (x) { return '<tr><td>' + x[0] + '</td><td>' + x[1] + '</td></tr>'; }).join('');
  }
  ids.forEach(function (k) { $(k).addEventListener('input', calc); $(k).addEventListener('change', calc); }); calc();
})();
