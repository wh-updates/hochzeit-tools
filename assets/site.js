// Gemeinsame Helfer: Speicher (nur im eigenen Browser), Euro-Format, Kopf/Fuß
window.HT = (function () {
  function load(key, def) { try { var v = localStorage.getItem('ht.' + key); return v ? JSON.parse(v) : def; } catch (e) { return def; } }
  function save(key, val) { try { localStorage.setItem('ht.' + key, JSON.stringify(val)); } catch (e) {} }
  var fmt = new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR', maximumFractionDigits: 0 });
  function eur(n) { return fmt.format(isFinite(n) ? n : 0); }
  function num(v) { var n = parseFloat(String(v).replace(/\./g, '').replace(',', '.')); return isFinite(n) ? n : 0; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  return { load: load, save: save, eur: eur, num: num, esc: esc };
})();

// Regionsfrage "Wo heiratet ihr?" + Hinweis für Mecklenburg-Vorpommern (nur lokal gespeichert, kein Tracking)
(function () {
  var LAENDER = ['Baden-Württemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen', 'Hamburg', 'Hessen', 'Mecklenburg-Vorpommern', 'Niedersachsen', 'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland', 'Sachsen', 'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thüringen', 'Ausland'];
  var MV = 'Mecklenburg-Vorpommern';
  function init() {
    var main = document.querySelector('main'); if (!main) return;
    var box = document.createElement('div'); box.className = 'region noprint';
    var h1 = main.querySelector('h1'), hero = main.querySelector('.hero');
    main.insertBefore(box, h1 && h1.parentNode === main ? h1.nextSibling : (hero ? hero.nextSibling : main.firstChild));
    function render() {
      var r = HT.load('region', ''), hide = HT.load('regionHide', '');
      if (r === MV && hide !== r) {
        box.innerHTML = '<div class="mv-banner"><button class="mv-x" aria-label="Hinweis schließen">✕</button>' +
          '<strong>Ihr heiratet in Mecklenburg-Vorpommern?</strong> Wir sind Bride &amp; Light – Hochzeitsfotografie und Brautstyling ' +
          'auf Rügen, in Stralsund und ganz MV. <a class="btn" href="https://bride-light.de/?utm_source=tools&amp;utm_medium=banner&amp;utm_campaign=mv">Bride &amp; Light ansehen</a></div>';
        box.querySelector('.mv-x').onclick = function () { HT.save('regionHide', r); render(); };
      } else if (!r) {
        box.innerHTML = '<label class="region-q">Wo heiratet ihr? <select><option value="">Bitte wählen (optional)</option>' +
          LAENDER.map(function (l) { return '<option>' + l + '</option>'; }).join('') + '</select></label>';
        box.querySelector('select').onchange = function () { HT.save('region', this.value); render(); };
      } else {
        box.innerHTML = '<p class="region-q">Hochzeitsort: ' + HT.esc(r) + ' · <a href="#" class="region-c">ändern</a></p>';
        box.querySelector('.region-c').onclick = function (e) { e.preventDefault(); HT.save('region', ''); HT.save('regionHide', ''); render(); };
      }
    }
    render();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();

// Paarcode: die Planung aus den Tools als Text-Code zum Mitnehmen (nur nach Klick, bleibt im Browser, bis ihr ihn selbst einfügt)
(function () {
  var TOOLS = ['budgetrechner', 'gaesteliste', 'sitzplan', 'ablaufplan', 'foto-wunschliste', 'packliste-hochzeit', 'hochzeitsdatum-finder', 'hochzeitstyp', 'checkliste', 'getraenkerechner', 'tischkarten'];
  function has(o) { return o && typeof o === 'object'; }
  function collect() {
    var d = {}, parts = [];
    var g = HT.load('gaeste', null);
    if (has(g) && g.list && g.list.length) { d.g = { ppp: g.ppp, list: g.list.slice(0, 600) }; parts.push(g.list.length + (g.list.length === 1 ? ' Gast' : ' Gäste')); }
    var b = HT.load('budget', null);
    if (has(b) && b.items && (b.total !== 15000 || b.guests !== 60 || b.items.some(function (i) { return i.r !== ''; }))) { d.b = { total: b.total, guests: b.guests, items: b.items.slice(0, 60) }; parts.push('Budget (' + HT.eur(b.total) + ')'); }
    var a = HT.load('ablauf', null);
    if (has(a) && a.items && a.items.length) { d.a = { start: a.start, items: a.items.slice(0, 60) }; parts.push('Ablaufplan'); }
    var f = HT.load('foto', null);
    if (has(f) && (f.names || f.note || f.loc || Object.keys(f.sel || {}).length)) { d.f = f; parts.push('Foto-Wunschliste'); }
    var s = HT.load('sitzplan', null);
    if (has(s) && s.t && s.t.length) { d.s = { t: s.t.slice(0, 80), g: (s.g || []).slice(0, 600) }; parts.push(s.t.length + (s.t.length === 1 ? ' Tisch' : ' Tische')); }
    var p = HT.load('packliste', null);
    if (has(p) && p.own && Object.keys(p.own).length) { d.p = { sel: p.sel, own: p.own }; parts.push('Packliste'); }
    var y = HT.load('hochzeitstyp', null);
    if (has(y) && y.r) { d.y = y.r; parts.push('Hochzeitstyp'); }
    var dt = HT.load('datum', null);
    if (has(dt) && dt.fav && dt.fav.length) { d.d = { y: dt.y, s: dt.s, wd: dt.wd, fav: dt.fav.slice(0, 20) }; parts.push('Wunschtermine'); }
    var r = HT.load('region', '');
    if (r) d.r = r;
    return { d: d, parts: parts };
  }
  function encode(d) {
    d.v = 1; d.ts = new Date().toISOString().slice(0, 10);
    var j = unescape(encodeURIComponent(JSON.stringify(d)));
    return 'BL1.' + btoa(j).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
  }
  function init() {
    var main = document.querySelector('main'); if (!main) return;
    var seg = location.pathname.replace(/\/+$/, '').split('/').pop();
    if (TOOLS.indexOf(seg) < 0) return;
    var c = collect(); if (!c.parts.length) return;
    var box = document.createElement('section'); box.className = 'card noprint paarcode';
    box.innerHTML = '<h2 style="margin-top:0">Eure Planung zu Bride &amp; Light mitnehmen</h2>' +
      '<p>Habt ihr bei uns gebucht, könnt ihr eure Planung aus den Tools mit einem Klick in euren Kundenbereich übernehmen. Das spart doppeltes Tippen.</p>' +
      '<p class="muted"><small>Gefunden in diesem Browser: ' + HT.esc(c.parts.join(', ')) + '. Der Code wird nur erzeugt, wenn ihr auf den Knopf klickt. Es wird nichts gesendet. Erst wenn ihr ihn selbst bei uns einfügt, sehen wir die Daten.</small></p>' +
      '<p><button type="button" class="pc-go">Planung als Code kopieren</button></p>' +
      '<div class="pc-out" hidden><textarea class="pc-ta" rows="3" readonly aria-label="Euer Planungscode"></textarea><p class="pc-msg muted"><small></small></p></div>' +
      '<details class="pc-mail"><summary>Oder die Planung per E-Mail bekommen</summary>' +
      '<form class="pc-form" novalidate><p><label>Name<br><input name="name" required maxlength="80" autocomplete="name"></label></p>' +
      '<p><label>E-Mail<br><input name="email" type="email" required maxlength="200" autocomplete="email"></label></p>' +
      '<p style="position:absolute;left:-9999px" aria-hidden="true"><label>Website<input name="website" tabindex="-1" autocomplete="off"></label></p>' +
      '<p><label><input type="checkbox" name="consent" value="1"> Ich bin einverstanden, dass Bride &amp; Light meine Planung und E-Mail-Adresse verarbeitet, um mir diese E-Mail zu senden. <a href="https://bride-light.de/datenschutzerklarung">Datenschutzerklärung</a></label></p>' +
      '<p><label><input type="checkbox" name="newsletter" value="1"> Ja, ich möchte außerdem Hochzeitstipps und Neuigkeiten von Bride &amp; Light per E-Mail (jederzeit abbestellbar, Bestätigungslink folgt)</label></p>' +
      '<p><button type="submit">Planung per E-Mail senden</button></p><p class="pc-fmsg muted" role="status"><small></small></p></form></details>' +
      '<p><a class="btn ghost pc-ask" href="#">Jetzt bei Bride &amp; Light anfragen</a> <small class="muted">Den Code könnt ihr im Anfrageformular einfügen.</small></p>';
    main.appendChild(box);
    var ask = box.querySelector('.pc-ask'), fav = (HT.load('datum', {}).fav || [])[0];
    ask.href = 'https://bride-light.de/?utm_source=tools&utm_medium=paarcode&utm_campaign=anfrage' + (fav ? '&datum=' + encodeURIComponent(fav) : '');
    box.querySelector('.pc-form').onsubmit = function (e) {
      e.preventDefault();
      var f = e.target, m = box.querySelector('.pc-fmsg small'), b = f.querySelector('button');
      if (!f.name.value.trim() || !/^\S+@\S+\.\S+$/.test(f.email.value.trim())) { m.textContent = 'Bitte Namen und eine gültige E-Mail-Adresse eingeben.'; return; }
      if (!f.consent.checked) { m.textContent = 'Bitte der Verarbeitung zustimmen.'; return; }
      var fd = new FormData(f); fd.append('code', encode(collect().d)); b.disabled = true; m.textContent = 'Wird gesendet …';
      fetch((window.HT_API || 'https://bride-light.de') + '/api/tools-plan', { method: 'POST', body: fd }).then(function (r) { return r.json().catch(function () { return {}; }); }).then(function (j) {
        m.textContent = j.ok ? 'Gesendet. Bitte schaut in euer Postfach' + (f.newsletter.checked ? ' und bestätigt den Newsletter.' : '.') : (j.error || 'Das hat leider nicht geklappt. Bitte versucht es später noch einmal.'); b.disabled = false;
      }, function () { m.textContent = 'Das hat leider nicht geklappt. Bitte versucht es später noch einmal.'; b.disabled = false; });
    };
    box.querySelector('.pc-go').onclick = function () {
      var cur = collect(), code = encode(cur.d), out = box.querySelector('.pc-out'), ta = box.querySelector('.pc-ta'), msg = box.querySelector('.pc-msg small');
      ta.value = code; out.hidden = false; ta.focus(); ta.select();
      function done(ok) { msg.textContent = ok ? 'Kopiert. Im Kundenbereich unter „Planung aus den Tools übernehmen“ einfügen.' : 'Bitte den Text markieren und selbst kopieren (Strg+C), dann im Kundenbereich einfügen.'; }
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(code).then(function () { done(true); }, function () { done(false); });
      else { try { done(document.execCommand('copy')); } catch (e) { done(false); } }
    };
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();

// Termin-Check im Hochzeitsdatum-Finder: zeigt je Wunschtermin, ob Bride & Light noch frei ist (öffentlicher Kalender von bride-light.de)
(function () {
  if (location.pathname.replace(/\/+$/, '').split('/').pop() !== 'hochzeitsdatum-finder') return;
  var API = window.HT_API || 'https://bride-light.de', AV = null, obs;
  function paint() {
    if (!AV) return; var rows = document.querySelectorAll('#rows tr'); if (obs) obs.disconnect();
    [].forEach.call(rows, function (tr) {
      var b = tr.querySelector('button[data-k]'), td = tr.querySelector('td'); if (!b || !td || td.querySelector('.avail')) return;
      var k = b.getAttribute('data-k'), st = AV.days[k], d = document.createElement('div'); d.className = 'avail noprint';
      if (st === 'busy') { d.className += ' busy'; d.textContent = 'Bei Bride & Light leider ausgebucht'; }
      else if (st === 'res') { d.className += ' res'; d.textContent = 'Bei Bride & Light reserviert'; }
      else if (k >= AV.from && k <= AV.to) { d.className += ' free'; d.innerHTML = 'Bei Bride &amp; Light noch frei · <a href="https://bride-light.de/?datum=' + encodeURIComponent(k) + '&amp;utm_source=tools&amp;utm_medium=termincheck&amp;utm_campaign=datum">Anfragen</a>'; }
      else return;
      td.appendChild(d);
    });
    watch();
  }
  function watch() { var r = document.getElementById('rows'); if (r && window.MutationObserver) { obs = obs || new MutationObserver(paint); obs.observe(r, { childList: true }); } }
  function init() {
    watch();
    fetch(API + '/verfuegbarkeit.json').then(function (r) { return r.ok ? r.json() : null; }).then(function (j) { if (j && j.days) { AV = j; paint(); } }, function () {});
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
