# Maßtheorie

Ein [**Maß**](https://de.wikipedia.org/wiki/Ma%c3%9f_(Mathematik)) $\mu$ auf einer Menge $M$ wie z.B. dem $\R^n$
ordnet geeigneten Teilmengen $A\subseteq M$
Zahlen
```{math}
\mu(A)\in[0,\infty]:=[0,\infty)\cup\{\infty\}
```
zu, eben das Maß von $A$.

## Mengensysteme

Ein Mengensystem ist eine Menge von Mengen. Wir nennen die Potenzmengen $2^M \equiv\mathcal{P}(M)$ von $M$ die Menge aller möglichen Teilmengen von $M$. In der Maßtheorie sind Mengensysteme $\mathcal{A} \subseteq \mathcal{P}(M)$ zentral, nämlich die der *meßbaren* Teilmengen von $M$. Das sind die Mengen, denen ein Maß zugeordnet wird, also eine nicht negative Zahl oder Unendlich. Schauen wir uns also an, welche Eigenschaften ein Maß haben muss.

### $\sigma$-Algebren und Maße

Zunächst müssen wir festlegen, welche Teilmengen der Grundmenge $M$ überhaupt messbar sein sollen. Wir wählen also wie gesagt ein Mengensystem $\mathcal{A} \subseteq \mathcal{P}(M)$ in der Potenzmenge von $M$ aus.
Am bequemsten wäre es, alles messen zu können, also $\mathcal{A} = \mathcal{P}(M)$, aber das ist nicht immer möglich. Wir fordern, dass $\mathcal{A}$ eine $\sigma$-Algebra ist.

````{prf:definition}
:label: def:sigmaalgebra
* $\mathcal{A} \subseteq \mathcal{P}(M)$ heißt **$\sigma$-Algebra (von $M$)**, wenn

    a) $M\in \mathcal{A}$

    b) $A\in \mathcal{A}$ impliziert, dass $A^c:=M\backslash A\in \mathcal{A}$

    c) $A_n\in \mathcal{A}\ (n\in\N)$ impliziert, dass $\bigcup_{n\in \N} A_n\in \mathcal{A}$.

* Für eine $\sigma$-Algebra $\mathcal{A} \subseteq \mathcal{P}(M)$ von $M$ heißt das Paar ($M,\mathcal{A}$) **Messraum**, und die Menge $\mathcal{A}$ heißen *messbar*.
````

Die kleinste $\sigma$-Algebra von $M$ ist damit \{\emptyset, M\}, die Größte $\mathcal{P}(M)$.

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
