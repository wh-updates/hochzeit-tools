(function () {
  var L = {
    braut: ['Hochzeitstag: Braut', ['Brautkleid, Schleier, Unterrock', 'Schuhe und Ersatzschuhe', 'Schmuck und Haarschmuck', 'Unterwäsche passend zum Kleid', 'Strumpfhose oder Strümpfe (Ersatz)', 'Make-up zum Nachlegen, Lippenstift, Puder', 'Haarnadeln, Haarspray, Haargummis', 'Taschentücher', 'Deo und Parfüm', 'Pflaster, Blasenpflaster', 'Nähset und Sicherheitsnadeln', 'Mini-Zahnbürste und Zahnpasta', 'Handtasche mit Handy, Ladegerät', 'Ringe, Eheversprechen, Redekarten', 'Dokumente fürs Standesamt']],
    braeutigam: ['Hochzeitstag: Bräutigam', ['Anzug, Hemd, Krawatte oder Fliege', 'Schuhe, Socken, Gürtel', 'Manschettenknöpfe, Einstecktuch', 'Rasierer und Pflegeprodukte', 'Deo und Parfüm', 'Taschentücher', 'Ersatzhemd', 'Ringe, Redekarten', 'Handy und Ladegerät', 'Dokumente fürs Standesamt']],
    notfall: ['Notfallset für Trauzeugen', ['Pflaster, Schmerztabletten, Magentabletten', 'Taschentücher, Feuchttücher', 'Nähset, Sicherheitsnadeln, Sekundenkleber', 'Fleckenentferner, Tuch', 'Haarspray, Haarnadeln, Haargummis', 'Deo, Kaugummi, Mundspülung', 'Regenschirme', 'Snacks und Wasser', 'Powerbank', 'Bargeld für Trinkgelder']],
    flitter: ['Flitterwochen', ['Reisepässe oder Ausweise', 'Buchungsbestätigungen (Hotel, Flug, Mietwagen)', 'Reiseversicherung, Impfpass, Medikamente', 'Kreditkarte, Bargeld', 'Ladegeräte, Adapter, Powerbank', 'Kleidung fürs Wetter, Badesachen', 'Sonnenschutz, Pflegeprodukte', 'Kamera oder Handy mit Speicher', 'Reiseapotheke', 'Kleine Überraschung für die Hochzeitsnacht']],
    dok: ['Dokumente und Papiere', ['Personalausweise oder Reisepässe', 'Geburtsurkunden (falls verlangt)', 'Anmeldung beim Standesamt, Terminbestätigung', 'Verträge mit Dienstleistern', 'Ablaufplan ausgedruckt', 'Zahlungsbelege und Restzahlungen vorbereitet', 'Notfallnummern aller Dienstleister']]
  };
  var $ = function (id) { return document.getElementById(id); }, st = HT.load('packliste', { sel: 'braut', done: {}, own: {} });
  $('sel').innerHTML = Object.keys(L).map(function (k) { return '<option value="' + k + '">' + L[k][0] + '</option>'; }).join(''); $('sel').value = L[st.sel] ? st.sel : 'braut';
  function render() {
    var k = $('sel').value; st.sel = k; var items = L[k][1].concat(st.own[k] || []), done = 0;
    $('ltitle').textContent = L[k][0];
    $('list').innerHTML = items.map(function (t, i) { var c = !!(st.done[k + '.' + i]); if (c) done++; return '<li><label><input type="checkbox" data-i="' + i + '"' + (c ? ' checked' : '') + '><span' + (c ? ' class="done"' : '') + '>' + HT.esc(t) + '</span></label></li>'; }).join('');
    var p = items.length ? Math.round(done / items.length * 100) : 0; $('prog').textContent = done + ' von ' + items.length + ' gepackt (' + p + ' %)'; $('pbar').style.width = p + '%'; HT.save('packliste', st);
  }
  $('sel').addEventListener('change', render);
  $('list').addEventListener('change', function (e) { var i = e.target.getAttribute('data-i'); if (i === null) return; var key = st.sel + '.' + i; if (e.target.checked) st.done[key] = 1; else delete st.done[key]; render(); });
  $('addbtn').onclick = function () { var v = $('newitem').value.trim(); if (!v) return; (st.own[st.sel] = st.own[st.sel] || []).push(v); $('newitem').value = ''; render(); };
  $('newitem').addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); $('addbtn').click(); } });
  $('reset').onclick = function () { if (confirm('Alle Haken dieser Liste entfernen?')) { Object.keys(st.done).forEach(function (k) { if (k.indexOf(st.sel + '.') === 0) delete st.done[k]; }); render(); } };
  render();
})();
