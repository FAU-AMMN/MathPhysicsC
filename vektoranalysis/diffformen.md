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

Um den Ableitungsbegriff auf topologischen Räumen $\M$ formal definieren zu können, benötigen wir zusätzlich zur Bijektivität der Abbildung $\phi \colon U \rightarrow \phi(U) \subset \R^n$ die Bedingung, dass für jede Teilmenge $U \subset M$ gilt,

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
Allerdings existieren durchaus Beispiele, in dnen sowohl $f\circ\phi^{-1}$ als auch $f\circ\psi^{-1}$ differenzierbar sind, aber der Kartenwechsel $\psi\circ\phi^{-1}$ nicht.
Deshalb führt man zusätzlich noch den folgenden Begriff ein.

````{prf:definition} Atlas
Es sei $\M$ ein topologischer Raum.
Eine Familie von Karten $\mathcal{A} = (U_i,\phi_i)_{i\in I}$ indiziert durch die Indexmenge $I$ heißt **Atlas**, falls die Vereinigung aller offenen Mengen eine Überdeckung des topologischen Raums darstellt, d.h., es gilt

```{math}
\M = \bigcup_{i\in I} U_i.
```

Wir nennen einen Atlas $k$-mal **differenzierbar** oder von der Klasse $C^k$, falls jeder Kartenwechsel $\phi_i^{-1}\circ\phi_j, i,j\in I$ $k$-mal stetig differenzierbar ist.

````

Die Begriffe *Karte* und *Atlas* stammen in der Tat aus mathematischen Überlegungen in der Kartographie.
Man kann Teile der Erdoberfläche mit einer Karte auf eine Ebene $\R^2$ abbilden.
Nähert man sich dem Rand einer Karte, so möchte man zu einer anderen Karte wechseln, die das angrenzende Gebiet darstellt.

So kann eine Mannigfaltigkeit durch einen vollständigen Satz von Karten vollständig beschrieben werden; man braucht dabei Regeln, wie sich beim Kartenwechsel die Karten überlappen.

### Differenzierbare Mannigfaltigkeiten

Für einen topologischen Raum $\M$ können mehrere Atlanten $\mathcal{A}$ existieren, weshalb es sinnvoll ist Äquivalenzklassen von Atlanten zu betrachten.
Für eine Differenzierbarkeitsstufe $k\in \N \cup \{\infty\}$ heißen zwei differenzierbare Atlanten $\mathcal{A}_1, \mathcal{A}_2$ der Klasse $C^k$ $k$-äquivalent, falls ihre Vereinigung $\mathcal{A}_1\cup \mathcal{A}_2$ wieder ein Atlas der Klasse $C^k$ ist.
Dies bedeutet insbesondere, dass die Kartenwechsel durch die Vereinigung der beiden Atlanten weiterhin $k$-mal stetig differenzierbar bleiben.
In diesem Fall notieren wir $\mathcal{A}_1\sim_k \mathcal{A}_2$.
Die Äquivalenzklasse $[\mathcal{A}]_{\sim_k}$ nennt man eine **$C^k$-differenzierbare Struktur**.

```{margin}
[Felix Hausdorff](https://de.wikipedia.org/wiki/Felix_Hausdorff) (geboren am 8. November 1868 in Breslau; gestorben am 26. Januar 1942 in Bonn) war ein deutscher Mathematiker.
```

Bisher haben wir $\M$ als allgemeinen topologischen Raum betrachtet.
In vielen Anwendungen benötigt man aber weitere nützliche Eigenschaften des Raumes.
Insbesondere wenn man [glatte Testfunktionen](https://de.wikipedia.org/wiki/Testfunktion) und [die Zerlegung der Eins](https://en.wikipedia.org/wiki/Partition_of_unity) benutzen möchte braucht man folgende zwei zusätzliche Eigenschaften.

Wir definieren zunächst die Eigenschaft eines Hausdorff-Raums.

````{prf:definition} Hausdorff-Raum
Ein topologischer Raum $\M$ heißt **Hausdorff-Raum**, falls für je zwei unterschiedliche Punkte $x,y\in \M, x\neq y$ offene Umgebungen $U(x), U(y)$ existieren, welche disjunkt sind, d.h., $U(x)\cap U(y) = \emptyset$.
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

````{prf:definition} Differenzierbare Funktion auf Mannigfaltigkeit
Sei $\M$ eine $k$-mal differenzierbare Mannigfaltigkeit $\mathcal{A}$ ein Atlas auf $\M$.
Dann nennen wir eine Abbildung $f:\M\to\R^m$ **$k$-mal differenzierbar**, falls für jeden Punkt $x\in\M$ eine differenzierbare Karte $(U(x),\phi)\in\mathcal{A}$ existiert, so dass $f\circ\phi^{-1} \in C^k(\phi(U(x)); \R^m)$.
Insbesondere schreiben wir in diesem Fall $f\in C^k(\M; \R^m)$. 
````

Die Eigenschaft der Differenzierbarkeit einer Funktion auf einer Mannigfaltigkeit ist kartenunabhängig, wie folgendes Lemma feststellt.

````{prf:lemma}
Es sei $\M$ eine glatte Mannigfaltigkeit und $\mathcal{A}$ ein Atlas auf $\M$.
Außerdem sei $f:\M \to \R^m$ eine Funktion, $(U,\phi)\in \mathcal{A}$ eine Karte und $x \in U$ ein Punkt in der offenen Menge $U$.
Ist $f\circ\phi^{-1}$ differenzierbar in $x$, so ist $f\circ\psi^{-1}$ auch differenzierbar in $x$ für jede Karte $(V,\psi)$ mit $x\in V$.
````

````{prf:proof}
In der Hausaufgabe zu zeigen.
````

In vielen Anwendungen beschränkt man sich nur auf *glatte Mannigfaltigkeiten* und *glatte Funktionen* in $C^\infty(\M; \R^m)$.
Wir werden im Folgenden der Einfachheit-halber auch dazu übergehen.

````{prf:lemma}
Es sei $\M$ eine glatte Mannigfaltigkeit.
Dann ist $C^\infty(\M; \R^m)$ ein reeller Vektorraum mit den Verknüpfungen

```{math}
(f + g)(p) := f(p) + g(p)\quad\text{ für } f,g\in C^\infty(\M; \R^m),\\
(\lambda \cdot f)(p) := \lambda\cdot f(p)\text{ für } f\in C^\infty(\M; \R^m), \lambda\in\R.
```

````

````{prf:proof}
In der Hausaufgabe zu zeigen.
````

### Der Tangentialraum

Aus Kapitel (??) ist bereits das Konzept der Linearisierung bekannt. Anschaulich gesprochen ersetzten wir eine diffenzierbare Funktion $f$ durch eine seine Linearisierung um ein einfacheres Problem zu erhalten. Dieses Konzept soll nun auf Funktionen $f:\M\to\R$ übertragen werden, wobei $\M$ eine glatte Mannigfaltigkeit ist. Wir haben bereits erkannt, wie wir den Begriff der Differenzierbarkeit definieren, insbesondere ist dieser kartenunabhängig. Der Tatsächliche der Wert der Ableitung von Funktionen $f\cic\phi^{-1}$ hängt aber noch immer von der Wahl der Karte $\phi$ ab. Um auch hier Kartenunabhängigkeit herzustellen brauchen wir einen anderen Begriff der Differenzierbarkeit. Hierbei wird uns der sogenannte **Tangentialraum** helfen. Intuitiv ist er eine Linearisierung der Mannigfaltigkeit $M$ an einem Punkt $p\in\M$.

````{prf:example}
Mannigfaltigkeit $\R^n$.
````

Es gibt verschiedene (äquivalente) Arten den Tangentialraum konkret einzuführen.

* **Geometrischer Tangentialraum**: Hierbei behält man die geometrische Anschauung und definiert Tangentialvektoren durch Richtungsvektoren die am Punkt $p\in\M$ anliegen. Diese Definition ist intuitiv und sehr anschaulich.

* **Algebrische Defnition**: Diese Definition zieht sich auf das Konzept der Derivationen zurück. Man verliert zwar die intuitive Anschauung, allerdings ist sie sehr einfach zu formulieren und hilft in den meisten Fällen die Sachverhalte auf einfache algebraische Konzept zurückzuführen.

In der Praxis (und in vielen Büchern) werden beide Definitionen parallel verwendet, die jeweilige Interpretation geht dann aus dem Kontext hervor. Da sich die beiden Konzepte schlecht voneinander trennen lassen werden wir im folgenden den geometrischen Tangentialraum $T^{\text{geom}}_p\M$ und den algebraischen Tangentialraum $T^{\text{alg}}_p\M$ einführen eine Isomorphie

```{math}
T^{\text{geom}}_p\M\cong T^{\text{alg}}_p\M
```

zeigen.

```{danger}
In der Literatur wird diese Unterscheidung oft nicht vorgenommen, stattdessen wird der Tangentialraum $T_p\M$ genannt. Elemente dieses Raums sind dann je nach Kontext geometrisch oder algebraisch zu verstehen.
```

#### Geometrische Definition

Von der Differentiation im Mehrdimensionalen ist bereits das Konzept der **Richtungsableitung** bekannt. Für eine Funktion $F:\R^n\to\R$ betrachtet man den Strahl $\gamma(t):= x + t\,v$, wobei $x,v\in\R^n$ und den Grenzwert

```{math}
\lim_{t\to 0} \frac{F(\gamma(t)) - F(\gamma(0))}{t} = \frac{F(x + t\,v) - F(x))}{t}.
```

Wir werden diese Konzept nun auf glatte $n$-dimensionale Mannigfaltigkeiten $\M$ verallgemeinern indem wir anstatt von Strahlen, differenzierbare *Kurven* $\gamma$ betrachten. Hierbei nennen wir eine Kurve differenzierbar am Punkt $0\in(-1,1)$ falls sie stetig ist und falls eine Karte $(U,\phi)$ für $\M$ existiert, wobei $U$ eine offene Umgebung von $\phi(0)$ ist, s.d., $\phi((-\varepsilon,\varepsilon))\subset U$ und $\phi \circ \gamma:(-\varepsilon,\varepsilon)\to\R^n$ differenzierbar in $0$ ist, wobei $\varepsilon$ klein genug ist. Wir werden im Folgenden stets die Ableitung im Punkt $t=0$ betrachten und sprechen deshalb verkürzt von *differenzierbaren* Kurven. Wir bemerken insbesondere, dass die obige Definition **nicht** von der Wahl der Karte abhängt.

````{prf:example}
Es sei $\M=\S^2$ die Einheitssphäre und $u:\M\to\R$ beschreibe eine Wärmeverteilung auf der Kugeloberfläche. Betrachtet man nun die Bahn eines Partikels auf der Oberfläche beschrieben durch $\gamma:(-t, t)\to \M$ so erhalten wir eine eindimensionale Abbildung 

```{math}
f\circ\gamma:(-t,t)\to \R
```

die zu jedem Zeitpunkt die Temperatur des Ortes an welchem sich der Partikel befindet beschreibt.
````

```{figure} ../img/velocity.jpg
---
height: 450px
name: "fig:velocity"
---
ToDo.
```

````{prf:definition} Richtungsableitung
:label: def:direcdiv

Es sei $\M$ eine glatte Mannigfaltigkeit, $\gamma:(-1,1)\to\M$ eine differenzierbare Kurve mit $\gamma(0)=p\in\M$, dann nennen wir die Abbildung

```{math}
D_\gamma &: C^\infty(\M)\to\R\\
f\mapsto D_\gamma(f)&:=\frac{d}{dt}(f\circ \gamma)\big\rvert_{t=0}
```

**Richtungsableitung** von $f$ durch $\gamma$ im Punkt $p$.
````

Sei nun $\gamma$ eine differenzierbare Kurve mit $\gamma(0)=p$, dann haben wir

```{math}
\frac{d}{dt}(f\circ \gamma)\big\rvert_{t=0} = \frac{d}{dt}\big( (f\circ \phi^{-1}) (\phi \circ \gamma) \big) = 
\big(\frac{d}{dt}(f\circ \phi^{-1})\big)(\phi(p))\cdot \frac{d}{dt}(\phi \circ \gamma)\rvert_{t=0}
```

und für eine weitere differenzierbare Kurve $\tilde{\gamma}, \tilde{\gamma}(0)=p$ ebenfalls

```{math}
\frac{d}{dt}(f\circ \tilde{\gamma})\big\rvert_{t=0} = 
\big(\frac{d}{dt}(f\circ \phi^{-1})\big)(\phi(p))\cdot \frac{d}{dt}(\phi \circ \tilde{\gamma})\rvert_{t=0}.
```

Wir erkennen also, dass der Wert der Richtungsableitung in derTat von der Kurve $\gamma$ abhängt. Dies führt auf einen natürlichen Äquivalenzbegriff von Kurven.

````{prf:lemma} Tangentialvektoren
:label: lem:tang

Es sei $\M$ eine glatte $n$-dimensionale Mannigfaltigkeit, $p\in\M$ und $(U,\phi)$ eine Karte in $\M$, mit $p\in U$. Für differenzierbare Kurven $\gamma,\tilde{\gamma}:(-1,1)\to U$ mit $\gamma(0) = \tilde{\gamma}(0) = p$ ist die Relation 

```{math}
\gamma \sim_p \tilde{\gamma} 
\Leftrightarrow 
\frac{d}{dt}(\phi \circ \gamma)\rvert_{t=0} = \frac{d}{dt}(\phi \circ \tilde{\gamma})\rvert_{t=0}\in R^d
```

eine Äquivalenzrelation. Die Äquivalenzklasse $\gamma^\prime(0):=[\gamma]_{\sim_p}$ wird als **Tangentialvektor** bezeichnet. Insbesondere ist die Klasse unabhängig von der Wahl der Karte $\phi$.
````

````{prf:proof}
Siehe Übung.
````

````{prf:example}
Tangentialvektoren im $\R^n$.
````

Da wir nun Tangentialvektoren eingeführt haben, sind wir in der Lage den **Tangentialraum** zu definieren, nämlich als Raum aller Tangentialvektoren.

```{danger}
ToDo: Quotientenräume machen es hier einfacher.
```

````{prf:definition}
Es sei $\M$ eine glatte $n$-dimensionale Mannigfaltigkeit, dann heißt der Raum der (geometrischen) Tangentialvektoren  

```{math}
T_p^{\text{geom}}\M := \{\gamma^\prime(0): \gamma\text{ ist differenzierbare Kurve mit }\gamma(0)=p\}
```

**geometrischer Tangentialraum** am Punkt $p$.
````

Um eine Vektorraumstruktur zu definieren, wählen wir eine Karte $\phi$ wie in {prf:ref}`lem:tang` und definieren die Abbildung

```{math}
d\phi\rvert_p [\gamma]_{\sim_p} = d\phi\rvert_p (\gamma^\prime(0)) := (\phi \circ \gamma)^\prime (0)
```

was eine Bijektion zwischen $\R^n$ und $T_p\M$ ist. Damit erhalten wie die Operationen

```{math}
\gamma^\prime(0) +_{p} \tilde{\gamma}^\prime(0) &:=
(d\phi\rvert_p)^{-1}\big(d\phi\rvert_p(\gamma^\prime(0)) + d\phi\rvert_p(\tilde{\gamma}^\prime(0))\big)\\
\lambda \cdot_p \gamma^\prime(0) &:= (d\phi\rvert_p)^{-1} (\lambda\,d\phi\rvert_p(\gamma^\prime(0))
```

welche erneut **unabhängig** von der Wahl der Karte $\phi$ definiert sind

````{prf:lemma}
Es sei $\M$ eine glatte Mannigfaltigkeit und $p\in\M$, das Tripel $(T_p^{\text{geom}}\M, +_p, \cdot_p)$ bildet einen reellen Vektorraum.
````

#### Algebraische Definition

Es gibt eine alternativen Weg den Tangentialraum einzuführen, über sogenannte Derivationen. Hierbei beschreiben wir Tangentialvektoren nun nicht mehr direkt als Richtungsableitungen, sondern als spezielle Funktionale, welche durch ihre Wirkung auf $C^\infty(\M)$ charakterisiert sind. 

````{prf:definition}
Es sei $\M$ eine glatte Mannigfaltigkeit und $p\in\M$, eine lineare Abbildung $D:C^\infty(\M)\to \R$ heißt **Derivation** an $p$, falls die folgende Kettenregel gilt, 

```{math}
D(fg) = D(f) g(p) + f(p) D(g).
```

Der Raum der Derivationen an $p$

```{math}
T^{\text{alg}}_p\M:=\{D\in C^\infty(\M)^\ast: D\text{ ist Derivation an }p\}
```

wird als **algebraischer Tangentialraum** bezeichnet.
````

Über die Menge der Derivation erhalten wir auf natürliche Art einen Vektorraum.

````{prf:lemma}
Es sei $\M$ eine glatte Mannigfaltigkeit, dann ist $T^{\text{alg}}_p\M$ ein reeller Vektorraum.
````

````{prf:proof}
Siehe Übung.
````

Wie bereits erwähnt ist diese Definition des Tangentialraums äquivalent zu der geomtrischen Version. Konkret heißt das, dass wir eine Isomorphie

```{math}
T^{\text{alg}}_p\M\cong T^{\text{geom}}_p\M
```

erhalten. Die Identifikation lässt sich sehr einfach angeben, ist nämlich $\gamma$ eine differenzierbare Kurve, so ist durch

```{math}
D_\gamma(f):= (f\circ \gamma)^\prime(0)
```

eine Derivation an $\gamma(0)$ gegeben. Ist umgekehrt eine Derivation $D$ gegeben, so erhalten wir über

```{math}
\gamma_D(t):= \phi^{-1} (\phi(p) + t (D(\phi_1), \ldots, D(\phi_n)))
```

eine differenzierbare Kurve durch $p$. Diese Idee wird in folgendem Lemma formalisiert.

````{prf:lemma}
Es sei $\M$ eine glatte Mannigfaltigkeit und $p\in\M$. Die Abbildung 

```{math}
\Theta: T^{\text{geom}}_p\M &\to T^{\text{alg}}_p\M\\
\gamma &\to D_\gamma
```

ist ein Isomorphismus.
````

### Basis des Tangentialraums

Wir wollen eine Basis des algebraischen Tangentialraums konstruieren. Im euklidischen können wir auf natürliche Art die Koordinatenrichtungen als Kurven wählen, also Funktionen der Form

```{math}
t\mapsto t e_i
```

für $i=1,\ldots,n$ wobei $e_i$ den $i$ten Einheitsvektor in $\R^n$ bezeichnet. Wir können diese Idee auf Mannigfaltigkeiten übertragen. Dazu wählen wir eine Karte $\phi:\M\to\R^n$, wobei man hier auch von $\phi = (\phi_1,\ldots,\phi_n) =: (x^1,\ldots,x^n)$ als **lokales Koordinatensystem** spricht. So erhalten Kurven

```{math}
\gamma_{x^i}(t):= p + \phi(t e_i)
```

und darüber die Derivationen

```{math}
\partial_{x^i}:C^\infty(\M)\to\R\\
\partial_{x^i}(f) := \frac{d}{dt} (f\circ \gamma_{x^i}(t)).
```

Wir interpretieren also im Folgenden das Symbol $\partial_{x^{i}}$ als Derivation, d.h. insbesondere, als lineare Abbildung von $C^\infty(\M)$ nach $\R$.

````{prf:lemma}
Es sei $\M$ ein $n$-dimensionale glatte Mannigfaltigkeit, dann bildet die Menge $\{\partial_{x^1},\ldots,\partial_{x^n}\}$ eine Basis des Vektorraums $T^{\text{alg}}_p$. Insbesondere gilt $\dim(T^{\text{alg}}_p)=\dim(T^{\text{geom}}_p)=n$.
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
Ein Element $\delta\in T^\ast\M$ ist also eine lineare Abbildung 

```{math}
\delta: (T_p^{\text{alg}}\M)\to\R,
```

welches eine Derivation $D\in C^\infty(\M)^\ast$ auf eine reelle Zahl $\delta(D)\in\R$ abbildet.
````

Ein wichtiges Element des Kotangentialraums ist das **totale Differential**, welches für jede Funktion $f\in\C^\infty(\M)$ definiert ist durch

```{math}
df:(T_p^{\text{alg}}\M)\to\R\\
D\mapsto df(D):= D(f).
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

gilt. Wegen (Lemma duale Basis) ist dann $\{dx^1,\ldots, dx^n\}$ eine Basis von $T^\ast_p\M$.

### Tangentialbündel

Im folgenden bezeichne $T_p\M\in\{T^{\text{alg}}_p\M, T^{\text{geom}}_p\M \}$ entweder den algebraischen oder den geometrischen Tangentialraum. Wir werden die Wahl an den entsprechenden Stellen spezifizieren.
Wir haben bisher für jedes $p\in\M$ einen Vektorraum betrachtet, nämlich den Tangentialraum an $p$. Wir wollen nun eine globale Struktur betrachten die alle diese Vektorräume (d.h. für jedes $p\in\M$) zusammenfasst.

Wir haben einen sogenannten **Basisraum** $B=\M$ aus welchem wir die Punkte $p$ entnehmen und für jedes einzelne $p$ erhalten wir einen Vektorraum
$T_p\M$. Der topologischer Raum $E$ der alle diese Vektorräume enthält, nennt man in diesem Kontext **Totalraum**, er wird über die disjunkte Vereinigung

```{math}
E = T\M:= \bigsqcup_{p\in\M}  T_p\M = \bigcup_{p\in\M} \{p\} \times T_p\M
```

definiert. Der Trick bei der Definition des Totalraums das erzeugende Element an erster Stelle zu schreiben, erlaubt uns die Projektion

```{math}
\pi:T\M\to \M\\
\{p\}\times T_p\M\mapsto p
```

zu definieren. D.h. von jedem Element des Totalraums, können wir eindeutig zurück auf $\M$ projizieren. Weiterhin erkennen wir aber auch, dass für jedes $p\in\M$ der Raum $\pi^{-1}(p) = \{p\}\times T_p\M$ ein reeller $n$-dimensionaler Vektorraum ist.

Die Situation die wir so erzeugt haben, führt auf das abstrakte Konzept der **Vektorbündel**.

````{prf:definition}
Es seien $\M$ der Basisraum und $E$ der Totalraum glatte Mannigfaltigkeiten und $\pi:E\to \M$ sei glatt und bijektiv. Weiterhin gelte

* für jedes $p\in \M$ sei die sogenannte **Faser** $E_p:= \pi^{-1}(p)$ ein $n$-dimensionaler Vektorraum,

* Zu jedem $p\in \M$ existiere eine offene Umgebung $U\subset \M$ und ein Diffeomorphimus $\psi: \pi^{-1}(U)\to U\times\R^n$, s.d., 
für alle $x\in U$

```{math}
\text{pr}_U(\psi(x)) &= \pi(x)\quad\forall x\in \pi^{-1}(U)\\
\psi\rvert_{E_q}&: \pi^{-1}(q) \to \{q\}\times \R^n \text{ ist ein Isomorphismus, für alle }q\in U.
```

Dann heißt $(E,\M,\pi)$ **Vektorbündel** vom Rang $n$. Hierbei bezeichnet $\text{pr}_U(q, z):= u$ die Projektion auf die $U$ Komponente eines Vektors $(q,z)\in U\times\R^n$.
````

````{prf:remark} Bündel-Notation
Anstatt das Vektorbündel $(E,\M,\pi)$ als Tripel aufzuschreiben, ist es üblich von einem Bündel $E\overset{\pi}{\to}\M$ oder sogar $E\to\M$ zu sprechen. Die Abbildung $\pi$ wird im zweiten Fall nur implizit vorausgesetzt.
````

Die Funktion $\psi$ heißt hier **lokale Trivialisierung**, denn sie erlaubt es uns den Totalraum $E$ lokal als Produktraum darzustellen. Die Idee des Vektorbündels kommt von der Anschauung, dass wir eine Familie von Vektorräumen haben, die durch einen anderen Raum parametrisiert sind. Die Parametrisierung ist hierbei durch die Funktion $\pi^{-1}$ charakterisiert.

````{prf:example} Zylinder
Wir wählen als Basisraum den Einheitskreis $\M:=\mathbb{S}^1\subset \R^2$. Für jeden Punkt auf dem Kreis wählen wir den Vektorraum $\R$, somit betrachten wir also eine konstante Abbildung 

```{math}
\chi(p):= \R\text{ für alle }p\in \M.
```

Damit definieren wir den Totalraum 

```{math}
E := \bigsqcup_{p\in\M} \chi(p) = \bigcup_{p\in\M} \{p\}\times \R = \M\times\R
```

und die Projektion $\pi:E\to\M$

```{math}
\pi(\{p\}\times \R):= \{p\}.
```

Wir erkennen, dass man in diesem Fall die Trivialisierung $\psi:=\mathrm{Id}$ wählen kann, welche nicht nur lokal sondern global gilt. 
Vektorbündel, für welche eine lokale Trivialisierung auf ganz $\M$ existiert heißen **trivial**. 
````

Im obigen Beispiel ordnen wir jedem Punkt $p\in\mathbb{S}^1$ den Vektorraum $\{p\}\times\R$ zu. Diese Idee wurde in der Definition eines Vektorbündels verallgemeinert. Wir fordern nicht konkret, dass für jedes $q\in\M$ der Vektorraum $E_q$ gleich $\{q\}\times\R^n$ ist, allerdings fordern wir die Isomorphie $E_q\cong \{q\}\times\R^n$ gibt. A priori könnte es für jedes $q\in\M$ nun unterschiedliche Isomorphismen $\psi_q$ geben die keineswegs miteinander übereinstimmen. Deshalb kontrollieren wir zusätzlich wie unterschiedlich die Isomporphismen für verschiedene $q$ sind. Konkret fordern wir das lokal für $U\subset\M$ ein Diffeomorphismus $\phi:\pi^{-1}(U)\to U\times\R^n$ existiert.

```{note}
Die Grundidee hinter Vektorbündeln ist der Wunsch Teile des Totalraums $E$ mit Mengen $U\times\R^n$ zu identifizieren.
```

````{prf:example}
Möbius-Band.
````

````{prf:lemma}
ToDo: $T\M$ ist glatte Mannigfaltigkeit.
````

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
Relativ lang, siehe hier [Skript Uni Hamburg](https://www.math.uni-hamburg.de/home/lindemann/material/DG2020L7_slides.pdf)
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
Es sei $\M$ eine glatte Mannigfaltigkeit und $E\overset{\pi}{\to}\M$ ein Vektorbündel. Eine glatte Abbildung 

```{math}
\sigma: \M\to E
```

heißt **glatter Schnitt**, falls 

```{math}
\pi(\sigma(p)) = p\quad\text{ für alle }p\in \M.
```

Die Menge der glatten Schnitte wird mit $\gamma(E)$ bezeichnet.
````

Für offenen Mengen im euklidischen kennen wir bereits den Begriff **Vektorfeld**, nämlich eine Funktion

```{math}
F:U\to\R^n
```

wobei $U\subset\R^n$ offen ist. Wir nehmen also Punkte $x\in\R^n$ und ordnen ihnen Vektoren $F(x)\in\R^n$ aus dem gleichen Raum zu.

Betrachten wir statt offenen Mengen $U\subset\R^n$ nun glatte Mannigfaltigkeiten $\M$ so stellt sich a priori die Frage in welchen Raum Vektorfelder abbilden sollen. Hierbei hilft uns nun der Tangentialraum $T\M$, welcher die richtige Wahl des Zielraums darstellt. Somit können wir Vektorfelder verallgemeinern indem wir als Schnitte des Tangenialraums auffassen.

````{prf:definition}
Es sei $\M$ eine glatte Mannigfaltigkeit, ein glatter Schnitt 

```{math}
X:\M\to T\M
```

heißt glattes Vektorfeld.
````

Für Tangentialbündel haben wir die Abbildung $\pi:T\M\to\M$ durch

```{math}
\pi(\{p\}\times v):= p\quad\text{ für } (p,v)\in\{p\}\times T_p\M
```

definiert. Ist $X$ nun ein glattes Vektorfeld, so gilt

```{math}
\pi(X(p)) = p
```

und somit insbesondere $X(p)\in T_p\M$. Ein Vektorfeld ordnet also jedem Punkt $p\in\M$ ein Element seines Tangentialraums zu. Falls $\M$ eine offene Menge in $\R^n$ ist, ist dies insbesondere konsistent zur bekannten Definition von Vektorfeldern.

## Tensorfelder

Der Begriff **Feld** tritt in sowohl in der Physik als auch in der Mathematik auf. Anschaulich versteht man unter einem Feld die Verteilung einer Größe über den Raum. Beispielweise versteht man unter Vektorfeldern eine Funktion

```{math}
F:U\to \R^m
```

wobei $U$ eine Teilmenge des $\R^n$ ist. Das Konzept hierbei ist also, anstatt nur Vektoren $y\in\R^m$ zu betrachten, ordnet ein **Feld** jedem $x\in U$ einen Vektor $F(x)\in\R^m$ zu. Wir wollen im Folgenden die Zielmenge $\R^m$ durch Tensorräume ersetzen. Zusätzlich, schränken wir uns nur auf glatte, d.h., unendlich oft differenzierbare Funktionen ein.

````{prf:definition} Tensorfeld
Es sei $V$ ein reeller $m$-dimensionaler Vektorraum und für $r,s \in \N_0$ sei $\{\tau_i\}_{i=1}^{m^{r+s}}$ eine Basis von $T^r_s(V)$.
Für eine offenen Teilmenge $U\subset\R^n$ und Funktionen $w_{i}:U\to\R$ für $i=1,\ldots, n^{r+s}$ heißt die Abbildung 

```{math}
\mathcal{T}&:U\rightarrow T^r_s(V)\\
\mathcal{T}(x)&:= \sum_{i=1}^{n^{r+s}} w_{i}(x) \tau_i
```

**Tensorfeld**. Gilt für alle Funktionen $w_{i}\in C^k(U)$ so nennt man $\mathcal{k}$ k-mal differenzierbar.
````

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