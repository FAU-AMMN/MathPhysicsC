# Potenzreihen

In diesem Abschnitt wollen wir genauer auf analytische Funktionen bzw. Potenzreihen eingehen, wir betrachten also Funktionen

```{math}
z\mapsto \sum_{j=0}^{\infty} a_j (z-p)^j,
```

mit komplexen Koeffizienten $a_j\in\C$.

## Analytische Funktionen

Wir betrachten zunächst Funktionen welche durch Potenzreihen gegeben sind und erhalten, dass sie auf Kreisscheiben schon holomorph sind.

````{prf:lemma}
:label: lem:potseries

Es sei $a_j\in\C, j\in\N_0$ eine Folge komplexer Zahlen, $p\in\C$ und die Reihe

```{math}
\sum_{j=0}^\infty a_j (z_0-p)^j 
```

konvergiere für $z\neq p$. Dann ist die Funktion $f:z\mapsto \sum_{j=0}^\infty a_j (z-p)^j$ holomorph auf der Kreisscheibe $B_r(p)$, wobei $r:=\abs{z_0-p}$ und

```{math}
f^\prime(z) = \sum_{j=1}^\infty a_j\cdot j\cdot (z-p)^{j-1}.
```
````

````{prf:proof}
Siehe {cite:p}`neeb_2017` Satz 2.19.
````

Eine besondere Klasse von Funktionen sind *analytische Funktonen*, die sich lokal mit Hilfe von Reihen darstellen lassen.

````{prf:definition} Analytische Funktion
Sei $U \subset \C$ offen und $f: U\to \C$ eine Funktion.

Wir nennen $f$ **analytisch** in einem Punkt $p \in U$ genau dann, wenn ein $r > 0$ existiert, so dass sich die Funktion lokal in $B_r(p)$ als Potenzreihe darstellen lässt,

```{math}
f(z) = \sum_{j=0}^\infty a_j (z-p)^j, \qquad \forall z\in B_r(p)
```

wobei $(a_n)_{n_\in\N}$ eine Folge in $\C$ ist.

Wir nennen die Funktion $f$ analytisch auf der Teilmenge $U$, wenn sie analytisch ist für alle Punkte $z_0 \in D$.

````

Der folgende Satz beschreibt den Zusammenhang zwischen analytischen und holomorphen Funktionen.

````{prf:theorem}
:label: thm:analytischHolomorph

Jede analytische Funktion $f$ auf einer Teilmenge $U \subset \C$ ist auch holomorph auf $U$.
````

````{prf:proof}
Folgt direkt aus {prf:ref}`lem:potseries`
````

Wir wollen im folgenden sehen, dass auch die Umkehrung gilt.

## Konvergenzradius

Ein wichtige Eigenschaft von Potenzreihen um $p\in\C$ ist, dass Konvergenz an einem Punkt $z$ schon die absolute und gleichmäßige Konvergenz innerhalb einer Kreisscheibe impliziert.

````{prf:lemma}
:label: lem:powerradius

Konvergiert die Reihe $\sum_{j=0}^\infty a_j (z_0-p)^j$ für $z_0\in\C$, so konvergiert die Reihe $\sum_{j=0}^\infty a_j (z-p)^n$ auf jeder offenen Kreisscheibe $B_r(p)$ mit $r< \abs{z_0 - p}$.
````

````{prf:proof}
O.B.d.A. gelte $p=0$, da $\sum_{j=0}^\infty a_j z_0^j$ konvergiert ist, $a_j z_0^j$ eine Nullfolge und insbesondere existiert eine Konstante $C>0$, s.d., $\abs{a_j z_0^j}< C$ für alle $j\in\N$. Sei nun $r<\abs{z_0}$, dann folgt für jedes $z\in B_r(0)$, dass

```{math}
\abs{a_j z^j} = \abs{a_j z_0^j}\abs{\frac{z}{z_0}}^j\leq C \left(\frac{r}{z_0}\right)^j
```

und damit

```{math}
\sum_{j=0}^\infty \abs{a_j z_j} \leq C \sum_{j=0}^\infty \left(\frac{r}{z_0}\right)^j
```

wobei die geometrische Reihe auf der linken Seite konvergiert. Somit konvergiert die Reihe auf $B_r(0)$ nach dem Majorantenkriterium gleichmäßig absolut.
````

Der maximale Radius für welchen eine Potenzreihe konvergiert, wird als Konvergenzradius bezeichnet.

````{prf:definition} Konvergenzradius
Für eine Koeeffizientenfolge $a_j\in\C$ und $p\in\C$ ist der **Konvergenzradius** der Potenzreihe definiert durch

```{math}
R :=\sup\left\{\abs{z - p}: \sum_{j=0}^\infty a_j (z-p)^j \text{ konvergiert}\right\}.
```
````

Die Definition ist äquivalent zum Wert

```{math}
R :=\sup\left\{r<0: \sum_{j=0}^\infty a_j r^j\text{ konvergiert} \right\}
```

was auf das bekannte **Wurzelkriterium** führt.

## Entwicklungssatz

In diesem Abschnitt erarbeiten wir mithilfe von Potenzreihen die komplexe Taylorreihe.

```{margin} Brook Taylor
[Brook Taylor](https://de.wikipedia.org/wiki/Brook_Taylor) (Geboren 18. August 1685 in Edmonton, Middlesex; Gestorben 29. Dezember 1731 in Somerset House, London) war ein britischer Mathematiker und Mitglied der Royal Society.
```

````{prf:theorem} Entwicklungssatz
Es sei $B_r(p)$ eine offene Kreisscheibe um $p\in\C$ und $f:B_r(p)\to\C$ eine Funktion. Die Funktion $f$ ist genau dann holomorph, wenn sie durch eine konvergente Potenzreihe mit Entwicklungspunkt $p$ dargestellt werden kann, d.h. falls eine Folge $a_j\in\C$ existiert, s.d.,

```{math}
f(z) = \sum_{j=0}^\infty a_j (z-p)^n.
```

In diesem Fall gilt insbesondere

```{math}
a_n = \frac{1}{n!} f^{(n)}(p)
```
````

````{prf:remark}
Diese Aussage bildet das Gegenstück zur Tatsache das analytische Funktionen holomorph sind. Insbesondere ist die Reihe die man so erhält die Taylorreihe

```{math}
\sum_{j=0}^\infty \frac{1}{n!} f^{(n)}(p) (z-p)^n.
```
````

````{prf:proof}
ToDo, siehe {cite:p}`neeb_2017` Satz 5.7.
````

````{prf:example}
ToDo, sehr wichtiges Beispiel aus {cite:p}`neeb_2017` 5.10.
````
