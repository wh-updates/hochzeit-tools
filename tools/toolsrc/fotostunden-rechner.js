(function () {
  var BEF = [['Getting Ready Braut', 60, 1], ['Getting Ready Bräutigam', 30, 0], ['First Look / Treffen vor der Trauung', 30, 0], ['Ankunft der Gäste', 20, 1]];
  var AFT = [['Gratulation und Gruppenfotos', 30, 1], ['Paarshooting', 45, 1], ['Sektempfang', 60, 1], ['Kaffee und Kuchen', 60, 0], ['Abendessen', 90, 0], ['Reden und Tortenanschnitt', 30, 0], ['Eröffnungstanz', 20, 0], ['Party', 60, 0]];
  var $ = function (id) { return document.getElementById(id); };
  var st = HT.load('fotostunden', null);
  if (!st) st = { cer: '14:00', cerd: '45', b: BEF.map(function (r) { return { on: !!r[2], m: r[1] }; }), a: AFT.map(function (r) { return { on: !!r[2], m: r[1] }; }) };
  if (st.b.length !== BEF.length || st.a.length !== AFT.length) st = { cer: '14:00', cerd: '45', b: BEF.map(function (r) { return { on: !!r[2], m: r[1] }; }), a: AFT.map(function (r) { return { on: !!r[2], m: r[1] }; }) };
  $('cer').value = st.cer; $('cerd').value = st.cerd;
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function fmt(m) { m = ((Math.round(m) % 1440) + 1440) % 1440; return pad(Math.floor(m / 60)) + ':' + pad(m % 60); }
  function list(el, defs, arr, key) {
    el.innerHTML = defs.map(function (d, i) {
      return '<div class="row" style="align-items:center;margin:.3rem 0"><label style="display:flex;gap:.5rem;align-items:center;margin:0"><input type="checkbox" style="width:auto" data-k="' + key + '" data-i="' + i + '" ' + (arr[i].on ? 'checked' : '') + '> ' + HT.esc(d[0]) + '</label><div><input style="width:5em;text-align:right" inputmode="numeric" data-k="' + key + '" data-i="' + i + '" data-m="1" value="' + arr[i].m + '" aria-label="Minuten: ' + HT.esc(d[0]) + '"> Min.</div></div>';
    }).join('');
  }
  function calc() {
    var p = ($('cer').value || '14:00').split(':'), c = (+p[0]) * 60 + (+p[1]), cd = Math.max(0, HT.num($('cerd').value));
    var b = 0, a = 0;
    st.b.forEach(function (x) { if (x.on) b += Math.max(0, HT.num(x.m)); });
    st.a.forEach(function (x) { if (x.on) a += Math.max(0, HT.num(x.m)); });
    var raw = b + cd + a, buf = Math.ceil(raw * 0.1 / 5) * 5, total = raw + buf;
    var h = Math.ceil(total / 30) / 2;
    var start = c - b - buf / 2, end = c + cd + a + buf / 2;
    st.cer = $('cer').value; st.cerd = $('cerd').value; HT.save('fotostunden', st);
    $('res').innerHTML = 'Ihr braucht etwa <b>' + String(h).replace('.', ',') + ' Stunden</b> Fotobegleitung, ungefähr von <b>' + fmt(start) + '</b> bis <b>' + fmt(end) + ' Uhr</b>.';
    $('rec').textContent = h <= 3 ? 'Das passt zu einer Trauung mit kurzem Empfang und Gruppenfotos.' : h <= 6 ? 'Das ist ein klassisches Paket mit Trauung, Empfang und Paarshooting.' : h <= 9 ? 'Das ist ein Tagespaket mit Vorbereitung, Feier und Essen.' : 'Das ist eine Ganztagsbegleitung bis in den Abend. Sprecht mit eurer Fotografin oder eurem Fotografen über Pausen.';
  }
  list($('before'), BEF, st.b, 'b'); list($('after'), AFT, st.a, 'a');
  document.addEventListener('input', function (e) {
    var t = e.target, k = t.getAttribute && t.getAttribute('data-k'); if (!k) { if (t.id === 'cer' || t.id === 'cerd') calc(); return; }
    var i = +t.getAttribute('data-i'); if (t.getAttribute('data-m')) st[k][i].m = t.value; else st[k][i].on = t.checked; calc();
  });
  calc();
})();
