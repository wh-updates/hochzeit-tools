(function () {
  var $ = function (id) { return document.getElementById(id); };
  var st = HT.load('tischkarten', { mode: 'tent', col: '#8a4a50', font: 'Georgia,serif', frame: '1', names: '', mtitle: 'Unser Hochzeitsmenü', mdate: '', msize: 'a6', mcourses: 'Vorspeise\nSalat der Saison\n\nHauptgang\nFisch oder Fleisch mit Beilagen\n\nDessert\nSüße Überraschung' });
  var F = ['mode', 'col', 'font', 'frame', 'names', 'mtitle', 'mdate', 'msize', 'mcourses'];
  F.forEach(function (k) { if (st[k] !== undefined && $(k)) $(k).value = st[k]; });
  function esc(s) { return HT.esc(s); }
  function render() {
    F.forEach(function (k) { st[k] = $(k).value; }); HT.save('tischkarten', st);
    var tent = st.mode === 'tent'; $('tentin').hidden = !tent; $('menuin').hidden = tent;
    var css = 'color:' + st.col + ';font-family:' + st.font + ';', fr = st.frame === '1' ? 'border:1.5px solid ' + st.col + ';' : '', out = '';
    if (tent) {
      var lines = st.names.split('\n').map(function (l) { return l.trim(); }).filter(Boolean);
      for (var i = 0; i < lines.length; i += 8) {
        out += '<div class="pg">' + lines.slice(i, i + 8).map(function (l) {
          var p = l.split(';'), n = esc(p[0].trim()), t = p.length > 1 ? esc(p.slice(1).join(';').trim()) : '';
          var half = function (rot) { return '<div class="half" style="' + (rot ? 'transform:rotate(180deg);' : '') + '"><div class="nm">' + n + '</div>' + (t ? '<div class="tb">' + t + '</div>' : '') + '</div>'; };
          return '<div class="tc" style="' + css + fr + '">' + half(true) + '<div class="fold"></div>' + half(false) + '</div>';
        }).join('') + '</div>';
      }
      if (!lines.length) out = '<p class="muted noprint">Tragt Namen ein, dann erscheint hier die Vorschau.</p>';
    } else {
      var a5 = st.msize === 'a5', blocks = st.mcourses.split(/\n\s*\n/).map(function (b) { return b.split('\n').map(function (x) { return x.trim(); }).filter(Boolean); }).filter(function (b) { return b.length; });
      var card = function () {
        return '<div class="mc ' + (a5 ? 'a5' : 'a6') + '" style="' + css + fr + '"><div class="mt">' + esc(st.mtitle) + '</div>' + (st.mdate ? '<div class="md">' + esc(st.mdate) + '</div>' : '') + '<div class="mrule" style="background:' + st.col + '"></div>' +
          blocks.map(function (b) { return '<div class="mb"><b>' + esc(b[0]) + '</b>' + b.slice(1).map(function (x) { return '<div>' + esc(x) + '</div>'; }).join('') + '</div>'; }).join('') + '</div>';
      };
      out = '<div class="pg ' + (a5 ? 'pg5' : 'pg6') + '">' + (a5 ? card() : card() + card() + card() + card()) + '</div>';
    }
    $('sheet').innerHTML = out;
  }
  F.forEach(function (k) { $(k).addEventListener('input', render); $(k).addEventListener('change', render); });
  $('imp').onclick = function () {
    var s = HT.load('sitzplan', null), m = $('msg');
    if (!s || !s.g || !s.g.length) { m.textContent = 'Im Sitzplan-Planer sind noch keine Gäste eingetragen.'; return; }
    var t = s.t || [];
    $('names').value = s.g.map(function (g) { var tb = g.t !== null && g.t !== undefined && t[g.t] ? t[g.t].n : ''; return g.n + (tb ? '; ' + tb : ''); }).join('\n');
    m.textContent = s.g.length + ' Namen übernommen.'; render();
  };
  render();
})();
