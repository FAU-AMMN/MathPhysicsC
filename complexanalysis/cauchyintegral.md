# Der Integralsatz von Cauchy

Wir wollen nun einen der zentralen Aussagen der Funktionentheorie formulieren, die Cauchysche Integralformel.
Diese besagt, dass sich die Werte einer holomorphen Funktion im Inneren eines bestimmten Gebietes bereits durch die Werte auf dem Gebietsrand bestimmen lassen. Ein erstes Resultat in diese Richtung erhalten wir indem wir *benachbarte Wege* betrachten.

## Benachbarte Wege

In der Definition eines Wegintegrals über beliebige Wege betrachtet man zulässige Zerlegungen mit offenen Kreisscheiben. Finden wir nun eine Zerlegung, s.d., sich zwei Wege die jeweiligen Kreisscheiben teilen, so wollen wir sie benachbart nennen.

````{prf:definition}
Es sei $U\subset \C$ offen und seien $\gamma_0,\gamma_1:[a,b]\to U$ zwei Wege. Falls eine Zerlegung $(a=t_0,\ldots,b=t_N)$ existiert mit Kreisscheiben $B^j$, welche zulässig für beide Wege ist, d.h.,

```{math}
\gamma_0([t_j, t_{j+1}])\cup \gamma_1([t_j,t_{j+1}]) \subset B^j
```

dann nennen wir $\gamma_0$ und $\gamma_1$ **benachbart**.
````

Der Begriff der Nachbarschaft hat tatsächlich auch eine geometrische Bedeutung, welche in folgendem Lemma festgehalten wird.

````{prf:lemma} Nachbarschaftslemma
:label: lem:closelem

Es sei $U\subset\C$ offen, dann existiert ein $\varepsilon>0$, s.d. falls für zwei Wege $\gamma_0,\gamma_1:[a,b]\to U$ gilt

```{math}
\abs{\gamma_0 - \gamma_1} < \varepsilon
```

so folgt schon, dass $\gamma_0,\gamma_1$ benachbart sind.
````

````{prf:proof}
Siehe z.B. {cite:p}`neeb_2017`.
````

Für benachbarte Wege erhalten wir nun das folgende Resultat, welches eine Vorstufe zum Integralsatz von Cauchy darstellt.

````{prf:lemma}
:label: lem:closepath

Es $U\subset\C$ eine offene Menge und $f:U\to\C$ eine holomorphe Funktion, weiterhin seien $\gamma_0,\gamma_1:[a,b]\to U$ zwei benachbarte Weg die eine der folgenden Bedingungen erfüllen

1. die Wege haben gleiche Anfangs- und Endpunkte, oder

2. die Wege sind geschlossen.

Dann gilt

```{math}
\int_{\gamma_0} f(z)\, dz = \int_{\gamma_1} f(z)\, dz.
```
````

````{prf:proof}
Siehe z.B. {cite:p}`neeb_2007` Lemma 4.5.
````

## Homotopie

Um nicht nur benachbarte Wege betrachten zu können definieren wir jetzt den Begriff von Homotopie.

````{prf:definition} Homotopie
Es sei $U\subset\C$ offen, zwei Wege $\gamma_0, \gamma_1:[a,b]\to U$ mit gleichen Anfangs und Endpunkten, 

```{math}
\gamma_0(a) = \gamma_1(a),\\
\gamma_0(b) = \gamma_1(b),
```

heißen **homotop**, falls eine stetige Abbildung $h:[a,b]\times[0,1]\to U$ existiert, so dass für alle $t\in[a,b]$ gilt

```{math}
h(t,0) = \gamma_0(t), \qquad h(t,1) = \gamma_1(t).
```

In diesem Fall nennen wir die Abbildung $h$ eine **Homotopie** zwischen den Wegen $\gamma_0$ und $\gamma_1$ und notieren auch $h_s:=h(\cdot,s):[a,b]\to U$ für den Weg am Punkt $s\in [0,1]$.

````

Anstatt nur Wege mit gleichen Anfangs und Endpunkten zu betrachten können wir auch Homotopie geschlossener Wege definieren.

````{prf:definition} Homotopie geschlossener Wege
Es sei $U\subset\C$ offen, zwei geschlossene Wege $\gamma_0, \gamma_1:[a,b]\to U$ heißen **frei homotop**, falls eine stetige Abbildung $h:[a,b]\times[0,1]\to U$ existiert, so dass für alle $t\in[a,b]$ gilt

```{math}
h(t,0) = \gamma_0(t), \qquad h(t,1) = \gamma_1(t)\quad
```

und der Weg $h_s$ geschlossen ist für alle $s\in [0,1]$.

Ein geschlossener Weg heißt **zusammenziehbar** oder **nullhomotop**, falls er frei homotop zu einem konstanten Weg ist.

````

````{prf:remark}
Man kann zeigen, dass der Begriff der Homotopie zwischen Wegen in einer Teilmenge $U \subset \C$ eine *Äquivalenzrelation* auf Wegen in $U$ induziert. Die zugehörigen Äquivalenzklassen werden auch *Homotopieklassen* genannt.
````

## Der Homotopiesatz und der Integralsatz von Cauchy

Für geschlossene Wege impliziert Homotopie eine besondere Eigenschaft bezüglich des Kurvenintegrals, wie folgendes Lemma festhält.

````{prf:lemma} Homotopiesatz
:label: lem:homotop

Es sei $U \subset \C$ offen und seien $\gamma_0$ und $\gamma_1:[a,b]\to U$ homotope oder frei homotope Wege.
Sei außerdem $f:U\to C$ eine holomorphe Funktion, dann gilt

```{math}
\oint_{\gamma_0} f(z) \, dz = \oint_{\gamma_1} f(z) \, dz.
```
````

````{prf:proof}
Es sei $h:[a,b]\times[0,1]\to U$ eine Homotopie, mit $h_0=\gamma_0, h_1=\gamma_1$. Die Menge $[a,b]\times[0,1]$ ist kompakt und somit ist $h$ gleichmäßig stetig, d.h. insbesondere, dass für $\varepsilon>0$ ein $\delta >0$ existiert, s.d.,

```{math}
\abs{h_{s_0}-h_{s_1}}_\infty <\varepsilon \text{ für } \abs{s_1-s_2}< \delta.
```

Wir können nach {prf:ref}`lem:closelem` somit $\delta$ klein genug wählen, s.d. Wege $h_{s_0}, h_{s_1}$ benachbart sind für $\abs{s_0-s_1}<\delta$. Somit gilt nach {prf:ref}`lem:closepath`, dass

```{math}
\int_{h_{s_0}} f(z)\, dz = \int_{h_{s_1}} f(z)\, dz
```

gilt für $\abs{s_0-s_1}<\delta$. Damit folgt die Aussage.

````

Es folgt, dass das Kurvenintegral einer holomorphe Funktionen über einen nullhomotopen Weg verschwindet, was als **Integralsatz von Cauchy** bekannt ist.

````{prf:theorem} Integralsatz von Cauchy
Es sei $U\subset\C$ offen und sei $\gamma:[a,b]\to U$ ein nullhomotoper Weg, für jede holomorphe Funktion $f:U\to\C$ gilt dann

```{math}
\oint_\gamma f(z)\, dz = 0.
```
````

````{prf:proof}
Folgt direkt aus {prf:ref}`lem:homotop`.
````

## Die Integralformel von Cauchy

Wir werden die obigen Konzepte nun auf Wegen betrachten welche den rnd einer Kreisscheibe parametrisieren. Dazu sei $B_r(p)\subset\C$ eine Kreisscheibe um den Punkt $p\in\C$ mit Radius $r>0$, wir wählen die natürliche Parametrisierung des Randes

```{math}
\gamma_{p,r}:[0,2\pi]&\to \partial B_r(p)\\
t&\mapsto p + r\exp(i t),
```

wobei wir die Eulersche Formel {eq}`eq:euler` benutzt haben.

Mithilfe der natürlichen Parametrisierung schreiben wir auch

```{math}
\int_{\partial B_r(p)} f(z)\, dz := \int_{\gamma_{p,r}} f(z)\, dz
```

und formulieren nun die Integralformel von Cauchy.

````{prf:theorem} Cauchy Integralformel
Sei $U \subset \C$ offen, $\overline{B_r(p)}\subset \C$ und $f:U\to \C$ holomorph$, dann gilt

```{math}
f(w) = \frac{1}{2\pi i} \int_{B_r(p)} \frac{f(z)}{z-w}\, dz
```

für alle $w\in B_r(p)$.
````

````{prf:proof}
Siehe z.B. {cite:p}`neeb_2017` Satz 4.13.
````

Als Korollar erhält man die Tatsache, dass Ableitungen holomorpher Funktionen selbst holomorph sind. Somit ist jede holomorphe Funktion unendlich oft differenzierbar.

````{prf:corollary}
:label: cor:infholo

Es sei $U\subset\C$ offen und $f:U\to\C$ holomorph, dann ist $f^\prime:U\to\C$ auch holomorph und für $\overline{B_r(p)}\subset U$ gilt

```{math}
f^{(n)}(w) = \frac{n!}{2\pi i} \int_{\partial B_r(p)} \frac{f(z)}{(z-w)^{n+1}}\, dz
```

für alle $w\in B_r(p)$.
````

Als weiteres Korollar erhalten wir, dass holomorphe Funktionen analytisch sind, was die Umkehrung zu {prf:ref}`thm:analytischHolomorph` ist.

````{prf:corollary}
Es sei $f:B_r(p)\to\C$ holomorph, dann ist $f$ für jeden Punkt $w \in B_r(p)$ durch eine konvergente Potenzreihe darstellbar (also analytisch),

```{math}
f(w) = \sum_{n=1}^\infty a_n (w-p)^n,
```

deren Koeffizienten $(a_n)_{n\in\N}$ für alle $r^\prime < r$ gegeben sind durch

```{math}
a_n  = \frac{1}{2\pi i}\,\oint_{\partial B_{r^\prime}(p)} \frac{f(z)}{(z - p)^{n+1}}\,dz.
```
````

````{prf:proof}
Siehe z.B. {cite:p}`baldes_2018` S.325f.
````

## Der Satz von Lioville

Eine weitere interessante Folgerung aus der Integralformel ist der Satz von Liouville.

```{margin} Joseph Liouville
[Joseph Liouville](https://de.wikipedia.org/wiki/Joseph_Liouville) (Geboren 24. März 1809 in Saint-Omer; Gestorben 8. September 1882 in Paris) war ein französischer Mathematiker.
```

````{prf:theorem} Satz von Lioville
Jede beschränkte holomorphe Funktion $f:\C\to\C$ ist konstant.
````

````{prf:proof}
Es gelte $\abs{f(z)}< C <\infty$ für alle $z\in\C$, dann gilt nach {prf:ref}`cor:infholo`, dass

```{math}
f^\prime(w) = \frac{1}{2\pi i} \int_{\partial B_r(w)} \frac{f(z)}{(z-w)^2}\, dz
```

für alle $w\in \C$ und alle $r> 0$. Damit folgt

```{math}
\abs{f^\prime(w)}\leq \frac{C}{2 \pi} \abs{\int_{\partial B_r(w)} dz}\leq \frac{C}{r}.
```

Da diese Ungleichung für alle $r>0$ und $w\in\C$ gilt folgt $\abs{f^\prime(w)} = 0$ für alle $w\in\C$ und somit ist $f$ konstant.
````

Hieraus folgt sofort der Fundamentalsatz der Algebra.

````{prf:theorem} Fundamentalsatz der Algebra
Hat ein Polynom 

```{math}
f(z)=\sum_{j=0}^N a_j z^j
```

keine Nullstellen, so ist es konstant.
````

````{prf:proof}
Wir nehmen o.B.d.A. an, dass $a_N=1$ gilt. Dann existiert ein Polynom $g$, s.d. $f(z) = z^n + g(z)$ und

```{math}
\lim_{z\to\infty} \frac{g(z)}{z^n} = 0,
```

wir finden also $r>0$, s.d. $\abs{g(z)} < 1/2 \abs{z^n}$ für alle $\abs{z}>r$. Dann folgt auch

```{math}
\abs{f(z)} = \abs{z^n + g(z)} \geq \abs{z^n} - 1/2 \abs{z^n}\geq r^n/2.
```

Besitzt $f$ keine Nullstellen, so ist $1/f:\C\to\C$ eine auf ganz $\C$ holomorphe Funktion. Weiterhin gilt 

```{math}
\abs{1/f(z)} \leq \frac{2}{r^n}
```

für alle $\abs{z}\geq r$ und somit

```{math}
\abs{1/f} \leq \max\{\max_{B_r(0)} \abs{f(z)}, \frac{2}{r^n} \} < \infty
```

daher ist $1/f$ beschränkt und nach dem Satz von Liouville konstant. Damit ist auch $f$ konstant.
````
