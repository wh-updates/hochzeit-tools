(function () {
  var T = {
    klassisch: { n: 'Klassisch-romantisch', d: 'Ihr liebt zeitlose Eleganz: Weiß, Creme und zarte Blüten, ein klarer Ablauf und Momente, die berühren.', deko: 'Weiß, Creme und Champagner, Rosen und Pfingstrosen, Kerzen auf langen Tafeln.', foto: 'Traditionelle Gruppenfotos, Porträts im weichen Licht, Details wie Ringe und Einladungskarten.', orte: 'Gutshaus oder Schloss im Hinterland, Hotels in den Seebädern, Kirche oder Standesamt in der Altstadt.', links: [['ratgeber/hochzeitslocations-ruegen-ostsee', 'Locations auf Rügen und an der Ostsee'], ['ratgeber/standesamt-unterlagen', 'Standesamt: Unterlagen']] },
    boho: { n: 'Boho-Natur', d: 'Ihr wollt es ungezwungen und naturnah: Wildblumen, offene Haare und eine Feier, die sich leicht anfühlt.', deko: 'Erdtöne, Trockenblumen, Pampasgras, Holz und Leinen, freie Tafeln statt starrer Reihen.', foto: 'Natürliche Szenen, Bewegung und Gespräche, viel Licht in Dünen, Feldern und Wald.', orte: 'Strand und Dünen, Wiese am Bodden, Darßer Wald, Scheune oder Gartenfest.', links: [['ratgeber/freie-trauung-mv', 'Freie Trauung in MV'], ['ratgeber/strandhochzeit-mv', 'Strandhochzeit in MV']] },
    modern: { n: 'Modern-elegant', d: 'Ihr mögt klare Linien und wenige, bewusste Akzente: Design, Ruhe und ein stimmiges Gesamtbild.', deko: 'Schwarz-Weiß oder gedeckte Töne mit einem Akzent, schlichte Blumen, Glas und Metall.', foto: 'Grafische Kompositionen, Architektur als Kulisse, reduzierte Porträts.', orte: 'Moderne Hotels und Lofts, Hafengebäude, Design-Locations in Stralsund und Rostock.', links: [['ratgeber/heiraten-stralsund', 'Heiraten in Stralsund'], ['ratgeber/hochzeitsfotos-tipps-paare', 'Tipps für Paarfotos']] },
    maritim: { n: 'Maritim-Küstenlook', d: 'Das Meer gehört dazu: Weiß und Blau, Muscheln, Seeluft und Weite sind euer Stil.', deko: 'Weiß, Blau und Sand, Kordeln, Treibholz, Muscheln und Gräser, Laternen für den Abend.', foto: 'Seebrücken, Strand und Kreideküste, Wind in den Haaren, Abendlicht über dem Wasser.', orte: 'Seebrücken und Strände auf Rügen und Usedom, Hafen, Kreidefelsen und Leuchttürme.', links: [['ratgeber/heiraten-auf-ruegen', 'Heiraten auf Rügen'], ['ratgeber/heiraten-usedom', 'Heiraten auf Usedom']] },
    vintage: { n: 'Vintage-verspielt', d: 'Ihr liebt Details mit Geschichte: Spitze, Porzellan, Blumenmuster und kleine Überraschungen.', deko: 'Pastell, Spitze, Porzellan, gemischte Gläser, Flohmarktfunde und viel Liebe zum Detail.', foto: 'Detailaufnahmen, Requisiten und Familienmomente, gerne mit Polaroid-Charme.', orte: 'Alte Gutshäuser, Gärten, Dorfkirchen, Backsteinscheunen und Altstadtgassen.', links: [['ratgeber/heiraten-stralsund', 'Heiraten in Stralsund'], ['ratgeber/unterkuenfte-hochzeitsgaeste-ruegen', 'Unterkünfte für Gäste']] }
  };
  var Q = [
    ['Wie sieht euer Traumort aus?', [['klassisch', 'Ein Schloss oder ein elegantes Gutshaus'], ['boho', 'Eine Wiese oder ein Waldrand'], ['modern', 'Ein Hotel oder Loft mit klarer Architektur'], ['maritim', 'Der Strand oder eine Seebrücke'], ['vintage', 'Ein Garten oder eine alte Scheune']]],
    ['Welche Farben gefallen euch am meisten?', [['modern', 'Schwarz, Weiß und ein Akzent'], ['vintage', 'Pastell: Rosé, Mint, Creme'], ['klassisch', 'Weiß, Champagner, Gold'], ['maritim', 'Weiß, Blau und Sand'], ['boho', 'Erdtöne: Terrakotta, Beige, Grün']]],
    ['Welche Blumen passen zu euch?', [['maritim', 'Gräser, Strandflieder, wenig und luftig'], ['klassisch', 'Rosen und Pfingstrosen'], ['boho', 'Wildblumen und Trockenblumen'], ['vintage', 'Gemischte Bündel wie aus Omas Garten'], ['modern', 'Wenige große Blüten, sehr reduziert']]],
    ['Wie soll das Brautkleid wirken?', [['boho', 'Leicht, fließend, mit offenem Rücken'], ['vintage', 'Spitze, Ärmel, ein Hauch Nostalgie'], ['klassisch', 'Prinzessin oder A-Linie'], ['modern', 'Schlicht, geradlinig, mit klarem Schnitt'], ['maritim', 'Luftig, passend für Wind und Sand']]],
    ['Wie soll die Feier sich anfühlen?', [['vintage', 'Gemütlich, mit vielen kleinen Ideen'], ['modern', 'Stilvoll und gut organisiert'], ['maritim', 'Frisch, weit und entspannt wie am Meer'], ['klassisch', 'Festlich mit Programm und Reden'], ['boho', 'Locker, draußen und ohne Zwang']]],
    ['Was soll auf den Tischen stehen?', [['klassisch', 'Kerzen und Kristallgläser'], ['maritim', 'Laternen, Muscheln, Treibholz'], ['vintage', 'Porzellan und verschiedene Gläser'], ['boho', 'Holz, Leinen und Kräuter'], ['modern', 'Schlichte Vasen und klare Linien']]],
    ['Welche Fotos wünscht ihr euch?', [['modern', 'Grafische Bilder mit Architektur'], ['boho', 'Natürliche Szenen mit Bewegung'], ['vintage', 'Details und Polaroid-Momente'], ['klassisch', 'Klassische Porträts und Gruppenbilder'], ['maritim', 'Weite Bilder am Wasser im Abendlicht']]],
    ['Welche Musik passt zum Einzug?', [['maritim', 'Sanfte Akustikklänge, leicht und frei'], ['klassisch', 'Streicher oder Klavier'], ['modern', 'Ein ruhiger moderner Titel'], ['vintage', 'Ein alter Schlager oder Swing'], ['boho', 'Folk mit Gitarre']]]
  ];
  var $ = function (id) { return document.getElementById(id); };
  var ans = [], i = 0;
  function show() {
    if (i >= Q.length) return done();
    $('quiz').hidden = false; $('result').hidden = true;
    $('prog').textContent = 'Frage ' + (i + 1) + ' von ' + Q.length; $('q').textContent = Q[i][0];
    $('opts').innerHTML = Q[i][1].map(function (o, k) { return '<button class="ghost" style="text-align:left" data-k="' + k + '">' + HT.esc(o[1]) + '</button>'; }).join('');
    $('back').hidden = i === 0;
  }
  function done() {
    var sc = {}; Object.keys(T).forEach(function (k) { sc[k] = 0; });
    ans.forEach(function (a, qi) { sc[Q[qi][1][a][0]]++; });
    var order = Object.keys(T).sort(function (a, b) { return sc[b] - sc[a]; }), t = T[order[0]], s = T[order[1]];
    HT.save('hochzeitstyp', { r: order[0] });
    $('quiz').hidden = true; $('result').hidden = false;
    $('rt').textContent = t.n; $('rd').textContent = t.d; $('r1').textContent = t.deko; $('r2').textContent = t.foto; $('r3').textContent = t.orte;
    $('r4').textContent = sc[order[1]] > 0 ? 'Auch dabei: ' + s.n + ' (' + sc[order[1]] + ' von ' + Q.length + ' Antworten). Viele Paare mischen Stile.' : '';
    $('links').innerHTML = 'Weiter lesen: ' + t.links.map(function (l) { return '<a href="../' + l[0] + '/">' + HT.esc(l[1]) + '</a>'; }).join(' · ');
  }
  $('opts').addEventListener('click', function (e) { var b = e.target.closest('button'); if (!b) return; ans[i] = +b.getAttribute('data-k'); i++; show(); });
  $('back').onclick = function () { if (i > 0) { i--; ans.length = i; show(); } };
  $('again').onclick = function () { ans = []; i = 0; show(); };
  show();
})();
