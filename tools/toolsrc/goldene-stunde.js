(function () {
  var PLACES = [['Stralsund', 54.3093, 13.0818], ['Binz (Rügen)', 54.4023, 13.6083], ['Kap Arkona (Rügen)', 54.6796, 13.4294], ['Sassnitz (Rügen)', 54.5139, 13.6431], ['Heringsdorf (Usedom)', 53.9553, 14.1624], ['Zingst', 54.4372, 12.6842], ['Prerow', 54.4569, 12.5750], ['Greifswald', 54.0865, 13.3924], ['Rostock', 54.0924, 12.0991], ['Wismar', 53.8914, 11.4647], ['Schwerin', 53.6355, 11.4012]];
  var $ = function (id) { return document.getElementById(id); };
  var R = Math.PI / 180;
  function jdOf(y, m, d, minutes) { // Julianisches Datum aus UTC-Datum
    if (m <= 2) { y--; m += 12; }
    var A = Math.floor(y / 100), B = 2 - A + Math.floor(A / 4);
    return Math.floor(365.25 * (y + 4716)) + Math.floor(30.6001 * (m + 1)) + d + B - 1524.5 + minutes / 1440;
  }
  function pos(jd) { // NOAA-Näherung: Deklination, Zeitgleichung (Minuten)
    var T = (jd - 2451545) / 36525;
    var L0 = (280.46646 + T * (36000.76983 + T * 0.0003032)) % 360;
    var M = 357.52911 + T * (35999.05029 - 0.0001537 * T);
    var e = 0.016708634 - T * (0.000042037 + 0.0000001267 * T);
    var C = Math.sin(M * R) * (1.914602 - T * (0.004817 + 0.000014 * T)) + Math.sin(2 * M * R) * (0.019993 - 0.000101 * T) + Math.sin(3 * M * R) * 0.000289;
    var tl = L0 + C, om = 125.04 - 1934.136 * T, lam = tl - 0.00569 - 0.00478 * Math.sin(om * R);
    var eps0 = 23 + (26 + (21.448 - T * (46.815 + T * (0.00059 - T * 0.001813))) / 60) / 60, eps = eps0 + 0.00256 * Math.cos(om * R);
    var decl = Math.asin(Math.sin(eps * R) * Math.sin(lam * R)) / R;
    var y = Math.pow(Math.tan(eps * R / 2), 2);
    var eq = 4 * (y * Math.sin(2 * L0 * R) - 2 * e * Math.sin(M * R) + 4 * e * y * Math.sin(M * R) * Math.cos(2 * L0 * R) - 0.5 * y * y * Math.sin(4 * L0 * R) - 1.25 * e * e * Math.sin(2 * M * R)) / R;
    return { decl: decl, eq: eq };
  }
  // Zeitpunkt (UTC-Minuten ab 0 Uhr UTC des Datums), an dem die Sonne die Höhe h (Grad) erreicht
  function ev(y, m, d, lat, lon, h, rising) { // korrekte Vorzeichen: Aufgang = 720 - 4*(lon + H) - eq ; Untergang = 720 - 4*(lon - H) - eq
    var t = rising ? 360 : 1080;
    for (var i = 0; i < 4; i++) {
      var p = pos(jdOf(y, m, d, t));
      var c = (Math.sin(h * R) - Math.sin(lat * R) * Math.sin(p.decl * R)) / (Math.cos(lat * R) * Math.cos(p.decl * R));
      if (c < -1 || c > 1) return null;
      var H = Math.acos(c) / R;
      t = 720 - 4 * (lon + (rising ? H : -H)) - p.eq;
    }
    return t;
  }
  var TZ = 'Europe/Berlin', fm = new Intl.DateTimeFormat('de-DE', { hour: '2-digit', minute: '2-digit', timeZone: TZ, hour12: false });
  function fmt(y, m, d, min) { return min === null ? '–' : fm.format(new Date(Date.UTC(y, m - 1, d) + Math.round(min) * 60000)); }
  function times(y, m, d, lat, lon) {
    return {
      rise: ev(y, m, d, lat, lon, -0.833, true), set: ev(y, m, d, lat, lon, -0.833, false),
      gSet: ev(y, m, d, lat, lon, 6, false), gRise: ev(y, m, d, lat, lon, 6, true),
      bSet: ev(y, m, d, lat, lon, -6, false), bRise: ev(y, m, d, lat, lon, -6, true)
    };
  }
  window.__sun = { times: times, fmt: fmt };
  var sel = $('loc');
  sel.innerHTML = PLACES.map(function (p, i) { return '<option value="' + i + '">' + HT.esc(p[0]) + '</option>'; }).join('') + '<option value="x">Eigene Koordinaten</option>';
  var now = new Date(), iso = now.getFullYear() + '-' + ('0' + (now.getMonth() + 1)).slice(-2) + '-' + ('0' + now.getDate()).slice(-2);
  var st = HT.load('goldene', { loc: '0', date: '' });
  sel.value = st.loc; if (sel.value !== st.loc) sel.value = '0';
  $('date').value = st.date || iso;
  function where() {
    if (sel.value === 'x') { return { name: 'eurem Ort', lat: HT.num($('lat').value), lon: HT.num($('lon').value) }; }
    var p = PLACES[+sel.value] || PLACES[0]; return { name: p[0], lat: p[1], lon: p[2] };
  }
  function calc() {
    $('custom').hidden = sel.value !== 'x';
    var v = $('date').value; if (!/^\d{4}-\d{2}-\d{2}$/.test(v)) { $('res').innerHTML = '<tr><td>Bitte ein Datum wählen.</td></tr>'; return; }
    var y = +v.slice(0, 4), m = +v.slice(5, 7), d = +v.slice(8, 10), w = where();
    if (!(w.lat >= -66 && w.lat <= 66 && w.lon >= -180 && w.lon <= 180)) { $('res').innerHTML = '<tr><td>Bitte gültige Koordinaten eingeben (Breite bis 66°).</td></tr>'; return; }
    st = { loc: sel.value, date: v }; HT.save('goldene', st);
    var t = times(y, m, d, w.lat, w.lon), f = function (x) { return fmt(y, m, d, x); };
    $('h').textContent = 'Sonnenzeiten für ' + w.name + ' am ' + d + '.' + m + '.' + y;
    $('res').innerHTML = [
      ['Sonnenaufgang', f(t.rise)], ['Goldene Stunde am Morgen', f(t.rise) + ' bis ' + f(t.gRise)],
      ['Goldene Stunde am Abend', f(t.gSet) + ' bis ' + f(t.set)], ['Sonnenuntergang', f(t.set)], ['Blaue Stunde am Abend', f(t.set) + ' bis ' + f(t.bSet)]
    ].map(function (r) { return '<tr><th scope="row" style="text-align:left">' + r[0] + '</th><td class="num"><b>' + r[1] + '</b></td></tr>'; }).join('');
    var MN = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'], rows = '';
    for (var mo = 1; mo <= 12; mo++) { var q = times(y, mo, 1, w.lat, w.lon), g = function (x) { return fmt(y, mo, 1, x); }; rows += '<tr><td>1. ' + MN[mo - 1] + '</td><td class="num">' + g(q.rise) + '</td><td class="num">' + g(q.gSet) + '</td><td class="num">' + g(q.set) + '</td></tr>'; }
    $('year').innerHTML = rows;
  }
  ['date', 'loc', 'lat', 'lon'].forEach(function (id) { $(id).addEventListener('input', calc); $(id).addEventListener('change', calc); });
  calc();
})();
