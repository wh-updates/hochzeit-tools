(function () {
  var N = { 1: 'Papierhochzeit', 2: 'Baumwollhochzeit', 3: 'Lederhochzeit', 4: 'Blumenhochzeit', 5: 'Hölzerne Hochzeit', 6: 'Zuckerhochzeit', 7: 'Kupferhochzeit', 8: 'Blechhochzeit', 9: 'Keramikhochzeit', 10: 'Rosenhochzeit', 12.5: 'Nickelhochzeit', 15: 'Kristallhochzeit', 20: 'Porzellanhochzeit', 25: 'Silberhochzeit', 30: 'Perlenhochzeit', 35: 'Leinenhochzeit', 40: 'Rubinhochzeit', 45: 'Messinghochzeit', 50: 'Goldene Hochzeit', 55: 'Smaragdhochzeit', 60: 'Diamantene Hochzeit', 65: 'Eiserne Hochzeit', 70: 'Gnadenhochzeit', 75: 'Kronjuwelen-Hochzeit' };
  var WD = ['So', 'Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa'], $ = function (id) { return document.getElementById(id); };
  var st = HT.load('hochzeitstag', { d: '', u: '25' }); $('date').value = st.d; $('upto').value = st.u;
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function render() {
    st = { d: $('date').value, u: $('upto').value }; HT.save('hochzeitstag', st);
    if (!/^\d{4}-\d{2}-\d{2}$/.test(st.d)) { $('rows').innerHTML = '<tr><td colspan="4">Bitte euer Hochzeitsdatum wählen.</td></tr>'; $('next').textContent = ''; return; }
    var y = +st.d.slice(0, 4), m = +st.d.slice(5, 7) - 1, d = +st.d.slice(8, 10), now = new Date(); now.setHours(12, 0, 0, 0);
    var rows = [], nxt = null, keys = Object.keys(N).map(Number).sort(function (a, b) { return a - b; });
    keys.forEach(function (k) {
      if (k > +st.u) return;
      var yy = y + Math.floor(k), mm = m + (k % 1 ? 6 : 0); if (mm > 11) { mm -= 12; yy++; }
      var dt = new Date(yy, mm, d, 12), days = Math.round((dt - now) / 864e5);
      if (days >= 0 && !nxt) nxt = [k, dt, days];
      rows.push('<tr' + (days >= 0 && nxt && nxt[0] === k ? ' style="background:var(--rose)"' : '') + '><td>' + String(k).replace('.', ',') + '</td><td>' + N[k] + '</td><td>' + WD[dt.getDay()] + ', ' + pad(dt.getDate()) + '.' + pad(dt.getMonth() + 1) + '.' + dt.getFullYear() + '</td><td class="num">' + (days < 0 ? 'vorbei' : days === 0 ? 'Heute! 🎉' : days + ' Tage') + '</td></tr>');
    });
    $('rows').innerHTML = rows.join('');
    $('next').innerHTML = nxt ? 'Der nächste Hochzeitstag ist die <b>' + N[nxt[0]] + '</b> (' + String(nxt[0]).replace('.', ',') + ' Jahre) in <b>' + nxt[2] + ' Tagen</b>.' : 'Für den gewählten Zeitraum liegen alle Hochzeitstage in der Vergangenheit.';
  }
  $('date').addEventListener('change', render); $('upto').addEventListener('change', render); render();
})();
