(function () {
  var $ = function (id) { return document.getElementById(id); };
  var STATES = { 'Baden-Württemberg': ['dk', 'fr', 'al'], 'Bayern': ['dk', 'fr', 'al'], 'Berlin': ['fm'], 'Brandenburg': ['rf'], 'Bremen': ['rf'], 'Hamburg': ['rf'], 'Hessen': ['fr'], 'Mecklenburg-Vorpommern': ['rf', 'fm'], 'Niedersachsen': ['rf'], 'Nordrhein-Westfalen': ['fr', 'al'], 'Rheinland-Pfalz': ['fr', 'al'], 'Saarland': ['fr', 'al'], 'Sachsen': ['rf', 'bb'], 'Sachsen-Anhalt': ['dk', 'rf'], 'Schleswig-Holstein': ['rf'], 'Thüringen': ['rf', 'wk'] };
  var MN = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'], WD = ['Sonntag', 'Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag'];
  var st = HT.load('datum', { y: '2027', s: 'Mecklenburg-Vorpommern', wd: '6', m: [4, 5, 6, 7, 8, 9], only: false, fav: [] });
  var thisY = new Date().getFullYear();
  $('year').innerHTML = [0, 1, 2, 3, 4].map(function (k) { return '<option>' + (thisY + k) + '</option>'; }).join('');
  $('state').innerHTML = Object.keys(STATES).map(function (k) { return '<option>' + k + '</option>'; }).join('');
  $('months').innerHTML = MN.map(function (m, i) { return '<label style="display:flex;gap:.3rem;align-items:center;margin:0"><input type="checkbox" style="width:auto" data-m="' + (i + 1) + '"> ' + m + '</label>'; }).join('');
  if (!$('year').querySelector('option[value="' + st.y + '"]') && ![].some.call($('year').options, function (o) { return o.value === st.y; })) st.y = String(thisY + 1);
  $('year').value = st.y; $('state').value = st.s; $('wd').value = st.wd; $('onlyspecial').checked = !!st.only;
  [].forEach.call($('months').querySelectorAll('input'), function (c) { c.checked = st.m.indexOf(+c.getAttribute('data-m')) >= 0; });
  function easter(y) { var a = y % 19, b = Math.floor(y / 100), c = y % 100, d = Math.floor(b / 4), e = b % 4, f = Math.floor((b + 8) / 25), g = Math.floor((b - f + 1) / 3), h = (19 * a + b - d - g + 15) % 30, i = Math.floor(c / 4), k = c % 4, l = (32 + 2 * e + 2 * i - h - k) % 7, m = Math.floor((a + 11 * h + 22 * l) / 451), mo = Math.floor((h + l - 7 * m + 114) / 31), da = ((h + l - 7 * m + 114) % 31) + 1; return new Date(y, mo - 1, da, 12); }
  function add(d, n) { var x = new Date(d.getTime()); x.setDate(x.getDate() + n); return x; }
  function key(d) { return d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate(); }
  function holidays(y, state) {
    var f = STATES[state] || [], h = {}, e = easter(y);
    function set(d, n) { h[key(d)] = n; }
    set(new Date(y, 0, 1, 12), 'Neujahr'); set(add(e, -2), 'Karfreitag'); set(add(e, 1), 'Ostermontag'); set(new Date(y, 4, 1, 12), 'Tag der Arbeit'); set(add(e, 39), 'Christi Himmelfahrt'); set(add(e, 50), 'Pfingstmontag'); set(new Date(y, 9, 3, 12), 'Tag der Deutschen Einheit'); set(new Date(y, 11, 25, 12), '1. Weihnachtstag'); set(new Date(y, 11, 26, 12), '2. Weihnachtstag');
    if (f.indexOf('rf') >= 0) set(new Date(y, 9, 31, 12), 'Reformationstag');
    if (f.indexOf('dk') >= 0) set(new Date(y, 0, 6, 12), 'Heilige Drei Könige');
    if (f.indexOf('fr') >= 0) set(add(e, 60), 'Fronleichnam');
    if (f.indexOf('al') >= 0) set(new Date(y, 10, 1, 12), 'Allerheiligen');
    if (f.indexOf('fm') >= 0) set(new Date(y, 2, 8, 12), 'Internationaler Frauentag');
    if (f.indexOf('wk') >= 0) set(new Date(y, 8, 20, 12), 'Weltkindertag');
    if (f.indexOf('bb') >= 0) { var d = new Date(y, 10, 22, 12); while (d.getDay() !== 3) d.setDate(d.getDate() - 1); set(d, 'Buß- und Bettag'); }
    return h;
  }
  function tags(d, hol) {
    var t = [], dd = d.getDate(), mm = d.getMonth() + 1, yy = d.getFullYear() % 100;
    if (hol[key(d)]) t.push('Feiertag: ' + hol[key(d)]);
    var h1 = hol[key(add(d, 1))], h2 = hol[key(add(d, -1))];
    if (h1 && !hol[key(d)]) t.push('Vor ' + h1);
    if (h2 && !hol[key(d)]) t.push('Nach ' + h2);
    if (dd === mm) t.push('Doppeltag (' + dd + '.' + mm + '.)');
    if (dd === yy) t.push('Tag = Jahreszahl (' + dd + '.' + mm + '.' + yy + ')');
    if (mm === yy) t.push('Monat = Jahreszahl');
    var s = pad(dd) + pad(mm) + pad(yy); if (/^(\d)\1{5}$/.test(s)) t.push('Schnapszahl');
    return t;
  }
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function fmtd(d) { return WD[d.getDay()] + ', ' + pad(d.getDate()) + '.' + pad(d.getMonth() + 1) + '.' + d.getFullYear(); }
  function save() { st = { y: $('year').value, s: $('state').value, wd: $('wd').value, m: [].filter.call($('months').querySelectorAll('input'), function (c) { return c.checked; }).map(function (c) { return +c.getAttribute('data-m'); }), only: $('onlyspecial').checked, fav: st.fav }; HT.save('datum', st); }
  function render() {
    save(); var y = +st.y, hol = holidays(y, st.s), out = [], wd = +st.wd;
    st.m.forEach(function (m) { var d = new Date(y, m - 1, 1, 12); while (d.getMonth() === m - 1) { if (d.getDay() === wd) { var t = tags(d, hol); if (!st.only || t.length) out.push([d, t]); } d = add(d, 1); } });
    $('count').textContent = out.length + ' Termine';
    $('rows').innerHTML = out.map(function (o) {
      var k = o[0].toISOString().slice(0, 10), fav = st.fav.indexOf(k) >= 0;
      return '<tr><td>' + fmtd(o[0]) + '</td><td>' + (o[1].length ? o[1].map(function (x) { return '<span class="pill">' + HT.esc(x) + '</span>'; }).join(' ') : '<span class="muted">–</span>') + '</td><td class="noprint"><button class="ghost" data-k="' + k + '" aria-pressed="' + fav + '">' + (fav ? '★ gemerkt' : '☆ merken') + '</button></td></tr>';
    }).join('') || '<tr><td colspan="3">Keine Termine für diese Auswahl.</td></tr>';
    var favs = st.fav.slice().sort();
    $('favcard').hidden = !favs.length;
    $('favs').innerHTML = favs.map(function (k) { var d = new Date(k + 'T12:00:00'); var t = tags(d, holidays(d.getFullYear(), st.s)); return '<li>' + fmtd(d) + (t.length ? ' · ' + HT.esc(t.join(', ')) : '') + '</li>'; }).join('');
  }
  document.addEventListener('change', function (e) { if (e.target.closest('.card') && !e.target.getAttribute('data-k')) render(); });
  $('rows').addEventListener('click', function (e) { var b = e.target.closest('button'); if (!b) return; var k = b.getAttribute('data-k'), i = st.fav.indexOf(k); if (i >= 0) st.fav.splice(i, 1); else st.fav.push(k); render(); });
  render();
})();
