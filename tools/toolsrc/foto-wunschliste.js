(function () {
  var G = [
    ['Getting Ready', ['Kleid und Schuhe', 'Ringe und Einladungskarte', 'Make-up und Frisur', 'Anziehen mit Helfern', 'Bräutigam beim Fertigmachen']],
    ['Trauung', ['Einzug', 'Blick des Partners', 'Ringtausch', 'Kuss', 'Reaktionen der Gäste', 'Auszug']],
    ['Paar', ['Entspannte Porträts', 'Spaziergang', 'Nahaufnahmen (Hände, Ringe)', 'Im Abendlicht', 'Besonderer Ort für euch']],
    ['Gäste und Familie', ['Gruppenfoto mit allen Gästen', 'Familiengruppen', 'Freunde und Trauzeugen', 'Kinder', 'Lachen und Gratulation']],
    ['Details und Feier', ['Deko, Torte und Tischkarten', 'Location und Gesamtbild', 'Reden', 'Tortenanschnitt', 'Eröffnungstanz', 'Party und Tanzfläche']]
  ];
  var $ = function (id) { return document.getElementById(id); }, st = HT.load('foto', { names: '', wd: '', loc: '', grp: '', note: '', sel: {}, must: {} });
  ['names', 'wd', 'loc', 'grp', 'note'].forEach(function (k) { $(k).value = st[k] || ''; });
  $('groups').innerHTML = G.map(function (g, gi) { return '<div class="card"><h2>' + g[0] + '</h2><ul class="check">' + g[1].map(function (t, ti) { var k = gi + '.' + ti; return '<li style="display:flex;gap:.6rem;align-items:center;justify-content:space-between"><label><input type="checkbox" data-s="' + k + '"> <span>' + t + '</span></label><label class="noprint" style="font-size:.85rem;color:var(--muted)"><input type="checkbox" data-m="' + k + '" style="width:auto"> besonders wichtig</label></li>'; }).join('') + '</ul></div>'; }).join('');
  [].forEach.call(document.querySelectorAll('[data-s]'), function (c) { c.checked = !!st.sel[c.getAttribute('data-s')]; });
  [].forEach.call(document.querySelectorAll('[data-m]'), function (c) { c.checked = !!st.must[c.getAttribute('data-m')]; });
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function build() {
    ['names', 'wd', 'loc', 'grp', 'note'].forEach(function (k) { st[k] = $(k).value; });
    st.sel = {}; st.must = {};
    [].forEach.call(document.querySelectorAll('[data-s]'), function (c) { if (c.checked) st.sel[c.getAttribute('data-s')] = 1; });
    [].forEach.call(document.querySelectorAll('[data-m]'), function (c) { if (c.checked) st.must[c.getAttribute('data-m')] = 1; });
    HT.save('foto', st);
    var L = ['Foto-Wunschliste' + (st.names ? ' von ' + st.names : '')];
    if (st.wd) { var d = new Date(st.wd + 'T12:00:00'); L.push('Datum: ' + pad(d.getDate()) + '.' + pad(d.getMonth() + 1) + '.' + d.getFullYear()); }
    if (st.loc) L.push('Ort: ' + st.loc);
    G.forEach(function (g, gi) { var it = g[1].map(function (t, ti) { var k = gi + '.' + ti; return st.sel[k] ? '- ' + t + (st.must[k] ? ' (besonders wichtig)' : '') : null; }).filter(Boolean); if (it.length) { L.push('', g[0] + ':'); L = L.concat(it); } });
    var groups = st.grp.split('\n').map(function (x) { return x.trim(); }).filter(Boolean);
    if (groups.length) { L.push('', 'Gruppenfotos (' + groups.length + '):'); groups.forEach(function (x) { L.push('- ' + x); }); }
    if (st.note.trim()) L.push('', 'Besondere Wünsche:', st.note.trim());
    $('grpinfo').textContent = groups.length ? groups.length + ' Gruppen. Plant für Gruppenfotos genug Zeit und jemanden ein, der die Gäste zusammenholt.' : '';
    $('out').textContent = L.join('\n'); $('mail').href = 'mailto:?subject=' + encodeURIComponent('Foto-Wunschliste') + '&body=' + encodeURIComponent(L.join('\n'));
  }
  document.addEventListener('input', build); document.addEventListener('change', build);
  $('copy').onclick = function () { var t = $('out').textContent; function ok() { $('msg').textContent = 'Kopiert.'; } function fail() { $('msg').textContent = 'Kopieren hat nicht geklappt. Bitte die Liste markieren oder drucken.'; } if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t).then(ok, fail); else fail(); };
  build();
})();
