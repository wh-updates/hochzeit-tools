(function () {
  var PRE = {
    std: [['Getting Ready (Haare, Make-up)', 90], ['Anfahrt und Ankunft der Gäste', 30], ['Trauung', 45], ['Gratulation und Sektempfang', 60], ['Gruppenfoto', 20], ['Paarshooting', 45], ['Kaffee und Kuchen', 60], ['Abendessen', 90], ['Eröffnungstanz', 15], ['Party', 180]],
    strand: [['Getting Ready', 90], ['Fahrt zum Strand', 30], ['Gäste kommen an', 20], ['Freie Trauung am Strand', 45], ['Sektempfang und Gratulation', 45], ['Paarshooting im weichen Licht', 60], ['Umzug zur Location', 30], ['Abendessen', 90], ['Reden und Torte', 45], ['Party', 180]],
    klein: [['Ankunft und Empfang', 30], ['Trauung', 30], ['Gruppenfoto', 15], ['Brunch', 120], ['Paarfotos', 30], ['Ausklang', 60]]
  };
  var $ = function (id) { return document.getElementById(id); };
  var st = HT.load('ablauf', null);
  if (!st || !st.items) st = { start: '11:00', items: PRE.std.map(function (r) { return { t: r[0], d: r[1], n: '' }; }) };
  $('start').value = st.start || '11:00';
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function fmt(m) { m = ((m % 1440) + 1440) % 1440; return pad(Math.floor(m / 60)) + ':' + pad(m % 60); }
  function startMin() { var p = ($('start').value || '11:00').split(':'); return (+p[0]) * 60 + (+p[1]); }
  function save() { st.start = $('start').value; HT.save('ablauf', st); }
  function render() {
    var m = startMin(), total = 0;
    $('rows').innerHTML = st.items.map(function (it, i) {
      var row = '<tr><td><b>' + fmt(m) + '</b></td>' +
        '<td><input data-i="' + i + '" data-k="t" value="' + HT.esc(it.t) + '" aria-label="Programmpunkt ' + (i + 1) + '"><span class="printonly">' + HT.esc(it.t) + '</span></td>' +
        '<td class="num noprint"><input style="width:4.5em;text-align:right" inputmode="numeric" data-i="' + i + '" data-k="d" value="' + it.d + '" aria-label="Dauer in Minuten"></td>' +
        '<td><input data-i="' + i + '" data-k="n" value="' + HT.esc(it.n) + '" placeholder="z. B. Ort, Zuständige" aria-label="Notiz"><span class="printonly">' + HT.esc(it.n) + '</span></td>' +
        '<td class="noprint" style="white-space:nowrap"><button class="ghost" data-up="' + i + '" aria-label="Nach oben">↑</button> <button class="ghost" data-dn="' + i + '" aria-label="Nach unten">↓</button> <button class="ghost" data-rm="' + i + '" aria-label="Entfernen">✕</button></td></tr>';
      m += Math.max(0, Math.round(HT.num(it.d))); total += Math.max(0, Math.round(HT.num(it.d)));
      return row;
    }).join('');
    $('endinfo').textContent = st.items.length ? 'Ende: ' + fmt(m) + ' Uhr · Gesamtdauer ' + Math.floor(total / 60) + ' Std. ' + (total % 60) + ' Min.' : 'Noch keine Programmpunkte.';
    save();
  }
  $('rows').addEventListener('input', function (e) {
    var i = e.target.getAttribute('data-i'), k = e.target.getAttribute('data-k'); if (i === null) return;
    st.items[i][k] = k === 'd' ? e.target.value : e.target.value;
    if (k === 'd') { updateTimes(); } save();
  });
  function updateTimes() { // nur Uhrzeiten aktualisieren, damit der Fokus im Feld bleibt
    var m = startMin(), rows = $('rows').children;
    st.items.forEach(function (it, i) { rows[i].firstChild.firstChild.textContent = fmt(m); m += Math.max(0, Math.round(HT.num(it.d))); });
    var total = st.items.reduce(function (s, it) { return s + Math.max(0, Math.round(HT.num(it.d))); }, 0);
    $('endinfo').textContent = 'Ende: ' + fmt(m) + ' Uhr · Gesamtdauer ' + Math.floor(total / 60) + ' Std. ' + (total % 60) + ' Min.';
  }
  $('rows').addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b) return;
    var u = b.getAttribute('data-up'), d = b.getAttribute('data-dn'), r = b.getAttribute('data-rm'), a = st.items;
    if (u !== null && +u > 0) { a.splice(+u - 1, 0, a.splice(+u, 1)[0]); }
    else if (d !== null && +d < a.length - 1) { a.splice(+d + 1, 0, a.splice(+d, 1)[0]); }
    else if (r !== null) { a.splice(+r, 1); }
    render();
  });
  $('start').onchange = function () { render(); };
  $('add').onclick = function () { st.items.push({ t: 'Neuer Punkt', d: 30, n: '' }); render(); var inp = $('rows').querySelectorAll('input[data-k="t"]'); if (inp.length) { inp[inp.length - 1].focus(); inp[inp.length - 1].select(); } };
  $('preset').onchange = function () {
    var p = PRE[this.value]; if (!p) return;
    if (st.items.length && !confirm('Die aktuelle Liste wird durch die Vorlage ersetzt. Fortfahren?')) { this.value = ''; return; }
    st.items = p.map(function (r) { return { t: r[0], d: r[1], n: '' }; }); this.value = ''; render();
  };
  $('reset').onclick = function () { if (confirm('Alle Programmpunkte löschen?')) { st.items = []; render(); } };
  $('copy').onclick = function () {
    var m = startMin(), lines = ['Ablaufplan'];
    st.items.forEach(function (it) { lines.push(fmt(m) + ' Uhr  ' + it.t + (it.n ? ' (' + it.n + ')' : '')); m += Math.max(0, Math.round(HT.num(it.d))); });
    lines.push(fmt(m) + ' Uhr  Ende');
    var txt = lines.join('\n');
    function ok() { $('msg').textContent = 'Der Ablauf wurde in die Zwischenablage kopiert.'; }
    function fail() { $('msg').textContent = 'Kopieren hat nicht geklappt. Bitte den Ablauf über „Drucken“ speichern.'; }
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(txt).then(ok, fail); else fail();
  };
  render();
})();
