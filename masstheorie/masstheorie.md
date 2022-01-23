# Maßtheorie

Wir wollen in diesem Kapitel formal die Maßtheorie einführen, die es uns erlaubt zu entscheiden welche Mengen messbar sind und wie sich das Volumen von Mengen in topologischen Räumen bestimmen lässt.
Die hier beschriebenen Werkzeuge werden uns im nächsten Kapitel bei der Einführung des *Lebesgue-Integrals* als Verallgemeinerung des Riemann-Integrals sehr dienlich sein.

Intuitiv ordnet ein [**Maß**](https://de.wikipedia.org/wiki/Ma%c3%9f_(Mathematik)) $\mu$, welches auf einer Menge $\Omega$ definiert ist, wie z.B. dem $\R^n$, allen geeigneten Teilmengen $A\subseteq \Omega$ nichtnegative reelle Zahlen zu, d.h.

```{math}
\mu(A)\in[0,\infty] := [0,\infty)\cup\{\infty\}.
```

Hierbei soll das Maß $\mu$ natürlich mit dem Volumen der Teilmenge $A$ zusammenhängen.
Man beachte, dass wir auch explizit unendliche Maße zulassen, z.B., falls die Menge $\Omega$ schon der gesamte $\R^n$ ist.

Bevor wir den Begriff des Maßes formal definieren können und dessen Eigenschaften näher diskutieren, müssen wir jedoch noch mehr Verständnis für die zu Grunde liegenden Mengen und Mengensystem entwickeln.

## $\sigma$-Algebren und Maße

Wir betrachten im Folgenden immer eine zu Grunde liegende Menge $\Omega$.
Diese kann endlich, abzählbar unendlich oder auch überabzählbar unendlich sein.
Wir betrachten nun die **Potenzmenge** $2^\Omega \equiv\mathcal{P}(\Omega)$ von $\Omega$, welche die Menge aller möglichen Teilmengen von $\Omega$ bildet.
Solche Mengen von Mengen nennen wir häufig *Mengensysteme*.
In der Maßtheorie sind bestimmte Mengensysteme $\mathcal{A} \subseteq \mathcal{P}(\Omega)$ zentral, nämlich die der *meßbaren* Teilmengen von $\Omega$.
Das sind die Mengen, denen ein Maß zugeordnet werden kann, also eine nichtnegative Zahl oder unendlich.

Zunächst müssen wir klären, welche Teilmengen der Grundmenge $\Omega$ überhaupt messbar sein sollen.
Am Einfachsten wäre es natürlich, alle möglichen Teilmengen messen zu können, also als Mengensystem $\mathcal{A} = \mathcal{P}(M)$ zu betrachten.
Wir wir sehen werden ist dies leider nicht immer möglich, denn es existieren *nichtmessbare Mengen*.
Es hat sich herausgestellt, dass es vernünftig ist zu fordern, dass das Mengensystem $\mathcal{A}$ eine sogenannte $\sigma$-Algebra ist, welche wir in der folgenden Definition einführen werden.

````{prf:definition} $\sigma$-Algebra und Messraum
:label: def:sigmaalgebra
Ein Mengensystem $\mathcal{A} \subseteq \mathcal{P}(\Omega)$ heißt **$\sigma$-Algebra (von $\Omega$)**, wenn die folgenden Eigenschaften erfüllt sind

1. $\Omega\in \mathcal{A}$

2. $A\in \mathcal{A} \quad \Rightarrow \quad A^c:=\Omega \setminus A\in \mathcal{A}$

3. $(A_n)_{n\in\N} \in \mathcal{A} \quad \Rightarrow \quad \bigcup_{n\in \N} A_n\in \mathcal{A}$.

Für eine $\sigma$-Algebra $\mathcal{A} \subseteq \mathcal{P}(\Omega)$ von $\Omega$ nennen wir das Paar ($\Omega,\mathcal{A}$) **Messraum** und die Mengen des Mengensystems $\mathcal{A}$ heißen **messbar**.
````

Das Symbol $\sigma$ erinnert uns an den Begriff der Summe, insbesondere wegen der dritten Eigenschaft in {prf:ref}`def:sigmaalgebra`, also der Abgeschlossenheit unter abzählbarer Vereinigung von Teilmengen.
Aus diesen drei Eigenschaften lässt sich auch direkt zeigen, dass $\sigma$-Algebren ebenfalls unter *abzählbaren Schnitten* abgeschlossen sind, wie das folgende Lemma zeigt.

````{prf:lemma} Abgeschlossenheit unter abzählbaren Schnitten
Es sei ($\Omega,\mathcal{A}$) ein Messraum und es sei $(A_n)n_\N$ eine Familie von Elementen der $\sigma$-Algebra $\mathcal{A}$ mit $A_n \in \mathcal{A}$ für $n \in \N$.
Dann sind abzählbare Schnitte dieser Mengen auch Elemente der $\sigma$-Algebra $\mathcal{A}$, d.h.,

```{math}
\bigcap_{n \in \N} A_n \in \mathcal{A}.
```
````

````{prf:proof}
In der Hausaufgabe zu zeigen.
````

Aus der {prf:ref}`def:sigmaalgebra` kann man sich leicht zwei Spezialfälle von $\sigma$-Algebren überlegen.
Es wird klar, dass das Mengensystem $\{\emptyset, \Omega\}$ die kleinstmögliche $\sigma$-Algebra bildet, wohingegen die Potenzmenge $\mathcal{P}(\Omega)$ die größtmögliche $\sigma$-Algebra darstellt.

Basierend auf dem Begriff einer $\sigma$-Algebra und eines Messraums können wir nun formal einführen, was wir mathematisch unter einem Maß verstehen.

````{prf:definition} Maß und Maßraum
:label: def:mass

Sei $(\Omega, \mathcal{A})$ ein Messraum.
Wir nennen eine Abbildung $\mu: \mathcal{A}\to [0, \infty]$ **Maß**, wenn die folgenden beiden Eigenschaften erfüllt sind.

1. Die leere Menge hat das Maß Null, d.h., $\mu(\emptyset) = 0$,

2. Für eine Familie von disjunkten Mengen $(A_n)_{n\in\N}$ der $\sigma$-Algebra $\mathcal{A}$ mit $A_i \cap A_j = \emptyset$ für $i \neq j$ gilt die sogenannte abzählbare oder $\sigma$-**Additivität**, d.h.,

```{math}
\mu\left( \bigcup_{n\in\N}A_n \right) = \sum_{n\in\N}\mu (A_n).
```

Wir nennen das Maß $\mu$ **endlich**, wenn $\mu(\Omega)<\infty$.
Das Tripel aus zu Grunde liegender Menge, $\sigma$-Algebra und Maß $(\Omega, \mathcal{A}, \mu)$ wird als **Maßraum** bezeichnet.

````

````{prf:remark}
:label: rem:wahrscheinlichkeitsmass

Maße spielen insbesondere in der *Wahrscheinlichkeitstheorie* eine zentrale Rolle.
Hier werden Sie die benötigt um die Wahrscheinlichkeit von Ereignismengen anzugeben.
Dabei wird nicht nur gefordert, dass das Maß $\mu$ endlich sein muss, sondern dass sogar $\mu(\Omega)=1$ gilt, damit es sich um ein **Wahrscheinlichkeitsmaß** handelt.
Diese finden vor allem in der Quantenmechanik Anwendung.
````

Aus den beiden grundlegenden Eigenschaften eines Maßes lassen sich weitere nützliche Eigenschaften herleiten, wie das folgende Lemma beschreibt.

````{prf:lemma} Eigenschaften von Maßen
Sei $(\Omega, \mathcal{A}, \mu)$ ein Maßraum.
Dann gelten die folgenden Eigenschaften für das Maß $\mu \colon \mathcal{A} \rightarrow [0,\infty]$.

1\. Für $A,B \in \mathcal{A}$ mit $B \subset A$ und $\mu(B) < \infty$ gilt:

```{math}
\mu(A \setminus B) = \mu(A) - \mu(B) \qquad \text{(Subtraktivität)}
```

2\. Für $A,B \in \mathcal{A}$ mit $B \subset A$ gilt:

```{math}
\mu(B) \leq \mu(A) \qquad \text{(Monotonie)}
```

3\. Für $A,B \in \mathcal{A}$ gilt stets:

```{math}
\mu(A \cup B) = \mu(A) + \mu(B) - \mu(A \cap B).
```

````

````{prf:proof}
In der Hausaufgabe zu zeigen.
````

Im Folgenden wollen wir ein paar Beispiele von geläufigen Maßen diskutieren.

````{prf:example} Maße
Wichtige Maße in der Mathematik und Physik sind beispielsweise die folgenden.

1\. Das [**Zählmaß**](https://de.wikipedia.org/wiki/Z%c3%a4hlma%c3%9f_(Ma%c3%9ftheorie)) $m$ auf einer *endlichen* Menge $M$, mit

```{math}
m(A):=|A|\qquad (A\subseteq M).
```

Hier sind insbesondere alle Teilmengen messbar, d.h., $(M, \mathcal{P}(M), m)$ bildet einen Maßraum.

2\. Das **Lebesgue--Maß** $\lambda^n$ auf dem $\R^n$, das wir bald kennen lernen, zeichnet sich dadurch aus, dass es einer verschobenen Menge das gleiche Volumen zuordnet wie einer unverschobenen.
Es besitzt also die nützliche Eigenschaft *translations-* und *rotationsinvariant* zu sein.
Dies gilt ebenfalls für Spiegelungen.
Außerdem ordnet das Lebesgue-Maß dem Einheitswürfel $[0,1]^n$ das Maß $1$ zu, was unserer Intuition entspricht.
Andererseits stellt sich heraus, dass das Lebesgue-Maß nicht auf der gesamten Potenzmenge $\mathcal{P}(\R^n)$ definiert werden kann.

3\. Das [**Dirac-Maß**](https://de.wikipedia.org/wiki/Diracma%c3%9f) $\delta_x$ ist im Punkt $x \in \R^n$ konzentriert, und für jede Teilmenge $A\subset\R^n$ gilt

```{math}
\delta_x(A) \equiv \int_A\delta_x := \begin{cases} 1, &  \text{ falls } x \in A,\\ 0, & \text{ sonst}. \end{cases}
```

Dieses Maß ist im Gegensatz zum Lebesgue-Maß nicht translationsinvariant, da es explizit von der Lage des Punkts $x\in\R^n$ abhängt.
Es wird beispielsweise in der Elektrodynamik benutzt, um eine in $x$ lokalisierte, punktförmige Ladung zu beschreiben.

4\. Häufig möchte man die Länge einer *Kurve* oder allgemeiner den Flächeninhalt einer $d$-dimensionalen Fläche im $\R^n$ messen.
Auch das dafür benutzte Maß $\mu_d$ ist translations- und rotationsinvariant, es ordnet aber der $d$-dimensionalen Einheitsfläche $[0,1]^d\times\{0\} \subset\R^d\times\R^{n-d}=\R^n$ das Maß $1$ zu.
Entsprechend hat aber für $d<n$ der Einheitswürfel das Maß $\mu_d([0,1]^n)=\infty$.

5\. Man kann sogar sogenannte [**Hausdorff-Maße**](https://de.wikipedia.org/wiki/Hausdorff-Ma%c3%9f) $\mu_d$ konstruieren, die Mengen beliebiger fraktaler Dimension $d\in[0,n]$ messen.
Genau genommen *definiert* man hierbei die Dimension der Menge $A\subset \R^n$ durch $d(A):=\inf\{d'>0\mid \mu_{d'}(A)=0\}.$

6\. Im Zusammenhang mit dem sogenannten Feynmanschen [**Pfadintegral**](https://de.wikipedia.org/wiki/Pfadintegral) der Quantenmechanik wird auf dem unendlich-dimensionalen Raum $\Omega$ der Weg zwischen zwei Punkten des Konfigurationsraumes $\R^d$ ein *Wahrscheinlichkeitsmaß* (siehe {prf:ref}`rem:wahrscheinlichkeitsmass`) definiert.
Dabei erhalten Pfade, die in der Nähe von Lösungskurven der DGL der Klassischen Mechanik sind, ein größeres Gewicht als beliebige Pfade.
````

Eine sehr nützliche Eigenschaft von gewissen Maßen auf topologischen Räumen ist die der Regularität, welche wir im Folgenden definieren wollen.

````{prf:definition} Regularität von Maßen
:label: def:regularitaet

Es sei $(\Omega, \tau)$ ein topologischer Raum und $(\Omega, \mathcal{A}, \mu)$ ein entsprechender Maßraum auf $\Omega$, so dass gilt $\tau \subset \mathcal{A}$.
Dann können wir die Regulariät des Maßes $\mu$ wie folgt definieren.

1. Wir nennen das Maß $\mu$ von **außen regulär**, wenn zu jeder messbaren Menge $A \in \mathcal{A}$ und jedem $\epsilon > 0$ eine offene Obermenge $U \in \tau$ existiert mit $A \subset U$, so dass für das Maß $\mu(U\setminus A) < \epsilon$ gilt.

2. Wir nennen das Maß $\mu$ von **innen regulär**, wenn zu jeder messbaren Menge $A \in \mathcal{A}$ und jedem $\epsilon > 0$ eine abgeschlossene Teilmenge $F \subset A$ gibt, so dass für das Maß $\mu(A\setminus F) < \epsilon$ gilt.
````

Hier noch eine Abbildung oder ein Beispiel zu Regularität?

## Borel-$\sigma$-Algebra und Borel-Maß

Da es viele unterschiedliche Möglichkeiten gibt eine Menge in Teilmengen zu unterteilen wünscht man sich eine möglichst kanonische Wahl einer $\sigma$-Algebra.
Es stellt sich heraus, dass die sogenannte Borel-$\sigma$-Algebra eine gute Wahl auf beliebigen topologischen Räumen definiert.

```{margin}
[Émile Borel](https://de.wikipedia.org/wiki/%C3%89mile_Borel) (geboren am 7. Januar 1871 in Saint-Affrique; gestorben am 3. Februar 1956 in Paris) war ein französischer Mathematiker und Politiker.
```

````{prf:definition} Borel-$\sigma$-Algebra
Die **Borel-$\sigma$-Algebra** auf einem topologischen Raum $(\Omega, \tau)$ ist die kleinste $\sigma$-Algebra auf der Menge $\Omega$, die die Topologie $\tau$ enthält, d.h.

```{math}
\B(\Omega) := \bigcap_{\substack{\mathcal{A} \text{ ist $\sigma$-Algebra}\\ \tau \subset \mathcal{A}}} \mathcal{A}
```

Man nennt die Borel-$\sigma$-Algebra auch **die von $\tau$ erzeugte $\sigma$-Algebra**.
````

Die folgende Bemerkung beschreibt die Borel-$\sigma$-Algebra, wenn als zu Grunde liegende Menge die reellen Zahlen $\R$ gewählt werden, wie es häufig in Anwendungen der Fall ist.

````{prf:remark} Borelsche $\sigma$-Algebra von $\R$
Wir untersuchen den topologischen Raum $(\R, \tau)$, wobei die Topologie $\tau$ gerade alle offenen Intervalle $(a,b) \subset \R$ mit rationalen Punkten $a,b \in \Q$ enthält.
Da dies die kanonische Topologie für die reellen Zahlen bildet sprcht man bei der von ihr erzeugten Borel-$\sigma$-Algebra als *die* Borelsche $\sigma$-Algebra.

Sie enthält alle wichtigen Teilmengen von $\R$, nämlich:

* alle *offenen, abgeschlossenen* und *kompakten* Mengen
* alle *Intervalle* der Form $(a,b), [a,b], (a,b], [a,b]$ für $a,b \in \R$, sowie alle Intervalle der Form $(-\infty, b), (-\infty, b]$ und $(a, \infty), [a,\infty)$
* alle *Punktmengen* der Form $\{a\}$ für $a \in \R$
* alle *endlichen* Teilmengen von $\R$
* alle *unendlich abzählbaren* Teilmengen von $\R$

Wir bemerken, dass die Borelsche $\sigma$-Algebra von $\R$ **nicht** alle Teilmengen von $\R$ enthält.
Es lässt sich sogar zeigen, dass die borelsche $\sigma$-Algebra von $\R$ gleichmächtig zu $\R$ ist, während die Potenzmenge $\mathcal{P}(\R)$ von $\R$ eine echt größere Mächtigkeit als $\R$ besitzt.
````

Für spezielle topologische Räume lässt sich eine wichtige Eigenschaft von Maßen über die Borel-$\sigma$-Algebra definieren.

````{prf:definition} Lokale Endlichkeit von Maßen
Sei $(\Omega, \tau)$ ein Haussdorf-Raum (siehe {prf:ref}`def:hausdorffraum`) und sei $\B(\Omega) = \sigma(\tau)$ die Borel-$\sigma$-Algebra, die durch $\tau$ erzeugt wird.
Wir nennen ein Maß $\sigma \colon \B(\Omega) \rightarrow [0, \infty]$ **lokal endlich**, falls jeder Punkt $x \in \Omega$ eine lokale Umgebung mit endlichem Maß besitzt.
````

Die lokale Endlichkeit ist essentiell bei der Untersuchung von Maßen auf topologischen Räumen, weil sie für jeden Punkt die Existenz einer Umgebung mit endlichem Maß garantiert.
Wie wir später sehen werden ist das Lebesgue-Maß auf dem Raum $\R^n$ lokal endlich.

Basierend auf der oben definierten Borel-$\sigma$-Algebra lässt sich nun das sogenannte Borel-Maß einführen.

````{prf:definition} Borel-Maß
Ein lokal endliches Maß $\sigma \colon \B(\Omega) \rightarrow [0, \infty]$ auf der Borelschen $\sigma$-Algebra eines Hausdorff-Raums $(\Omega,\tau)$ heißt **Borel-Maß**.
````

## Jordan- und Lebesgue-messbare Mengen

Bei der Einführung des Riemann Integrals verwendet man Intervalle zur Unterteilung des Definitionsbereichs.
Diese Partitionierung einer Menge lässt sich im $\R^n$ auf mehrdimensionale Quader verallgemeinern.

````{prf:definition} Mehrdimensionale Quader
:label: def:quader

Seien $a = (a_1,\ldots,a_n) \in \R^n$ und $b = (b_1,\ldots,b_n) \in \R^n$ zwei Punkte im $\R^n$.
Wir definieren zunächst folgende Anordnungsrelation mit

```{math}
a < b \qquad \Leftrightarrow \qquad a_i < b_i \quad i=1,\ldots,n.
```

Analog können wir die Anordnungsrelationen $a \leq b, a > b$ und $a \geq b$ definieren und darüber im Folgenden **offene, halboffene** und **abgeschlossene Quader** im $\R^n$ respektive beschreiben durch

```{math}
(a,b) &= \lbrace x \in \R^n : a < x < b \rbrace,\\
(a,b] &= \lbrace x \in \R^n : a < x \leq b \rbrace,\\
[a,b] &= \lbrace x \in \R^n : a \leq x \leq b \rbrace.
```

Das *Volumen* eines halboffenen Quaders $Q := (a,b] \subset \R^n$ lässt sich mittels einer Funktion $\mu^n \colon \R^n \rightarrow [0,\infty)$, den sogenannten **Lebesgue-Inhalt**, berechnen als

```{math}
\mu^n(Q) := \prod_{i=1}^n (b_i - a_i).
```

````

Es stellt sich heraus, dass die Menge der halboffenen, diskunkten Quader eine besondere mathematische Struktur bilden, nämlich einen Ring.
Diesen wollen wir zunächst definieren.

````{prf:definition} Ring
:label: def:ring

Ein Mengensystem $\mathcal{R} \subset \mathcal{P}(\Omega)$ heißt **Ring** auf einer Menge $\Omega$, falls die folgenden Eigenschaften erfüllt sind:

1. $\emptyset \in \mathcal{R}$
2. $A,B \in \mathcal{R} \Rightarrow (A \setminus B) \in \mathcal{R}$
3. $A,B \in \mathcal{R} \Rightarrow (A \cup B) \in \mathcal{R}$
````

````{prf:lemma} Der von halboffenen Quadern erzeugte Ring
Wir betrachten eine Teilmenge $\mathcal{R}$ der Potenzmenge $\mathcal{P}(\R^n)$, die durch disjunkte, halboffene Quader des $\R^n$ erzeugt wird mit

```{math}
\mathcal{R} := \left\{ \bigsqcup_{i=1,\ldots,k} Q_i \colon Q_i \text{ ist halboffener Quader im } \R^n \right\}.
```

Dann bildet das Mengensystem $\mathcal{R}$ einen Ring.
````

````{prf:proof}
Um zu zeigen, dass es sich bei dem Mengensystem $\mathcal{R}$ um einen Ring handelt müssen wir die Eigenschaften aus {prf:ref}`def:ring` nachweisen.

1\. Wir müssen zunächst zeigen, dass die leere Menge im Mengensystem $\mathcal{R}$ enthalten ist, d.h., dass gilt $\emptyset \in \mathcal{R}$.
Wählen wir hierzu einen beliebigen Punkt $a \in \R^n$, dann können wir den $n$-dimensionalen halboffenen Quader $Q_a := (a,a] \in \mathcal{R}$ betrachten.
Es ist klar, dass dieser Quader keinen Punkt aus $\R^n$ enhält (auch nicht den Punkt $a$) und somit die leere Menge beschreibt.
Daher gilt schon $\emptyset = Q_a \in \mathcal{R}$.

2\. Als nächstes müssen wir zeigen, dass für zwei Mengen $A,B \in \mathcal{R}$ gilt, dass auch die Mengendifferenz in $\mathcal{R}$ enthalten ist, d.h., dass gilt $(A \setminus B) \in \mathcal{R}$.
Da die Mengen $A$ und $B$ aus dem Mengensystem $\mathcal{R}$ stammen, existiert also eine endliche Zerlegung in disjunkte halboffene Quader der beiden Mengen mit

```{math}
A = \bigsqcup_{i=1}^k Q_i, \qquad B = \bigsqcup_{j=1}^m Q'_j.
```

Dann können wir die Mengendifferenz also schreiben als

```{math}
:label: eq:mengendifferenz
B\setminus A = \bigsqcup_{i=1}^k Q_i \setminus \bigsqcup_{j=1}^m Q'_j = \bigsqcup_{i=1}^k (\ldots((Q_i \setminus Q'_1) \setminus Q'_2)\ldots) \setminus Q'_m.
```

Um diesen Term zu vereinfachen wollen wir im Folgenden zeigen, dass die Mengendifferenz $C \setminus D$ zweier halboffener Quader $C, D \subset \R^n$ wieder eine Menge ergeben, die sich als Vereinigung disjunkter halboffenen Quader beschreiben lässt.
Hierbei können wir $3$ unterschiedliche Fälle unterscheiden:

a) Für den Fall $C \cap D = \emptyset$ ist die Behauptung trivial, da dann einfach $C \setminus D = C$ gilt und die Menge somit als Vereinigung halboffener Quader, in dem Fall nur $C$, geschrieben werden kann.

b) Ebenfalls trivial ist der Fall $C \subset D$, da hierbei gilt $C \setminus D = \emptyset$.
Wie für die erste Eigenschaft eines Rings oben gezeigt können wir die leere Menge einfach als halboffenen Quader $Q_a := (a,a]$ für einen beliebigen Punkt $a \in \R^n$ darstellen und somit gilt die Behauptung auch hier.

c) Betrachten wir nun den Fall $D \subsetneq C$. **ToDo**

d) Zuletzt diskutieren wir den Fall $C \not \subset D, D \not \subset C, C \cap D \neq \emptyset$. **ToDo**

Wir wissen also nun, dass der innerste Term $Q_i \setminus Q'_1$ in [eq:mengendifferenz] als Mengendifferenz von zwei halboffenen Quadern
Induktiv lässt sich nun zeigen, dass der Term $(\ldots((Q_i \setminus Q'_1) \setminus Q'_2)\ldots) \setminus Q'_m$ in [eq:mengendifferenz] als Vereinigung von geeigneten disjunkten halboffenen Quadern schreiben lässt mit:

```{math}
(\ldots((Q_i \setminus Q'_1) \setminus Q'_2)\ldots) \setminus Q'_m = \bigsqcup_{l=1}^{L_i} Q_l^i.
```

Und somit folgt insgesamt, dass

```{math}
A \setminus B = \bigsqcup_{i=1}^k (\ldots((Q_i \setminus Q'_1) \setminus Q'_2)\ldots) \setminus Q'_m = \bigsqcup_{i=1}^k \bigsqcup_{l=1}^{L_i} Q_l^i
```

und damit gilt offensichtlich $(A \setminus B) \in \mathcal{R}$.

3\. Zuletzt zeigen wir, dass für zwei Mengen $A,B \in \mathcal{R}$ gilt, dass auch die Vereinigung in $\mathcal{R}$ enthalten ist, d.h., dass gilt $(A \cup B) \in \mathcal{R}$.
Da $A$ und $B$ a priori nicht disjunkt sein müssen, versuchen wir die Vereinigung so umzuschreiben, dass sie aus disjunkten halboffenen Quadern besteht.
Hierzu sehen wir ein, dass gilt

```{math}
A \cup B = (A \setminus B) \sqcup B = \bigsqcup_{i=1}^k \bigsqcup_{l=1}^{L_i} Q_l^i \sqcup B.
```

Hierbei haben wir die Aussage 2\. oben benutzt, nämlich dass sich die Mengendifferenz zweier halboffener Quader als Vereinigung geeigneter halboffener disjunkter Quader schreiben lässt.
Somit erhalten wir insgesamt, dass $(A \cup B) \in \mathcal{R}$ gilt.

Damit haben wir gezeigt, dass das Mengensystem $\mathcal{R}$, welches durch disjunkte halboffene Quader im $\R^n$ erzeugt wird, einen Ring bildet.

````

### Das Jordan-Maß

Mittels der eingeführten Quader in {prf:ref}`def:quader` können wir in diesem Abschnitt formal definieren, wann Teilmengen des $\R^n$ Jordan-messbar sind.
Dazu benötigen wir zunächst eine Abbildung die einem Element $A$ des von halboffenen Quadern Rings $\mathcal{R}$ ein Volumen zuordnet.
Hierzu führen wir das sogenannte Jordan-Maß zunächst ein.

````{prf:definition} Jordan-Maß
Sei $A = \bigsqcup_{i=1}^k Q_i \in \mathcal{R}$.
Dann definieren wir das **Jordan-Maß** $\mu^n \colon \mathcal{R} \rightarrow [0,\infty)$ von $A$ als

```{math}
\mu^n(A) := \sum_{i=1}^k \mu^n(Q_i).
```

````

Im folgenden Theorem beschreiben wir die mathematischen Eigenschaften der Jordan-Maß genannten Abbildung.

````{prf:theorem} Eigenschaften des Jordan-Maßes

Das Jordan-Maß $\mu^n \colon \mathcal{R} \rightarrow [0,\infty)$ hat folgende Eigenschaften:

1\. $\mu^n(\emptyset) = 0$

2\. Seien $A_1, \ldots, A_k \in \mathcal{R}$ disjunkte Mengen.
Dann gilt:

```{math}
\mu^n \left( \bigsqcup_{i=1,\ldots,k} A_i \right) = \sum_{i=1}^k \mu^n(A_i) \qquad (\text{endliche Additivität})
```

3\. Für zwei Mengen $A, B \in \mathcal{R}$ mit $A \subset B$ gilt:

```{math}
\mu^n(A) \leq \mu^n(B) \qquad (\text{Monotonie}).
```

4\. Für zwei Mengen $A, B \in \mathcal{R}$ gilt:

```{math}
\mu^n(A \cup B) + \mu^n(A \cap B) = \mu^n(A) + \mu^n(B).
```

5\. Für beliebige Mengen $A_1, \ldots, A_k \in \mathcal{R}$ gilt:

```{math}
\mu^n\left( \bigcup_{i=1,\ldots,k} A_i\right) \leq \sum_{i=1}^k \mu^n(A_i) \qquad (\text{endliche Subadditivität}).
```

6\. Sei $(A_n)_{k\in\N}$ eine Folge von disjunkten Mengen in $\mathcal{R}$ und sei $B \in \mathcal{R}$, so dass $\bigcup_{k=1}^\infty A_k \subset B$.
Dann gilt:

```{math}
\sum_{k=1}^\infty  \mu^n(A_k) \leq \mu(B).
```

````

````{prf:proof}
S. 84-85 in Schulz-Baldes 
````

Das oben eingeführte Jordan-Maß ist die zu Grunde liegende Abbildung für das Riemann-Integral in mehreren Dimensionen.
A priori haben wir diese Abbildung nur auf Elementen des Rings $\mathcal{R}$ der halboffenen Quader definiert.
Um dieses auf beliebige Teilmengen des $\R^n$ zu erweitern benötigen wir zunächst die Definition von Jordan-messbare Mengen.

````{prf:definition} Jordan-messbare Mengen

Sei $A \subset \R^n$ eine beliebige Teilmenge.
Wir betrachten die folgenden *endlichen* Ober- und Untersummen für die Teilmenge $A$:

```{math}
O(A) &:= \inf \left\{ \sum_{i=1}^k \mu^n(Q_i) \, : \, Q_i \text{ ist halboffener disjunkter Quader}, A \subset \bigsqcup_{i=1,\ldots,k} Q_i\right\}, \\
U(A) &:= \sup \left\{ \sum_{i=1}^k \mu^n(Q_i) \, : \, Q_i \text{ ist halboffener disjunkter Quader}, \bigsqcup_{i=1,\ldots,k} Q_i \subset A\right\}.
```

Wir nennen die Teilmenge $A \subset \R^n$ **Jordan-messbar**, genau dann wenn $A$ beschränkt ist und die Ober- und Untersumme übereinstimmen, d.h., es gilt $O(A) = U(A)$.
Für Jordan-messbare Mengen $A$ ist dann das Jordan-Maß $\mu^n$ gegeben durch:

```{math}
\mu^n(A) = O(A) = U(A).
```

````

````{prf:theorem}
Seien $Q$ und $(Q_k)_{k\in\N}$ halboffene Quader mit $Q \subset \bigcup_{k=1}^\infty Q_k$.
Dann gilt

```{math}
\mu^n(Q) \leq \sum_{k=1}^\infty \mu^n(Q_k).
```

````

````{prf:proof}
S.87-S.88 in Schulz-Baldes
````

````{prf:remark}
Die Menge der Jordan-messbaren Mengen bildet keine $\sigma$-Algebra und daher ist das Jordan-Maß kein Maß im Sinne der {prf:ref}`def:mass`, sondern lediglich ein sogenanntes **Prämaß**.
Das zu Grunde liegende Problem ist, dass abzählbare unendliche Vereinigungen von Jordan-messbaren Mengen, im Gegensatz zu endlichen Vereinigungen, nicht notwendigerweise Jordan-messbar sein müssen.
Dies sieht man beispielsweise mit Hilfe der Dirichlet-Funktion in {prf:ref}`ex:dirichletFunktion` ein.
````

````{prf:example} Jordan-messbare Mengen
**ToDo:** Ein Beispiel messbar, eins nicht.
````

### Das Lebesgue-Maß

Verglichen mit der Reichhaltigkeit der Potenzmenge $\mathcal{P}(\R^n)$ sind nur relativ wenige Mengen Jordan-messbar.
Daher wollen wir in diesem Abschnitt das Jordan-Maß auf geeignete Weise erweitern.
Wir führen darum zunächst das sogenannte äußere Lebesgue-Maß ein.

````{prf:definition} Äußeres Lebesgue-Maß

Wir definieren das **äußere Lebesgue-Maß** $\mu^* \colon \mathcal{P}(\R^n) \rightarrow [0,\infty]$ einer Menge $A \subset \R^n$ als

```{math}
\mu^*(A) = \inf \left\{ \sum_{k=1}^\infty \mu^n(Q_k) : Q_k \text{ sind halboffene Quader mit } A \subset \bigcup_{k=1}^\infty Q_k \right\}.
```

````

Im folgenden Theorem beschreiben wir die mathematischen Eigenschaften des äußeren Lebesgue-Maßes.

````{prf:theorem} Eigenschaften des äußeren Lebesgue-Maßes
Das äußere Lebesgue-Maß $\mu^*$ hat folgende Eigenschaften:

1\. $\mu^*(\emptyset) = 0$

2\. Für zwei Mengen $A, B \in \R^n$ mit $A \subset B$ gilt:

```{math}
\mu^*(A) \leq \mu^*(B) \qquad (\text{Monotonie}).
```

3\. Für eine Folge $(A_k)_{k\in\N}$ von Teilmengen des $\R^n$ gilt:

```{math}
\mu^*\left( \bigcup_{k=1}^\infty A_k \right) \leq \sum_{k=1}^\infty \mu^*(A_k) \qquad (\sigma\!-\!\text{Subadditivität}).
```

4\. Für jeden halboffenen Quader $Q$ gilt:

```{math}
\mu^*(Q) = \mu^n(Q).
```

5\. Für jede Teilmenge $A \subset \R^n$ und jeden halboffenen Quader $Q$ gilt:

```{math}
\mu^*(A) = \mu^*(A \setminus Q) + \mu^*(A \cap Q).
```

````

````{prf:proof}
S.90-91 Schulz-Baldes
````

Eine besondere Eigenschaft des äußeren Lebesgue Maßes ist es, dass es *bewegungsinvariant* ist, d.h., dass es unter Translationen und Rotationen den gleichen Wert behält.
Dies ist für viele Anwendungen eine fundamentale Eigenschaft.
Die folgende Bemerkung hält die Wirkung von geometrischen Transformationen auf das äußere Lebesgue Maß fest.

````{prf:remark} Wirkung von Transformationen auf das äußere Lebesgue Maß

1\. Sei $A \subset \R^n$ eine beliebige Teilmenge und $a \in \R^n$ ein beliebiger Vektor.
Dann ist das äußere Lebesgue Maß **translationsinvariant** unter der Wirkung von $a$, d.h., es gilt

```{math}
\mu^*(A + a) = \mu^*(A).
```

Außerdem gilt, dass die Teilmenge $A$ genau dann Lebesgue-messbar ist, wenn die verschobene Teilmenge $A + a$ Lebesgue-messbar ist.

2\. Sei $A \subset \R^n$ eine beliebige Teilmenge und $M \in \R^{n\times n}$ eine beliebige Matrix.
Dann gilt für das äußere Lebesgue Maß der folgende Zusammenhang unter der Wirkung der linearen Transformation $M$

```{math}
\mu^*(MA) = |\!\operatorname{det}(M)| \, \mu^*(A).
```

Das heißt insbesondere, dass das äußere Lebesgue Maß invariant unter Transformationen der orthogonalen Gruppe (z.B. **Rotationen** und **Spiegelungen**) ist, da für diese Transformationen $|\!\operatorname{det}(M)| = 1$ gilt (siehe Kapitel 3.6 in {cite:p}`tenbrinck_2021`).

Außerdem gilt, dass die Teilmenge $A$ genau dann Lebesgue-messbar ist, wenn die linear transformierte Teilmenge $MA$ Lebesgue-messbar ist.

````

Auf Carathéodory zurückgehende Konstruktion:

````{prf:definition} Lebesgue-Maß
Wir nennen eine Teilmenge $A \subset \R^n$ **Lebesgue-messbar**, genau dann wenn für alle Teilmengen $E \subset \R^n$ gilt:

```{math}
\mu^*(E) = \mu^*(E \cap A) + \mu^*(E \setminus A).
```

Wir notieren die Menge der Lebesgue-messbaren Mengen als

```{math}
\mathcal{A} = \lbrace A \subset \R^n : A \text{ ist Lebesgue-messbar } \rbrace
```

Wir definieren das **Lebesgue-Maß** $\mu \colon \mathcal{A} \rightarrow [0,\infty]$ messbarer Mengen durch

```{math}
\mu(A) = \mu^*(A).
```

````

````{prf:definition} Lebesgue-Nullmengen
Wir nennen eine Teilmenge $N \subset \R^n$ eine **(Lebesgue-)Nullmenge**, falls ihr äußeres Lebesgue-Maß Null ist, d.h., es gilt

```{math}
\mu^*(N) = 0.
```

````

````{prf:lemma} Eigenschaften von Lebesgue-Nullmengen
:label: lem:eigenschaftenNullmengen

Für Lebesgue-Nullmengen gelten die folgenden Eigenschaften:

1\. Jede Nullmenge ist Lebesgue-messbar mit $\mu(N) = 0$.

2\. Sei $(N_n)_{n\in\N}$ eine Familie von Nullmengen.
Dann ist auch $\bigcup_{n\in\N} N_n$ eine Nullmenge.

3\. Alle abzählbare Mengen sind Nullmengen.

4\. Alle Teilmengen von Nullmengen sind Nullmengen.
````

````{prf:proof}
<br/>

1\. Für alle Teilmengen $E \subset \R^n$ gilt wegen der *Monotonie-Eigenschaft* des äußeren Lebesgue-Maßes

```{math}
\mu^*(E) \geq \mu^*(E\setminus N), \qquad \mu^*(N) \geq \mu^*(N \cap E).
```

Sei also $E \subset \R^n$ eine beliebige Teilmenge.
Da $N$ nach Voraussetzung eine Lebesgue-Nullmenge ist gilt 

```{math}
\mu^*(E) = \mu^*(E) + \mu^*(N) \geq \mu^*(E\setminus N) + \mu^*(N \cap E).
```

Andererseits können wir wegen der *$\sigma$-Subadditivität* des äußeren Lebesgue-Maßes folgende Abschätzung treffen

```{math}
\mu^*(E) = \mu^*((E\setminus N) \cup (E \cap N)) \leq \mu^*(E\setminus N) + \mu^*(E \cap N).
```

Also muss schon Gleichheit gelten, d.h., es gilt für beliebige Teilmengen $E \subset \R^n$

```{math}
\mu^*(E) = \mu^*(E\setminus N) + \mu^*(E \cap N).
```

Per Definition ist die Nullmenge $N$ also Lebesgue-messbar und es gilt $\mu(N) = \mu^*(N) = 0$.

2\. Auf Grund der *$\sigma$-Subadditivität* des äußeren Lebesgue-Maßes folgt direkt

```{math}
0 \leq \mu^* \left( \bigcup_{n\in\N} N_n \right) \leq \sum_{n\in\N} \mu^*(N_n) = 0.
```

Da $\mu^* \left( \bigcup_{n\in\N} N_n \right)$ gilt ist also $\bigcup_{n\in\N} N_n$ auch eine Nullmenge.

3\. **ToDo**

4\. **ToDo**
````

````{prf:remark} Rationale Zahlen als Nullmenge
Insbesondere die dritte Eigenschaft aus {prf:ref}`lem:eigenschaftenNullmengen` ist für uns interessant, da sie impliziert, dass die Menge der rationalen Zahlen $\Q \subset \R$ als abzählbare Menge eine Nullmenge in den reellen Zahlen darstellt.
Dies löst unser anfängliches Problem in {prf:ref}`ex:dirichletFunktion`, wie wir noch sehen werden.
````

````{prf:theorem} Lebesgue-Messbarkeit von Teilmengen im $\R^n$
:label: theorem:lebesgueOffenAbgeschlossen

Sowohl offene als auch abgeschlossene Teilmengen des $\R^n$ sind Lebesgue-messbar.
````

````{prf:proof}
S. 99 Schulz-Baldes
````

````{prf:theorem} Regularität des Lebesgue Maßes

Das Lebesgue Maß ist von außen und innen regulär im Sinne von {prf:ref}`def:regularitaet`, d.h., für jede Lebesgue-messbare Teilmenge $A \subset \R^n$ gilt

1\. für jedes $\epsilon > 0$ existiert eine offene Menge $U$ mit $A \subset U$ für die gilt $\mu(U \setminus A) < \epsilon$,

2\. für jedes $\epsilon > 0$ existiert eine abgeschlossene Menge $F$ mit $F \subset A$ für die gilt $\mu(A \setminus F) < \epsilon$.

````

````{prf:proof}
Schulz-Baldes S.101f.
````

````{prf:theorem} Charakterisierung Lebesgue-messbarer Mengen

Die folgenden drei Aussagen sind äquivalent, so dass sie eine Charakterisierung der Lebesgue-messbaren Mengen darstellen.

1\. Eine Teilmenge $A \subset \R^n$ ist Lebesgue messbar.

2\. Für jedes $\epsilon > 0$ existiert eine offene Menge $U$ und eine abgeschlossene Menge $F$, so dass $F \subset A \subset U$ und es gilt $\mu(U \setminus F) < \epsilon$.

3\. Für jedes $\epsilon > 0$ existiert eine offene Menge $U$ mit $A \subset U$ für die gilt $\mu(U \setminus A) < \epsilon$.

````

````{prf:proof}
Schulz-Baldes S.104
````

Man kann für die Borel-$\sigma$-Algebra von $\R^n$ zeigen, dass gilt

```{math}
\B(\R^n) = \sigma(\lbrace A \subset \R^n \text{ offen }\rbrace) ) = \sigma(\lbrace A \subset \R^n \text{ abgeschlossen }\rbrace)
```

Die letzte Gleichung gilt, da $\sigma$-Algebren abgeschlossen unter Komplementbildung sind.
Zusammen mit {prf:ref}`theorem:lebesgueOffenAbgeschlossen` folgt dann schon, dass die Borel-$\sigma$-Algebra $\B(\R^n)$ eine Teilmenge der Lebesgue messbaren Mengen ist.
Der folgende Satz zeigt, dass es eine echte Teilmenge ist indem er den Unterschied der Mengen als Lebesgue Nullmengen charaterisiert.

````{prf:theorem}
Eine Teilmenge $A \subset \R^n$ ist genau dann Lebesgue-messbar, wenn eine Teilmenge $B \in \B(\R^n)$ und eine Nullmenge $N \subset \R^n$ existiert, so dass $A = B \sqcup N$ ist.
````

````{prf:proof}
Schulz-Baldes S.107
````

Man könnte sich an dieser Stelle fragen, ob nicht eventuell alle Teilmengen des $\R^n$ Lebesgue-messbar sind, was einen Großteil der Theorie unnötig machen würde.
Hierzu sei folgender wichtiger **Satz von Vitali** erwähnt, der explizit nichtmessbare Mengen konstruiert.

```{margin}
[Giuseppe Vitali](https://de.wikipedia.org/wiki/Giuseppe_Vitali) (geborgen am 26. August 1875 in Ravenna; gestorben am 29. Februar 1932 in Bologna) war ein italienischer Mathematiker.
```

````{prf:theorem} Nichtmessbare Teilmengen des $\R^n$
Es sei zunächst folgende *Äquivalenzrelation* für zwei Vektoren $x, y \in \R^n$ gegeben.

```{math}
x \sim y \quad \Leftrightarrow \quad x -y \in \Q^n.
```

Die Menge aller Äquivalenzklassen $[x]_\sim$ mit 

```{math}
[x]_\sim := \lbrace y \in \R^n : x \sim y \rbrace \subset \R^n
```

bildet eine *Partition* von $\R^n$.

Mittels des [Auswahlaxiom](https://de.wikipedia.org/wiki/Auswahlaxiom) kann man nun eine sogenannte *Vitali-Menge* $V\subset [0,1]$ auswählen, die einen Repräsentanten jeder Äquivalenzklasse enthält, d.h., für jede Äquivalenzklasse $[x]_\sim$ enthält die Menge $V \cap [x]_\sim$ nur ein einziges Element.

Dann ist die Vitali-Menge $V$ nicht Lebesgue-messbar.

````

````{prf:proof}
**ToDo:** Referenz!
````
