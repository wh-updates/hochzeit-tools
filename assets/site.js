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
          'auf Rügen, in Stralsund und ganz MV. <a class="btn" href="https://bride-light.de/?utm_source=tools&amp;utm_medium=banner&amp;utm_campaign=mv&amp;von=tools-banner">Bride &amp; Light ansehen</a></div>';
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
    var gl = (c.d.g && c.d.g.list) ? c.d.g.list.filter(function (x) { return x.r !== 'nein'; }).length : ((c.d.b && c.d.b.guests) || 0);
    ask.href = 'https://bride-light.de/?utm_source=tools&utm_medium=paarcode&utm_campaign=anfrage&von=tools-paarcode&art=wedding' + (fav ? '&datum=' + encodeURIComponent(fav) : '') + (gl > 0 ? '&gaeste=' + gl : '');
    box.querySelector('.pc-form').onsubmit = function (e) {
      e.preventDefault();
      var f = e.target, m = box.querySelector('.pc-fmsg small'), b = f.querySelector('button');
      if (!f.name.value.trim() || !/^\S+@\S+\.\S+$/.test(f.email.value.trim())) { m.textContent = 'Bitte Namen und eine gültige E-Mail-Adresse eingeben.'; return; }
      if (!f.consent.checked) { m.textContent = 'Bitte der Verarbeitung zustimmen.'; return; }
      var fd = new FormData(f); fd.append('code', encode(collect().d)); b.disabled = true; m.textContent = 'Wird gesendet …';
      fetch((window.HT_API || 'https://bride-light.de') + '/_form/tools-plan', { method: 'POST', body: fd }).then(function (r) { return r.json().catch(function () { return {}; }); }).then(function (j) {
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
      else if (k >= AV.from && k <= AV.to) { d.className += ' free'; d.innerHTML = 'Bei Bride &amp; Light noch frei · <a href="https://bride-light.de/?datum=' + encodeURIComponent(k) + '&amp;art=wedding&amp;von=tools-termincheck&amp;utm_source=tools&amp;utm_medium=termincheck&amp;utm_campaign=datum">Anfragen</a>'; }
      else return;
      td.appendChild(d);
    });
    watch();
  }
  function watch() { var r = document.getElementById('rows'); if (r && window.MutationObserver) { obs = obs || new MutationObserver(paint); obs.observe(r, { childList: true }); } }
  function init() {
    watch();
    fetch(API + '/_form/verfuegbarkeit').then(function (r) { return r.ok ? r.json() : null; }).then(function (j) { if (j && j.days) { AV = j; paint(); } }, function () {});
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();

// ---- 10.9.179: Verbindung zu bride-light.de: Chat, Paketempfehlung, Bewertungen, Probetermin ----
(function () {
  var API = window.HT_API || 'https://bride-light.de';
  var seg = location.pathname.replace(/\/+$/, '').split('/').pop();
  var ALL = ['budgetrechner', 'gaesteliste', 'hochzeitsdatum-finder', 'ablaufplan', 'checkliste', 'fotostunden-rechner', 'getraenkerechner', 'hochzeitstorte-rechner', 'sitzplan', 'tischkarten', 'goldene-stunde', 'einladungs-rechner', 'brautstrauss-konfigurator', 'foto-wunschliste', 'packliste-hochzeit', 'hochzeitstyp', 'fotograf-test', 'gastgeschenke-rechner', 'hochzeitstag-rechner'];
  var isTool = ALL.indexOf(seg) >= 0;
  function ready(f) { if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', f); else f(); }
  function card(html, cls) { var main = document.querySelector('main'); if (!main) return null; var s = document.createElement('section'); s.className = 'card noprint ' + (cls || ''); s.innerHTML = html; main.appendChild(s); return s; }
  function q(o) { return Object.keys(o).map(function (k) { return k + '=' + encodeURIComponent(o[k]); }).join('&'); }

  // Chat (nur, wenn er auf bride-light.de eingeschaltet ist)
  function chat() {
    var t = (document.title || '').split(/\s[–|-]\s/)[0].trim().slice(0, 60);
    window.HT_CHAT_CTX = window.HT_CHAT_CTX || (isTool ? 'Tool: ' + t : 'Tools-Startseite');
    fetch(API + '/_form/chat/status').then(function (r) { return r.json(); }).then(function (j) {
      if (!j || !j.on) return;
      var cfg = document.createElement('script'); cfg.type = 'application/json'; cfg.id = 'lc-widget-cfg';
      cfg.textContent = JSON.stringify({ peers: [new URL(API).host], api: API + '/_form/chat', privacy: 'https://bride-light.de/datenschutzerklarung',
        th: { primary: '#8A4F55', onprimary: '#ffffff', bg: '#FBF5F0', surface: '#ffffff', text: '#3B2A2A', line: '#e6d9cf', body: '"Hanken Grotesk",system-ui,sans-serif', head: 'Fraunces,Georgia,serif', r: '15px' },
        t: { title: 'Chat mit Sebastian', on: 'Online – ich antworte sofort', off: 'Gerade nicht da – hinterlasst eine Nachricht', name: 'Vorname', mail: 'E-Mail (optional, für die Antwort)', msg: 'Eure Nachricht', consent: 'Ich bin einverstanden, dass meine Angaben für diesen Chat gespeichert werden.', privacy: 'Datenschutz', start: 'Chat starten', send: 'Senden', write: 'Nachricht schreiben …', err: 'Das hat leider nicht geklappt. Bitte versucht es später noch einmal.', open: 'Chat öffnen', hint_on: 'Fragen zu eurer Hochzeit? Ich bin online und antworte sofort.', hint_off: 'Fragen zu eurer Hochzeit? Hinterlasst mir gern eine Nachricht.', close: 'Schließen' } });
      document.body.appendChild(cfg);
      var s = document.createElement('script'); s.src = API + '/assets/livechat10173.js'; document.body.appendChild(s);
    }, function () {});
  }

  // Paketempfehlung im Fotostunden-Rechner
  function pakete() {
    var res = document.getElementById('res'), rec = document.getElementById('rec'); if (!res || !rec) return;
    var P = null, box = document.createElement('p'); box.className = 'pc-paket noprint'; rec.parentNode.insertBefore(box, rec.nextSibling);
    function hours() { var b = res.querySelector('b'); return b ? parseFloat(b.textContent.replace(',', '.')) : 0; }
    function show() {
      var h = hours(); if (!P || !h) return;
      var name = h <= 3.5 ? P.s : h <= 7 ? P.m : P.l; if (!name) return;
      var d = (HT.load('datum', {}).fav || [])[0], o = { art: 'wedding', leistung: 'foto', paket: 'foto:' + name, von: 'tools-paket', utm_source: 'tools', utm_medium: 'paketempfehlung', utm_campaign: 'fotostunden' };
      if (d) o.datum = d;
      window.HT_CHAT_CTX = 'Fotostunden-Rechner: ' + String(h).replace('.', ',') + ' Std., empfohlen: ' + name;
      box.innerHTML = 'Dazu passt unser Paket <b>„' + HT.esc(name) + '“</b>. <a class="btn ghost" href="' + HT.esc((P.base || API) + '/?' + q(o)) + '" target="_blank" rel="noopener">Dieses Paket anfragen</a>';
    }
    fetch(API + '/_form/pakete').then(function (r) { return r.json(); }).then(function (j) { if (j && j.pk && j.pk.length) { P = j; show(); } }, function () {});
    if (window.MutationObserver) new MutationObserver(show).observe(res, { childList: true });
  }

  // Bewertungen als Vertrauen
  function trust() {
    fetch(API + '/_form/vertrauen').then(function (r) { return r.json(); }).then(function (j) {
      if (!j || !j.reviews || !j.reviews.length) return;
      var h = '<h2 style="margin-top:0">Das sagen Paare über Bride &amp; Light</h2>';
      j.reviews.forEach(function (r) {
        h += '<blockquote style="margin:.8rem 0"><span aria-label="' + (+r.s) + ' von 5 Sternen" style="color:#B58A5E">' + new Array((+r.s || 5) + 1).join('★') + '</span><br>' + HT.esc(r.t) + '<br><small class="muted">' + HT.esc(r.n) + (r.d ? ' · ' + HT.esc(r.d) : '') + '</small></blockquote>';
      });
      h += '<p><a class="btn ghost" href="' + HT.esc((j.base || API) + '/?' + q({ utm_source: 'tools', utm_medium: 'vertrauen', utm_campaign: seg || 'start' })) + '" target="_blank" rel="noopener">Mehr von uns ansehen</a></p>';
      card(h, 'trust');
    }, function () {});
  }

  // Probetermin
  function probe() {
    if (seg !== 'checkliste' && seg !== 'packliste-hochzeit') return;
    var u = API + '/?' + q({ art: 'wedding', leistung: 'styling', probe: 1, von: 'tools-probe', utm_source: 'tools', utm_medium: 'probetermin', utm_campaign: seg });
    card('<h2 style="margin-top:0">Brautstyling-Probe einplanen</h2><p>Frisur und Make-up in Ruhe ausprobieren, bevor es ernst wird. Ein guter Punkt für eure Liste.</p><p><a class="btn" href="' + HT.esc(u) + '" target="_blank" rel="noopener">Brautstyling-Probe anfragen</a></p>', 'probe');
  }

  ready(function () { chat(); if (isTool) { pakete(); trust(); probe(); } });
})();
