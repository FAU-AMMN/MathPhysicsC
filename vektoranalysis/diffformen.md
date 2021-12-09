# Differentialformen

In diesem Kapitel werden wir nun [Differentialformen](https://de.wikipedia.org/wiki/Differentialform) einführen. Die entscheidende Neuerung im Vergleich zum vorhergehenden Kapitel, ist 
dass wir zusätzlich zur Vektorraumstruktur nun ein Konzept von Räumlichkeit einführen, speziell betrachten wir eine offene Menge $U\subset\R^n$. Ein weiterer wichtiger Aspekt, ist dass wir im Folgenden mit glatten Funktion arbeiten wollen, d.h., mit dem Raum $C^\infty(U,\R^n)$.

## Mannifaltigkeiten

Wir beschäftigen uns im folgenden zunächst mit Mannigfaltigkeiten, bzw. speziell mit differenzierbaren Mannigfaltigkeiten. A priori betrachten wir hier topologische Räume $\M$ mit speziellen Strukturen und Eigenschaften. 

**Was ist ein topologischer Raum?**

Wir wiederholen kurz den Begriff des topologischen Raums. Das zentrale Konzept sind hier sogenannte offene Mengen. Konkret sei $\M$ eine Menge und $\tau\subset 2^\M$ eine Teilmenge der Potenzmenge, dann heißt $(\M,\tau)$ topologischer Raum, falls die folgenden Eigenschaften erfüllt sind, 

* $\emptyset, \M \in \tau$,

* für eine beliebige (insbesondere auch unendlich große) Indexmenge $I$ seien $U_i\in\tau, i\in I$, dann gilt 

```{math}
    \bigcup_{i\in I} U_i \in \tau,
```

* für endlich viele $U_j\in\tau, j=1,\ldots, k$ gilt

```{math}
    \bigcap_{j=1}^k U_j \in \tau.
```

Man nennt hier $\tau$ die **Topologie** und Elemente davon $U\in\tau$ **offene Mengen**. Für jeden Punkt $x\in \M$ nennen wir eine offene Menge $U(x)$ **Nachbarschaft** oder **Umgebung** um $x$, falls $x\in U(x)$.

**Warum betrachten wir Mannigfaltigkeiten?**

Wir haben bereits gesehen, wie man im mehrdimensionalen differenziert, siehe z.B., [MP-2 Skript](https://fau-ammn.github.io/MathDataScience2/ableitungen/ableitungen.html). In vielen Bereichen der Physik und der Mathematik möchte man aber nicht nur af offenen Teilmengen des $\R^d$ ableiten, stattdessen benötigt man auch ein ähnliches Konzept für topologische Räume $\M$. Betrachten wir z.B. die Oberfläche der Einheitskugel im $\R^3$,

```{math}
(x,y,z)\in\R^3,\text{ s.d. } x^2 + y^2 + z^2 = 1
```

so erlaubt uns unsere bisheriges Konzept von Differenzierbarkeit nicht, auf diesem Objekt abzuleiten.

**Wie können wir den Ableitungsbegriff auf topologische Räume übertragen?**

Die grundlegende Idee ist es, den topologischen Raum $\M$ lokal mit einer Teilmenge des $\R^n$ zu identifizieren. Für eine belibige offene
Teilmenge $U\subset \M$ betrachten wir also eine Abbildung $\phi:U\rightarrow \phi(U) \R^n$. Wir wollen hierbei aber nur injektive Abbildungen betrachten, s.d., eine inverse Abbildung $\phi^{-1}:\phi(U)\rightarrow U$ existiert. Haben wir also eine Funktion $f:\M\to\R$ gegeben die wir ableiten möchten, so sehen wir dass die Verknüpfung

```{math}
f \circ \phi^{-1} : \R^n \supset \phi(U)\to \R
```

rein konzeptionell in den bekannten Rahmen passt.

````{prf:example}
Kurve
````

Um den Ableitungsbegriff tatsächlich definieren zu können, benötigen wir aber zusätzlich zur Bijektivität die Bedingung, dass für jede Teilmenge $V\subset U$ gilt,

```{math}
\phi(V)\text{ ist offen}\Leftrightarrow V \text{ ist offen}.
```

Erste Implikation: $\phi(V)$ ist offen $\Rightarrow V $ ist offen.

Für jede offene Menge $E\subset\phi(U)$ haben wir $E=\phi(\phi^{-1}(E))$, somit ist diese Implikation äquivalent zur Forderung, dass Urbilder offener Mengen selbst wider offen sind. Diese bedeutet wiederum genau, dass $\phi$ stetig ist. Insbesondere sehen wir, dass es für den Begriff der Stetigkeit reicht auf einer Topologie zu arbeiten.

Zweite Implikation: $\phi(V)$ ist offen $\Leftarrow V $ ist offen.

Analog zur obigen Überlegung sehen wir, dass diese Bedingung gerade aussagt, dass $\phi^{-1}$ stetig ist. Das folgende Beispiel zeigt, dass es tatsächlich stetige bijektive Abbildung gibt, s.d. $\phi^{-1}$ nicht stetig ist.

````{prf:example}
:label: ex:nonho

Wir betrachten die Funktion 

```{math}
\phi:[0,2\pi)\to\R^2,\\
\phi(t):= (\cos(t), \sin(t)).
```

Wir erkennen, dass $\S^1 = \phi([0,2\pi))$ gerade der Einheitskreis ist und, dass $\phi:[0,2\pi)\to\S^1$ bijektiv und stetig ist.
Allerdings sehen wir, dass die Umkehrabbildung nicht stetig ist. Sei dazu $(x_i)_{i\in\N}$ eine Folge von Punkten, s.d. für alle $i\in\N$ gilt,

```{math}
x_i&\in \S^1,\\
(x_i)_2 &<0,\\
\lim_{i\rightarrow\infty} x_i &=: x = (1,0).
```

Dann sehen wir aber, dass 

```{math}
\lim_{i\to\infty} \phi^{-1} (x_i) = 2\pi \neq 0 = \phi^{-1}(x)
```

und somit ist $\phi^{-1}$ nicht stetig.

````

```{figure} ../img/nonhomöo.jpg
---
height: 450px
name: "fig:nonh"
---
Visualisierung für {prf:ref}`ex:nonho`.
```

Insgesamt forder wir also, dass $\phi:U\rightarrow\phi(U)$ bijektiv ist und, dass $\phi,\phi^-1$ stetig sind,eine solche Abbildung nennt man auch **Homöomorphismus**. Speziell im Kontext von Mannigfaltigkeiten haben nun das Konzept einer **Karte** eingeführt.

```{prf:definition} Karte
Es sei $\M$ ein topologischer Raum, $U\subset\M$ offen und $\phi:U\rightarrow \phi(U)\subset \R^n$ sei ein Homöomorphismus, dann heißt das Tupel $(U,\phi)$ **Karte** auf $\M$.
```

Die Situation nun den Ableitungsbegriff für Funktionen $f:\M\to\R$ über eine Karte $(U,\phi)$ und der Verknüpfung $f\circ \phi$ zu definieren ist noch immer nicht komplett durchdacht. Denn in der Situation, dass $(V,\psi)$ eine zweite Karte ist mit $U\cap V\neq \emptyset$ erhalten wir auf dem Schnitt dieser Mengen zwei Parametrisierungen,

```{math}
f\circ \phi^{-1} = (f\circ\psi^{-1})\circ(\psi\circ \phi^{-1}),\\
f\circ \psi^{-1} = (f\circ\phi^{-1})\circ(\phi\circ \psi^{-1}).
```

````{prf:definition}
Es sei $\M$ ein topologischer Raum und $(U,\phi), (V,\psi)$ zwei Karten auf $\M$ mit nicht-leerem Schnitt, d.h., $U\cap V\neq \emptyset$. Dann nennt man 

```{math}
\psi\circ\phi^{-1}: \phi(U\cap V)\rightarrow \psi(U\cap V)
```

**Kartenwechsel**.

````

```{figure} ../img/chartchange.jpg
---
height: 450px
name: "fig:chartchange"
---
Kartenwechsel.
```

Wir erkennen also, dass Umparametrisierungen der Form $\psi\circ \phi^{-1}$ entscheidend sind. Wäre nun $\psi\circ \phi^{-1}$ und respektive $\phi\circ \psi^{-1}$ differnzierbar, so könnte man die jeweiligen Ableitungen leicht durch die Kettenregel ineinander umrechnen. Allerdings existieren durchaus Fälle, in welchen sowohl $f\circ\phi^{-1}$ als auch $f\circ\psi^{-1}$ differenzierbar sind, aber $\psi\circ\phi^{-1}$ nicht. Deshalb führt man zusätzlich folgenden Begriff ein.

````{prf:definition} Atlas
Es sei $\M$ ein topologischer Raum, eine Familie von Karten $\mathcal{A} = (U_i,\phi_i)_{i\in I}$ indiziert durch die Indexmenge $I$ heißt **Atlas**, falls 

```{math}
M = \bigcup_{i\in I} U_i.
```

Wir nennen einen Atlas $k$-mal differenzierbar oder von der der Klasse $C^k$, falls jeder Kartenwechsel $\phi_i^{-1}\circ\phi_j, i,j\in I$ $k$-mal stetig differenzierbar ist.

````

### Differenzierbare Struktur

Für eine topologischen Raum $\M$ können mehrere Atlanten $\mathcal{A}$  existieren, weshalb man zusätzlich eine Äquivalenzklasse definiert. Für eine Differenzierbarkeitsstufe $k\in \N \cup \{\infty\}$ heißen zwei $C^k$ Atlanten  $\mathcal{A}_1, \mathcal{A}_2$ $k$-äquivalent, $\mathcal{A}_1\sim_k \mathcal{A}_2$, falls ihre Vereinigung

```{math}
\mathcal{A}_1\cup \mathcal{A}_2
```

ein $C^k$ Atlas ist. Die Äquivalenzklasse $[\mathcal{A}]_{\sim_k}$ nennt man $C^k$-differenzierbare Struktur.

### Differenzierbare Mannigfaltigkeiten

```{margin}
[Felix Hausdorff](https://de.wikipedia.org/wiki/Felix_Hausdorff) (geboren am 8. November 1868 in Breslau; gestorben am 26. Januar 1942 in Bonn) war ein deutscher Mathematiker.
```

Bisher haben wir $\M$ als topologischen Raum betrachtet. In vielen Anwendungen benötigt man aber zusätzliche. Insbesondere wenn man [glatte Testfunktionen](https://de.wikipedia.org/wiki/Testfunktion) und [die Zerlegung der Eins](https://en.wikipedia.org/wiki/Partition_of_unity) benutzen möchte braucht man folgende zwei Eigenschaften.

````{prf:definition} Hausdorff-Raum
Ein topologischer Raum $\M$ heißt **Hausdorff-Raum**, falls für je zwei unterschiedliche Punkte $x,y\in \M, x\neq y$ offene Umgebungen $U(x), U(y)$ existieren, welche disjunkt sind, d.h., $U(x)\cap U(y) = \emptyset$.
````

````{prf:definition} Zweites Abzählbarkeitsaxiom
Ein toplogischer Raum $\M$ erfüllt das **zweite Abzählbarkeitsaxiom**, falls **abzählbar** viele offene Mengen $(V_i)_{i\in\N}$existieren, s.d., für jedes $x\in \M$ und jede Umgebung $U(x)$ mindestens ein $k\in\N$ existiert, s.d., $V_k\subset U(x)$.
````

Diese zwei Bedingung wirken zunächst abstrakt, allerdings werden sie von vielen Räumen erfüllt. So ist z.B. jeder metrische Raum ein zweitabzählbarer Hausdorff-Raum.

```{danger}
Falls der Begriff eines zweitabzählbaren Hausdorff-Raums zu unhandlich erscheint, kann man für die meisten Anwendungen in der Physik auch einfach metrische Räume betrachten.
```

Wir sind nun in der Situation den Begriff einer Mannigfaltigkeit einzuführen.

````{prf:definition} Mannigfaltigkeit
Es sei $\M$ ein zweitabzählbarer Hausdorff-Raum und für $k\in\N\cup \{\infty\}$ sei $A$ eine $C^k$-differenzierbare Struktur, dann heißt $(M,A)$ 
$k$-**mal differenzierbare Mannigfaltigkeit**. Für $k=\infty$ spricht man auch von einer **glatten** Mannigfaltigkeit. Bilden alle Karten in $\M$ nach $\R^n$ ab, so nennt man die MAnnigfaltigkeit $n$-dimensional.
````

In den meisten Fällen spricht man nur von der Mannigfaltigkeit $\M$, die differenzierbare Struktur $A$ wird dabei implizit vorausgesetzt.

### Ableiten auf Mannigfaltigkeiten

Sei nun $M$ eine $k$-mal differenzierbare Mannigfaltigkeit mit Atlas $\mathcal{A}$, dann heißt $f:\M\to\R$ $k$-mal differenzierbar, falls für jedes $p\in\M$ eine differenzierbare Karte $(u,\phi)\in\mathcal{A}$ existiert, sodass $f\circ\phi^{-1}\in C^k(\phi(U))$. Insbsondere schreiben wir in diesem Fall $f\in C^k(\M)$. In vielen Anwendungen betrachtet man nur glatte Mannigfaltigkeiten und Funktionen. Wir werden im folgenden auch dazu übergehen.

````{prf:lemma}
Es sei $\M$ eine glatte Mannigfaltigkeit, dann ist $C^\infty(\M)$ ein reeller Vektorraum mit den Verknüpfungen

```{math}
(f + g)(p) := f(p) + g(p)\quad\text{ für } f,g\in C^\infty(\M),\\
(\lambda \cdot f)(p) := \lambda\cdot f(p)\text{ für } f\in C^\infty(\M), \lambda\in\R.
```

````

````{proof}
Siehe Übung
````

Wir halten insbesondere fest, dass die Differenzierbarkeit Kartenunabhängig ist.

````{prf:lemma}
Es sei $\M$ eine glatte Mannigfaltigkeit mit Atlas $\mathcal{A}$, $f:\M\to\R$ eine Funktion und $(U,\phi)\in A$ eine Karte mit $p\in U$. Ist $f\circ\phi$ differenzierbar in $p$, so ist $f\circ\psi$ auch differenzierbar in $p$ für jede Karte $(V,\psi)$ mit $p\in V$.
````

````{proof}
Siehe Übung.
````

### Der Tangentialraum

Zusätzlich zum obigen Ableitungsbegriff definieren wir die sogenannte **Richtungsableitung** einer Funktion $f:\M\to\R$. Hierbei, betrachten wir *Kurven* $\gamma:(-t,t)\to\M$ und interessieren uns für das Verhalten der Abbildung $f\circ\gamma$.

````{prf:example}
Es sei $\M=\S^2$ die Einheitssphäre und $u:\M\to\R$ beschreibe eine Wärmeverteilung auf der Kugeloberfläche. Betrachtet man nun die Bahn eines Partikels auf der Oberfläche beschrieben durch $\gamma:(-t, t)\to \M$ so erhalten wir eine eindimesnionale Abbildung 

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

Es ist in diesem Fall einen verallgemeinerten Begriff der Geschwindikeit zu definieren. Für eine gegeben Bahnkurve ist diese eine lineare Abbildung, welche jeder glatten Funktion $f:\M\to\R$ den Wert der Richtungsableitung zuweist.

````{prf:definition} Geschwindigkeit
Es sei $\M$ eine glatte Mannigfaltigkeit, $f\in C^\infty(\M)$ und 
````

### Bündel


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