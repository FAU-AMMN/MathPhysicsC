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

````{prf:definition} $\sigma$-Algebra und Maßraum
:label: def:sigmaalgebra
Ein Mengensystem $\mathcal{A} \subseteq \mathcal{P}(\Omega)$ heißt **$\sigma$-Algebra (von $\Omega$)**, wenn die folgenden Eigenschaften erfüllt sind

1. $\Omega\in \mathcal{A}$

2. $A\in \mathcal{A} \quad \Rightarrow \quad A^c:=\Omega \setminus A\in \mathcal{A}$

3. $(A_n)_{n\in\N} \in \mathcal{A} \quad \Rightarrow \quad \bigcup_{n\in \N} A_n\in \mathcal{A}$.

Für eine $\sigma$-Algebra $\mathcal{A} \subseteq \mathcal{P}(\Omega)$ von $\Omega$ nennen wir das Paar ($\Omega,\mathcal{A}$) **Maßraum** und die Mengen des Mengensystems $\mathcal{A}$ heißen **messbar**.
````

Die kleinste $\sigma$-Algebra von $M$ ist damit $\{\emptyset, \Omega\}$, die Größte $\mathcal{P}(\Omega)$.

Das Symbol $\sigma$ soll an den Begriff der Summe erinnern, entsprechend der
dritten Forderung in Def. \ref{def:sigmaalgebra}, also der Stabilität unter abzählbarer Vereinigung.
Sigma–Algebren sind offensichtlich auch unter dem Schnitt abz ̈ahlbar vieler
Mengenstabil $A_n\in \mathcal{A}\ (n\in\N)$ impliziert, dass $\bigcap_{n\in \N} A_n = \left(\bigcup_{n\in\N} A_n^c\right)^c\in \mathcal{A}$.

````{prf:definition}
* Für einen Messraum ($M, \mathcal{A}$) heißt eine Abbildung $\mu: \mathcal{A}\to [0, \infty]$ **Maß**, wenn

    a) $\mu(\emptyset) = 0$

    b) Für disjunkte (das heißt $A_m\cap A_n = \emptyset\ (m\neq n)$) $A_n\in \mathcal{A}\ (n\in\N)$ gilt: $\mu\left( \bigcup_{n\in\N}A_n \right) = \sum_{n\in\N}\mu (A_n)$ \quad (abzählbare oder $\sigma$-**Additivität**).

* Dann heißt das Tripel $(M, \mathcal{A}, \mu)$ **Maßraum**.

* Das Maß $\mu$ heißt **endlich**, wenn $\mu(M)<\infty$, und **Wahrscheinlichkeitsmaß**, wenn $\mu(M)=1$.
````


````{prf:example}
Wichtige Maße sind z.B. die folgenden.

1. Das [**Zählmaß**](https://de.wikipedia.org/wiki/Z%c3%a4hlma%c3%9f_(Ma%c3%9ftheorie)) $m$ auf einer endlichen Menge $M$, mit 
```{math}
m(A):=|A|\qquad (A\subseteq M).
```
Hier sind insbesondere alle Teilmengen messbar.

2. Das **Lebesgue--Maß** $\lambda^n$ auf dem $\R^n$, das wir bald kennen lernen, zeichnet sich dadurch aus, dass es einem verschobenen Körper das gleiche Volumen zuordnet wie dem unverschobenen, es also *translationsinvariant* ist, und der Einheitswürfel $[0,1]^n$ Maß $1$ besitzt.

3. Das [**Dirac-Maß**](https://de.wikipedia.org/wiki/Diracma%c3%9f) $\delta_x$ ist im Punkt $x$ des $\R^n$ konzentriert, und für $A\subset\R^n$ ist.
```{math}
\delta_x(A)\equiv \int_A\delta_x := \begin{cases} 1, &  x \in A\\ 0, & \text{sonst.} \end{cases}

```
Dieses Maß ist also nicht translationsinvariant. Es wird beispielsweise in der Elektrodynamik benutzt, um eine bei $x$ lokalisierte punktförmige Ladung zu beschreiben.

4. Wir wollen z.B. auch die Länge der Spur einer *Kurve* oder allgemeiner den Flächeninhalt einer $d$--dimensionalen Fläche im $\R^n$ messen. Auch das dafür benutzte Maß $\mu_d$ ist translations- und rotationsinvariant, es ordnet aber der $d$--dimensionalen Einheitsfläche $[0,1]^d\times\{0\} \subset\R^d\times\R^{n-d}=\R^n$ Maß 1 zu. Entsprechend hat aber für $d<n$ der Einheitswürfel Maß $\mu_d([0,1]^n)=\infty$.

5. Man kann sogar sog. [**Hausdorff-Maß**](https://de.wikipedia.org/wiki/Hausdorff-Ma%c3%9f) $\mu_d$ konstruieren, die Mengen beliebiger fraktaler Dimension $d\in[0,n]$ messen. Genau genommen *definiert* man die Dimension der Menge $A\subset \R^n$ durch $d(A):=\inf\{d'>0\mid \mu_{d'}(A)=0\}.$

6. Im Zusammenhang mit dem sog. Feynmanschen [**Pfadintegral**](https://de.wikipedia.org/wiki/Pfadintegral) der Quantenmechanik wird auf dem unendlich-dimensionalen Raum $M$ der Wege zwischen zwei Punkten des Konfigurationsraumes $\R^d$ ein [**Wahrscheinlichkeitsmaß**](https://de.wikipedia.org/wiki/Wahrscheinlichkeitsma%c3%9f) (also ein Maß $\mu$ auf $M$ mit $\mu (M)=1$) definiert. Dabei erhalten Wege, die in der Nähe von Lösungskurven der DGL der Klassischen Mechanik sind, ein großes Gewicht.
````

## Borel-$\sigma$-Algebra und Borel-$\sigma$-Maß

````{prf:definition} Borel $\sigma$-Algebra
S. 106 und 119 Schulz-Baldes
Die **Borel $\sigma$-Algebra** auf einem topologischen Raum $(\Omega, \tau)$ ist die kleinste $\sigma$-Algebra auf der Menge $\Omega$, die die Topologie $\tau$ enthält, d.h.

```{math}
\B(\Omega) := \bigcap_{\substack{\mathcal{A} \text{ ist $\sigma$-Algebra}\\ \tau \subset \mathcal{A}}} \mathcal{A}
```

Man nennt die Borel-$\sigma$-Algebra auch **die von $\tau$ erzeugte $\sigma$-Algebra**.
````

````{prf:definition} Lokale Endlichkeit von Maßen
Sei $\sigma \colon \B(\Omega) \rightarrow [0, \infty]$ ein Maß auf einem topologischem Raum $\Omega$.
Wir nennen das Maß $\sigma$ **lokal endlich**, falls jeder Punkt $x \in \Omega$ eine lokale Umgebung mit endlichem Maß besitzt.
````

Es ist klar, dass das Lebesgue-Maß auf dem Raum $\R^n$ lokal endlich ist.

````{prf:definition} Borel-Maß
Ein lokal endliches Maß $\sigma \colon \B(\Omega) \rightarrow [0, \infty]$ auf der Borelschen $\sigma$-Algebra eines topologischen Raums $\Omega$ heißt **Borel-Maß**.
````

## Riemann- und Lebesgue-messbare Mengen

````{prf:definition} Mehrdimensionale Quader
Seien $a = (a_1,\ldots,a_n) \in \R^n$ und $b = (b_1,\ldots,b_n) \in \R^n$ zwei Punkte im \R^n.
Wir definieren zunächst folgende Anordnungsrelation mit

```{math}
a < b \qquad \Leftrightarrow \qquad a_i < b_i \quad i=1,\ldots,n.
```

Analog können wir die Anordnungsrelationen $a \leq b, a > b$ und $a \geq b$ definieren und darüber im Folgenden **offene, halboffene** und **abgeschlossene Quader** im $\R^n$ respektive beschreiben durch

```{math}
(a,b) = \lbrace x \in \R^n : a < x < b \rbrace,\\
(a,b] = \lbrace x \in \R^n : a < x \leq b \rbrace,\\
[a,b] = \lbrace x \in \R^n : a \leq x \leq b \rbrace,.
```

````

````{prf:definition} Mehrdimensionale Treppenfunktion
Wir nennen eine Funktion $f \colon \R^n \rightarrow \C$ **Treppenfunktion**, falls es paarweise disjunkte Quader $Q_1, \ldots, Q_k \subset \R^n$ gibt, so dass die folgenden Eigenschaften gelten:

1. Die Funktion $f$ ist konstant auf jedem der Quader, d.h.,
```{math}
f|_{Q_i} = c \in \C, \quad 1 \leq i \leq k,
```

2. Die Funktion ist überall Null außerhalb der Quader, d.h.,
```{math}
f|_{\R^n \setminus (Q_1 \cup \ldots \cup Q_k)} = 0.
```


````

Illustration hier von Quadern und Treppenfunktionen!

````{prf:definition} Ring
Ein Mengensystem $\mathcal{R} \subset \mathcal{P}(\Omega)$ heißt **Ring** auf einer Menge $\Omega$, falls die folgenden Eigenschaften erfüllt sind:

1. $\emptyset \in \mathcal{R}$
2. $A,B \in \mathcal{R} \Rightarrow (A \setminus B) \in \mathcal{R}
3. $A,B \in \mathcal{R} \Rightarrow (A \cup B) \in \mathcal{R}
````

````{prf:lemma} Der von halboffenen Quadern erzeugte Ring
S. 79 Schulz-Baldes
````


````{prf:remark} Riemann-messbare Mengen
S. 78 Schulz-Baldes
````

````{prf:example} Riemann-Messbarkeit
Ein Beispiel messbar, eins nicht.
````

Verglichen mit der Reichhaltigkeit der Potenzmenge $\mathcal{P}(\Omega)$ sind nur relativ wenige Mengen Riemann-messbar.

````{prf:definition} Äußeres Lebesguesches Maß
S. 78 u. 89 Schulz-Baldes
````

````{prf:theorem} Eigenschaften des Lebesgue Maßes
S. 89 Schulz-Baldes
````

````{prf:definition} Lebesgue-messbare Mengen
S. 92 Schulz-Baldes
````

````{prf:example} Lebesgue-messbare Mengen
S. 92 Schulz-Baldes
````

````{prf:definition} Lebesgue-Nullmengen
S. 98 Schulz-Baldes
````

````{prf:lemma} Eigenschaften von Lebesgue-Nullmengen
S. 98 Schulz-Baldes
````

````{prf:theorem} Lebesgue-Messbarkeit von Teilmengen im $\R^n$
Sowohl offene als auch abgeschlossene Teilmengen des $\R^n$ sind Lebesgue-messbar.
````
````{prf:proof}
S. 99 Schulz-Baldes
````