# Laurententwicklung und Residuensatz

In diesem Abschnitt betrachten wir nun Singularitäten holomorpher Funktionen auf gelochten Kreisscheiben. Konkret betrachten wir holomorphe Funktionen $f:B_r(p)\setminus\{p\}\to\C$ und interessieren uns speziell für das Verhalten nahes des entfernten Mittelpunktes $p\in\C$.

## Singularitäten holomorpher Funktionen

In diesem Abschnitt beschäftigen wir uns mit speziell ausgezeichneten Punkten, den sogenannten Singularitäten.

````{prf:definition} Singularitäten
Sei $U \subset \C$ offen und $p\in U$ ein Punkt und $f: U \setminus \{p\}\to\C$ eine holomorphe Funktion ist, dann nennen wir den Punkt $p$ eine **isolierte Singularität** von $f$.

1. Der Punkt $p\in U$ heißt **hebbare Singularität**, falls $p$ eine isolierte Singularität ist und es eine holomorphe Funktion $g:U\to\C$ gibt, so dass $g(z) = f(z)$ gilt für alle $z \in U \setminus \{p\}$.

2. Der Punkt $p\in U$ heißt **Pol**, wenn ein $k\in\N$ existiert, s.d., $z\mapsto (z-p)^k f(z)$ eine hebbare Singularität in $p$ hat. Das kleinste $k\in\N$, das diese erfüllt heißt **Ordnung** des Pols.

3. Wir nennen den Punkt $p$ eine **wesentliche Singularität**, wenn $p$ weder hebbar noch Pol ist.
````

Intuitiv ist eine Polstelle hebbar, falls die Funktion um die Polstelle herum beschränkt ist. Dies ist die Aussage des Riemannschen Hebbarkeitssatzes.

````{prf:theorem}
:label: thm:hebbar

Es sei $U\subset \C$ offen, $p\in U$ und $f:U\setminus\{p\}\to\C$ holomorph. Falls eine Umgebung $V\subset U, p\in V$ existiert, s.d., $f$ auf $V\setminus\{p\}$ beschränkt ist, so ist $p$ eine hebbare Singularität.
````

````{prf:proof}
Wir nehmen o.B.d.A. an, dass $p=0$ gilt und betrachten die Funktion

```{math}
g(z) :=
\begin{cases}
z^2\cdot f(z)&\text{ für } z\neq 0,\\
0&\text{ für } z=0.
\end{cases}
```

Dann gilt

```{math}
\lim_{z\to 0} \frac{g(z) - g(0)}{z} = \lim_{z\to 0} z\cdot f(z) =0
```

da $f$ beschränkt in einer Umgebung um $0$ ist. Somit ist $g$ holomorph auf $U$ und lässt sich damit als Potenzreihe in der $0$ entwickeln,

```{math}
g(z) = \sum_{j=0}^\infty a_j z^j,\quad 0 = g(0) = a_0, 0=g^\prime(0)=a_1.
```

Insbesondere gilt dann für $z\in U\setminus\{0\}$

```{math}
f(z) = g(z)/z^2 = \sum_{j=2}^\infty a_j z^{j-2}
```

wobei die Reihe auf der rechten Seite eine holomorphe Funktion auf ganz $U$ definiert, daher ist $0$ eine hebbare Singularität.
````

## Laurent-Reihen

Zusätzlich zu Potenzreihen betrachtet man für Singularitäten sogenannte **Laurent-Reihen**, wobei man nicht nur Potenzen $(z-p)^j$ für $j\in \N$ betrachtet, sondern auch negative Exponenten zulässt und somit effektive rationale Funktionen $\frac{1}{(z-p)^j}$ hinzuaddiert.

```{margin} Pierre Alphonse Laurent
[Pierre Alphonse Laurent](https://de.wikipedia.org/wiki/Pierre_Alphonse_Laurent) (Geboren 18. Juli 1813 in Paris; Gestorben 2. September 1854 ebenda) war ein französischer Mathematiker.
```

````{prf:definition} Laurent-Reihen
Für eine Folge $a_j\in\C, j\in \Z$ nennen wir die Reihe

```{math}
\sum_{j=-\infty}^\infty a_j (z-p)^j
```

**Laurent-Reihe** am Entwicklungspunkt $p\in\C$. Wir nennen die Reihe konvergent, falls die Teilsummen

```{math}
\sum_{j=0}^\infty a_j (z-p)^j\qquad \sum_{j=1}^\infty a_{-j} \frac{1}{(z-p)^j}
```

konvergieren und setzten den Grenzwert als Summe der beiden einzelnen Grenzwerte.
````

Für Laurent-Reihen erhält man zwei Konvergenzradien, jeweils für die beiden Teilsummen.

````{prf:definition} Laurent Konvergenzradien
Für eine Laurent-Reihe sei $R>0$ der Konvergenzradius der Reihe

```{math}
\sum_{j=0}^\infty a_j (z-p)^j
```

und $\tilde{r}$ der Konvergenzradius der Reihe 

```{math}
\sum_{j=1}^\infty a_{-j} \frac{1}{(z-p)^j}.
```

Dann heißt $R$ **äußerer** und $\frac{1}{\tilde{r}}$ **innerer** Konvergenzradius.
````

Anstatt von Kreisscheiben betrachten wir hier nun offene Ringe

```{math}
B_{r,R}(p) := \{z\in \C: r< \abs{z-p} < R\}
```

und erhalten folgende Aussage.

````{prf:lemma}
Es sei $\sum_{j=-\infty}^\infty a_j (z-p)^j$ eine Laurent-Reihe mit äußerem Konvergenzradius $R$ und innerem Konvergenzradius $r$, dann gilt

* Die Reihe divergiert auf $\C\setminus\overline{B_{r,R}(p)},

* Die Reihe konvergiert auf $B_{r,R}(p)$,

* für $r<\tilde{r}<\tilde{R}< R$ konvergiert die Reihe gleichmäßig absolut auf $B_{\tilde{r},\tilde{R}}(p)$
````

````{prf:proof}
Folgt direkt aus {prf:ref}`lem:powerradius`
````

Analog zur Entwicklung in die Taylorreihe haben wir auf offenen Ringen eine Entwicklung in Laurent-Reihen.

````{prf:lemma} Laurent-Entwicklung
:label: lem:laurent

Es sei $f:B_{r,R}(p)\to\C$ holomorph, dann gilt

```{math}
f(z) = \sum_{j=-\infty}^\infty a_j (z-p)^j,
```

wobei die Koeffizienten für $j\in\Z$ gegeben sind durch

```{math}
a_j = \frac{1}{2\pi i} \oint_{\partial B_s(p)} \frac{f(z)}{(z-p)^{j+1}} dz \text{ für beliebiges } s\in (r,R).
```
````

````{prf:proof}
ToDo, siehe {cite:p}`neeb_2017` Satz 6.7.
````

Mithilfe der Laurent-Entwicklung auf der gelochten Kreisscheibe $B_{0,R}(p)$ können wir nun Singularitäten von holomorphen Funktionen charakterisieren.

````{prf:lemma}
Es sei $f:U\setminus\{p\}\to\C$ holomorph, $B_{0,R}(p)\subset U\setminus\{p\}$ und $a_j\in\C, j\in\Z$ seien die Koeffizienten der Laurent-Entwicklung auf $B_{0,R}$ welche nach {prf:ref}`lem:laurent` existieren. Dann gilt:

1. Die Singularität $p$ ist genau dann *hebbar*, wenn $a_{j}=0$ für alle $j<0$.

2. Die Singularität $p$ ist genau dann ein *Pol* der Ordnung $k\in\N$, $a_{-k}\neq 0$ und $a_j = 0$ für alle $j<k$.

3. Die Singularität $p$ ist genau dann *wesentlich*, falls $a_{-j}\neq 0$ für fast alle $j\in\N$.
````

````{prf:proof}
**Ad 1.**

Gilt $a_j=0$ für alle $j<0$ so ist die Laurent-Reihe

```{math}
f(z) = \sum_{0}^\infty a_j (z-p)^j,
```

holomorph von $B_{0,R}(p)$ auf $B_R(p)$ fortsetzbar und die Singularität somit hebbar.

**Ad 2.**

Ist $f(z) = \sum_{j \geq -k} a_j (z-p)^j$ mit $a_k \neq 0$, so ist

```{math}
(z-p)^k f(z) = \sum_{j \geq -k} a_j (z-p)^j+k
```

auf der Kreisscheibe $K_R(0)$ eine holomorphe Funktion und der Index $k$ ist minimal mit dieser Eigenschaft, denn für $m < k$ ist

```{math}
(z-p)^m f(z) = \sum_{j \geq -k} a_j (z-p)^{j+m} = (z-p)^{m-k} \sum_{j \geq -k} a_j (z-p)^{j+k} = (z-p)^m F(z),
```

wobei $F(p) = a_k \neq 0$ ist und $|z-p|^{m-k} \rightarrow \infty$ für $z \rightarrow p$ gilt.
Also besitzt $f$ in $p$ einen Pol der Ordnung $k$.

**Ad 3.**

In diesem Fall erhalten wir für kein $k \in \N$ eine hebbare Singularität von

```{math}
(z-p)^k f(z) = \sum_{j \geq k} a_j (z-p)^{j+k},
```

so dass die Singularität von $f$ in $p$ wesentlich ist.
````

````{prf:definition} Meromorphe Funktion
Sei $D \subset \C$ eine offene Teilmenge.
Wir nennen eine Funktion $f \colon D \rightarrow \C$ **meromorph** auf $D$ genau dann, wenn eine lokalendliche Menge $P$ existiert, so dass die Funktion $f$ holomorph auf $D \setminus P$ mit Polen in $P$ ist. 
````

````{prf:example} Meromorphe Funktionen
Rationale Funktionen oder konkretes Beispiel

Schulz-Baldes S.332

````

## Der Satz von Casorati--Weierstraß

Für wesentliche Singularitäten $p$ können wir weder einen Wert der Funktion am Punkt $p$ definieren, noch feststellen, dass die Funktion hier eindeutig gegen unendlich strebt. Tatsächlich nimmt eine Funktion um eine wesentliche Singularität herum überaschend viele verschiedene Werte an. Diese ist die Aussage des Satzes von Casorati--Weierstraß.

```{margin} Felice Casorati
[Felice Casorati](https://de.wikipedia.org/wiki/Felice_Casorati_(Mathematiker)) (Geboren 17. Dezember 1835 in Pavia; Gestorben 11. September 1890 in Casteggio) war ein italienischer Mathematiker.
```

```{margin} Karl Weierstraß
[Karl Theodor Wilhelm Weierstraß](https://de.wikipedia.org/wiki/Karl_Weierstra%C3%9F) (Geboren 31. Oktober 1815 in Ostenfelde bei Ennigerloh, Münsterland; Gestorben 19. Februar 1897 in Berlin) war ein deutscher Mathematiker.
```

````{prf:theorem} Casorati--Weierstraß
Es sei $U \subset \C$ offen und $p\in U$ eine wesentliche Singularität der holomorphen Funktion $f:U\setminus\{p\}\to\C$, dann gilt, dass $f(U\setminus\{p\})$ dicht in $\C$ liegt.
````

````{prf:proof}
Angenommen $f(U\setminus\{p\})$ wäre nicht dicht, dann existiert ein $w\in\C$ und ein $r>0$, s.d.

```{math}
B_r(w) \cap f(U\setminus\{p\}) = \emptyset.
```

Da das Bild von $f$ somit einen echten Abstand zum Punkt $p$ hat ist die Funktion

```{math}
z\mapsto\frac{1}{f(z) - w}
```

beschränkt und holomorph auf $U\setminus\{p\}$. Somit folgt mit dem Hebbarkeitssatz in {prf:ref}`thm:hebbar`, dass diese Funktion einen hebbaren Pol bei $p$ hat und somit zur holomorphen Funktion $h:U\to\C$ fortsetzbar auf $U$ ist. Diese Funktion hat keine Nullstellen 

ToDo
````

## Umlaufzahlen

Eine charakteristische Größe von Integrationswegen ist die sogenannte **Umlaufzahl**, welche beschreibt wie oft ein Weg um einen Punkt $w\in\C$ herum läuft.

````{prf:definition} Umlaufzahl
Sei $\gamma:[a,b]\to\C$ ein Integrationsweg und $w \in \C \setminus \operatorname{Bild}(\gamma)$ ein Punkt.
Dann bezeichnet

```{math}
\operatorname{Um}_\gamma(w) := 
\frac{1}{2\pi i} \oint_\gamma \frac{1}{z - w} dz
```

die **Umlaufzahl** (manchmal auch **Index**) von $\gamma$ um $w$.

````

Anschaulich möchten wir für geschlossene Wege $\gamma$ zählen, wie oft $\gamma$ um einen Punkt $w$ herumläuft.
A priori ist allerdings nicht klar, dass die Umlaufzahl tatsächlich ganzzahlig ist.
Dafür erhalten wir zunächst das folgende Resultat.

````{prf:lemma} Ganzzahligkeit der Umlaufzahl
Für $r>0$, $w\in\C \setminus \operatorname{Bild}(\gamma)$ ein Punkt, und $k\in\Z$ eine ganze Zahl.
Sei außerdem ein Weg $\gamma_{r,k}:[0,2\pi]\to\C$ gegeben durch
```{math}
\gamma_{r,k}(t) := w + r \exp(ikt).
```

Dann gilt

```{math}
\operatorname{Um}_{\gamma_{r,k}}(w) = k.
```
````

````{prf:proof}
Wir berechnen explizit

```{math}
\operatorname{Um}_{\gamma_{r,k}}(w) &:= 
\frac{1}{2\pi i} \oint_{\gamma_{r,k}} \frac{1}{z - w} dz\\ 
&=
\frac{1}{2\pi i} \oint_{\gamma_{r,k}} \frac{r k \exp(ikt)}{r \exp(ikt)} dz\\
&= k,
```

was die Behauptung zeigt.
````

**ToDo: Abbildung mit Beispiel von [Wikipedia](https://de.wikipedia.org/wiki/Umlaufzahl_(Mathematik))**

Wir wissen bereits aus dem Homotopiesatz in {prf:ref}``, dass homotope Wege die gleiche Umlaufzahl liefern.
Bisher wissen wir jedoch nicht, dass alle Wege zu einem Weg der Gestalt $\gamma_{r,k}$ homotop sind.
Der folgende Satz liefert uns diese Aussage.

````{prf:theorem}
Sei $\gamma \colon [a,b] \rightarrow \C \setminus \{w\}$ ein geschlossenen Integrationsweg und $w \in \C$ ein Punkt.
Dann gilt $\operatorname{Um}_\gamma(w) \in \Z$.
Sind außerdem $\gamma_0, \gamma_1 \colon [a,b] \rightarrow \C \setminus \{w\}$ zwei geschlossene Integrationswege und $\gamma_0(a) = \gamma_1(a)$, so sind die beiden Integrationswege genau dann homotop, wenn ihre Umlaufzahlen übereinstimmen, d.h.,

```{math}
\operatorname{Um}_{\gamma_0}(w) = \operatorname{Um}_{\gamma_1}(w)$ 
```

````

````{prf:proof}
Sei also $\gamma \colon [a,b] \rightarrow \C \setminus \{w\}$ ein geschlossener Integrationsweg und sei $\gamma(a) = z_0 \in \C$.
Für die Funktion

```{math}
\eta &\colon [a,b] \rightarrow \C, \\
\eta(t) &:= \int_{\gamma|_{[a,t]}} \frac{\mathrm{d}z}{z-w} = \int_a^t \frac{\gamma'(s)}{\gamma(s) - w} \mathrm{d}s 
```

gilt dann nach dem Hauptsatz der Integral- und Differentialrechnung $\eta'(t) = \frac{\gamma'(t)}{\gamma(t)-w}$ für jedes $t$ in dem $\gamma$ differenzierbar ist.
Damit erhalten wir

```{math}
\frac{\mathrm{d}}{\mathrm{d}t} \left( (\gamma(t) - w)\exp^{-\eta(t)}\right) &= \gamma'(t)\exp^{-\eta(t)} + (\gamma(t) - w)\exp^{-\eta(t)}(-\eta'(t))\\
&= \gamma'(t)\exp^{-\gamma(t)} - \gamma'(t)\exp^{-\eta(t)}\\
&= 0.
```

Da offensichtlich $\eta(a) = 0$ gilt erhalten wir

```{math}
(\gamma(t) - w)\exp^{-\gamma(t)} = (\gamma(a) - w)\exp^{-\eta(a)} = \gamma(a) - w = z_0 - w,
```

so dass gilt

```{math}
\gamma(t) = w + \exp^{\gamma(t)}(z_0 - w) \quad \text{ für } \quad a \leq t \leq b.
```

Für $t = b$ erhalten wir insbesondere aus $\gamma(a) = \gamma(b) = z_0$ die Beziehung $\exp^{\gamma(b)} = 1$.
Andererseits gilt aber $\eta(b) = 2\pi i \operatorname{Um}_\gamma(w)$ und somit folgt schon $\operatorname{Um}_\gamma(w) \in \Z$.

Seien also nun $\gamma_0, \gamma_1 \colon [a,b] \rightarrow \C \setminus \{w\}$ geschlossene Integrationswege mit dem gleichen Anfangspunkt $z_0 \in C$.
Wir definieren zwei Funktionen $\eta_0, \eta_1 : [a,b] \rightarrow \C$ analog wie oben.
Diese Funktionen sind stückweise stetig differenzierbare Kurven mit

```{math}
\gamma_0(a) = \gamma_1(a) = 0 \quad \text{ und } \quad \eta_0(b) = 2 \pi i \operatorname{Um}_{\gamma_1}(w) = 2 \pi i \operatorname{Um}_{\gamma_2}(w) = \eta_1(b).
```

Sei nun

```{math}
h(s,t) := s \eta_1(t) + (1-s) \eta_0(t)
```

eine Homotopie von $\eta_0$ nach $\eta_1$ mit festen Endpunkten.
Also ist

```{math}
H(s,t) := w + \exp^{h(s,t)}(z_0 - w)
```

eine Homotopie von $\gamma_0$ nach $\gamma_1$ mit festen Endpunkten.

````

Aus der Einsicht, dass jede Umlaufzahl ganzzahlig ist, stellt sich die Frage, wie diese Umlaufzahl von der Wahl des Punktes abhängt.
Dies beantwortet uns das folgene Korollar.

````{prf:corollary}
Sei $\gamma \colon [a,b] \rightarrow \C$ ein geschlossener Weg.
Dann ist die Menge $U := \C \setminus \operatorname{Bild}(\gamma)$ offen und $\operatorname{Um}_\gamma \colon U \rightarrow \Z$ ist eine Funktion, die *konstant* auf jeder Zusammenhangskomponente von $U$ ist.

Außerdem existiert ein Radius $R > 0$, so dass für die Kreisscheibe $K_{>R}(0)$ gilt

```{math}
K_{>R}(0) := \lbrace z \in \C : |z| > R \rbrace \subset U
```

und es gilt $\operatorname{Um}_\gamma(w) = 0$ für alle $w \in \K_{>R}(0)$.

````

````{prf:proof}
Aus der Formel

```{math}
\operatorname{Um}_\gamma(w) = \frac{1}{2 \pi i} \oint_\gamma \frac{1}{z-w} \mathrm{d}z = \frac{1}{2 \pi i} \int_a^b \frac{\gamma'(t)}{\gamma(t) - w} \mathrm{d}t
```

und aus der Stetigkeit des Integranden als Funktion von $(t,w)$ in der Menge $[a,b] \times U$ folgt die Stetigkeit der Funktion $\operatorname{Um}_\gamma$.
Da die Funktion $\operatorname{Um}_\gamma$ Werte in $\Z$ annimmt, muss sie auf jeder Zusammenhangskomponente von $U$ konstant sein.
Andererseits gilt für die Länge $L(\gamma) = \int_a^b |\gamma'(t)| \mathrm{d}t$ die Abschätzung

```{math}
\left| \int_a^b \frac{\gamma'(t)}{\gamma(t)-w} \mathrm{d}t \right| \leq \int_a^b \frac{|\gamma'(t)|}{|\gamma(t) - w|} \mathrm{d}t \leq \int_a^b \frac{|\gamma'(t)|}{|w| - R} \mathrm{d}t = \frac{1}{|w| - R} L(\gamma). 
```

Hieraus folgt schon $\lim_{w \rightarrow \infty} \operatorname{Um}_\gamma(w) = 0$, also ist $\operatorname{Um}_\gamma(w) = 0$ für alle Punkte $w \in \C$ mit $|w| > R$.


````

**ToDo: Abbildung hier zu Korollar - S.51 in Neeb**

## Cauchyscher Residuensatz

In diesem letzten Abschnitt zur Funktionentheorie widmen wir uns einem der zentralen Aussagen der Funktionentheorie - den *Cauchyschen Residuensatz*.
Er erlaubt es die Berechnung von Kurvenintegralen auf eine wesentlich einfachere Berechnung von Umlaufzahlen und sogenannten Residuen zu reduzieren, was für viele Anwendungen in der Physik sehr praktisch ist.

Wir beginnen zunächst mit der Einführung des Begriffs des Residuums einer Laurententwicklung.

````{prf:definition} Residuum
Sei $U \subset \C$ eine offene Menge, $p \in U$ ein Punkt und $f \colon U \setminus \{p\} \rightarrow \C$ eine holomorphe Funktion.
Sei außerdem

```{math}
f(z) = \sum_{j=-\infty}^\infty a_j (z-p)^j
```

die Laurententwicklung von $f$ bei der isolierten Singularität $p$.

Dann nennen wir

```{math}
\operatorname{Res}_p f := a_{-1}
```

das **Residuum$ von $f$ bei $p$.
````

Das folgende Lemma erlaubt die explizite Berechnung des Residuums.

````{prf:lemma} Berechnung des Residuums

Sei $U \subset \C$ eine offene Teilmenge und $p \in U$ Pol einer holomorphen Funktion $f \colon U \setminus \{p\} \rightarrow \C$.

Für genügend kleine $\epsilon > 0$ lässt sich das Residuum von $f$ bei $p$ angeben als

```{math}
\operatorname{Res}_{p}(f) = \oint_{\partial B_\epsilon(p)} f(z) \frac{\mathrm{d}z}{2\pi i}.
```

Falls der Pol von Ordnung $-m$ ist, lässt sich das Residuum von $f$ bei $p$ sogar angeben als

```{math}
\operatorname{Res}_{p}(f) = \partial_z^{m-1}\left( (z-p)^m \frac{f(z)}{(m-1)!}\right)|_{z=p}.
```

````

````{prf:proof}
Schulz-Baldes S.333f.
````

````{prf:example} Berechnung des Residuums
Rationale Funktion bei Schulz-Baldes S.335
````

Der folgende Residuensatz von Cauchy stellt eine der zentralen Aussagen der Funktionentheorie dar.
Er erlaubt es uns Kurvenintegrale mit Hilfe der Umlaufzahl und des Residuums zu berechnen, was sich als sehr nützlich herausstellt.

````{prf:theorem} Cauchyscher Residuensatz
Sei $U \subset \C$ eine offene Teilmenge und $f \colon U \rightarrow \C$ eine meromorphe Funktion mit endlicher Menge $P \subset U$ von Polstellen.
Sei außerdem $\gamma$ ein geschlossener und zusammenziehbarer Weg in $U$ mit $\operatorname{Bild}(\gamma) \cap P = \emptyset$.

Dann gilt der folgende Zusammenhang

```{math}
\int_\gamma f(z) \frac{\mathrm{d}z}{2\pi i} = \sum_{p \in P} \operatorname{Um}_\gamma(p) \operatorname{Res}_{p}(f).
```
````

````{prf:proof}
Sei $p \in P$ und $f(z) = \sum_{n=-\infty}^\infty a_n(z-p)^n$ die Laurent-Entwicklung von $f$ um $p$.
Dann ist

```{math}
h_p(z) := \sum_{n \leq -2} a_n(z-p)^n
```

eine auf $\C \setminus \{p\}$ holomorphe Funktion mit Stammfunktion

```{math}
H(z) := \sum_{n \leq -2} \frac{a_n}{n+1} (z-p)^{n+1}$.
```

Also verschwindet jedes Integral $\int_\delta h_p(z)$ für jeden geschlossenen Weg $\delta$ in $\C \setminus \{p\}$.
Die Funktion 

```{math}
F(z) := f(z) - \sum_{p\in P} h_p(z) - \sum_{p\in P} \frac{\operatorname{Res}_p f}{z-p}
```

hat nun in allen $p \in P$ hebbare Singularitäten und ist somit holomorph auf $U$.
Nach dem Integralsatz von Cauchy in {prf:ref}`` gilt schließlich

```{math}
0 &= \int_\gamma \left( f(z) - \sum_{p \in P} h_p(z) - \sum_{p\in P} \frac{\operatorname{Res}_p f}{z-p} \right) \mathrm{d}z\\
&= \int_\gamma f(z) \mathrm{d}z - \sum_{p \in P} \operatorname{Res}_p f \cdot \int_\gamma \frac{1}{z-p} \mathrm{d}z\\
&= \int_\gamma f(z) \mathrm{d}z - 2\pi i \sum_{p\in P} \operatorname{Res}_p f \cdot \operatorname{Um}_\gamma(p).
```

````

````{prf:remark}
Für holomorphe Funktionen $f$ entspricht der Residuensatz gerade dem Cauchyschen Integralsatz.
Wenn $D$ als Sterngebiet angenommen wird ist die Zusammenziehbarkeit des Wegs $\gamma$ immer erfüllt. 
````

````{prf:example}
Viele konkrete Beispiele in Schulz-Baldes S.338-344
oder zu uneigentlichen Integralen in Neeb S. 53f.
````
