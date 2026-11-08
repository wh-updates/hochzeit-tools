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
