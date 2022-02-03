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
Es sei ($\Omega,\mathcal{A}$) ein Messraum und es sei $(A_n)_{n\in_\N}$ eine Familie von Elementen der $\sigma$-Algebra $\mathcal{A}$ mit $A_n \in \mathcal{A}$ für $n \in \N$.
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

## Borel-Maße

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

## Das Lebesgue Maß

```{margin} Henri Lebesgue
[Henri Léon Lebesgue](https://en.wikipedia.org/wiki/Henri_Lebesgue) (Geboren 28. Juni 1875 in Beauvais; Gestorben 26. Juli 1941 in Paris) war ein französischer Mathematiker.
```

Bei der Einführung des Riemann Integrals verwendet man Intervalle zur Unterteilung des Definitionsbereichs.
Diese Partitionierung einer Menge lässt sich im $\R^n$ auf mehrdimensionale Quader verallgemeinern. Für $a = (a_1,\ldots,a_n) \in \R^n$ und $b = (b_1,\ldots,b_n) \in \R^n$ verwenden wir hierbei die Anordnungsrelation

```{math}
a < b \qquad \Leftrightarrow \qquad a_i < b_i \quad i=1,\ldots,n
```

und analog für $a \leq b, a > b$ und $a \geq b$.

````{prf:definition} Mehrdimensionale Quader
:label: def:quader

 und darüber im Folgenden **offene, halboffene** und **abgeschlossene Quader** im $\R^n$ respektive beschreiben durch

```{math}
(a,b) &= \lbrace x \in \R^n : a < x < b \rbrace,\\
(a,b] &= \lbrace x \in \R^n : a < x \leq b \rbrace,\\
[a,b] &= \lbrace x \in \R^n : a \leq x \leq b \rbrace.
```

Das **Volumen** bzw. der Lebesgue-Inhalt eines halboffenen Quaders $Q := (a,b] \subset \R^n$ definieren wir über

```{math}
\lambda^n(Q) := \prod_{i=1}^n (b_i - a_i).
```
````

Wir wollen im Folgenden das Teilmengensystem $\mathcal{R}_{\text{Q}}\subset\ 2^{\R^n}$ aller halboffenen Quader betrachten,

```{math}
\mathcal{R}_{\text{Q}} := \left\{ \bigsqcup_{i=1,\ldots,k} Q_i \colon Q_i \text{ ist halboffener Quader im } \R^n \right\}.
```

Wir fordern hierbei nicht, dass nur disjunkte Quader vereinigt werden dürfen. Jedoch kann man direkt herleiten, dass man jede Vereinigung von Quadern in eine disjunkte Umschreiben kann. Seien dazu $Q_1,\ldots,Q_k\subset\R^n$ halboffene Quader, wir erkennen, dass der Rand eines Quaders $Q_i=(a^i,b^i]$ genau $2n$ Hyperebenen der Form

```{math}
x_j = a^i_j\\
x_j = b^i_j
```

für $j=1,\ldots,n$ aufspannt. Weiterhin, können wir einen anderen Quader $Q_m=(a^k,b^k)$ mit einer Hyperebene $x_l=c\in\R$ zerteilen, im Falle $a^k_l < c < b^k_l$, indem wir zwei neue Quader definieren mit

```{math}
\alpha^m&:=(a^m_1,\ldots,c,\ldots,a^m_n)\\
\beta^m&:=(b^m_1,\ldots,c,\ldots,b^m_n)\\
Q_m^1&=(a^m,\beta^m]\\
Q_m^2&=(\alpha^m,b^m].
```

Iterativ gehen wir folgendermaßen vor:

1. Betrachte den ersten Quader $Q_1$, zerteile alle Quader $Q_i$ an allen seinen Hyperebenen und erhalte so neue Quader $W^1_j$.

2. Im $i+1$ten Schritt betrachte die Hyperebenen des Quaders $Q_{i+1}$ und zerteile damit alle Quader $W^i_j$ aus dem vorherigen Schritt und erhalte damit neue Quader $W^{i+1}_j$.

Führen wir diesen Prozess bis $i=k$ durch, so erhalten wir folgendes Resultat, welches in {numref}`fig:disrect` visualisiert ist.

```{figure} ../img/DisRect.jpg
---
width: 400px
name: "fig:disrect"
---

Nicht disjunkte Quader werden in System disjunkter Quader überführt. Man erkennt insbesondere, dass die Vereinigung gleich bleibt und, dass sich jeder einzelne ursprüngliche Quader, aus den neuen Quadern zusammensetzbar ist. 
```

````{prf:lemma}
:label: lem:disRect

Es seien $Q_1,\ldots,Q_k\subset\R^d$ halboffene Quader, dann existieren paarweise disjunkte halboffene Quader $W_1,\ldots, W_M$ mit Indexmengen $J_i\subset\{1,\ldots,M\}$, s.d. 

```{math}
\bigcup_{i=1}^k Q_i = \bigcup_{j=^1}^M W_j
```

und für jedes $i\in\{1,\ldots,n\}$ gilt

```{math}
\bigcup_{j\in J_i} W_j = Q_i.
```
````

Das System der halboffenen Quadern bildet eine besondere mathematische Struktur, einen sogenannten Mengen-Ring.

````{prf:definition} Ring
:label: def:ring

Ein Mengensystem $\mathcal{R} \subset 2^{\Omega}$ heißt **Mengen-Ring** (im maßtheoretischen Sinne) auf einer Menge $\Omega$, falls die folgenden Eigenschaften erfüllt sind:

1. $\emptyset \in \mathcal{R}$
2. $A,B \in \mathcal{R} \Rightarrow (A \setminus B) \in \mathcal{R}$
3. $A,B \in \mathcal{R} \Rightarrow (A \cup B) \in \mathcal{R}$
````

````{prf:lemma} Der von halboffenen Quadern erzeugte Ring
Das System der halboffenen Quadern $\mathcal{R}_{\text{Q}}$ bildet einen Mengenring.
````

````{prf:proof}
Um zu zeigen, dass es sich bei dem Mengensystem $\mathcal{R}_{\text{Q}}$ um einen Ring handelt müssen wir die Eigenschaften aus {prf:ref}`def:ring` nachweisen.

1\. Für einen beliebigen Punkt $a \in \R^n$ gilt $\emptyset = (a,a] \in \mathcal{R}_{\text{Q}}$.

2\. Als nächstes müssen wir zeigen, dass für zwei Mengen $A,B \in \mathcal{R}_{\text{Q}}$ gilt, dass auch die Mengendifferenz in $\mathcal{R}_{\text{Q}}$ enthalten ist, d.h., dass gilt $(A \setminus B) \in \mathcal{R}_{\text{Q}}$. Nach {prf:ref}``disRect` existieren paarweise disjunkte halboffene Quader $S_j$, $j=1,\ldots,n$, und Indexmengen $I_A,I_B\subset\{1,\ldots,n\}$, s.d., 

```{math}
A = \bigcup_{j\in I_A} S_j\\
B = \bigcup_{j\in I_B} S_j.
```

Somit gilt dann 

```{math}
A\setminus B &= \left(\bigcup_{j\in I_A} S_j\right) \setminus \left(\bigcup_{j\in I_B} S_j\right)\\ 
&= \bigcup_{j\in I_A\setminus I_B} S_j
```

was wieder eine Vereinigung von halboffenen Quadern ist und deshalb gilt $A\setminus B\in \mathcal{R}_{\text{Q}}$.

3\. Zuletzt erkennen wir für zwei Mengen $A,B \in \mathcal{R}_{\text{Q}}$, dass mit der Zerlegung aus 2. gilt

```{math}
A\cup B = \bigcup_{j=1}^n S_j
```

und somit ist auch $A\cup B\in\mathcal{R}_{\text{Q}}$ als Vereinigung halboffener Quader.

Damit haben wir gezeigt, dass das Mengensystem $\mathcal{R}_{\text{Q}}$, welches durch disjunkte halboffene Quader im $\R^n$ erzeugt wird, einen Ring bildet.

````

Wir können den Lebesgue-Inhalt nun auf Elemente von $\mathcal{R}_{\text{Q}}$ fortsetzen

````{prf:definition}
Es sei $A\in\mathcal{R}_{\text{Q}}$ mit $A=\bigcup_{i=1}^n$ wobei $Q_1,\ldots,Q_n$ **paarweise disjunkte** halboffene Quader sind, dann setzen wir

```{math}
\lambda^n(A):=\sum_{i=1}^{n} \lambda^n(Q_i).
```
````

````{prf:remark}
Man erkennt leicht, dass der Wert $\lambda^n(A)$ **nicht** von der Wahl der Zerlegung $Q_1,\ldots,Q_n$ abhängt, der Lebesgue-Inhalt ist also wohldefiniert.
````

Für den Lebesgue-Inhalt auf $\mathcal{R}$ können wir folgende Eigenschaften zeigen.

````{prf:theorem}
:label: thm:lebesguevolume

Der Lebesgue-Inhalt $\lambda^n$ auf $\mathcal{R}$ hat folgende Eigenschaften:

1\. $\lambda^n(\emptyset) = 0$

2\. Seien $A_1, \ldots, A_k \in \mathcal{R}$ disjunkte Mengen.
Dann gilt:

```{math}
\lambda^n \left( \bigcup_{i=1,\ldots,k} A_i \right) = \sum_{i=1}^k \lambda^n(A_i) \qquad (\text{endliche Additivität})
```

3\. Für zwei Mengen $A, B \in \mathcal{R}$ mit $A \subset B$ gilt:

```{math}
\lambda^n(A) \leq \lambda^n(B) \qquad (\text{Monotonie}).
```

4\. Für zwei Mengen $A, B \in \mathcal{R}$ gilt:

```{math}
\lambda^n(A \cup B) + \lambda^n(A \cap B) = \lambda^n(A) + \lambda^n(B).
```

5\. Für beliebige Mengen $A_1, \ldots, A_k \in \mathcal{R}$ gilt:

```{math}
\lambda^n\left( \bigcup_{i=1,\ldots,k} A_i\right) \leq \sum_{i=1}^k \lambda^n(A_i) \qquad (\text{endliche Subadditivität}).
```

6\. Sei $(A_n)_{k\in\N}$ eine Folge von disjunkten Mengen in $\mathcal{R}$ und sei $B \in \mathcal{R}$, so dass $\bigcup_{k=1}^\infty A_k \subset B$, dann gilt

```{math}
\sum_{k=1}^\infty  \lambda^n(A_k) \leq \mu(B).
```

````

````{prf:proof}
**Ad 1.**

Für $a\in\R^d$ haben wir 

```{math}
\lambda^n(\emptyset) = \lambda^n((a,a]) = \Pi_{i=1}^n (a_i - a_i) = 0.
```

**Ad 2.**

Für disjunkte Mengen $A_1,\ldots, A_k\in\mathcal{R}$ wählen wir für jedes $i\in\{1,\ldots,k\}$ paarweise disjunkte Quader 
$Q^i_1,\ldots, Q^i_{n_i}$, welche nach {prf:ref}`lem:disRect` existieren, s.d., 

```{math}
A_i = \bigcup_{j=1}^{n_i} Q^i_j.
```

Da die $A_i$ paarweise disjunkt sind, gilt insbesondere 

```{math}
Q^i_j \cap Q^r_s = \emptyset
```

für $(i,j)\neq (r,s)$. Somit haben wir 

```{math}
\lambda^n\left(\bigcup_{i=1}^k A_i \right) &= \lambda^n\left(\bigcup_{i=1}^k \bigcup_{j=1}^{n_i} Q^i_j \right) 
\\&=
\sum_{i=1}^k \sum_{j=1}^{n_i} \lambda^n(Q^i_j)
\\&= 
\sum_{i=1}^k \lambda^n(A_i).
```

**Ad 3.**

Es sei $A\subset B$, dann können wir $B$ disjunkt zerlegen mit 

```{math}
B = A \cup B\setminus A
```

und sehen dann unter Ausnutzung von 2.

```{math}
\lambda^n(B) = \lambda^n((A\cap B)\cup B\setminus B) \overset{2.}{=} 
\lambda^n(A) + \underbrace{\lambda(B\setminus A)}_{\geq 0} \geq \lambda^n(A).
```

**Ad 4.**

Für zwei Mengen $A,B\in\mathcal{R}_{\text{Q}}$ sehen wir, dass  

```{math}
A\cup B = A \cup (B\setminus A),
```

gilt, wobei die Mengen auf der rechten Seite paarweise disjunkt sind. Mit 2. haben wir dann

```{math}
\lambda^n(A\cup B) + \lambda^n(A\cap B)
&= \lambda^n(A) + \lambda^n(B\setminus A) + \lambda^n(A\cap B)
\\&= 
\lambda^n(A) + \lambda^n(B).
```

**Ad 5.**

Nach 4. gilt für zwei Mengen $A,B\in\mathcal{R}$,

```{math}
\lambda^n(A\cup B) = \lambda^n(A) + \lambda^n(B) - \lambda^n(A\cap B) \leq \lambda^n(A) + \lambda^n(B).
```

Diese Eigenschaft lässt sich direkt auf endliche viele Mengen $A_1,\ldots,A_k\in\mathcal{R}$ übertragen.

**Ad 6.** 

Es sei $(A_i)_{i\in\N}\subset \mathcal{R}_{\text{Q}}$ eine Folge paarweiser disjunkter Mengen, s.d., 
```{math}
\bigcup_{i\in\N} A_i\subset B\in \mathcal{R}_{\text{Q}}.
```
Dann gilt für $N\in\N$

```{math}
\sum_{i=1}^N \lambda^n(A_i) 
\overset{2.}{=} \lambda^n\left(\bigcup_{i=1}^N\right) 
\overset{3.}{\leq} \lambda^n\left(\bigcup_{i=1}^\infty\right)
\overset{3.}{\leq} \lambda^n(B).
```

Somit gilt mit $N\to\infty$

```{math}
\sum_{i=1}^\infty \lambda^n(A_i) \leq \lambda^n(B).
```

````

### Der Jordan-Inhalt und Jordan-messbare Mengen

Wir haben bisher einen Inhalt auf $\mathcal{R}_{\text{R}}$ definiert. Diese Klasse an Mengen ist aber relativ klein, weshalb der Begriff ausgedehnt werden soll. Eine Möglichkeit hier ist die Idee des Riemann-Integrals mit Ober- und Untersummen zu benutzen. Es stellt aber auch hier heraus, dass der Begriff zu einschränkend ist. Insbesondere führt deses Konzept **nicht** auf ein Maß. Wir werden es im Folgenden trotzdem betrachten.

````{prf:definition} Jordan-messbare Mengen

Sei $A \subset \R^n$ eine beliebige Teilmenge.
Wir betrachten die folgenden **endlichen** Ober- und Untersummen für die Teilmenge $A$,

```{math}
\iota^\ast(A) &:= \inf \left\{ \lambda^n(O) \, : A \subset O \in\mathcal{R}_{\text{R}}\right\},\\
\iota_\ast(A) &:= \sup \left\{ \lambda^n(U \, : A \supset U\in\mathcal{R}_{\text{R}} \right\}.
```

Wir nennen die Teilmenge $A \subset \R^n$ **Jordan-messbar**, genau dann wenn $A$ beschränkt ist und die Ober- und Untersumme übereinstimmen, d.h., es gilt $\iota^\ast(A) = \iota_\ast(A)$.
Für Jordan-messbare Mengen $A$ ist dann der Jordan-Inhalt $\iota$ gegeben durch:

```{math}
\iota(A) = \iota^\ast(A) = \iota_\ast(A).
```

````

```{figure} ../img/jordanmeasure.jpg
---
width: 400px
name: "fig:jordanmeasure"
---

Visualisierung einer Approximation für das äußere (blau) und das inner (orange) Maß.
```

Die Klasse der Jordan-messbaren Mengen ist erneut recht klein. Insbesondere hat dieses Konzept erneut Schwierigkeiten mit abzählbar unendlich großen Mengen umzugehen wie folgendes Beispiel zeigt.

````{prf:example}
:label: ex:jordan

Wir betrachten die Menge 

```{math}
A = (0,1]\cap \mathbb{Q}
```

der rationalen Zahlen im Intervall $[0,1]$. Wir betrachten zunächst das äußere Maß und dazu eine Menge 

```{math}
J = \bigcup_{i=1}^N Q_i \supset A,
```

mit halboffenen Quader $Q_1,\ldots,Q_N$. Da aber $J$ und $(0,1]$ jeweils Elemente aus $\mathcal{R}_{\text{Q}}$ sind gilt auch 
$L = (0,1]\setminus J \in\mathcal{R}$. Wäre nun $L$ nicht leer, so gäbe es per Definition der halboffenen Quader eine offene Umgebung 

```{math}
U\subset L.
```

Da aber $A$ dicht in $(0,1]$ liegt und somit auch $J$ führt dies auf einen Widerspruch. Deshalb folgt $L=\emptyset$ und daher 

```{math}
(0,1]\subset J \Rightarrow 1\leq \iota^\ast(A).
```

Für das innere Maß betrachten wir 

```{math}
J = \bigcup_{i=1}^N Q_i \subset A,
```

angenommen $J$ wäre nicht leer, dann folgt dass eine offenen Umgebung $U$ existiert s.d. 

```{math}
U\subset J.
```

Da aber auch die irrationalen Zahlen $\R\setminus \mathbb{Q}$ dicht in $\R$ liegen folgt daher 

```{math}
\left[U\cap\R\setminus \mathbb{Q} \neq \emptyset\right] 
\Rightarrow 
\left[J \cap \R\setminus \mathbb{Q} \neq \emptyset\right]
\Rightarrow 
\left[J\not\subset \mathbb{Q}\right]
```

was im Widerspruch zu $J\subset A$ steht, daher gilt 

```{math}
J=\emptyset\Rightarrow \iota_\ast(J) = 0
```

und somit 

```{math}
\iota_\ast(J) \neq \iota^\ast(J).
```
````

Die Menge der Jordan-messbaren Mengen bildet weiterhin keine $\sigma$-Algebra und daher ist der Jordan-Inhalt kein Maß im Sinne von {prf:ref}`def:mass`. Dies ist an folgendem Beispiel ersichtlich.

````{prf:example}
Wir wollen den Jordan-Inhalt einer Punktmengen $\{a\}$ für $a\in\R$ berechnen. Mit der Argumentation aus {prf:ref}`ex:jordan` erkennen wir, dass das innere Maß gleich null ist, also

```{math}
\iota_\ast(\{a\}) = 0.
```

Für das äußere Maß wählen wir eine Folge von offenen Quadern $Q_i:= (a-1/i, a] \supset \{a\}$ und erkennen, dass 

```{math}
\iota^\ast(\{a\})\leq \lim_{i\to\infty} \lambda^n(Q_i) = \lim_{i\to\infty} 1/i = 0
```

und damit ist jede Punktmenge Jordan-messbar. 

Da aber $\mathbb{Q}$ abzählbar ist, können wir eine Folge $(q_i)_{i\in\N}$ finden, s.d. 

```{math}
A = (0,1]\cap \mathbb{Q} = \bigcup_{i\in\N} \{q_i\},
```

die Menge $A$ lässt sich also als abzählbare Vereinigung von Jordan-messbaren Mengen darstellen. Aus {prf:ref}`ex:jordan` wissen wir aber, dass $A$ nicht Jordan-messbar ist und somit bildet die Klassen der Jordan-messbaren Menge **keine** $\sigma$-Algebra.

````

### Das äußere Lebesgue-Maß

Wir der letzte Abschnitt zeigt ist der Begriff der Jordan-messbarkeit einerseits zu einschränkend (siehe {prf:ref}`ex:jordan`) und andererseits führt er nicht auf eine $\sigma$-Algebra. Wir werden diesen Begriff nun erweitern indem wir uns zunächst nur auf den äußeren Inhalt konzentrieren.

```{note}
Der innere und äußere Inhalt sind intuitiv nicht gleichberechtigt, da das Problem asymmetrisch ist. Konkret ist Subadditivität die inhärente Eigenschaft eines Maßes, da Mengenvereinigungen mehrfach auftretenden Elemente nicht berücksichtigen, während die Addition in $\R$ für positive Zahlen stets ein größeres Ergebnis liefert. Das äußere Maß ist auf natürliche Weise subadditiv und deshalb zu bevorzugen.
```

````{prf:definition} Äußeres Lebesgue-Maß

Das **äußere Lebesgue-Maß** $\lambda^* \colon 2^{\R^n} \rightarrow [0,\infty]$ ist definiert durch

```{math}
\lambda^*(A) = \inf \left\{ \sum_{k=1}^\infty \mu^n(Q_k) : Q_k \text{ sind halboffene Quader mit } A \subset \bigcup_{k=1}^\infty Q_k \right\}.
```

````

Im Vergleich zum Jordan-Inhalt lassen wir nun also unendliche Vereinigungen zu und werten dann Reihen aus über welche das Infimum gebildet wird. Die erste wichtige Aussage in diesem Kontext geht auf Lebesgue zurück. Der Beweis des Satzes benutzt den Satz von Heine-Borel.

````{prf:theorem} Heine-Borel
:label: thm:heineborel

Für eine Menge $\Omega\subset\R^n$ sind die folgenden beiden Aussagen äquivalent:

1. $\Omega$ ist beschränkt und abgeschlossen.
2. Jede offene Überdeckung von $\Omega$ enthält eine endliche Teilüberdeckung.
````

````{prf:proof}
Siehe z.B. {cite:p}`forster_2017`.
````

Mit diesem Resultat können wir die folgende Aussage beweisen.

````{prf:theorem}
:label: thm:lebesgue

Es sei $J\in\mathcal{R}_{\text{Q}}$ und $(Q_k)_{k\in\N}$ Folge halboffene Quader mit $J \subset \bigcup_{k=1}^\infty Q_k$.
Dann gilt

```{math}
\lambda^n(J) = \iota(J) = \leq \sum_{k=1}^\infty \lambda^n(Q_k).
```
````

````{prf:proof}
Wir zeigen die Aussage zunächst für $J=Q$ wobei $Q$ ein halboffener Quader ist.

**Idee:** Verkleinere $Q$ und vergrößere die $Q_i$ um Heine-Borel anwenden zu können.

Es sei $\varepsilon>0$ gegeben. Für $Q=(a,b]$ können wir einen kleineren halboffenen Quader $Q_\varepsilon$ wählen, s.d. 

```{math}
\overline{Q_\varepsilon} \subset Q\\
\lambda^n(Q_\varepsilon) > \lambda^n(Q) - \varepsilon.
```

Beachte, dass der Quader so gewählt wird, dass auch sein Abschluss noch in $Q$ enthalten ist, die zweite Bedingung gibt eine unter Schranke an wie klein der Quader gewählt werden darf. Man kann leicht nachrechnen, dass ein solcher Quader existiert. 

Weiterhin wählen wir für jeden Quader $Q_k$ einen größeren Quader $Q_k^\varepsilon$, s.d., 

```{math}
\text{Int}(Q_k^\varepsilon)\supset Q_k\\
\lambda^n(Q_k^\varepsilon) < \lambda^n(Q_k) + \frac{\varepsilon}{2^k},
```

wobei $\text{Int}(\cdot)$ das Innere einer Menge bezeichnet.

Mit dieser Konstruktion gilt 

```{math}
\overline{Q_\varepsilon} \subset Q\subset \bigcup_{k\in\N} Q_k \subset 
\bigcup_{k\in\N}\text{Int}(Q_k^\varepsilon)
```

daher bilden die Mengen $\text{Int}(Q_k^\varepsilon)$ eine abzählbare offenen Überdeckung der kompakten Menge $\overline{Q_\varepsilon}$. 
Nach dem Satz von Heine-Borel ({prf:ref}`thm:heineborel`) existiert somit eine endliche Teilüberdeckung und daher ein $N\in\N$, s.d.,

```{math}
\overline{Q_\varepsilon}\subset \bigcup_{k=1}^N\text{Int}(Q_k^\varepsilon).
```

Für endlich viele Quader können wir nun die Eigenschaften aus {prf:ref}`thm:lebesguevolume` benutzen und folgern

```{math}
\lambda^n(Q) -\varepsilon &< \lambda^n(Q_\varepsilon) \leq 
\lambda^n\left(\bigcup_{k=1}^N\text{Int}(Q_k^\varepsilon\right) 
\\&\leq 
\sum_{k=1}^N \lambda^n(Q_k^\varepsilon) < 
\sum_{k=1}^N \lambda^n(Q_k) + \frac{\varepsilon}{2^k} 
\\&\leq
\sum_{k=1}^\infty \lambda^n(Q_k) + \frac{\varepsilon}{2^k} = \sum_{k=1}^\infty \lambda^n(Q_k) +\varepsilon.
```

Da $\varepsilon>0$ beliebig war folgt die Aussage indem wir $\varepsilon$ gegen $0$ schicken.


Sei nun $J\in\mathcal{R}_{\text{Q}}$, wobei $W_1,\ldots,W_N$ paarweise disjunkte halboffene Quader existieren, s.d., 

```{math}
J = \bigcup_{i=1}^N W_i.
```

Dann sehen wir, dass für jedes $i=1,\ldots,N$ die Folge $(Q_k\cap W_i)_{k\in\N}$ erneut eine Folge halboffener Quader mit

```{math}
W_i \subset \bigcup_{k\in\N} Q_k\cap W_i
```

ist und daher können wir den ersten Fall anwenden. Somit folgt

```{math}
\iota(J) = \sum_{i=1}^N \lambda^n(W_i) \leq \sum_{i=1}^N \sum_{k=1}^\infty \lambda^n(W_i\cap Q_k) = 
\sum_{k=1}^\infty\sum_{i=1}^N \lambda^n(W_i\cap Q_k) = \sum_{k=1}^\infty \lambda^n(Q_k).
```
````

Analog zum Lebesgue-Inhalt auf $\mathcal{R}_\text{Q}$ in {prf:ref}`thm:lebesguevolume` können wir auch für das äußere Lebesgue-Maß ähnliche Eigenschaften zeigen.

````{prf:theorem} Eigenschaften des äußeren Lebesgue-Maßes
:label: thm:outerlebesgue

Das äußere Lebesgue-Maß $\lambda^*$ hat folgende Eigenschaften:

1\. $\lambda^*(\emptyset) = 0$

2\. Für zwei Mengen $A, B \in \R^n$ mit $A \subset B$ gilt:

```{math}
\lambda^*(A) \leq \lambda^*(B) \qquad (\text{Monotonie}).
```

3\. Für eine Folge $(A_k)_{k\in\N}$ von Teilmengen des $\R^n$ gilt:

```{math}
\lambda^*\left( \bigcup_{k=1}^\infty A_k \right) \leq \sum_{k=1}^\infty \lambda^*(A_k) \qquad (\sigma\!-\!\text{Subadditivität}).
```

4\. Für $J\in\mathcal{R}_{\text{Q}}$ gilt,

```{math}
\lambda^*(J) = \iota(J).
```

5\. Für jede Teilmenge $A \subset \R^n$ und jeden halboffenen Quader $Q$ gilt:

```{math}
\lambda^*(A) = \lambda^*(A \setminus Q) + \lambda^*(A \cap Q).
```

````

````{prf:proof}
**Ad 1.**

Da $\emptyset$ ein halboffener Quader ist gilt 

```{math}
0\leq \lambda^\ast(\emptyset) \leq \lambda^n(\emptyset) = 0.
```

**Ad 2.**

Es bezeichne

```{math}
\mathcal{C}(B) = \{ (Q_i)_{i\in\N}: Q_i \text{ ist halboffener Quader, für }i\in\N, B\subset \bigcup_{i\in\N} Q_i  \}
```

die Menge der möglichen Quaderüberdeckungen. Aus $A\subset B$ folgt dann $\mathcal{C}(B) \subset \mathcal{C}(A)$, da jede Überdeckung für $B$ auch eine Überdeckung für $A$ ist und daher 

```{math}
\lambda^\ast(A) = \inf_{\sum_{i=1}^\infty:(Q_i)_{i\in\N}\in \mathcal{C}(A)} \leq 
\inf_{\sum_{i=1}^\infty:(Q_i)_{i\in\N}\in \mathcal{C}(B)} = \lambda^\ast(B).
```

**Ad 3.**

Sei $\varepsilon>0$ gegeben. Per Definition des Infimums existiert für jede Menge $A_k$ eine Folge von halboffenen Quadern $Q_k^i, i\in\N$, s.d. 

```{math}
A_k \subset \bigcup_{i\in\N} Q_i\\
\lambda^\ast(A_k) > \sum_{i=1}^\infty \lambda^n(Q_k^i) - \frac{\varepsilon}{2^k}.
```

Dann folgt aber auch, dass 

```{math}
\bigcup_{k\in\N} A_k \subset \bigcup_{k\in\N}\bigcup_{i\in\N} Q_k^i
```

und da die rechte Seite erneut eine Quaderüberdeckung ist folgt per Definition

```{math}
\lambda^\ast\left(\bigcup_{k\in\N} A_k\right) 
&\leq \sum_{k=1}^\infty\sum_{i=1}^\infty \lambda^n(Q_k^i)\\
&<
\sum_{k=1}^\infty \lambda^\ast(A_k) - \frac{\varepsilon}{2^k} =
\sum_{k=1}^\infty \lambda^\ast(A_k) - \varepsilon.
```

Die Aussage folgt indem wir $\varepsilon$ gegen 0 schicken.

**Ad 4.** 

Es sei $J\in\mathcal{R}_{\text{Q}}$, per Definition folgt direkt 

```{math}
\lambda^\ast(Q)\leq \iota^\ast(Q).
```

Mit {prf:ref}`thm:lebesgue` folgt aber auch 

```{math}
\iota^\ast(Q)\leq \lambda^\ast(Q).
```

**Ad 5.**

Es seien zunächst $A$ und $Q$ halboffene Quader, dann ist auch $A\cap Q$ ein halboffener Quader und wir finden paarweise disjunkte halboffene Quader $Q_0,\ldots,Q_N$, s.d.

```{math}
A\cap Q = Q_0\\
A = \bigcup_{i=1}^N Q_i
```

und damit 

```{math}
\lambda^n(A) &= \lambda^n\left(\bigcup_{i=0}^N Q_i\right)\\
&= 
\lambda^n(A\cap Q) + \lambda^n\left(\bigcup_{i=1}^N Q_i\right)\\
&\geq \lambda^n(A\cap Q) + \lambda^n(A\setminus Q) \\
&\geq \lambda^n(A).
```

Durch die Abschätzung nah oben und nach unten folgt dann 

```{math}
\lambda^n(A) = \lambda^n(A\cap Q) + \lambda^n(A\setminus Q).
```

Als nächsten Schritt betrachten wir eine Folge halboffener Quader $(Q_i)_{i\in\N}\mathcal{C}(A)$ und erhalten dann 

```{math}
\sum_{i=1}^\infty \lambda^n(Q_i) &= 
\sum_{i=1}^\infty \lambda^n(Q_i\cap Q) + \lambda^n(Q_i\setminus Q)\\
&\overset{2.}{\geq}
\lambda^n(A\cap Q) + \lambda^n(A\setminus Q)
&\overset{2.}{\geq}
\lambda^n(A).
```

Nehmen wir das Infimum über $\mathcal{C}(A)$ folgt 

```{math}
\lambda^n(A) \geq \lambda^n(A\cap Q) + \lambda^n(A\setminus Q) \geq 
\lambda^n(A)
```

und daher die Behauptung.
````

Als Korollar von {prf:ref}`thm:lebesgue` und den vorherigen Eigenschaften erhalten wir eine Abschätzung für das äußere Lebesgue-Maß sowohl von oben durch den äußeren Jordan-Inhalt als auch von unten durch den inneren Jordan-Inhalt.

````{prf:corollary}
Es sei $A\subset\R^n$, dann gilt 

```{math}
\iota_\ast(A) \leq \lambda^\ast(A) \leq \iota^\ast(A).
```
````

````{prf:proof}
Für jedes Element $J\in\mathcal{R}_{\text{Q}}$ und beliebige halboffene Quader $Q_i,\i\in\N$, s.d.,

```{math}
J\subset A\subset \bigcup_{i\in\N} Q_i
```

folgt aus {prf:ref}`thm:lebesgue`

```{math}
\lambda^n(J)\leq \sum_{i=1}^\infty Q_i.
```

Dies gilt für jedes $J\in \mathcal{R}_{\text{Q}}$ mit $J\subset A$ und daher insbesondere auch für das Supremum, daher

```{math}
\iota_\ast(A) \leq \sum_{i=1}^\infty Q_i.
```

Diese Aussage gilt wiederum für eine beliebige Folge halboffener Quader welche $A$ überdecken und daher auch für das Infimum, also

```{math}
\iota_\ast(A) \leq \lambda^\ast(A).
```

Die andere Ungleichung folgt per Definition da jede endliche Überdeckung mit halboffenen Quadern (welche im Infimum für $\iota^\ast$ betrachtet werden) auch im Infimum über abzählbare Überdeckungen berücksichtigt wird, daher 

```{math}
\lambda^\ast(A)\leq\iota^\ast(A).
```
````

Die obige Eigenschaft liefert zusätzlich die Aussage, dass für Jordan-messbare Mengen $A$ gilt

```{math}
\iota(A)\leq\lambda^\ast(A)\leq\iota(A)\Rightarrow \lambda^\ast(A) = \iota(A).
```

````{prf:remark} Wirkung von Transformationen auf das äußere Lebesgue Maß
:label: rem:transinvariance

Eine besondere Eigenschaft des äußeren Lebesgue Maßes ist es, dass es *bewegungsinvariant* ist, d.h., dass es unter Translationen und Rotationen den gleichen Wert behält.
Dies ist für viele Anwendungen eine fundamentale Eigenschaft.
Die folgende Bemerkung hält die Wirkung von geometrischen Transformationen auf das äußere Lebesgue Maß fest.

1\. Sei $A \subset \R^n$ eine beliebige Teilmenge und $a \in \R^n$ ein beliebiger Vektor.
Dann ist das äußere Lebesgue Maß **translationsinvariant** unter der Wirkung von $a$, d.h., es gilt

```{math}
\lambda^*(A + a) = \lambda^*(A).
```

Außerdem gilt, dass die Teilmenge $A$ genau dann Lebesgue-messbar ist, wenn die verschobene Teilmenge $A + a$ Lebesgue-messbar ist.

2\. Sei $A \subset \R^n$ eine beliebige Teilmenge und $M \in \R^{n\times n}$ eine beliebige Matrix.
Dann gilt für das äußere Lebesgue Maß der folgende Zusammenhang unter der Wirkung der linearen Transformation $M$

```{math}
\lambda^*(MA) = |\!\operatorname{det}(M)| \, \lambda^*(A).
```

Das heißt insbesondere, dass das äußere Lebesgue Maß invariant unter Transformationen der orthogonalen Gruppe (z.B. **Rotationen** und **Spiegelungen**) ist, da für diese Transformationen $|\!\operatorname{det}(M)| = 1$ gilt (siehe Kapitel 3.6 in {cite:p}`tenbrinck_2021`).

Außerdem gilt, dass die Teilmenge $A$ genau dann Lebesgue-messbar ist, wenn die linear transformierte Teilmenge $MA$ Lebesgue-messbar ist.

````

### Nullmengen

Eine relevante Klasse von Teilmengen des $\R^n$ bilden sogenannten **Lebesgue-Nullmengen**.

````{prf:definition} Lebesgue-Nullmengen
Eine Teilmenge $N \subset \R^n$ eine **(Lebesgue-)Nullmenge**, falls ihr äußeres Lebesgue-Maß Null ist, d.h., es gilt

```{math}
\lambda^*(N) = 0.
```

````

Für die Klasse der Nullmengen können wir folgende Eigenschaften zeigen.

````{prf:lemma} Eigenschaften von Lebesgue-Nullmengen
:label: lem:eigenschaftenNullmengen

Für Lebesgue-Nullmengen gelten die folgenden Eigenschaften:

1. Sei $(N_n)_{n\in\N}$ eine Familie von Nullmengen.
Dann ist auch $\bigcup_{n\in\N} N_n$ eine Nullmenge.

2. Alle abzählbaren Mengen sind Nullmengen.

3. Alle Teilmengen von Nullmengen sind Nullmengen.
````

````{prf:proof}
<br/>


**Ad 1.**

Auf Grund der *$\sigma$-Subadditivität* des äußeren Lebesgue-Maßes folgt direkt

```{math}
0 \leq \mu^* \left( \bigcup_{n\in\N} N_n \right) \leq \sum_{n\in\N} \mu^*(N_n) = 0.
```

Da $\mu^* \left( \bigcup_{n\in\N} N_n \right)$ gilt ist also $\bigcup_{n\in\N} N_n$ auch eine Nullmenge.

**Ad 2.**

Es sei $A\subset\R^d$ eine abzählbare Menge, d.h., es existiert eine Folge $(a_k)_{k\in\N}\subset\R^d$, s.d., 

```{math}
A = \bigcup_{k\in\N} a_k.
```

Es sei nun $\varepsilon>0$ gegeben, dann wählen wir die Folge halboffener Quader 

```{math}
Q_k := (a_k - \frac{\varepsilon}{2^k},a_k]
```

s.d., 

```{math}
A\subset \bigcup_{k\in\N} Q_k.
```

Dann folgt aber,

```{math}
\lambda^\ast(A) \leq \sum_{k\in\N} \lambda^n(Q_k) = \sum_{k\in\N} \frac{\varepsilon}{2^k} = \varepsilon.
```

Wir können nun $\varepsilon$ gegen 0 schicken und erhalte die Aussage.

**Ad 3.**

Es sei $N$ eine Nullmenge und $A\subset N$, dann folgt aus der Monotonie 

```{math}
0\leq \lambda^\ast(A)\leq \lambda^\ast(N) = 0.
```
````

Intuitiv könnten man meinen, dass lediglich abzählbare MEngen Lebesgue Nullmengen sind, dies ist jedoch nicht der Fall. Ein Beispiel ist die [canto-Menge](https://de.wikipedia.org/wiki/Cantor-Menge) welche überabzählbar ist, aber Lebesgue-Maß null hat.

(s:vitali)=
### Das äußere Maß ist kein Maß

Für das äußere Lebesgue Maß kann man einige Eigenchaften zeigen (siehe {prf:ref}`thm:outerlebesgue`) welche zwar eine Maß erinnern. Der größte Unterschied bisher ist, dass wir nur $\sigma$-Subadditivität und nicht $\sigma$-Additivität zeigen konnten. Insbesondere arbeitet das äußere Maß auf der gesamten Potenzmenge $2^{\R^d}$ und nicht auf einer kleineren $\sigma$-Algebra, man könnte also vermuten, dass diese Menge zu groß ist um $\sigma$-Additivität zeigen zu können, was tatsächlich der Fall ist.

Um das zu sehen betrachten wir die sogenannte Vitali Menge auf $\R$.

```{margin} Giuseppe Vitali
[Giuseppe Vitali](https://de.wikipedia.org/wiki/Giuseppe_Vitali) (geboren 26. August 1875 in Ravenna; gestorben 29. Februar 1932 in Bologna) war ein italienischer Mathematiker.
```

Für zwei Punkte $x,y\in\R$ definiert man die Äquivalenzrelation

```{math}
x \sim y \quad \Leftrightarrow \quad x-y \in \Q.
```

d.h. zwei Punkte gehören der selben Äquivalenzklasse an sofern ihre Differenz rational ist. Es gilt also

```{math}
[x] = \{y: y-x\in\Q\}
```

jede Klasse $[x]$ ist abzählbar und $[0] = \Q$. Falls $[x]\cap [y]\neq \emptyset$, so folgt, dass ein $z\in[x]\cap [y]$ existiert und damit

```{math}
\left.
\begin{matrix}
z-x\in\Q\\
z-y\in\Q\\
\end{matrix}
\right\}
\Rightarrow x-y\in\Q\Rightarrow [x]=[y],
```

daher sind zwei Äquivalenzklassen entweder gleich oder disjunkt. Da aber

```{math}
\R = \bigcup_{x\in\R} [x]
```

gilt, muss es überabzählbar viele disjunkte Äquivalenzklassen geben, ansonsten wäre $\R$ selbst abzählbar. Mithilfe des [Auswahl-Axioms](https://de.wikipedia.org/wiki/Auswahlaxiom) können wir nun für jede einzelne Äquivalenzklasse einen Repräsentanten wählen, wobei wir die Menge der Repräsentanten $V$ als **Vitali-Menge** bezeichnen. Zwei Elemente $x,y\in V, x\neq y$ unterscheiden sich stets um eine irrationale Zahl, denn

```{math}
x-y\in\Q \Rightarrow [x] = [y]
```

ist ein Widerspruch zur Konstruktion.

Es sei nun $(q_k)_{k\in\N}$ eine Abzählung der rationalen Zahlen und definiere die verschobenen Vitali Mengen

```{math}
V_k :=\{x+q_k: x\in V\}.
```

````{prf:lemma}
Mit den obigen Definitionen gilt 

1. $\lambda^\ast(V) = \lambda^\ast(V_k)$ für alle $k\in\N$,

2. $V_k\cap V_l=\emptyset$ für $k\neq l$,

3. $\bigcup_{k\in\N} V_k = \R$.
````

````{prf:proof}
<br/>

**Ad 1.**

Diese Tatsache folgt, da das äußere Lebesgue-Maß Translationsinvariant ist, siehe {prf:ref}`rem:transinvariance`.

**Ad 2.**

Für $x,y\in V$ gilt

```{math}
x + q_k = y + q_l&\Rightarrow x-y\in\Q\\
\Rightarrow [x]=[y]&\Rightarrow x=y\\
\Rightarrow q_k=q_l&\Rightarrow k=l
```

wobei wir in der zweiten Zeile erneut ausnutzen, dass die Elemente aus $V$ jeweils disjunkte Äquivalenzklassen erzeugen. 

**Ad 3.**

Trivialerweise gilt 

```{math}
\bigcup_{k\in\N} V_k \subset \R.
```

Andererseits sei $x\in\R$ dann existiert $v\in V$ s.d. $[v] = [x]$. Somit gilt $x-v\in\Q$ und es existiert $k\in\N$, s.d. 

```{math}
q_k = x-v.
```

Somit folgt $x=v+q_k\in V_k$ und daher $x\in\bigcup_{k\in\N} V_k$.
````

Mithilfe einer Vitali-Menge können wir nun die $\sigma$-Additivität des äußeren Lebesgue-Maßes zum Widerspruch führen.

````{prf:lemma}
Das äußere Lebesgue-Maß $\lambda^\ast$ ist nicht $\sigma$-Additiv auf $2^{\R}$.
````

````{prf:proof}

**Annahme**: Das äußere Lebesgue-Maß sei $\sigma$-Additiv auf $2^{\R}$.

Die Mengen $V_k$ sind paarweise disjunkt und überdecken $\R$, daher folgt 

```{math}
0<\lambda^\ast(\R) = \lambda^\ast(\bigcup_{k\in\N} V_k) = \sum_{k\in\N} \lambda^\ast(V_k) = \sum_{k\in\N} \lambda^\ast(V)
```

und daher $\lambda^\ast(V)>0$. Diese Folgerung wollen wir nun zum Widerspruch führen. Dazu betrachten wir die folge halboffener Quader $Q_k:=(k,k]$ und erkennen unter Ausnutzung **endlicher** Additivität, dass

```{math}
\lambda^\ast(V) \geq \lambda^\ast\left(V \cap \bigcup_{k=1}^N Q_k\right) = 
\sum_{k=1}^N \lambda^\ast(V\cap Q_k).
```

Somit folgt mithilfe der $\sigma$-Subadditivität

```{math}
\lambda^\ast(V) \geq \sum_{k=1}^\infty \lambda^\ast(V\cap Q_k) \geq
\lambda^\ast\left(\bigcup_{k\in\N} V\cap Q_k\right) = \lambda^\ast(V).
```

Da wir $\lambda^\ast(V)>0$ folgern konnten, muss daher ein $N\in\N$ existieren, s.d.,

```{math}
\lambda^\ast(V\cap Q_N) >0.
```

Analog zum Beweis, dass die $V_k$ paarweise disjunkt sind, folgert man auch, dass die Mengen $\frac{1}{m}+(V\cap Q_N)$ für verschieden $m\in\N$ paarweise disjunkt sind und wegen der Translationsinvarianz folgt

```{math}
\lambda^\ast(\frac{1}{m}+(V\cap Q_N)) = \lambda^\ast((V\cap Q_N)) >0.
```

Wir erkennen allerdings, dass 

```{math}
\bigcup_{m\in\N} \frac{1}{m}+(V\cap Q_N) \subset (-N,N+1]
```
und nutzen wir nun erneut die angenommene $\sigma$-Additivität so erhalten wir

```{math}
\infty = \sum_{m=1}^\infty \lambda^\ast(\frac{1}{m}+(V\cap Q_N)) = 
\lambda^\ast\left(\bigcup_{m\in\N}  \frac{1}{m}+(V\cap Q_N) \right)\leq 
\lambda^\ast((-N,N+1]) = 2N + 1
```

und somit 

```{math}
\infty \leq 2N + 1
```

was ein Widerspruch ist. Daher ist die Annahme der $\sigma$-Additivität falsch.
````

Ähnliche Konstruktionen können auch allgemein für $\R^n$ durchgeführt werden. Man hat allgemein die Aussage, dass $\lambda^\ast$ auf $\R^n$ **kein** Maß ist.

### Das Lebesgue-Maße

Der vorherige Abschnitt zeigt, dass die Potenzmenge $2^{\R^n}$ zu groß ist, d.h. auf dieser $\sigma$-Algebra ist $\lambda^\ast$ kein Maß. Deshalb wollen wir nun eine Klasse messbarer Mengen definieren, welche dann eine kleinere $\sigma$-Algebra liefert.

````{prf:remark} Das Jordan-Konzept
Eine mögliche Idee um messbare Mengen zu definieren haben wir bereits beim Jordan-Inhalt kennengelernt. Hierbei wird zusätzlich zum äußeren Maß ein inneres Maß definiert. Beim Übergang vom äußeren Jordan-Inhalt zum äußeren Lebesgue-Maß werden endliche Vereinigungen durch unendliche ersetzt, weshalb man versuchen könnte, das nun auch hier zu tun, indem man das innere Lebesgue-Maß auch über unendliche Vereinigungen definiert 

```{math}
\lambda_\ast(A) := \sup\left\{\sum_{i=1}^\infty Q_i: \bigcup_{i\in\N} Q_i \subset A, Q_i\text{ disjunkte halboffener Quader}\right\}.
```

Offensichtlich folgt mit dieser Definition

```{math}
\iota_\ast(A)\leq \lambda_\ast(A)
```

da das Supremum über mehr Ausschöpfungen gebildet wird. Nun sei aber $Q_i$ eine beliebiger Folge halboffener Quader, welche $A$ von innen ausschöpfen, dann gilt für jedes $N\in\N$

```{math}
\iota_\ast(A) \geq \sum_{i=1}^N \lambda^n(Q_i)
```

und daher 

```{math}
\iota_\ast(A)\geq \sum_{i=1}^\infty \lambda^n(Q_i).
```

Diese Ungleichung erhalten wir deshalb so einfach, da für jedes $N\in\N$ auch $\bigcup_{i=1}^N Q_i\subset A$ gilt. Beim äußern Maßen konnten wir aber andersherum nicht einfach aus $A\subset \bigcup_{i=1}^\infty W_i$ auch $A\subset \bigcup_{i=1}^N W_i$ folgern. 

Da die obige Ungleichung für beliebig Folgen halboffener Quader gilt, folgt

```{math}
\iota_\ast(A) \geq \lambda_\ast(A).
```

Wir erkennen also, dass für das innere Maß keinen Unterschied macht ob wir endliche oder unendliche Vereinigungen betrachten.

Würden wir Messbarkeit über die Bedingung

```{math}
\lambda_\ast(A)=\lambda^\ast(A)
```

definieren erhielten wir erneut keine $\sigma$-Algebra. Denn für die Menge $A=[0,1]\setminus\Q$ gilt

```{math}
J\in\mathcal{R}_{\text{Q}}, J\subset A\Rightarrow J=\emptyset
```

und daher $\lambda_\ast(J) = 0$. Der Trick die Menge mit kleinen Quadern zu approximieren wie beim äußeren Maß funktioniert auch nicht, da wir in diesem Fall jeweils die Teilmengen Bedingung verletzt wäre. 

Es gilt aber 

```{math}
\lambda^\ast(A) = \lambda^\ast([0,1]) - \underbrace{\lambda^\ast(\Q)}_{=0} = 1
```

und daher wäre $A$ nicht messbar, obwohl sowohl $\Q$, als auch $[0,1]$ messbar wären. Damit hätten wir erneut keine $\sigma$-Algebra konstruiert.

````

Es gibt verschiedene Ansätze Lebesgue-Messbarkeit zu definieren (welche alle äquivalent sind), wir wählen im Folgenden das Konzept von
Carathéodory.

```{margin} Constantin Carathéodory
[Constantin Carathéodory](https://de.wikipedia.org/wiki/Constantin_Carath%C3%A9odory) (Geboren 13. September 1873 in Berlin; Gestorben 2. Februar 1950 in München) war ein Mathematiker griechischer Herkunft.
```

````{prf:definition} Lebesgue-Maß
Wir nennen eine Teilmenge $A \subset \R^n$ **Lebesgue-messbar**, genau dann wenn für alle Teilmengen $E \subset \R^n$ gilt:

```{math}
\lambda^*(E) = \lambda^*(E \cap A) + \lambda^*(E \setminus A).
```

Wir notieren die Menge der Lebesgue-messbaren Mengen als

```{math}
\mathcal{A} = \lbrace A \subset \R^n : A \text{ ist Lebesgue-messbar } \rbrace
```

Wir definieren das **Lebesgue-Maß** $\lambda \colon \mathcal{A} \rightarrow [0,\infty]$ messbarer Mengen durch

```{math}
\lambda(A) = \lambda^*(A).
```

````

````{prf:remark}
Es ist wichtig zu bemerken, dass diese Bedingung eine Einschränkung ist, da das äußere Lebesgue-Maß **nicht** additiv ist auf $2^{\R^n}$, es gilt lediglich 

```{math}
\lambda^*(E) \leq \lambda^*(E \cap A) + \lambda^*(E \setminus A).
```

für alle $A,E\subset\R^d$. Aus diesem Grund scheint die Einschränkung sinnvoll zu sein um Additivität zu erhalten. 
````

Wir betrachten im Folgenden verschiedene Beispiele messbarer Mengen, was zeigt, dass $\mathcal{A}\neq \emptyset$.

````{prf:lemma} Lebesgue-messbare Mengen
:label: thm:lebesguemes

1. Jede Lebesgue-Nullmenge ist Lebesgue-messbar, insbesondere ist $\emptyset$ Lebesgue-messbar.

2. Jeder halboffene Quader ist messbar.

````

````{prf:proof}
** Ad 1.**

Es sei $N$ eine Lebesgue-Nullmenge und $E\subset\R^d$, dann gilt

```{math}
\lambda^\ast(E) \leq \underbrace{\lambda^\ast(E\cap\N)}_{=0} + \lambda^\ast(E\setminus N)\leq
 \lambda^\ast(E)
```

und daher $\lambda^\ast(E) = \lambda^\ast(E\cap\N) + \lambda^\ast(E\setminus N)$.

**Ad 2.**

Folgt aus {prf:ref}`thm:outerlebesgue` Eigenschaft 4.

````

Weiterhin erhält man über den Begriff der Lebesgue-messbarkeit endlich die erhoffte $\sigma$-Algebra Struktur.

````{prf:lemma}
Die Klasse der Lebesgue-messbaren Mengen $\mathcal{A}$ bildet eine $\sigma$-Algebra.
````

````{prf:proof}
1\. Von {prf:ref}`thm:lebesguemes` erhalten wir zunächst, dass $\emptyset\in\mathcal{A}$.

2\. Weiterhin sei $A\in\mathcal{A}$ messbar und $E\subset\R^d$ beliebig, dann gilt

```{math}
\lambda^\ast(E) = \lambda^\ast(\underbrace{A\cap E}_{=E\setminus A^C}) + \lambda^\ast(\underbrace{E\setminus A}_{=E\cap A^C}) = 
\lambda^\ast(E\setminus A^C) + \lambda^\ast(E\cap A^c) 
```

und daher ist auch $A^C\in\mathcal{A}$.

3\. Wir zeigen zunächst, dass $\mathcal{A}$ unter endlichen Vereinigungen, Schnitten und Differenzen abgeschlossen ist. 

Es seien $A,B\in\mathcal{A}$ und $E\subset\R^d$ dann gilt 

```{math}
\lambda^\ast(E) &= \lambda^\ast(E\cap A) + \underbrace{\lambda^\ast(E\setminus A)}_{\text{wende Messbarkeit von} B\text{ an}}\\
&=\lambda^\ast(E\cap A) + \lambda^\ast((E\setminus A)\cap B) + \lambda^\ast((E\setminus A)\setminus B)\\
&=
\underbrace{\lambda^\ast(E\cap (A\cup B)\cap A) + \lambda^\ast((E\cap A\cup B)\setminus A)}_{\text{wende Messbarket von } A \text{ an}} + \lambda^\ast(E\setminus(A\cup B))\\
&=
\lambda^\ast(E\cap (A\cup B)) + \lambda^\ast(E\setminus(A\cup B))
```

und daher ist $A\cup B$ messbar. Weiterhin folgt $A\cap B = (A^C\cup B^C)^C\in\mathcal{A}$ und daher auch $A\cap B\in\mathcal{A}$. Außerdem gilt $A\setminus B = A\cap B^C$ und somit auch $A\setminus B\in\mathcal{A}$.

4\. Sei nun $A_i\in\mathcal{A}$ für $i\in\N$ eine **disjunkte** Folge von Mengen und setze $A=\bigcup_{i\in\N} A_i$. Unter Ausnutzung von $A_1\in\mathcal{A}$ haben wir für $E\subset\R^d$

```{math}
\lambda^\ast(E\cap (A_1\cup A_2)) &= \lambda^\ast(E\cap(A_1\cup A_2)\cap A_1) + \lambda^\ast(E\cap(A_1\cup A_2)\setminus A_1)\\
&=
\lambda^\ast(E\cap A_1) + \lambda^\ast(E\cap A_2)
```

und somit gilt für endliche Vereinigungen

```{math}
\lambda^\ast(E\cap \bigcup_{i=1}^N A_i) = \sum_{i=1}^N \lambda^\ast(E\cap A_i).
```

Mit Monotonie folgt dann für jedes $N\in\N$ 

```{math}
\lambda^\ast(E\cap A)\geq \lambda^\ast(E\cap \bigcup_{i=1}^N A_i) = \sum_{i=1}^N \lambda^\ast(E\cap A_i)
```

und daher mit der $\sigma$-Subadditivität

```{math}
:label: eq:LebesgueAlgebra

\lambda^\ast(E\cap A) \geq \sum_{i=1}^\infty \lambda^\ast(E\cap A_i)\geq \lambda^\ast\left(\bigcup_{i\in\N} E\cap A_i\right) = \lambda^\ast(E\cap A).
```

Weiterhin wissen wir nach 3., dass endliche Vereinigungen messbarer Mengen messbar sind, daher 

```{math}
\lambda^\ast(E) &= \lambda^\ast\left(E\cap \bigcup_{i=1}^N A_i\right) + \lambda^\ast\left(E\setminus \bigcup_{i=1}^N A_i\right)\\
&\geq
\sum_{i=1}^N \lambda^\ast(E\cap A_i) + \lambda^\ast(E\setminus A)
```

für alle $N\in\N$ und somit 

```{math}
\lambda^\ast(E)\geq \sum_{i=1}^\infty \lambda^\ast(E\cap A_i) + \lambda^\ast(E\setminus A)\geq 
\lambda^\ast(E\cap A) + \lambda^\ast(E\setminus A) \geq \lambda^\ast(E).
```

Daraus schließen wir mit , dass {eqref}`eq:LebesgueAlgebra`

```{math}
\lambda^\ast(E) = \sum_{i=1}^\infty \lambda^\ast(E\cap A_i) + \lambda^\ast(E\setminus A) =
\lambda^\ast(E\cap A) + \lambda^\ast(E\setminus A).
```

5.\ Es bleibt die Aussage für eine belibige nicht notwendigerweise disjunkte Folge $A_i\in\mathcal{A}, i\in\N$ zu zeigen. Dazu definieren wir die Mengen $B_1:=A_1$,

```{math}
B_k := A_i\setminus \left(\bigcup_{i=1}^k B_i  \right)
```

wobei wir erkennen, dass die $B_i$ paarweise disjunkt sind und insbesondere gilt 

```{math}
\bigcup_{k\in\N} B_k = \bigcup_{i\in\N} A_i.
```

Nach 4. ist damit auch diese Vereinigung messbar.

````

Mit dieser Aussage können wir weitere messbare Mengen identifizieren.

````{prf:lemma}
:label: thm:lebesgueOffenAbgeschlossen

Offene und abgeschlossene Teilmengen des $\R^n$ sind Lebesgue-messbar.

````

````{prf:proof}
Es sei $U\subset\R^d$ offen, wir betrachten die Menge

```{math}
\bigcup_{a,b\in \Q^d, (a,b]\subset U} (a,b]\subset U
```

Sei nun $x\in U$, dann existiert auch $a,b\in\Q^d$, s.d. $x\in(a,b]\subset U$ und somit $x\in\bigcup_{a,b\in \Q^d, (a,b]\subset U}$, woraus wir schließen

```{math}
\bigcup_{a,b\in \Q^d, (a,b]\subset U} (a,b] = U.
```

Somit ist $U$ abzählbare Vereinigung messbarer Mengen und daher selbst messbar. 

Abgeschlossene Mengen sind als Komplemente offener und daher messbarer Mengen, selbst messbar.
````

Da wir nun eine $\sigma$-Algebra zu Verfügung haben können wir ein Maß definieren.

````{prf:definition} Lebesgue-Maß
Wir definieren das Lebesgue-Maß $\lambda^n:\mathcal{A}\to[0,\infty]$ über die Einschränkung des äußeren Maßes, d.h.,

```{math}
\lambda^n(A):= \lambda^\ast(A)\text{ für } A\in\mathcal{A}.
```
````

```{danger}
ToDo
```

````{prf:theorem} Regularität des Lebesgue Maßes

Das Lebesgue Maß ist von außen und innen regulär im Sinne von {prf:ref}`def:regularitaet`, d.h., für jede Lebesgue-messbare Teilmenge $A \subset \R^n$ gilt

1\. für jedes $\epsilon > 0$ existiert eine offene Menge $U$ mit $A \subset U$ für die gilt $\mu(U \setminus A) < \epsilon$,

2\. für jedes $\epsilon > 0$ existiert eine abgeschlossene Menge $F$ mit $F \subset A$ für die gilt $\mu(A \setminus F) < \epsilon$.

````

````{prf:proof}
ToDo.
````

````{prf:theorem} Charakterisierung Lebesgue-messbarer Mengen

Die folgenden drei Aussagen sind äquivalent, so dass sie eine Charakterisierung der Lebesgue-messbaren Mengen darstellen.

1\. Eine Teilmenge $A \subset \R^n$ ist Lebesgue messbar.

2\. Für jedes $\epsilon > 0$ existiert eine offene Menge $U$ und eine abgeschlossene Menge $F$, so dass $F \subset A \subset U$ und es gilt $\mu(U \setminus F) < \epsilon$.

3\. Für jedes $\epsilon > 0$ existiert eine offene Menge $U$ mit $A \subset U$ für die gilt $\mu(U \setminus A) < \epsilon$.

````

````{prf:proof}
ToDo
````

Man kann für die Borel-$\sigma$-Algebra von $\R^n$ zeigen, dass gilt

```{math}
\B(\R^n) = \sigma(\lbrace A \subset \R^n \text{ offen }\rbrace) ) = \sigma(\lbrace A \subset \R^n \text{ abgeschlossen }\rbrace)
```

Die letzte Gleichung gilt, da $\sigma$-Algebren abgeschlossen unter Komplementbildung sind.
Zusammen mit {prf:ref}`thm:lebesgueOffenAbgeschlossen` folgt dann schon, dass die Borel-$\sigma$-Algebra $\B(\R^n)$ eine Teilmenge der Lebesgue messbaren Mengen ist.
Der folgende Satz zeigt, dass es eine echte Teilmenge ist indem er den Unterschied der Mengen als Lebesgue Nullmengen charaterisiert.

````{prf:theorem}
Eine Teilmenge $A \subset \R^n$ ist genau dann Lebesgue-messbar, wenn eine Teilmenge $B \in \B(\R^n)$ und eine Nullmenge $N \subset \R^n$ existiert, so dass $A = B \cup N$ ist, wobei $B\cap N=\emptyset$.
````

````{prf:proof}
ToDo
````
