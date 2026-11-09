(function () {
  var $ = function (id) { return document.getElementById(id); };
  var st = HT.load('torte', { g: 60, p: 90, s: '28', t: '3' });
  $('guests').value = st.g; $('pct').value = st.p; $('size').value = st.s; $('tiers').value = st.t;
  var STEP = 6, H = 10, DENS = 0.85;
  function area(d) { return Math.PI / 4 * d * d; }
  function calc() {
    var g = Math.max(0, Math.round(HT.num($('guests').value))), p = Math.min(100, Math.max(0, HT.num($('pct').value))), s = +$('size').value, n = +$('tiers').value;
    st = { g: $('guests').value, p: $('pct').value, s: $('size').value, t: $('tiers').value }; HT.save('torte', st);
    var need = Math.ceil(g * p / 100), A = need * s;
    var d0 = 8, ds;
    for (; d0 <= 60; d0 += 2) { ds = []; for (var k = 0; k < n; k++) ds.push(d0 + k * STEP); var sum = 0; ds.forEach(function (d) { sum += area(d); }); if (sum >= A) break; }
    if (!need) { $('sum').textContent = 'Bitte Gästezahl eingeben.'; $('rows').innerHTML = ''; $('viz').innerHTML = ''; $('tp').textContent = ''; $('tw').textContent = ''; return; }
    var tp = 0, tw = 0, rows = '';
    ds.slice().reverse().forEach(function (d, i) {
      var por = Math.floor(area(d) / s), w = area(d) * H * DENS / 1000; tp += por; tw += w;
      rows += '<tr><td>' + (i + 1) + '. Etage' + (i === 0 ? ' (unten)' : i === n - 1 && n > 1 ? ' (oben)' : '') + '</td><td class="num">' + d + ' cm</td><td class="num">' + por + '</td><td class="num">' + w.toFixed(1).replace('.', ',') + ' kg</td></tr>';
    });
    $('rows').innerHTML = rows; $('tp').textContent = tp; $('tw').textContent = tw.toFixed(1).replace('.', ',') + ' kg';
    $('sum').innerHTML = 'Ihr braucht etwa <b>' + need + ' Portionen</b>. Mit ' + n + ' Etage' + (n > 1 ? 'n' : '') + ' (' + ds.join(' / ') + ' cm) bekommt ihr <b>' + tp + '</b>.' + (ds[n - 1] > 34 ? ' <span class="muted">Eine untere Etage über 34 cm ist selten. Mehr Etagen oder eine zusätzliche Schnitttorte machen die Torte alltagstauglicher.</span>' : '');
    var maxd = ds[n - 1], W = 360, hh = 34, svg = '<svg viewBox="0 0 ' + W + ' ' + (n * hh + 24) + '" role="img" aria-label="Skizze der Torte mit ' + n + ' Etagen" style="width:100%;height:auto">';
    ds.slice().reverse().forEach(function (d, i) { // unten zuerst
      var w = 300 * d / maxd, y = 10 + (n - 1 - i) * hh;
      svg += '<rect x="' + ((W - w) / 2) + '" y="' + y + '" width="' + w + '" height="' + (hh - 4) + '" rx="6" fill="#f4e6e3" stroke="#8a4a50" stroke-width="2"/><text x="' + (W / 2) + '" y="' + (y + 20) + '" text-anchor="middle" font-size="13" fill="#6b3a3f">' + d + ' cm</text>';
    });
    svg += '<line x1="30" y1="' + (n * hh + 12) + '" x2="' + (W - 30) + '" y2="' + (n * hh + 12) + '" stroke="#8a4a50" stroke-width="2"/></svg>';
    $('viz').innerHTML = svg;
  }
  ['guests', 'pct', 'size', 'tiers'].forEach(function (id) { $(id).addEventListener('input', calc); $(id).addEventListener('change', calc); });
  calc();
})();
