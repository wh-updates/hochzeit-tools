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
