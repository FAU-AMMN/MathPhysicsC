# Differentialformen auf Mannigfaltigkeiten

In diesem Kapitel der Vektoranalysis werden wir nun [Differentialformen](https://de.wikipedia.org/wiki/Differentialform) einführen.
Die entscheidende Neuerung im Vergleich zum vorangegangen Kapitel über Tensoren ist, dass wir zusätzlich zur Vektorraumstruktur nun ein Konzept von Räumlichkeit einführen.
Außerdem werden wir im Folgenden mit *glatten Funktion* arbeiten, d.h., mit Funktionen aus dem Raum $C^\infty(U,\R^n)$.

Um Differentialformen vernünftig einführen zu können benötigen wir allerdings einige zusätzliche mathematische Konzepte, die bisher noch nicht behandelt wurden.
Wir definieren zunächst den Begriff des topologischen Raums als Verallgemeinerung von metrischen Vektorräumen.
Anschließend sind wir in der Lage Mannigfaltigkeiten als spezielle topologische Räume zu definieren, die lokal dem Euklidischen Raum $\R^n$ ähneln, jedoch global verschieden sein können.
Schließlich werden wir Tensorfelder und Differentialformen diskutieren.

## Topologische Räume

Wir haben bisher immer Mathematik auf **metrischen** oder gar **normierten Vektorräumen** betrieben, da uns diese Struktur für alle erklärten Konzepte am dienlichsten war (siehe Kapitel 4 \& 5 in {cite:p}`burger_2020` und [MP-2 Skript](https://fau-ammn.github.io/MathDataScience2/normierte_raeume/normierte_raeume.html)).
Als Vorbereitung für {ref}`s:mannigfaltigkeiten` wollen wir von den metrischen Räumen zu allgemeineren Strukturen wechseln - den sogenannten **topologischen Räumen**.

Das zentrale Konzept topologischer Räume ist die folgende Definition der *offene Mengen*.

````{prf:definition} Offene Mengen und topologischer Raum
 Sei $\M$ eine Menge und $\tau \subset \mathcal{P}(M)$ eine Teilmenge der Potenzmenge.
 Wir nennen das Tupel $(\M,\tau)$ **topologischer Raum**, falls die folgenden Eigenschaften erfüllt sind, 

* $\emptyset, \M \in \tau$,

* für eine beliebige (insbesondere auch *unendlich große*) Indexmenge $\mathcal{I}$ seien $U_i\in\tau, i\in \mathcal{I}$. Dann gilt auch schon $\bigcup_{i\in I} U_i \in \tau$,

* für *endlich viele* $U_j\in\tau, j=1,\ldots, k$ gilt auch schon $\bigcap_{j=1}^k U_j \in \tau$.

Wir bezeichnen mit $\tau$ die **Topologie** des Raumes und dessen Elemente $U\in\tau$ heißen **offene Mengen**.
Für jeden Punkt $x\in \M$ nennen wir eine offene Menge $U(x) \in \tau$ **Nachbarschaft** oder **Umgebung** um $x$, falls $x\in U(x)$.

Analog zur Definition auf metrischen Räumen bezeichnen wir das Komplement $\M \setminus U$ \einer offenen Menge $U$ als **abgeschlossen**.
````

Es gibt viele interessante topologische Räume, die den Namen ihrer Entdecker tragen, wie zum Beispiel der [Arens-Fort-Raum](https://de.wikipedia.org/wiki/Arens-Fort-Raum), der [Cantor-Raum](https://de.wikipedia.org/wiki/Cantor-Raum), oder der [Hilbertwürfel](https://de.wikipedia.org/wiki/Hilbertw%C3%BCrfel).
Im Folgenden wollen wir ein relativ generisches Beispiel für einen topologischen Raum betrachten.

````{prf:example} Diskrete Topologie
:label: ex:diskreteTopologie

Es sei $M$ eine beliebige Menge. 
Dann können wir eine Topologie $\tau$ auf $\M$ definieren, in dem wir alle Teilmengen von $\M$ als offen definieren.
In diesem Beispiel folgt trivialerweise, dass $\tau = \mathcal{P}(\M)$ gilt.
Dann ist $(\M, \tau)$ ein topologischer Raum.
Diese Topologie nennt man **diskrete Topologie**, da für jeden diskreten Punkt $x \in \M$ die Menge $\lbrace x \rbrace$ offen ist.

Die diskrete Topologie wird durch eine spezielle Metrik erzeugt, wie man im Folgenden einsieht.
Seien $x,y \in M$ Punkte der Menge und $d \colon \M \times \M \rightarrow \R^+_0$ eine Metrik auf $\M$ mit

```{math}
d(x,y) := \begin{cases} 0, \quad \text{ falls } x=y,\\ 1, \quad \text{ falls } x\neq y. \end{cases}
```

Über diese Metrik kann man nun *offene Umgebungen* von Punkten $x \in \M$ wie folgt konstruieren,

```{math}
B_1(x) := \lbrace y \in \M : d(x,y) < 1 \rbrace = \lbrace x \rbrace.
```

Dies führt dazu, dass alle Teilmengen, die nur einen Punkt der Menge enthalten, offen sind.
Über beliebige Vereinigung dieser Punktmengen, lassen sich dann alle Teilmengen der Potenzmenge $\mathcal{P}(\M)$ als offen definieren und man erhält somit die diskrete Topologie.
````

````{prf:remark} Notation von topologischen Räumen
Häufig spielt die konkrete Wahl einer Topologie $\tau \subset \mathcal{P}(\M)$ keine Rolle für die mathematischen Aussagen, die man treffen möchte.
Da wir jede beliebige Menge $\M$ mit der diskreten Topologie aus {prf:ref}`ex:diskreteTopologie` zu einem topologischen Raum $(\M, \tau)$ ausstatten können, wird die Angabe der konkreten Topologie $\tau$ häufig ausgelassen.
In solchen Fällen identifiziert man den topologischen Raum einfach mit der zu Grunde liegenden Menge $\M$, d.h., wir nennen $\M$ einen topologischen Raum, wenn die konkrete Topologie im gewählten Kontext eindeutig ist oder keine Rolle spielt.
````

Viele mathematische Konzepte lassen sich von metrischen oder normierten Räumen auf topologische Räume übertragen, wie zum Beispiel der Begriff einer stetigen Funktion.

````{prf:definition} Stetige Funktionen auf topologischen Räumen
:label: def:stetigkeitTopologie

Seien $(\M_1, \tau_1)$ und $(\M_2, \tau_2)$ topologische Räume und $f$ eine Funktion mit

```{math}
f \colon (\M_1, \tau_1) \rightarrow (\M_2, \tau_2).
```

Wir nennen $f$ **stetig**, wenn die Urbilder offener Mengen in $\tau_2$ unter $f$ wieder offene Mengen in $\tau_1$ ergeben, d.h.,

```{math}
f \ \text{ stetig } \quad \Leftrightarrow \quad \forall \, O \in \tau_2 : f^{-1}(O) \in \tau_1.
```

````

Das folgende Diagramm zeigt die Relationen zwischen verschiedenen mathematischen Konzepten innerhalb einer hierarchischen Struktur.

```{math}
\begin{gathered}
\text{Skalarprodukt (Euklidischer / Unitärer Vektorraum)}\\
\downarrow \text{induziert}\\
\text{Norm (Normierter Vektorraum)}\\
\downarrow \text{induziert}\\             
\text{Metrik (Metrischer Vektorraum)}\\
\downarrow \text{induziert}\\                 
\text{Topologie (Topologischer Vektorraum)}
\end{gathered}
```

(s:mannigfaltigkeiten)=

## Mannigfaltigkeiten

In diesem Abschnitt führen wir das grundlegende Konzept von [Mannigfaltigkeiten](https://de.wikipedia.org/wiki/Mannigfaltigkeit) als Spezialfall eines topologischen Raums ein, der lokal mit dem Euklidischen Raum $\R^n$ identifiziert werden kann.
Mannigfaltigkeiten spielen insbesondere im mathematischen Teilgebiet der [Differentialgeometrie](https://de.wikipedia.org/wiki/Differentialgeometrie) eine zentrale Rolle.

### Motivation

Das wohl verständlichste Bild einer Mannigfaltigkeit ist die Oberfläche einer dreidimensionalen Kugel

```{math}
\mathbb{S}^2 := \lbrace (x,y,z)\in\R^3 : x^2 + y^2 + z^2 = 1 \rbrace,
```

wie sie zum Beispiel genutzt wird um die Erdoberfläche zu modellieren.
Möchte man Mathematik auf solch einer Oberfläche betreiben, so benötigt man vollkommen andere Konzepte als in offenen Teilmengen des $\R^n$.
Möchte man beispielsweise berechnen, wie weit man reisen muss, um von einem Punkt auf der Oberfläche zu einem anderen Punkt zu kommen, so benötigt man einen angepassten Abstandsbegriff, da die Euklidische Norm nur die direkte Entfernung messen würde, welche die Kugeloberfläche jedoch durchschneidet.
Dies ist in folgender Abbildung visualisiert.

```{figure} ../img/mannigfaltigkeit.png
---
height: 300px
name: "fig:kugel"
---
Visualisierung zweier unterschiedlicher Abstandsbegriffe für Punkte auf der Kugeloberfläche $\mathbb{S}^2$.
```

Aus dieser Anschauung wird klar, dass unser bisheriges Konzept von Differenzierbarkeit im Mehrdimensionalen aus dem [MP-2 Skript](https://fau-ammn.github.io/MathDataScience2/ableitungen/ableitungen.html) nicht ausreicht, um auf diesem Objekt geeignet Funktionen abzuleiten.
Da man in vielen Bereichen der Physik und der Mathematik nicht nur auf offenen Teilmengen des $\R^n$ ableiten möchte, benötigen wir ein analoges Prinzip für topologische Räume $\M := (\M, \tau)$.

**Wie können wir den Ableitungsbegriff auf topologische Räume übertragen?**

Die grundlegende Idee ist es, den topologischen Raum $\M$ lokal mit einer Teilmenge des $\R^n$ zu identifizieren.
Für eine beliebige offene Teilmenge $U\subset \M$ betrachten wir also eine Abbildung

```{math}
\phi:U\rightarrow \R^n.
```

Wir wollen fordern, dass es sich bei $\phi$ um eine *injektive Abbildung* handelt, so dass eine inverse Abbildung $\phi^{-1}$ existiert.
Diese Umkehrabbildung müssen wir jedoch auf das Bild $\phi(U) \subset \R^n$ einschränken, damit sie wohldefiniert ist.
Damit erhalten wir eine *lokale Bijektion* $\phi^{-1}:\phi(U)\rightarrow U$.

Betrachten wir nun eine Funktion $f \colon \M \rightarrow \R^m$, die Punkte des topologischen Raumes auf Punkte des $\R^m$ abbildet.
Wenn wir diese Funktion differenzieren möchten, so sehen wir ein, dass die Verknüpfung

```{math}
f \circ \phi^{-1} : \phi(U) \subset \R^n \to \R^m
```

es uns erlaubt, das Problem der Ableitung in topologischen Räumen auf das Konzept der mehrdimensionalen Differentiation im $\R^n$ zurückzuführen.

### Karten und Atlanten auf topologischen Räumen

Um den Ableitungsbegriff auf topologischen Räumen $\M$ formal definieren zu können, benötigen wir zusätzlich zur Bijektivität der Abbildung $\phi \colon U \rightarrow \phi(U) \subset \R^n$ die Bedingung, dass für jede Teilmenge $U \subset \M$ gilt,

```{math}
\phi(U)\text{ ist offen} \ \Leftrightarrow \ U \text{ ist offen}.
```

Diese Forderung bedeutet, dass offene Teilmengen in $U \subset \M$ gerade mit offenen Teilmengen in $\phi(U) \subset \R^n$ identifiziert werden.
Wir wollen im Folgenden beide Implikationsrichtungen diskutieren.

1\. $\phi(U)$ ist offen $\Rightarrow U $ ist offen.

Diese Implikation ist äquivalent zur Forderung, dass Urbilder offener Mengen selbst wieder offen sind.
Mit {prf:ref}`def:stetigkeitTopologie` bedeutet dies wiederum, dass die Abbildung $\phi$ stetig ist.

2\. $\phi(U)$ ist offen $\Leftarrow U $ ist offen.

Analog zur obigen Überlegung sehen wir ein, dass diese Bedingung gerade aussagt, dass $\phi^{-1}$ stetig ist.
Diese Forderung ist nicht immer trivialerweise erfüllt.

Das folgende Beispiel zeigt, dass es tatsächlich stetige bijektive Abbildung $\phi$ gibt, für die gilt, dass die Umkehrabbildung $\phi^{-1}$ *nicht stetig* ist.

````{prf:example}
:label: ex:nonho

Wir betrachten in diesem Beispiel die Funktion 

```{math}
\phi:[0,2\pi)&\to\R^2,\\
t &\mapsto \phi(t):= (\cos(t), \sin(t)).
```

Wir erkennen, dass $\phi([0,2\pi)) = \S^1$ gerade der Einheitskreis ist, und dass $\phi:[0,2\pi)\to\S^1$ bijektiv und stetig ist.
Allerdings stellen wir fest, dass die Umkehrabbildung nicht stetig ist. 
Sei dazu $(x_i)_{i\in\N}$ eine Folge von Punkten auf dem Einheitskreis $\S^1$, deren $y$-Koordinate negativ ist und die gegen den Punkt $x = (1,0) \in \S^1$ konvergieren, d.h.,

```{math}
\lim_{i\rightarrow\infty} x_i =: x = (1,0) \in \S^1.
```

Betrachten wir jedoch den Grenzwert der Folge von Funktionswerten $(\phi^{-1}(x_i))_{i\in I}$, so sehen wir, dass 

```{math}
\lim_{i\to\infty} \phi^{-1} (x_i) = 2\pi \neq 0 = \phi^{-1}(x)
```

und somit ist $\phi^{-1}$ offensichtlich nicht stetig.

````

```{figure} ../img/nonhomöo.jpg
---
height: 450px
name: "fig:nonh"
---
Visualisierung einer unstetigen Umkehrabbildung für das {prf:ref}`ex:nonho`.
```

Insgesamt fordern wir also, dass $\phi:U\rightarrow\phi(U)$ bijektiv ist und zusätzlich, dass sowohl $\phi$ als auch die Umkehrabbildung $\phi^-1$ stetig sind.
Eine solche Abbildung definiert man unter dem Begriff *Homöomorphismus*.

````{prf:definition} Homöomorphismus
Seien $X$ und $Y$ topologische Räume.
Dann nennen wir eine Abbildung $f \colon X \rightarrow Y$ einen **Homöomorphismus**, wenn sie folgende Eigenschaften erfüllt:

1. $f$ ist bijektiv
2. $f$ ist stetig
3. die Umkehrfunktion $f^{-1}$ ist ebenfalls stetig.
````

Speziell im Kontext von Mannigfaltigkeiten $\M$, als Spezialfall topologischer Räume (wie wir noch sehen werden), nennt man eine offene Menge zusammen mit einem Homöomorphismus eine **Karte** auf $\M$.

```{prf:definition} Karte
Es sei $\M$ ein topologischer Raum und $U\subset\M$ eine offene Menge.
Sei außerdem $\phi:U\rightarrow \phi(U)\subset \R^n$ ein Homöomorphismus.
Dann heißt das Tupel $(U,\phi)$ **Karte** auf $\M$.
```

Um einen Ableitungsbegriff für Funktionen $f:\M\to\R^m$ über eine Karte $(U,\phi)$ und der Verknüpfung $f\circ \phi^{-1}$ zu definieren benötigen wir noch ein zusätzliches Konzept.
Denn in der Situation, dass $(V,\psi)$ eine zweite Karte ist, deren offene Menge $V$ einen nichtleeren Schnitt mit der offenen Menge $U$ hat, d.h., $U\cap V \neq \emptyset$, erhalten wir genau auf dem Schnitt dieser Mengen zwei unterschiedliche Parametrisierungen,

```{math}
f\circ \phi^{-1} = (f\circ\psi^{-1})\circ(\psi\circ \phi^{-1}),\\
f\circ \psi^{-1} = (f\circ\phi^{-1})\circ(\phi\circ \psi^{-1}).
```

Um von einer Karte zur nächsten Karte zu kommen benötigen wir eine geeignete Abbildung.

````{prf:definition} Kartenwechsel
Es sei $\M$ ein topologischer Raum und es seien $(U,\phi)$ und $(V,\psi)$ zwei Karten auf $\M$ mit nicht-leerem Schnitt, d.h., $U\cap V\neq \emptyset$. 
Dann nennt man die Abbildung

```{math}
\psi\circ\phi^{-1}: \phi(U\cap V)\rightarrow \psi(U\cap V)
```

einen **Kartenwechsel** von $(U,\phi)$ nach $(V,\psi)$.

````

```{figure} ../img/chartchange.jpg
---
height: 450px
name: "fig:chartchange"
---
Kartenwechsel.
```

Wir erkennen also, dass Umparametrisierungen der Form $\psi\circ \phi^{-1}$ entscheidend sind, um von einer lokalen Identifikation des topologischen Raums zur nächsten zu gelangen.
Wäre nun der Kartenwechsel $\psi\circ \phi^{-1}$ und respektive $\phi\circ \psi^{-1}$ differenzierbar, so könnte man die jeweiligen Ableitungen leicht durch die Kettenregel ineinander umrechnen.
Allerdings existieren durchaus Beispiele, in denen sowohl $f\circ\phi^{-1}$ als auch $f\circ\psi^{-1}$ differenzierbar sind, aber der Kartenwechsel $\psi\circ\phi^{-1}$ nicht.
Deshalb führt man zusätzlich noch den folgenden Begriff ein.

````{prf:definition} Atlas
Es sei $\M$ ein topologischer Raum.
Eine Familie von Karten $\mathcal{A} = (U_i,\phi_i)_{i\in I}$ indiziert durch die Indexmenge $I$ heißt **Atlas**, falls die Vereinigung aller offenen Mengen eine Überdeckung des topologischen Raums darstellt, d.h., es gilt

```{math}
\M = \bigcup_{i\in I} U_i.
```

Wir nennen einen Atlas $k$-mal **differenzierbar** oder von der Klasse $C^k$, falls jeder Kartenwechsel $\phi_i\circ\phi_j^{-1}, i,j\in I$ $k$-mal stetig differenzierbar ist.

````

Die Begriffe *Karte* und *Atlas* stammen in der Tat aus mathematischen Überlegungen in der Kartographie.
Man kann Teile der Erdoberfläche mit einer Karte auf eine Ebene $\R^2$ abbilden.
Nähert man sich dem Rand einer Karte, so möchte man zu einer anderen Karte wechseln, die das angrenzende Gebiet darstellt.

So kann eine Mannigfaltigkeit durch einen vollständigen Satz von Karten vollständig beschrieben werden; man braucht dabei Regeln, wie sich beim Kartenwechsel die Karten überlappen.

### Differenzierbare Mannigfaltigkeiten

Für einen topologischen Raum $\M$ können mehrere Atlanten $\mathcal{A}$ existieren, weshalb es sinnvoll ist Äquivalenzklassen von Atlanten zu betrachten.

````{prf:definition} $C^k$-differenzierbare Struktur
Für einen Index $k\in \N \cup \{\infty\}$ heißen zwei differenzierbare Atlanten $\mathcal{A}_1, \mathcal{A}_2$ der Klasse $C^k$ **$k$-äquivalent**, falls ihre Vereinigung $\mathcal{A}_1\cup \mathcal{A}_2$ wieder ein Atlas der Klasse $C^k$ ist.
Dies bedeutet insbesondere, dass die Kartenwechsel durch die Vereinigung der beiden Atlanten weiterhin $k$-mal stetig differenzierbar bleiben.
In diesem Fall notieren wir $\mathcal{A}_1\sim_k \mathcal{A}_2$.
Die Äquivalenzklasse $[\mathcal{A}]_{\sim_k}$ nennt man eine **$C^k$-differenzierbare Struktur**.
````

```{margin}
[Felix Hausdorff](https://de.wikipedia.org/wiki/Felix_Hausdorff) (geboren am 8. November 1868 in Breslau; gestorben am 26. Januar 1942 in Bonn) war ein deutscher Mathematiker.
```

Bisher haben wir $\M$ als allgemeinen topologischen Raum betrachtet.
In vielen Anwendungen benötigt man aber weitere nützliche Eigenschaften des Raumes.
Insbesondere wenn man [glatte Testfunktionen](https://de.wikipedia.org/wiki/Testfunktion) und [die Zerlegung der Eins](https://en.wikipedia.org/wiki/Partition_of_unity) benutzen möchte braucht man folgende zwei zusätzliche Eigenschaften.

Wir definieren zunächst die Eigenschaft eines Hausdorff-Raums.

````{prf:definition} Hausdorff-Raum
Ein topologischer Raum $\M$ heißt **Hausdorff-Raum**, falls für je zwei unterschiedliche Punkte $x,y\in \M, x\neq y$ offene Umgebungen $U(x), U(y) \subset \M$ existieren, welche disjunkt sind, d.h., $U(x)\cap U(y) = \emptyset$.
Man nennt $\M$ dann auch einen **separierten Raum**.
````

Als zweite nützliche Eigenschaft fordern wir, dass unser topologischer Raum $\M$ das zweite Abzählbarkeitsaxiom erfüllen soll.

````{prf:definition} Zweites Abzählbarkeitsaxiom
Ein toplogischer Raum $(\M, \tau)$ erfüllt das **zweite Abzählbarkeitsaxiom**, falls *abzählbar* viele offene Mengen $(V_i)_{i\in\N} \in \tau$ existieren, so dass für jeden Punkt $x\in \M$ und jede offene Umgebung $U(x) \in \tau$ von $x$ mindestens ein Index $k\in\N$ existiert mit $V_k \subset U(x)$.
Man nennt $(\M, \tau)$ dann auch **zweitabzählbar**.
````

Diese zwei Bedingung wirken zunächst abstrakt.
Glücklicherweise werden sie jedoch von vielen üblichen topologischen Räumen erfüllt, wie zum Beispiel dem Euklidischen Raum $\R^n$.

```{prf:remark}
Falls der Begriff eines zweitabzählbaren Hausdorff-Raums zu unhandlich erscheint, kann man für die meisten Anwendungen in der Physik auch einfach **metrische Räume** betrachten, die diese beiden Eigenschaften implizieren.
```

Nun haben wir alle nötigen Voraussetzungen geschaffen um den Begriff einer Mannigfaltigkeit formal einzuführen.

````{prf:definition} Differenzierbare Mannigfaltigkeit
Es sei $\M$ ein zweitabzählbarer Hausdorff-Raum und für $k\in\N\cup \{\infty\}$ sei $[\mathcal{A}]_{\sim_k}$ eine $C^k$-differenzierbare Struktur.
Dann nennen wir $(\M,[\mathcal{A}]_{\sim_k})$ eine $k$-**mal differenzierbare Mannigfaltigkeit**.
Für den Spezialfall $k=\infty$ sprechen wir auch von einer **glatten Mannigfaltigkeit**.

Falls alle Karten auf $\M$ nach $\R^n$ abbilden, so nennt man die Mannigfaltigkeit *$n$-dimensional*.
````

Ähnlich wie bei topologischen Räumen spricht man in den meisten Fällen nur von der Mannigfaltigkeit $\M$; die differenzierbare Struktur $[\mathcal{A}]_{\sim_k}$ wird dabei implizit vorausgesetzt.

Basierend auf einer differenzierbaren Mannigfaltigkeit $\M$ können wir nun differenzierbare Funktionen auf $\M$ definieren.

````{prf:definition} Differenzierbare Funktion auf einer Mannigfaltigkeit
Sei $\M$ eine $k$-mal differenzierbare Mannigfaltigkeit $\mathcal{A}$ ein Atlas auf $\M$.
Dann nennen wir eine Abbildung $f:\M\to\R^m$ **$k$-mal differenzierbar**, falls für jeden Punkt $x\in\M$ eine differenzierbare Karte $(U(x),\phi)\in\mathcal{A}$ existiert, so dass $f\circ\phi^{-1} \in C^k(\phi(U(x)); \R^m)$.
Insbesondere schreiben wir in diesem Fall $f\in C^k(\M; \R^m)$. 
````

In vielen Anwendungen beschränkt man sich nur auf *glatte Mannigfaltigkeiten* und *glatte Funktionen* in $C^\infty(\M; \R^m)$.
Wir werden im Folgenden der Einfachheit-halber auch dazu übergehen.

````{prf:lemma}
Es sei $\M$ eine glatte Mannigfaltigkeit.
Dann ist $C^\infty(\M; \R^m)$ ein reeller Vektorraum mit den Verknüpfungen

```{math}
(\lambda \cdot f)(x) := \lambda\cdot f(x)\text{ für } f\in C^\infty(\M; \R^m), \lambda\in\R,\\
(f + g)(x) := f(x) + g(x)\quad\text{ für } f,g\in C^\infty(\M; \R^m).
```

````

````{prf:proof}
In der Hausaufgabe zu zeigen.
````

Die Eigenschaft der Differenzierbarkeit einer Funktion auf einer Mannigfaltigkeit ist kartenunabhängig, wie folgendes Lemma feststellt.

````{prf:lemma}
:label: lem:differenzierbarkeitKartenunabhaengig
Es sei $\M$ eine glatte Mannigfaltigkeit und $\mathcal{A}$ ein Atlas auf $\M$.
Außerdem sei $f:\M \to \R^m$ eine Funktion, $(U,\phi)\in \mathcal{A}$ eine Karte und $x \in U$ ein Punkt in der offenen Menge $U$.
Ist $f\circ\phi^{-1}$ differenzierbar in $x$, so ist $f\circ\psi^{-1}$ auch differenzierbar in $x$ für jede Karte $(V,\psi) \in \mathcal{A}$ mit $x\in V$.
````

````{prf:proof}
In der Hausaufgabe zu zeigen.
````

### Tangentialräume an Mannigfaltigkeiten

Aus dem Kapitel {ref}`s:linearisierung_ruhelage` ist bereits das Konzept der *Linearisierung* bekannt.
Anschaulich gesprochen haben wir eine differenzierbare Funktion $f$ durch ihre Linearisierung ersetzt um ein einfacheres Problem zu erhalten.
Dieses Konzept soll nun auf glatte Mannigfaltigkeiten übertragen werden.

Wir haben bereits erkannt, wie wir den Begriff der Differenzierbarkeit einer Funktion auf einer Mannigfaltigkeit definieren.
Und obwohl die Frage nach der Differenzierbarkeit einer Funktion nach {prf:ref}`lem:differenzierbarkeitKartenunabhaengig` kartenunabhängig ist, so stellt sich heraus, dass der tatsächliche *Wert der Ableitung* einer Verknüpfung $f \circ\phi^{-1}$ noch immer von der konkreten Wahl des Homöomorphismus $\phi$ abhängt.
Um auch hier die gewünschte Kartenunabhängigkeit zu erreichen, brauchen wir einen anderen Begriff der Differenzierbarkeit.
Hierbei wird uns der sogenannte **Tangentialraum** helfen.
Man kann ihn als eine Linearisierung der Mannigfaltigkeit $\M$ an einem Punkt $p\in\M$ interpretieren.

Das folgende Beispiel erklärt anschaulich den Tangentialraum an eine Mannigfaltigkeit.

````{prf:example}
Wir betrachten zunächst den Einheitskreis $\M = \mathbb{S}^1$ und den Punkt $p = (1, 0)^T \in \mathbb{S}^1$.
Der Tangentialraum $T_p\M$ an $\M$ im Punkt $p$ ist der eindimensionale Unterraum

```{math}
T_p\M = \lbrace \lambda \cdot (0, 1)^T : \lambda \in \R \rbrace \subset \R^2.
```
````

Es gibt in der Literatur zwei verschiedene, jedoch äquivalente Arten den Tangentialraum zu definieren.

* **Geometrischer Tangentialraum**: Bei diesem Ansatz wählt man eine geometrisch Anschauung und definiert den Tangentialraum durch Richtungsvektoren, die am Punkt $p\in\M$ anliegen.
Der Vorteil dieser Definition ist es, dass sie intuitiv und geometrisch anschaulich ist.

* **Algebraische Defnition**: Bei diesem Ansatz führt man den Tangentialraum mittels spezieller linearer Abbildungen, genannt Derivationen, zurück.
Man verliert hierbei zwar die geometrische Anschauung, allerdings ist das Konzept relativ einfach zu formulieren und hilft die Sachverhalte auf algebraische Zusammenhänge zurückzuführen.

In der Praxis (und in vielen Mathematikbüchern) werden beide Definitionen nebeneinander verwendet und die jeweilige Interpretation geht dann aus dem Kontext hervor.
Da sich die beiden Konzepte somit schlecht voneinander trennen lassen werden wir im Folgenden den geometrischen Tangentialraum $T^{\text{geo}}_p\M$ und den algebraischen Tangentialraum $T^{\text{alg}}_p\M$ explizit einführen und anschließend eine Isomorphie

```{math}
T^{\text{geo}}_p\M\cong T^{\text{alg}}_p\M
```

zwischen den beiden Tangentialräumen zeigen.

```{danger}
In der Literatur wird diese explizite Unterscheidung oft nicht vorgenommen.
Stattdessen wird der Tangentialraum einfach nur $T_p\M$ genannt.
Elemente dieses Raums sind dann je nach Kontext geometrisch oder algebraisch zu interpretieren.
```

#### Geometrische Definition

Von der Differentiation im Mehrdimensionalen ist bereits das Konzept der **Richtungsableitung** bekannt (siehe Kapitel 6.2.2 in {cite:p}`tenbrinck_2021`).
Hierbei betrachtet man für eine Funktion $F:\R^n\to\R$ den Strahl $\gamma(t):= x + t\cdot v$, wobei $x,v\in\R^n$ und den Grenzwert

```{math}
\lim_{t\to 0} \frac{F(\gamma(t)) - F(\gamma(0))}{t} = \frac{F(x + t\cdot v) - F(x))}{t}.
```

Wir werden dieses Konzept nun auf glatte $n$-dimensionale Mannigfaltigkeiten $\M$ verallgemeinern, indem wir anstatt von Strahlen differenzierbare *Kurven* auf der Mannigfaltigkeit betrachten.

````{prf:definition} Differenzierbare Kurve
Sei $\M$ eine glatte Mannigfaltigkeit und sei 

```{math}
\gamma \colon (-1,1) \rightarrow \M
```

eine Kurve auf der Mannigfaltigkeit $\M$.
Wir nennen $\gamma$ **differenzierbar** im Punkt $0\in(-1,1)$, falls die Kurve *stetig* ist und falls eine Karte $(U,\phi)$ von $\M$ existiert, so dass für genügend kleines $\varepsilon$ auch $\gamma((-\varepsilon,\varepsilon))\subset U$ gilt und die Verknüpfung

```{math}
\phi \circ \gamma:(-\varepsilon,\varepsilon)\to\R^n
```

differenzierbar in $0$ ist .
````

Wir werden im Folgenden ausschließlich die Ableitung der Kurve im Punkt $t=0$ betrachten und sprechen deshalb verkürzt einfach nur von *differenzierbaren* Kurven.
Zusätzlich sei zu bemerken, dass die obige Definition **nicht** von der Wahl der Karte abhängt.

````{prf:example}
Es sei $\M=\S^2$ die Einheitssphäre und $f:\M\to\R$ beschreibe eine Wärmeverteilung auf deren Oberfläche.
Betrachtet man nun die Bahn eines Partikels auf der Oberfläche beschrieben durch die Kurve $\gamma:(-t, t)\to \M$ so erhalten wir eine eindimensionale Abbildung 

```{math}
f\circ\gamma:(-t,t)\to \R,
```

die zu jedem Zeitpunkt die Temperatur des Ortes, an dem sich der Partikel befindet, beschreibt.
````

```{figure} ../img/velocity.jpg
---
height: 300px
width: 350px
name: "fig:velocity"
---
Visualisierung einer Kurve auf der oberen Hälfte der Einheitssphäre im $\R^3$.
```

Mit Hilfe von differenzierbaren Kurven auf Mannigfaltigkeiten können wir im Folgenden die Richtungsableitung an einer Mannigfaltigkeit definieren.

````{prf:definition} Richtungsableitung an Mannigfaltigkeit
:label: def:direcdiv

Es sei $\M$ eine glatte Mannigfaltigkeit, $\gamma:(-1,1)\to\M$ eine differenzierbare Kurve mit $\gamma(0)=p\in\M$ und $f \in C^\infty(\M)$ eine glatte Funktion.
Dann nennen wir die Abbildung

```{math}
D_\gamma : C^\infty(\M) &\to \R\\
f &\mapsto D_\gamma(f):=\frac{d}{dt}(f\circ \gamma)\big\rvert_{t=0}
```

**Richtungsableitung** von $f$ durch $\gamma$ im Punkt $p$.
````

Betrachten wir nun eine differenzierbare Kurve $\gamma \colon (-1, 1) \rightarrow \M$ mit $\gamma(0)=p \in \M$ und eine glatte Funktion $f \in \C^\infty(\M)$ definiert auf einer glatten Mannigfaltigkeit $\M$.
Dann können wir die Richtungsableitung $D_\gamma(f)$ mit Hilfe der **Kettenregel für die Differentiation** darstellen als

```{math}
D_\gamma(f) = \frac{d}{dt}(f\circ \gamma)\big\rvert_{t=0} = \frac{d}{dt}\big( (f\circ \phi^{-1}) (\phi \circ \gamma) \big)\rvert_{t=0} = 
\big(D(f\circ \phi^{-1})\big)(\phi(p))\cdot \frac{d}{dt}(\phi \circ \gamma)\rvert_{t=0}
```

und für eine weitere differenzierbare Kurve $\eta \colon (-1, 1) \rightarrow \M$ mit $\eta(0)=p$ erhalten wir analog

```{math}
D_\eta(f) = \frac{d}{dt}(f\circ \eta)\big\rvert_{t=0} = 
\big(D(f\circ \phi^{-1})\big)(\phi(p))\cdot \frac{d}{dt}(\phi \circ \eta)\rvert_{t=0}.
```

Wir erkennen also, dass der Wert der Richtungsableitung in der Tat von der Kurve $\gamma$ abhängt.
Dies führt auf einen natürlichen Äquivalenzbegriff von Kurven, wie die folgende Bemerkung beschreibt.

````{prf:remark} Tangentialvektoren
:label: rem:tang

Es sei $\M$ eine glatte $n$-dimensionale Mannigfaltigkeit, $p\in\M$ ein Punkt auf der Mannigfaltigkeit und $(U,\phi)$ eine Karte von $\M$, für die gilt, dass $p\in U$ ist.
Für zwei differenzierbare Kurven $\gamma, \eta:(-1,1) \to U$ mit $\gamma(0) = \eta(0) = p$ ist die Relation 

```{math}
\gamma \sim_p \eta
\qquad \Leftrightarrow \qquad
\frac{d}{dt}(\phi \circ \gamma)\rvert_{t=0} = \frac{d}{dt}(\phi \circ \eta)\rvert_{t=0}\in \R^n
```

eine Äquivalenzrelation (siehe Kapitel 2.1.1 in {cite:p}`burger_2020`).
Insbesondere ist die Äquivalenzklasse unabhängig von der Wahl des Homöomorphismus $\phi$.
````

Mittels der oben beschriebenen Äquivalenzrelation sind wir in der Lage den Begriff der *Tangentialvektoren* und des *Tangentialraums* zu definieren.

````{prf:definition} Geometrische Tangentialvektoren und Tangentialraum
Es sei $\M$ eine glatte $n$-dimensionale Mannigfaltigkeit, $p\in\M$ ein Punkt auf der Mannigfaltigkeit und $(U,\phi)$ eine Karte von $\M$, für die gilt, dass $p\in U$ ist.

Die Äquivalenzklasse $\gamma^\prime(0):=[\gamma]_{\sim_p}$ wird als **geometrischer Tangentialvektor** an $\M$ im Punkt $p$ bezeichnet.
Der Raum der (geometrischen) Tangentialvektoren

```{math}
T_p^{\text{geo}}\M := \{\gamma^\prime(0): \gamma\text{ ist differenzierbare Kurve mit }\gamma(0)=p\}
```

heißt **geometrischer Tangentialraum** der Mannigfaltigkeit $\M$ am Punkt $p \in \M$.
````

Der Tangentialraum induziert sogar eine Vektorraumstruktur wie folgende Bemerkung festhält.

````{prf:remark}

Es sei $\M$ eine glatte $n$-dimensionale Mannigfaltigkeit, $p\in\M$ ein Punkt auf der Mannigfaltigkeit und $(U,\phi)$ eine Karte von $\M$, für die gilt, dass $p\in U$ ist.
Sei außerdem $\gamma \colon (-1,1) \rightarrow \M$ eine differenzierbare Kurve auf $\M$ mit $\gamma(0) = p$.
Wir definieren nun die folgende Bijektion auf dem Tangentialraum

```{math}
d\phi\rvert_p \colon T^{\text{geo}}_p\M &\rightarrow \R^n,\\
[\gamma]_{\sim_p} &\mapsto d\phi\rvert_p (\gamma^\prime(0)) := (\phi \circ \gamma)^\prime (0).
```

Basierend auf dieser Abbildung lassen sich die folgenden Operationen für den Punkt $p \in \M$ definieren

```{math}
\gamma^\prime(0) +_{p} \eta^\prime(0) \ &:= \
(d\phi\rvert_p)^{-1}\big[d\phi\rvert_p(\gamma^\prime(0)) + d\phi\rvert_p(\eta^\prime(0))\big]\\
\lambda \cdot_p \gamma^\prime(0) \ &:= \ (d\phi\rvert_p)^{-1} (\lambda \cdot d\phi\rvert_p(\gamma^\prime(0))
```

Insgesamt ergibt somit das Tripel $(T_p^{\text{geo}}\M, +_p, \cdot_p)$ einen reellen Vektorraum.
Man bemerke, dass die oben definierten Abbildungen erneut **unabhängig** von der Wahl des Homöomorphismus $\phi$ sind.

````

#### Algebraische Definition

Alternativ zur geometrischen Herleitung lässt sich der Tangentialraum auch algebraisch definieren über sogenannte Derivationen. Hierbei beschreiben wir Tangentialvektoren nun nicht mehr als Kurven, sondern als spezielle Funktionale, welche durch ihre Wirkung auf $C^\infty(\M)$ charakterisiert sind. Die Motivation hierbei soll die Richtungsableitung aus {prf:ref}`def:direcdiv` sein und speziell die folgenden Eigenschaften.

````{prf:lemma}
Es sei $\M$ eine glatte Mannigfaltigkeit, $p\in\M$ und $\gamma:[-1,1]\to\M$ eine glatte Kurve durch $p$, dann gilt für die Richtungsableitung $D_\gamma:C^\infty(\M)\to\R$, 

* $D_\gamma\in (C^\infty(\M))^\ast$,

* Für $f,g\in C^\infty(\M)$ gilt $D_\gamma(fg) = D_\gamma(f) g(p) + f(p) D_\gamma(f)$.

````

````{prf:proof}
Siehe Übung.
````

Die zweite Eigenschaft wird auch *Produktregel* oder *Leibnizregel* genannt. Wir wollen nun im folgenden nicht nur Richtungsableitungen betrachten, sondern allgemeine Funktionale, die diese Eigenschaft erfüllen.

````{prf:definition} Derivation und algebraischer Tangentialraum
Es sei $\M$ eine glatte Mannigfaltigkeit und $p\in\M$ ein Punkt der Mannigfaltigkeit.
Wir nennen eine lineare Abbildung $D: C^\infty(\M) \to \R$ eine **Derivation** an $p$, falls sie die folgende Produktregel erfüllt, 

```{math}
D(fg) = D(f) g(p) + f(p) D(g).
```

Der Raum der Derivationen an $p$

```{math}
T^{\text{alg}}_p\M:=\{D\in C^\infty(\M)^\ast: D\text{ ist Derivation an }p\}
```

wird als **algebraischer Tangentialraum** bezeichnet.
````

Über die Menge der Derivation erhalten wir auf natürliche Art einen Vektorraum, da per Definition

```{math}
T^{\text{alg}}_p\M \subset C^\infty(\M)^\ast
```

gilt. Somit erbt der algebraischer Tangentialraum die Vektorraumoperationen von $C^\infty(\M)^\ast$ und es muss lediglich nachgeprüft werden, dass diese Teilmenge noch immer ein Vektorraum ist.

````{prf:lemma}
Es sei $\M$ eine glatte Mannigfaltigkeit und $p\in\M$, dann ist $T^{\text{alg}}_p\M$ ein reeller Vektorraum.
````

````{prf:proof}
Siehe Übung.
````

Wir der Name schon erkennen lässt haben Derivationen gewisse Eigenschaften, die von der Ableitungsoperation bekannt sind. So z.B. bildet jede Derivation konstante Funktionen auf $0$ ab.

````{prf:lemma}
:label: lem:constder

Es sei $\M$ eine glatte Mannigfaltigkeit, $p\in\M$ und $f\in C^\infty(\M)$ sei konstant, d.h., es existiert $c\in\R$, s.d., 

```{math}
f(q) = c\quad\forall q\in\M,
```

dann gilt $D(f)=0$ für alle Derivationen $D\in T^{\text{alg}}_p\M$.
````

````{prf:proof}
Es sei $D\in T^{\text{alg}}_p\M$, wir betrachten die Funktion 

```{math}
g:&\M\to \R\\
&q\mapsto 1
```

also die konstante Einsfunktion. Dann gilt

```{math}
D(g) = D(g\cdot g) = D(g)\,g(p) + g(p)\, D(g) = 2\,D(g)
```

und somit $D(g) = 0$. Per Annahme wissen wir $f= c\,g$ und unter Ausnutzung der Linearität von $D$ erhalten wir 

```{math}
D(f) = D(c\,g) = c\,D(g) = 0.
```
````

Wir haben nun zwei verschiedene Arten gesehen den Tangentialraum einzuführen. Tatsächlich sind diese Definitionen äquivalent in dem Sinne, dass ein Isomorphismus zwischen dem geometrischen und algebraischen Tangentialraum existiert.

````{prf:lemma}
Es sei $\M$ eine glatte Mannigfaltigkeit und $p\in\M$, dann gilt 

```{math}
T^{\text{geom}}_p\M \cong T^{\text{alg}}_p\M.
```

````

````{prf:proof}
Siehe z.B. {cite:p}`Jnich2003` Kapitel 2.3.
````

(sec:TPBasis)=
#### Basis des algebraische Tangentialraums

Wir wollen eine Basis des algebraischen Tangentialraums konstruieren.
Im Euklidischen Raum können wir auf natürliche Art die Koordinatenrichtungen als Kurven wählen, also Funktionen der Form

```{math}
t\mapsto t e_i
```

für $i=1,\ldots,n$, wobei $e_i$ den $i$-ten Einheitsvektor in $\R^n$ bezeichnet.
Um diese Idee auf Mannigfaltigkeiten zu übertragen wählen wir eine Karte $\varphi:\M\to\R^n$, wobei man hier auch von

```{math}
\phi = (\varphi_1,\ldots,\varphi_n) =: (x^1,\ldots,x^n)
```

als **lokales Koordinatensystem** spricht. Wir erhalten somit Kurven

```{math}
\gamma_{x^i}(t):= \varphi^{-1}(\varphi(p) + t e_i)
```

und mithilfe der Richtungsableitung die Derivationen

```{math}
\partial_{x^i}^p: C^\infty(\M) \to \R\\
\partial_{x^i}^p(f) := \frac{d}{dt} (f\circ \gamma_{x^i}(t)).
```

Wir interpretieren also im Folgenden das Symbol $\partial_{x^{i}}^p$ als Derivation an $p\in\M$, d.h., insbesondere als lineare Abbildung von $C^\infty(\M)$ nach $\R$. Diese partiellen Derivationen erhalten die Intuition, dass die partielle Ableitung in eine Richtung auch nur Änderungen in diese Richtung respektiert. Wir formalisieren diese Anschauung in folgendem Lemma.

````{prf:lemma}
:label: lem:partderkron

Es sei $\M$ eine glatte Mannigfaltigkeit, $p\in\M$ und $(U,\phi)$ sei Karte mit $p\in U$, dann gilt 

```{math}
\partial_{x^i}^p(\varphi_j) = \delta_{ij}
```

wobei $\delta$ das Kronecker-Delta bezeichnet.
````

````{prf:proof}
Wir betrachten zunächst die Funktion $\varphi_j \circ \gamma_{x^i}$ und erhalten für $t\in [-1,1]$

```{math}
\varphi_j \circ \gamma_{x^i}(t)
&= \varphi_j \circ \varphi^{-1}(\phi(p) + t e_i)\\
&= (\varphi(p) + t e_i)_j\\ 
&=
\begin{cases}
\varphi(p) + t e_i &\text{ für } i=j\\
\varphi_j(p)&\text{ sonst}
\end{cases}.
```

Somit gilt für die partielle Derivation 

```{math}
\partial_{x^i}^p(\varphi_j)=
\frac{d}{dt} \varphi_j \circ \gamma_{x^i}(t) = 
\begin{cases}
1&\text{ für } i=j\\
0&\text{ sonst}
\end{cases}.
```

````

Das folgende Hauptresultat dieses Abschnitts erlaubt es uns beliebige Derivationen mithilfe der partiellen Derivationen darzustellen, da diese eine Basis des algebraischen Tangentialraums bilden.

````{prf:theorem}
:label: thm:tanbasis

Es sei $\M$ eine $n$-dimensionale glatte Mannigfaltigkeit, dann bildet die Menge $\{\partial_{x^1}\rvert_p,\ldots,\partial_{x^n}\rvert_p\}$ eine Basis des Vektorraums $T^{\text{alg}}_p$. Insbesondere gilt $\dim(T^{\text{alg}}_p)=\dim(T^{\text{geom}}_p)=n$.
````

````{prf:proof}
Es sei $(U,\varphi)$ eine Karte und o.B.d.A. nehmen wir an, dass $\varphi(p)=0$ gilt, was stets durch Translation des Koordinatensystems erreicht werden kann. Zusätzlich finden wir dann $r>0$ klein genug, s.d., $B_r(0)\subset \varphi(U)$ gilt und betrachten als Karte die Einschränkung von $\varphi$ auf $\tilde{U}:= \varphi^{-1}(B_r(0))$, $\tilde{\varphi} := \varphi\rvert_{\tilde{U}}$. Wegen der Kartenunabhängigkeit und der Tatsache, dass $(\tilde{U},\tilde{\varphi})$ auch eine Karte für $\M$ ist, mit $p\in \tilde{U}$ können wir diese Karte betrachten. 

Da das Bild nun der Ball $B_r(0)$ ist dürfen wir Strahlen von $0$ zu einem beliebigen Punkt im Bild von $\tilde{\varphi}$ betrachten, wobei der gesamte Strahl selbst schon im Bild enthalten ist.

Sei nun $f\in C^\infty(\M)$, dann betrachten wir $g:= f\circ \tilde{\varphi}^{-1}$ und somit gilt insbesondere $g\in C^\infty(\R^n)$. Für beliebiges $q\in\tilde{U}$ und $z:=\tilde{\varphi}(q)\in B_r(0)$ können wir dann die Einschränkung auf den eindimensionalen Strahl zwischen $0$ und $z$ betrachten, konkret 

```{math}
\tilde{g}:&[0,1]\to\R\\
t&\mapsto g(t\cdot z)
```

wobei wir erneut erkennen, dass $\tilde{g}\in C^\infty([0,1])$. Insbesondere, können wir den Hauptsatz der Integralrechnung anwenden und erhalten 

```{math}
\tilde{g}(1) = \tilde{g}(0) + \int_{0}^1 \tilde{g}^\prime(t) dt.
```

Wir berechnen die Ableitung im Integral und erhalten, 

```{math}
\int_{0}^1 \tilde{g}^\prime(t) dt
&=\int_{0}^1 \langle (\nabla g)(t\cdot z), z \rangle dt\\
&=\sum_{i=1}^{n} \int_{0}^1  (\partial_i g)(t\cdot z)\,z_i dt.
```

Da

```{math}
\tilde{g}(1) = g(z)=f(q)
```

und 

```{math}
\tilde{g}(0) = g(0) = g(\varphi(p))=f(p)
```

gilt, folgt daraus

```{math}
f(q) = 
f(p) + 
\sum_{i=1}^{n} \varphi_i(q)\, \underbrace{\int_{0}^1  \partial_i (f\circ \varphi^{-1})(t\cdot \varphi(q)) dt}_{:=F_i(q)}.
```

An diesem Punkt, beachten wir, dass $f\circ \varphi^{-1} \in C^\infty(\R^n)$ eine klassisch differenzierbare Funktion ist während $f$ auf der Mannigfaltigkeit $\M$. Wenden wir nun die $j$te partielle Derivation auf $f$ an, erhalten wir unter Ausnutzung der Linearität von $\partial_{x^j}^p$

```{math}
\partial_{x^j}^p (f) = 
\underbrace{\partial_{x^j}^p (f(p))}_{=0} + 
\sum_{i=1}^{n} \partial_{x^j}^p(\varphi_i \cdot F_i) = 
\sum_{i=1}^{n} \partial_{x^j}^p(\varphi_i \cdot F_i)
```

wobei wir {prf:ref}`lem:constder` und die Tatsache, dass $\varphi_i, F_i\in C^\infty(\M)$ gilt, benutzt haben. Weiterhin folgt 

```{math}
\partial_{x^j}^p(\varphi_i \cdot F_i(q)) = 
\underbrace{\partial_{x^j}^p(\varphi)}_{=\delta_{ij}} F_i(p)+ \underbrace{\varphi_i(p)}_{=0} \partial_{x^j}^p(F_i)
```

wobei wir {prf:ref}`lem:partderkron` und $\varphi(p)=0$ ausgenutzt haben. Somit folgt 

```{math}
\partial_{x^j}^p (f) = F_j(p)
```

und damit insbesondere 

```{math}
f = f(p) + \sum_{i=1}^{n} \varphi_i \partial_{x^i}^p(f).
```

Dies führt nun darauf, dass die partiellen Derivationen ein Erzeugendensystem bilden, denn sei $D\in T^{\text{alg}}_p$ beliebig, dann gilt 

```{math}
D(f) = \underbrace{D(f(p))}_{=0} + \sum_{i=1}^n \partial_{x^i}^p(f) D(\varphi_i).
```

D.h., dass jede Derivation $D$ über eine Linearkombination aus partiellen Derivationen dargestellt werden kann, wobei die Faktoren durch $D(\varphi_i)$ gegeben sind. 

Es bleibt die Eindeutigkeit zu zeigen, seien dazu Faktoren $\alpha_i$ gegeben, s.d. für jede Funktion $f\in C^\infty(\M)$ gilt

```{math}
D:= \sum_{i=1}^n \alpha_i \partial_{x^i}^p(f) = 0.
```

Erneut unter Benutzung von {prf:ref}`lem:partderkron` erhalten wir aber, dass 

```{math}
0 = D(\varphi_j) = \alpha_j 
```

für alle $j=1,\ldots,n$ und somit gilt die lineare Unabhängigkeit.

````

#### Kotangentialraum

Da wir den Tangentialraum $T^{\text{alg}}_p$ als Vektorraum identifiziert haben, können wir auch den algebraischen Dualraum betrachten.

````{prf:definition}
Es sei $\M$ eine glatte Mannigfaltigkeit, dann bezeichnen wir mit 

```{math}
T_p^\ast\M:= (T_p^{\text{alg}}\M)^\ast
```

den algebraischen Dualraum des Tangentialraums, der sogenannte **Kotangentialraum**.
````

````{prf:remark}
Ein Element $\delta\in T_p^\ast\M$ ist also eine lineare Abbildung 

```{math}
\delta: (T_p^{\text{alg}}\M)\to\R,
```

welches eine Derivation $D\in C^\infty(\M)^\ast$ auf eine reelle Zahl $\delta(D)\in\R$ abbildet.
````

Ein wichtiges Element des Kotangentialraums ist das **totale Differential**, welches für jede Funktion $f\in\C^\infty(\M)$ definiert ist durch

```{math}
df_p:(T_p^{\text{alg}}\M)\to\R\\
D\mapsto df_p(D):= D(f).
```

Insbesondere können wir $df$ mit einer Funktion $C^\infty(M)$ identifizieren, was den Zusammenhang von $T^\ast_p$ als Bidualraum von
$C^\infty(\M)$ unterstreicht.

Die Basis von $T^\ast_p$ wird kanonisch als duale Basis gewählt. Jeder Vektor $v\in T_p^{\text{alg}}\M$ hat eine eindeutige Darstellung

```{math}
v = \sum_{i=1}^n \alpha_i \partial_{x^i},
```

und wir wählen die Abbildung $dx^i\in T^\ast_p$ gerade so, dass

```{math}
(dx^i)(v) = \alpha_i
```

gilt.

````{prf:lemma}
Es sei $\M$ eine glatte Mannigfaltigkeit und $p\in\M$, dann gilt 

```{math}
\{dx^1,\ldots, dx^n\}
```

ist eine Basis von $T_p^\ast\M$.
````

````{prf:proof}
Die Aussage folgt direkt aus {prf:ref}`lem:dualeBasis`.
````

### Tangentialbündel

```{note}
Im folgenden bezeichne $T_p\M\in\{T^{\text{alg}}_p\M, T^{\text{geom}}_p\M \}$ entweder den algebraischen oder den geometrischen Tangentialraum, die konkrete Wahl wird an den entsprechenden Stellen spezifiziert.
```

Bisher haben wir für eine $n$-dimesnionale glatte Mannigfaltigkeit $\M$ für jedes einzele $p\in\M$ einen Vektorraum betrachtet, nämlich den Tangentialraum $T_p\M$, welcher wiedrum wegen {prf:ref}`thm:tanbasis` isomorph zum $\R^n$ ist. Wir interessieren uns jetzt dafür, wie sich Tangentialräume für verschiedene $p,q\in \M$ in Beziehung setzten lasse und wollen auch eine globale Struktur definieren welche alle Tangentialräume (d.h. für jedes $p\in\M$) zusammenfasst.

Hierbei spricht man nun vom **Basisraum** $B=\M$, da die Punkte $p$ welche die Vektorräume erzeugen aus diesem Raum entnommen werden. Ein erster Ansatz für eine globale Struktur ist die Vereinigung

```{math}
\bigcup_{p\in\M} T_p\M.
```

Ist z.B. als Mannigfaltigkeit der Einheitskreis $\M = \mathbb{S}^1\subset\R^2$ gegeben und wählt man als Repräsentanten für jedes $p=(\cos(\alpha), \sin(\alpha))\in\M, \alpha\in [0,2\pi)$ die Kurve $\gamma_p(t) := p - t \cdot\big(1, \frac{\cos(\alpha)}{\sin(\alpha)}\big)$ so erhalten wir anschualich die in {numref}`fig:bundleA` visualisierte Menge.

```{figure} ../img/bundlea.jpg
---
height: 300px
name: "fig:bundleA"
---
Visualisierung der Tangentialräume am Einheitskreises.
```

Es fällt auf, dass sich zwar einzelene Kurven schneiden können, die Kurven selbst und die assozierten Vektorräume alledings nicht gleich sind. Um diese Tatsache zu verdeutlichen ist es praktisch die disjunkte Vereinigung

```{math}
\bigsqcup_{p\in\M} T_p\M = \bigcup_{p\in\M} \{p\} \times T_p\M
```

zu betrachten. Für den Einheitskreis erhalten wir so den Zylinder in {numref}`fig:bundleB`.

```{figure} ../img/bundleb.jpg
---
height: 300px
name: "fig:bundleB"
---
Visualisierung der disjunkt vereinigten Tangentialräume am Einheitskreises.
```

````{prf:definition}
Es sei $\M$ eine glatte Mannigfaltigkeit, die Menge

```{math}
T\M := \bigsqcup_{p\in\M}  T_p\M = \bigcup_{p\in\M} \{p\} \times T_p\M
```

zusammen mit der Projektion 


```{math}
\pi:T\M\to \M\\
\{p\}\times T_p\M\mapsto p
```

heißt **Tangentialbündel** von $\M$.

````

Insbesondere erkenn wir, dass wir mithilfe der Projektion $\pi$ jedem Element des Tangentialbündels eindeutig den Punkt $p\in\M$ zuordnen können, der den entsprechenden Tangentialraum erzeugt hat.

````{prf:example}
<br/>

1\. Sei $\M=\R^n$, dann ist das Tangentialbündel gerade gegeben durch $T\M = \R^n\times\R^n = \R^{2n}$.

<br/>

2\. Wie bereits gesehen erhalten wir für $\M=\mathbb{S}^1$ als Tangentialbündel den unendlich hohen Zylinder $T\M = \mathbb{S}^1\times \R$.

````

In den bisher betrachten Beispielen, haben wir als Tangentialbündel jeweils eine Menge der Form $\M\times \R^n$ erhalten. Dies ist allerdings nicht immer der Fall, tatsächlich bilden diese Tangentialbündel eine spezielle Unterklasse.

````{prf:definition}
Sei $\M$ eine glatte $n$-dimesnionale Mannigfaltigkeit, das Tangentialbündel heißt **trivial**, falls 

```{math}
T\M\cong \M\times\R^n
```

gilt. In diesem Fall heißt $\M$ **parallelisierbar**.
````

````{prf:remark}
Es lässt sich zeigen, dass $\mathbb{S}^1, \mathbb{S}^3,\mathbb{S}^7$ die einzigen paralleslisierbaren Spähren sind, siehe {cite:p}`lee2003`. Die Tatsache, dass $\mathbb{S}^2$ nicht parallelsierbar ist wird beim Satz vom gekämmten Igel (??) erneut auftauchen.
````

Wir wollen nun zusätzlich charakteriseren, wie sich die Tangentialräume für unterschiedliche $p,q\in B$ zueinander verhalten, insbesondere wenn $p$ und $q$ nahe aneinander liegen. Hierbei hilft es das abstrakter Konzept eines **Vektorbündels** zu betrachten.

````{prf:definition} Vektorbündel
Es seien $\M$ der Basisraum und $E$ der Totalraum glatte Mannigfaltigkeiten und $\pi:E\to \M$ sei glatt und bijektiv. Weiterhin gelte

* für jedes $p\in \M$ sei die sogenannte **Faser** $E_p:= \pi^{-1}(p)$ ein $n$-dimensionaler Vektorraum,

* Zu jedem $p\in \M$ existiere eine offene Umgebung $U\subset \M$ und ein Diffeomorphimus $\Psi: \pi^{-1}(U)\to U\times\R^n$, s.d., 
für alle $x\in U$

```{math}
\text{pr}_U(\Psi(x)) &= \pi(x)\quad\forall x\in \pi^{-1}(U)\\
\Psi\rvert_{E_q}&: \pi^{-1}(q) \to \{q\}\times \R^n \text{ ist ein Isomorphismus, für alle }q\in U.
```

Dann heißt $(E,\M,\pi)$ **Vektorbündel** vom Rang $n$. Hierbei bezeichnet $\text{pr}_U(q, z):= q$ die Projektion auf die $U$ Komponente eines Vektors $(q,z)\in U\times\R^n$.
````

````{prf:remark} Bündel-Notation
Anstatt das Vektorbündel $(E,\M,\pi)$ als Tripel aufzuschreiben, ist es üblich von einem Bündel $E\overset{\pi}{\to}\M$ oder sogar $E\to\M$ zu sprechen. Die Abbildung $\pi$ wird im zweiten Fall nur implizit vorausgesetzt.
````

Die Funktion $\Psi$ heißt hier **lokale Trivialisierung**, denn sie erlaubt es uns den Totalraum $E$ lokal als Produktraum darzustellen. Analog zum Tangentialbündel nennen wir ein Vektorbündel **trivial**, falls eine Trivialsierung $\Psi:E\to \M\times\R^n$ existiert, s.d. also

```{math}
E \cong \M\times\R^n
```

gilt.

````{prf:example}
Möbius-Band.
````

Wir wollen nun zeigen, dass das Tangentialbündel ein Vektorbündel ist. Dazu benötigen wir zunächst die Aussage, dass $T\M$ selbst eine glatte Mannigfaltigkeit ist.

````{prf:lemma}
:label: lem:tanman

Es sei $\M$ eine glatte $n$-dimensionale Mannigfaltigkeit, dann ist das Tangentialbündel $T\M$ eine glatte $2n$-dimensionale Mannigfaltigkeit. Insbesondere ist auch 

```{math}
\pi:T\M\to \M\\
\{p\}\times T_p\M\mapsto p
```

eine glatte bijektive Abbildung.
````

````{prf:proof}
Wir werden lediglich die Idee skizzieren, für den vollständingen Beweis siehe {cite:p}`lee2003` Prposition 3.18. Wir benutzen hier die algebraische Definition des Tangentialraums.

Es sei $(U,\varphi)$ eine Karte, wir betrachten die Menge $\pi^{-1}(U)\subset T\M$ und die Abbildung 

```{math}
\psi:\pi^{-1}(U) \to \phi(U)\times \R^{n}\subset\R^{2n}\\
(p,v)\to (\varphi(p), v(\varphi))
```

wobei wir für $v\in T_p\M\subset (C^\infty(\M))^\ast$ die Notation 

```{math}
v(\varphi) := (v(\varphi_1),\ldots, v(\varphi_n))
```

benutzt haben. Es stellt sich dann heraus, dass so definierte Abbildungen $\psi$ Karten auf $T\M$ und tatsächlich auch eine Mannigfaltigkeit definieren. Insbsondere ist ein so definiertes $\psi$ ein Diffeomorphismus.
````

Mithilfe dieser Aussage können wir nun zeigen, dass $T\M$ ein Vektorbündel ist.

````{prf:lemma}
Es sei $\M$ eine glatte $n$-dimensionale Mannigfaltigkeit mit dem Tangentialraum 

```{math}
T\M:= \bigsqcup_{p\in\M}  T_p\M = \bigcup_{p\in\M} \{p\} \times T_p\M
```

und der Abbildung

```{math}
\pi:T\M\to \M\\
\{p\}\times T_p\M\mapsto p.
```

Dann ist $(T\M, \M, \pi)$ ein Vektorbündel vom Rang $n$.
````

````{prf:proof}
Es sei $(U,\varphi)$ eine Karte für $\M$, dann definieren wir die Abbildung 

```{math}
\Psi: \pi^{-1}(U)\to U\times \R^n\\
(p,v)\mapsto (p, v(\varphi)).
```

Wir erkennen sofort, dass $\Psi$ linear ist und, dass $(\text{pr}_U\circ\Psi)(p,v) = p = \pi(p,v)$ gilt. 
Da $\phi$ ein Diffeomorphismus ist, ist auch 

```{math}
\phi\times\text{Id}:U\times \R^n\to \phi(U)\times\R^n\\
(p,z)\mapsto (\phi(p), z)
```

ein Diffeomorphismus. Hier beobachten wir aber, dass 

```{math}
\big((\phi\times\text{Id})\circ \Psi\big)(p,v) = (\phi\times\text{Id})(p, v(\varphi)) = (\phi(p), v(\varphi))
```

gilt somit enstpricht $(\phi\times\text{Id})\circ \Psi$ gerade der Karte aus dem Beweis von {prf:ref}`lem:tanman` und ist somit auch ein Diffeomorphismus. Daraus folgt aber, dass $\Psi$ schon ein Diffeomorphismus sein muss.

````

### Vektorfelder

Wir führen zunächst sogenannte Schnitte auf Bündeln ein. Anschaulich abstrahieren wir hier das Konzept der Graphen von Funktionen.

Es sei $f:\M\to\R^n$ eine Funktion$, dann ist ihr Graph gegeben durch

```{math}
\{(p,f(p)): p\in\M\}\subset \M\times\R^n.
```

Hierbei sehen wir, dass $\M\times\R^n\overset{\pi}{\to}\M$ ein triviales Bündel ist mit

```{math}
\pi(p,(f(p))) = p.
```

Verallgemeinert betrachten führt diese Überlegung auf folgende Definition.

````{prf:definition}
Es sei $\M$ eine glatte Mannigfaltigkeit und $E\overset{\pi}{\to}\M$ ein Vektorbündel. Für $U\subset\M$ offen, heißt eine glatte Abbildung

```{math}
\sigma: U\to E
```

**lokaler glatter Schnitt**, falls 

```{math}
\pi(\sigma(p)) = p\quad\text{ für alle }p\in U.
```

Die Menge der glatten Schnitte auf $U$ wird mit $\Gamma(E\rvert_U)$ bezeichnet. Für $U=\M$ heißt $\sigma$ **glatter Schnitt** und wir definieren 
$\Gamma(E):=\Gamma(E\rvert_\M)$.

````

Für offenen Mengen im euklidischen kennen wir bereits den Begriff **Vektorfeld**, nämlich eine Funktion

```{math}
F:U\to\R^n
```

wobei $U\subset\R^n$ offen ist. Wir nehmen also Punkte $x\in\R^n$ und ordnen ihnen Vektoren $F(x)\in\R^n$ aus dem gleichen Raum zu. Betrachten wir statt offenen Mengen $U\subset\R^n$ nun glatte Mannigfaltigkeiten $\M$ so stellt sich a priori die Frage in welchen Raum Vektorfelder abbilden sollen. Hierbei hilft uns nun der Tangentialraum $T\M$, welcher die richtige Wahl des Zielraums darstellt. Somit können wir Vektorfelder verallgemeinern indem wir als Schnitte des Tangenialraums auffassen.

````{prf:definition}
Es sei $\M$ eine glatte Mannigfaltigkeit, ein glatter Schnitt 

```{math}
X:\M\to T\M
```

heißt glattes Vektorfeld. Das Argument von $X$ wird hierbei meist als subskript notiert, d.h., $X_p = X(p)$.
````

Für Tangentialbündel haben wir die Abbildung $\pi:T\M\to\M$ durch

```{math}
\pi(p,v):= p\quad\text{ für } (p,v)\in\{p\}\times T_p\M
```

definiert. Ist $X$ nun ein glattes Vektorfeld, so gilt

```{math}
\pi(X(p)) = p
```

und somit insbesondere $X_p\in T_p\M$. Ein Vektorfeld ordnet also jedem Punkt $p\in\M$ ein Element seines Tangentialraums zu. Falls $\M$ eine offene Menge in $\R^n$ ist, ist dies insbesondere konsistent zur bekannten Definition von Vektorfeldern.

#### Wirkung von Vektorfeldern

Von der algebraischen Definition des Tangentialraums ist das totale Differential $df_p\in T^\ast_p\M$ bekannt, welches für $D\in T^{\text{alg}}_p\M$ definiert ist durch

```{math}
df_p(D):= D(f)
```

für eine Funktion $f\in C^\infty(M)$. Mithilfe dieses Konzepts können wir die Wirkung eines Vektorfelds definieren.

````{prf:definition} Wirkung von Vektorfeldern
Es sei $\M$ eine glatte Mannigfaltigkeit und $X\in\Gamma(T\M)$, die **Wirkung** von $X$ auf $C^\infty$ ist definiert durch 

```{math}
X(\cdot):C^\infty(M)\to C^\infty(\M)\\
f\mapsto [p\mapsto X_p(f) := df_p(X)].
```
````

#### Lokale Basis von Vektorfeldern

Aus {numref}`sec:TPBasis` wissen wir bereits, dass wir für $p\in\M$ Tangentialvektoren $v\in T_p\M$ durch die Vektoren $\partial_{x^i}^p$ darstellen können. Im Kontext von Tangentialbündeln stellt sich auf natürliche Art die Frage, wie sich diese Vektoren verändern, wenn der Punkt $p$ variiert wird. Hierzu definieren wir folgende Abbildungen.

````{prf:definition}
Es sei $\M$ eine glatte $n$-dimesnionale Mannigfaltigkeit und $(U,\phi)$ eine Karte, dann definieren wir die lokalen Koordinatenfelder 
für $i=1,\ldots,n$ durch

```{math}
\partial_{x^{i}}&:\M\to T\M\\
\partial_{x^{i}}(p)&:= \partial_{x^{i}}\rvert_p
```
````

Mithilfe dieser lokalen Koordiantenfelder können wir nun Vektorfelder lokal darstellen.

````{prf:lemma}
Es sei $\M$ eine glatte Mannigfaltigkeit und $(U,\phi)$ sei eine Karte, dann gilt für $X\in\Gamma(T\M\rvert_U)$ und die Koeffizientfunktionen $X^i:=X(\phi_i)\in C^\infty(U)$ 

```{math}
X = \sum_{i=1}^n X^i \partial_{x^{i}}.
```
````

````{prf:proof}
Es sei $p\in\M$, dann haben wir wegen  {prf:ref}`thm:tanbasis` die Darstellung

```{math}
X_p = \sum_{i=1}^n X_p(\phi_i) \partial_{x^i}^p.
```

Mit der Defintion der Wirkung von Vektorfeldern folgt dann 

```{math}
X = \sum_{i=1}^n X(\phi_i) \partial_{x^i}.
```
````

Aus dieser Darstellung folgt auch, dass lokal für eine Karte $(U,\phi)$ die Wirkung auf $f\in C^\infty(U)$ geschrieben werden kann als

```{math}
X(f) := \sum_{i=1}^n X^i \frac{\partial f}{\partial_{x^i}}.
```

### Tensorfelder

Als natürliche Verallgemeinerung wollen wir nun das Konzept der Felder auf Mannigfaltigkeiten von Vektoren auf Tensoren übertragen. Hierfür benötigen wir zunächst Kotangentialbündel, welches direkt über den Kotangentialraum definiert werden kann.

````{prf:definition}
Es sei $\M$ eine glatte Mannigfaltigkeit, dann ist das **Kotangentialbündel** $((T\M)^\ast, \M, \pi^\ast)$ über die Abbildung 

```{math}
\pi^{\ast}(p):= T^\ast\M = (T\M)^\ast
```

definiert.
````

Um ein Tensorfeld definieren zu können müssen wir zunächst klären, wie das Tensorprodukt von Tangentialbündeln aussehen soll. Für zwei Vektorbündel $E\overset{\pi_E}{\to}{\M}, F\overset{\pi_F}{\to}{\M}$ wissen wir, dass für jedes $p\in\M$ die Fasern $E_p, F_p$ endlichdimensionale Vektorräume sind. Insbeonsdere können wir also das Tensorprodukt

```{math}
E_p\otimes F_p
```

betrachten und damit ein Bündel auf dem Totalraum

```{math}
E\otimes F:= \bigsqcup_{p\in\M} E_p\otimes F_p
```

betrachten. Die entsprechende Projektion $\pi_{E\otimes F}:E\otimes F\to\M$ ist gegeben durch

```{math}
\pi_{E\otimes F}^{-1}(p):= E_p\otimes F_p := (E\otimes F)_p.
```

````{prf:Lemma}
Es sei $E\overset{\pi_E}{\to}{\M}$ ein Vektorbündel vom Rang $k$ und $F\overset{\pi_F}{\to}{\M}$ ein Vektorbündel vom Rang $l$, dann ist 

```{math}
\pi_{E\otimes F}:(E\otimes F)\to \M
```

ein Vektorbündel vom Rang $kl$.
````

````{prf:proof}
Siehe Übung.
````

Die Definition des Tensorbündels lässt sich direkt auf mehrfache Tensorprodukte übertragen und führt uns direkt auf gemischte Tensorbündel.

````{prf:definition}
Es sei $\M$ eine glatte Mannigfaltigkeit und $r,s\in\N$, s.d. $r+s>0$, dann heißt 

```{math}
T^r_s\M := \bigsqcup_{p\in\M} T^r_s(T_p\M) \to \M
```

Tensorbündel der Stufe $(r,s)$. Ein **Tensorfeld** ist dann ein glatter Schnitt $A\in \Gamma(T^r_s\M)$.
````

```{danger}
Lokale Darstellung.
```

## Differentialformen

### Einsformen


## Differentialformen auf offenen Mengen

Eine Differentialform $\omega$ auf $U\subseteq\R^n$ ist eine von Ort zu Ort variierende äußere Form, deren Variation wir als glatt voraussetzen.

Wir schreiben eine allgemeine *$k$--Form* $\omega$ in der *Grundform*
```{math}
\omega = \sum_{1\leq i_1<\ldots<i_k\leq n}\omega_{i_1\ldots i_k}
dx_{i_1}\wedge\ldots\wedge dx_{i_k}\in\Omega^k(U),
```
wobei
* die $\omega_{i_1\ldots i_k}\in \Omega^0(U):=C^\infty(U,\R)$, also glatte reelle Funktionen auf $U$ sind,

* und die $dx_i$ den Koordinatenfunktionen $x_i:\R^n\to\R$ zugeordnete $1$--Differentialformen sind ($dx_i\in\Omega^1(\R^n)$).

* Den Raum der $k$--Differentialformen schreiben wir ab jetzt zur Unterscheidung vom Raum der äußeren $k$--Formen mit dem Symbol $\Omega$ statt $\Lambda$.

%
Die $dx_i$ sind durch ihre Wirkung auf ein Vektorfeld $v:U\to
\R^n$ definiert, und $dx_i(v)( y) := v_i( y)$.
$1$--Differentialformen machen also aus Vektorfeldern Funktionen, und für $k$ Vektorfelder $v^{(l)}:U\to\R^n$ ist für das $\omega$ aus der Grundform
```{math}
\omega\left(v^{(1)},\ldots,v^{(k)}\right) := \sum_{1\leq i_1<\ldots<i_k\leq n}
\omega_{i_1\ldots i_k}\cdot\det\begin{pmatrix} dx_{i_1}(v^{(1)})&\ldots& dx_{i_k}(v^{(1)})\\
\vdots&&\vdots\\
dx_{i_1}(v^{(k)})&\ldots& dx_{i_k}(v^{(k)}) \end{pmatrix}
```
definiert. Das Ergebnis ist also eine reelle Funktion auf $U$.\\
Die Rechenregeln übertragen sich von den äußeren Formen auf die Differentialformen.

Auf dem $\R$--Vektorraum
```{math}
\Omega^*(U) := \bigoplus_{k=0}^n\Omega^k(U)
```
der Differentialformen betrachten wir jetzt
den *Differentialoperator* $d$, der durch

* $df := \sum_{i=1}^n\frac{\partial f}{\partial x_i}dx_i$ für Funktionen
$f\in C^\infty(U,\R) = \Omega^0(U)$

* und $d\omega := \sum_{1\leq i_1<\ldots<i_k\leq n}d\omega_{i_1\ldots i_k}
\wedge dx_{i_1}\wedge\ldots\wedge dx_{i_k}$ für $k$--Formen \linebreak
$\omega = \sum_{1\leq i_1<\ldots<i_k\leq n}\omega_{i_1\ldots i_k}
dx_1\wedge\ldots\wedge dx_{i_k}$

definiert ist. $d$ verwandelt eine $k$--Form also in eine $(k+1)$--Form.
%
````{prf:definition}
:label: aeussere Ableitung
Die lineare Abbildung $d:\Omega^*(U)\to\Omega^*(U)$ heißt [**äußere Ableitung**](https://de.wikipedia.org/wiki/%C3%84u%C3%9Fere_Ableitung).
````
%

````{prf:example} Äußere Ableitung
:label: ex:10.14
1. Für $\omega\in\Omega^0(\R^3)$ ist $d\omega = \frac{\partial\omega}{\partial x_1}dx_1+
\frac{\partial\omega}{\partial x_2}dx_2+\frac{\partial\omega}{\partial x_3}dx_3$.

2. Für $\omega = \omega_1dx_1+\omega_2dx_2+\omega_3dx_3\in\Omega^1(\R^3)$ ist
```{math}
d\omega &=& (d\omega_1)\wedge dx_1+(d\omega_2)\wedge dx_2+(d\omega_3)\wedge
dx_3\\
&=& \left(\frac{\partial\omega_2}{\partial x_1}-\frac{\partial\omega_1}{\partial x_2}\right)
dx_1\wedge dx_2+ \left(\frac{\partial\omega_3}{\partial x_2}-\frac{\partial\omega_2}{\partial x_3}\right)
dx_2\wedge dx_3\\
&& + \left(\frac{\partial\omega_1}{\partial x_3}-\frac{\partial\omega_3}{\partial x_1}\right)
dx_3\wedge dx_1
```

3. Für $\omega = \omega_{12}dx_1\wedge dx_2+\omega_{23}dx_2\wedge dx_3
+\omega_{31}dx_3\wedge dx_1 \in\Omega^2(\R^3)$ ist
```{math}
d\omega = \left(\frac{\partial\omega_{12}}{\partial x_3} + \frac{\partial\omega_{23}}{\partial x_1}
+ \frac{\partial\omega_{31}}{\partial x_2}\right)dx_1\wedge dx_2\wedge dx_3.
```

4. Für $\omega\in\Omega^3(\R^3)$ ist $d\omega=0$.
````

%
````{prf:theorem}
:label: Antiderivation
$d$ ist eine [**Antiderivation**](https://de.wikipedia.org/wiki/Derivation_(Mathematik)#Antiderivationen), d.h. für $\alpha\in\Omega^k(U)$ und $\beta\in\Omega^l(U)$ ist
```{math}
d(\alpha\wedge\beta) = (d\alpha)\wedge\beta+(-1)^k\alpha\wedge d\beta.
```
````

````{prf:proof}
Wegen der Linearität von $d$ genügt es, diese Gleichung für Monome
```{math}
\alpha := f\underbrace{dx_{i_1}\wedge\ldots\wedge dx_{i_k}}_{\tilde
{\alpha}},\ \beta := g\underbrace{dx_{j_1}\wedge\ldots\wedge dx_{j_l}}_
{\tilde{\beta}},\ f,g\in C^\infty(U,\R)
```
zu beweisen.
Es gilt
```{math}
d(\alpha\wedge\beta) &=& d(f\cdot g)\tilde{\alpha}\wedge
\tilde{\beta} = \big((df)g+f(dg)\big)\,\tilde{\alpha}\wedge\tilde{\beta}\\
&=& (df)\tilde{\alpha}\wedge g\tilde{\beta}+ (-1)^kf\tilde{\alpha}
```
````
%
````{prf:theorem}
:label: thm:dd
Auf $\Omega^*(U)$ gilt
````

````{prf:proof}

1. Für $f\in\Omega^0(U)$ ist
```{math}
ddf &=& d\left(\sum_{i=1}^n\frac{\partial f}
{\partial x_i}dx_i\right) = \sum_{i=1}^n\sum_{l=1}^n\frac{\partial^2f}{\partial x_l\partial x_i}
dx_l\wedge dx_i\\
& =& \sum_{1\leq r< s\leq n}\left(\frac{\partial^2 f}{\partial x_r
\partial x_s} - \frac{\partial^2f}{\partial x_s\partial x_r}\right)dx_r\wedge dx_s = 0,
```
da wir wegen der Glattheit von $f$ die partiellen Ableitungen vertauschen
können.

2. Für $\omega = \sum\omega_{i_1\ldots i_k}dx_{i_1}\wedge\ldots\wedge dx_{i_k}
\in\Omega^k(U)$ ist\
```{math}
dd\omega = \sum(\underbrace{dd\omega_{i_1\ldots i_k}}_0)
\wedge dx_{i_1}\wedge\ldots\wedge dx_{i_k} = 0,
```
denn gemäß Satz {prf:ref}`Antiderivation` wird die äußere Ableitung auf die
1-Formen $d\omega_{i_1\ldots i_k}$ und $dx_{i_l}$ angewandt, und nach Teil 1.
ist das Ergebnis Null.
````

````{prf:definition}
:label: geschlossen:exakt
Eine Differentialform $v\in\Omega^*(U)$ heißt
* **geschlossen**, wenn $dv=0$, ***exakt**, wenn $v=d\psi$ für ein $\psi\in\Omega^*(U)$ gilt.

%
Nach Satz {prf:ref}`thm:dd` sind exakte Differentialformen geschlossen.\\ Für $k$--Formen auf konvexen offenen Teimengen $U\subseteq \R^n$ gilt für $k\ge 1$auch die Umkehrung (sog.
[**Poincaré-Lemma**](https://de.wikipedia.org/wiki/Poincar%c3%a9-Lemma) ),  siehe Kapitel {prf:ref}`sect:Poinca`).
%