(function () {
  var T = {
    doku: { n: 'Dokumentarisch und unauffällig', d: 'Ihr wollt echte Momente statt gestellter Posen. Die Fotos sollen erzählen, wie sich der Tag angefühlt hat.', l: ['Reportage-Erfahrung und Portfolio mit ganzen Hochzeiten ansehen', 'Dezent arbeiten: Wie viel Anleitung gibt es bei Paarfotos?', 'Lange Begleitung einplanen, damit viele Momente entstehen'], q: ['Wie erlebt ihr den Tag: eher im Hintergrund oder mit Anleitung?', 'Könnt ihr uns eine komplette Galerie zeigen?', 'Wie viele Bilder liefert ihr ungefähr?'] },
    klassisch: { n: 'Klassisch und gut organisiert', d: 'Ihr wünscht euch schöne Porträts, saubere Gruppenfotos und alle wichtigen Personen im Bild.', l: ['Gruppenfotos vorab planen (Liste bereitstellen)', 'Zeit für Porträts und Paarfotos fest im Ablauf einplanen', 'Erfahrung mit Familien und Gruppen erfragen'], q: ['Wie läuft die Gruppenfoto-Planung ab?', 'Wie viel Zeit rechnet ihr für Porträts ein?', 'Gibt es Ersatzpläne bei schlechtem Wetter?'] },
    paar: { n: 'Paarfotos im Mittelpunkt', d: 'Euch sind die Bilder zu zweit am wichtigsten: Licht, Landschaft und ruhige Momente nur für euch.', l: ['Paarshooting im weichen Licht einplanen (Goldene Stunde)', 'Orte vorab absprechen und Wege kurz halten', 'Anleitung beim Posieren besprechen'], q: ['Wie bereitet ihr Paarshootings vor?', 'Wie viel Zeit sollten wir dafür blocken?', 'Kennt ihr Orte in der Nähe unserer Location?'] },
    rundum: { n: 'Rundum begleitet', d: 'Ihr möchtet den ganzen Tag erinnern, von der Vorbereitung bis zur Party.', l: ['Pakete mit langer Begleitung und klarem Zeitplan vergleichen', 'Absprache zu Pausen und Verpflegung des Fotografen', 'Ablaufplan früh teilen'], q: ['Was ist in welchem Paket enthalten?', 'Wie läuft die Begleitung über viele Stunden?', 'Gibt es Zusatzstunden und was kosten sie?'] },
    kunst: { n: 'Künstlerisch und stilvoll', d: 'Euch gefallen besondere Bildsprache, Details und ein klares visuelles Konzept.', l: ['Stil im Portfolio genau ansehen und mit euren Wünschen abgleichen', 'Moodboard oder Beispielbilder mitbringen', 'Nachbearbeitung und Bildlook besprechen'], q: ['Wie würdet ihr euren Stil beschreiben?', 'Wie läuft die Bildbearbeitung?', 'Wie viel kreative Freiheit habt ihr bei der Ortswahl?'] }
  };
  var Q = [
    ['Welche Bilder möchtet ihr später am liebsten ansehen?', [['doku', 'Echte, ungestellte Momente'], ['klassisch', 'Schöne Porträts und Gruppenbilder'], ['paar', 'Viele Fotos nur von uns beiden'], ['rundum', 'Den ganzen Tag, jedes Detail'], ['kunst', 'Besondere, künstlerische Bilder']]],
    ['Wie fühlt ihr euch vor der Kamera?', [['doku', 'Am liebsten, wenn wir sie vergessen'], ['klassisch', 'Okay, wenn jemand sagt, was zu tun ist'], ['paar', 'Wir genießen Zeit zu zweit'], ['rundum', 'Es darf ruhig viel passieren'], ['kunst', 'Wir probieren gerne Neues aus']]],
    ['Wie soll der Ablauf der Fotos sein?', [['klassisch', 'Fester Plan mit Gruppenfoto-Liste'], ['doku', 'Locker, der Tag bestimmt das Tempo'], ['rundum', 'Von Getting Ready bis Tanz'], ['kunst', 'Mit kreativen Pausen für Ideen'], ['paar', 'Mit eigenem Zeitfenster für uns']]],
    ['Wie wichtig sind Gruppenfotos?', [['klassisch', 'Sehr, die Familie muss drauf'], ['doku', 'Nur ein paar wichtige'], ['paar', 'Eher nebensächlich'], ['rundum', 'Wichtig, plus Gäste im Alltag'], ['kunst', 'Gerne anders als üblich']]],
    ['Was zeigt euer Wunschfoto?', [['paar', 'Uns allein in schöner Landschaft'], ['kunst', 'Ein ungewöhnliches Motiv mit Stimmung'], ['doku', 'Ein Lachen mitten in der Feier'], ['klassisch', 'Uns mit den Eltern'], ['rundum', 'Die ganze Gesellschaft beim Tanzen']]],
    ['Wie viel Zeit wollt ihr für Fotos investieren?', [['rundum', 'Viel, der Tag soll komplett erinnert werden'], ['paar', 'Eine ruhige Stunde zu zweit'], ['klassisch', 'Gezielt am Anfang des Tages'], ['doku', 'Wenig Unterbrechung der Feier'], ['kunst', 'So viel, wie das Konzept braucht']]],
    ['Wie wählt ihr die Fotografin oder den Fotografen?', [['kunst', 'Nach dem Stil im Portfolio'], ['doku', 'Nach kompletten Hochzeitsgalerien'], ['klassisch', 'Nach Empfehlung und Erfahrung'], ['paar', 'Nach Paarbildern und Orten'], ['rundum', 'Nach Paketen und Leistungen']]],
    ['Was ist euch am Ende am wichtigsten?', [['doku', 'Dass es sich echt anfühlt'], ['kunst', 'Dass es besonders aussieht'], ['paar', 'Dass wir uns als Paar sehen'], ['klassisch', 'Dass nichts und niemand fehlt'], ['rundum', 'Dass wir den ganzen Tag wiederfinden']]]
  ];
  var $ = function (id) { return document.getElementById(id); }, ans = [], i = 0;
  function show() {
    if (i >= Q.length) return done();
    $('quiz').hidden = false; $('result').hidden = true; $('prog').textContent = 'Frage ' + (i + 1) + ' von ' + Q.length; $('q').textContent = Q[i][0];
    $('opts').innerHTML = Q[i][1].map(function (o, k) { return '<button class="ghost" style="text-align:left" data-k="' + k + '">' + HT.esc(o[1]) + '</button>'; }).join(''); $('back').hidden = i === 0;
  }
  function done() {
    var sc = {}; Object.keys(T).forEach(function (k) { sc[k] = 0; }); ans.forEach(function (a, qi) { sc[Q[qi][1][a][0]]++; });
    var order = Object.keys(T).sort(function (a, b) { return sc[b] - sc[a]; }), t = T[order[0]], s = T[order[1]];
    HT.save('fotograftest', { r: order[0] }); $('quiz').hidden = true; $('result').hidden = false;
    $('rt').textContent = t.n; $('rd').textContent = t.d;
    $('rl').innerHTML = t.l.map(function (x) { return '<li>' + HT.esc(x) + '</li>'; }).join(''); $('rq').innerHTML = t.q.map(function (x) { return '<li>' + HT.esc(x) + '</li>'; }).join('');
    $('r4').textContent = sc[order[1]] > 0 ? 'Auch dabei: ' + s.n + ' (' + sc[order[1]] + ' von ' + Q.length + ' Antworten). Viele Paare mischen Stile.' : '';
    $('links').innerHTML = 'Weiter planen: <a href="../fotostunden-rechner/">Fotostunden-Rechner</a> · <a href="../foto-wunschliste/">Foto-Wunschliste</a> · <a href="../ratgeber/hochzeitsfotograf-finden/">Hochzeitsfotograf finden</a>';
  }
  $('opts').addEventListener('click', function (e) { var b = e.target.closest('button'); if (!b) return; ans[i] = +b.getAttribute('data-k'); i++; show(); });
  $('back').onclick = function () { if (i > 0) { i--; ans.length = i; show(); } };
  $('again').onclick = function () { ans = []; i = 0; show(); };
  show();
})();
