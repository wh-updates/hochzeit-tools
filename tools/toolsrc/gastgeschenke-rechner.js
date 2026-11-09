(function () {
  var $ = function (id) { return document.getElementById(id); }, ids = ['g', 'res', 'mode', 'val', 'pack', 'wd'];
  var st = HT.load('gastgeschenk', { g: '60', res: '10', mode: 'budget', val: '300', pack: '0,50', wd: '' });
  ids.forEach(function (k) { if (st[k] !== undefined) $(k).value = st[k]; });
  var IDEAS = [[0, 1.5, ['Saatgut-Tütchen mit Blumensamen', 'Teelicht im Glas', 'Schokoladen-Taler mit Namen', 'Kleine Seife']], [1.5, 3, ['Mini-Marmelade oder Honig', 'Gebäck oder Kekse in der Tüte', 'Kräutertopf', 'Sektbonbons mit Anhänger']], [3, 6, ['Pralinen-Schachtel', 'Duftkerze', 'Tee- oder Kaffeemischung', 'Kleine Pflanze im Topf']], [6, 999, ['Lokale Spezialitäten im Set', 'Personalisiertes Glas oder Becher', 'Fotoabzug oder Postkarte im Rahmen', 'Dekanter oder Flaschenset']]];
  function eur(n) { return n.toLocaleString('de-DE', { style: 'currency', currency: 'EUR' }); }
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function calc() {
    ids.forEach(function (k) { st[k] = $(k).value; }); HT.save('gastgeschenk', st);
    $('vallabel').textContent = st.mode === 'budget' ? 'Gesamtbudget (€)' : 'Preis pro Stück (€)';
    var g = Math.max(0, Math.round(HT.num(st.g))), n = Math.ceil(g * (1 + Math.max(0, HT.num(st.res)) / 100)), v = HT.num(st.val), pk = HT.num(st.pack), per, tot;
    if (!n) { $('sum').textContent = 'Bitte die Anzahl eintragen.'; return; }
    if (st.mode === 'budget') { tot = v; per = v / n; $('sum').innerHTML = 'Bei <b>' + n + ' Stück</b> (inkl. Reserve) stehen euch <b>' + eur(per) + '</b> pro Stück zur Verfügung, davon etwa ' + eur(Math.max(0, per - pk)) + ' für das Geschenk selbst.'; }
    else { per = v + pk; tot = per * n; $('sum').innerHTML = 'Bei <b>' + n + ' Stück</b> (inkl. Reserve) kosten die Geschenke zusammen <b>' + eur(tot) + '</b> (' + eur(per) + ' pro Stück inkl. Verpackung).'; }
    var w = st.wd, t = '';
    if (/^\d{4}-\d{2}-\d{2}$/.test(w)) { var d = new Date(w + 'T12:00:00'); d.setDate(d.getDate() - 42); t = 'Bestellt oder bastelt spätestens bis etwa ' + pad(d.getDate()) + '.' + pad(d.getMonth() + 1) + '.' + d.getFullYear() + ' (sechs Wochen vorher), damit Lieferzeit und Verpacken nicht knapp werden.'; }
    $('when').textContent = t;
    var gift = Math.max(0, per - pk), set = IDEAS.filter(function (x) { return gift >= x[0] && gift < x[1]; })[0] || IDEAS[0];
    $('ideas').innerHTML = '<p>Bei etwa ' + eur(gift) + ' pro Geschenk passen zum Beispiel:</p><ul>' + set[2].map(function (x) { return '<li>' + x + '</li>'; }).join('') + '</ul>';
  }
  ids.forEach(function (k) { $(k).addEventListener('input', calc); $(k).addEventListener('change', calc); }); calc();
})();
