
# Hamiltonsche Differentialgleichungen

Ein wichtiges Prinzip für viele physikalischen Anwendungen und dynamische Systeme sind *Erhaltungssätze* und die dazugehörigen *Erhaltungsgrößen*. 
Aus der klassichen Mechanik kennen wir beispielsweise die *Energieerhaltung* oder die *Impulserhaltung*.
In [](s:fluesse) haben wir Bewegungsgleichungen als System von gewöhnlichen Differentialgleichungen hergeleitet und gelöst, deshalb wollen wir nun die nötige Theorie entwickeln, die es uns erlaubt Erhaltungsgrößen direkt aus der Formulierung des Differentialgleichungssystems abzulesen.

Hamiltonsche Differentialgleichungen haben in der Physik eine besondere Rolle, insbesondere in der klassischen Mechanik bei Abwesenheit von Reibung.
Typischerweise tauchen diese bei der Untersuchung von Bewegungen im Phasenraum auf, d.h., bei der Betrachtung von Paaren aus Orts- und Impulswerten.
Ihre Lösungen liefern uns Trajektorien im Phasenraum für die die Gesamtenergie des Systems erhalten bleibt.
Dies macht sie für uns besonders interessant.

Bevor wir die hamiltonschen Differentialgleichungen und ihre Eigenschaften näher diskutieren führen wir zunächst ein wann wir ein Vektorfeld auf dem Phasenraum Hamiltonsch nennen und was eine Hamilton-Funktion dieses Vektorfelds ist.

````{prf:definition} Hamilton-Funktion
:label: def:hamiltonsch

Sei $n \in N$ die **Anzahl der Freiheitsgrade** des betrachteten dynamischen Systems und sei $U\subset \R^n \times \R^n$ der zugehörige Phasenraum. 
Wir nennen ein Vektorfeld $X \colon U \rightarrow \R^{2n}$ mit $X \in C^1(P;\R^{2n})$ **Hamiltonsch**, falls eine reellwertige Funktion $H \colon U \rightarrow \R$ sowie eine Matrix $J \, \coloneqq \, \begin{pmatrix}0 & -\mathbf{1}\\ \mathbf{1} & 0 \end{pmatrix} \in \R^{2n \times 2n}$ existiert, so dass sich das Vektorfeld darstellen lässt als

```{math}
:label: eq:hamilton_Gleichung
X(p,q) = J \, \nabla H (p,q) \quad \forall (p,q) \in U.
```

In diesem Fall nennen wir die Funktion $H$ eine **Hamilton-Funktion** des Vektorfelds $X$.

````

Folgende Bemerkungen zur Hamilton-Funktion wollen wir festhalten.

````{prf:remark}
1. Die Hamilton-Funktion lässt sich auch als Legendre-Transformation der Lagrange-Funktion des Systems herleiten, was weitere interessante Zusammenhänge in der Physik erklärt.
In dieser Vorlesung verzichten wir auf diesen Zugang zur Hamilton-Funktion und verweisen die interessierten Leser\*innen auf Kapitel 2 {cite:p}`nolting_2011`.
2. Im Folgenden werden wir annehmen, dass die Hamilton-Funktion $H$ nicht explizit von der Zeitvariable $t \in I$ abhängt, was jedoch im Allgemeinen sein kann.
````

Basierend auf der Hamilton-Funktion aus {prf:ref}`def:hamiltonsch` können wir nun die Hamiltonschen Differentialgleichungen definieren.

````{prf:definition} Hamiltonsche Differentialgleichung
Sei $x(t) = (p(t),q(t)) \in U$ eine Bahnkurve des Phasenraums $U \subset \R^{2n}$.
Wird das hamiltonsche Vektorfeld auf der linken Seite von [](eq:hamilton_Gleichung) als 

```{math}
X = \dot{x}(t) = \begin{pmatrix} \dot{p} \\ \dot{q} \end{pmatrix} (t)
```

gewählt, so lässt sich die Gleichung für $J \, \coloneqq \, \begin{pmatrix}0 & -\mathbf{1}\\ \mathbf{1} & 0 \end{pmatrix} \in \R^{2n \times 2n}$ schreiben als

```{math}
:label: eq:hamilton_DGL
\dot{x}(t) = J \nabla H(x(t)).
```

In dieser Form wird die entstehende Differentialgleichung in [](eq:hamilton_DGL) **Hamiltonsche Differentialgleichung** genannt.

Äquivalent lässt sich dieses System von gewöhnlichen Differentialgleichungen auch explizit für die $2n$ unbekannten Orts- und Impulsfunktionen $q_i, p_i$ für $1 \leq i \leq n$ schreiben als

```{math}
\dot{q_i}(t) = \frac{\partial H}{\partial p_i}(t), \quad \dot{p_i}(t) = -\frac{\partial H}{\partial q_i}(t), \quad i=1,\ldots,n.
```

````

Für den einfachen Fall einer zeitunabhängigen Hamilton-Funktion $H$ lässt sich beobachten, dass die Lösungskurven der Hamiltonschen Differentialgleichungen sich nicht schneiden und durch jeden Punkt des Phasenraums eine Lösungskurve verläuft. 

Die Hamilton-Funktion $H$ als Funktion des Phasenraumes kann als die Energie eines Systems von Teilchen aufgefasst werden.
Wir wollen uns die Rolle der Hamilton-Funktion $H$ an Hand eines physikalischen Beispiels klar machen.

````{prf:example} Newtonsche Kraftgleichung
Im folgenden Beispiel wollen wir die Bewegung eines Teilchens mit Masse $m>0$ in einem Kraftfeld $F \colon \R^3 \rightarrow \R^3$  untersuchen, welches nur vom Ort $q \in \R^3$ abhängt.
Nach dem 2. Newtonschen Gesetz erhalten wir die Bewegungsgleichung

```{math}
:label: eq:newton
m\ddot{q}(t) = F(q(t)).
```

Die gewöhnliche Differentialgleichung 2. Ordnung in [](eq:newton) lässt sich durch die Definition des Impulses des Teilchens $p(t) \, \coloneqq \, m \dot{q(t)}$ in ein gewöhnliches Differentialgleichungssystem 1. Ordnung überführen:

```{math}
\dot{p}(t) = F(q(t)), \quad \dot{q}(t) = \frac{1}{m}p(t).
```

Wir nehmen zur Vereinfachung nun an, dass das gegebene Kraftfeld $F$ *konservativ* sei, d.h., wir können annehmen, dass $F = - \nabla V$ gilt für ein Potential $V \colon \R^3 \rightarrow \R$ (z.B. die Erdanziehungskraft). 
Dann können wir das physikalische Modell als kontinuierliches dynamisches System interpretieren mit dem erweiterten Phasenraum $I \times U \subset \R^+_0 \times \R^6$.
Betrachten wir nun einen Punkt $x = \begin{pmatrix} p \\ q\end{pmatrix} \in U$ im Phasenraum, so lässt sich das autonome gewöhnliche Differentialgleichungssystem kompakt schreiben als 

```{math}
:label: eq:newton_DGL
\dot{x}(t) = \begin{pmatrix} \dot{p} \\ \dot{q} \end{pmatrix}(t) = \begin{pmatrix} -\nabla V(q) \\ \frac{p}{m} \end{pmatrix}(t)
```

Wählen wir nun die **Hamilton-Funktion** aus {prf:ref}`def:hamiltonsch`

```{math}
H(p,q) \, \coloneqq \, \frac{||p||^2}{2m} + V(q),
```

so erkennen wir, dass diese sich aus *kinetischer* und *potentieller Energie* zusammensetzt. 
Durch diese Hamilton-Funktion $H$ lässt sich [](eq:newton) als **Hamiltonsche Differentialgleichung** schreiben mit

```{math}
\dot{x}(t) = \begin{pmatrix}\dot{p} \\ \dot{q} \end{pmatrix}(t) = \begin{pmatrix} -\nabla V(q) \\ \frac{p}{m} \end{pmatrix}(t) = \begin{pmatrix}0 & -\mathbf{1}\\ \mathbf{1} & 0 \end{pmatrix} \begin{pmatrix} \frac{p}{m} \\ \nabla V(q) \end{pmatrix}(t) = J \nabla H(p(t),q(t)).
```

````

Ergänzend wollen wir noch folgendes Beispiel einer Hamilton-Funktion nennen.


````{prf:example}
Im Fall des eindimensionalen harmonischen Oszillators mit Masse $m > 0$ aus {prf:ref}`ex:oscillations` lässt sich ebenfalls eine Hamilton-Funktion des dynamischen Systems angeben. 
Sei $(x,p) \in U$ als Punkt des Phasenraums $U \subset \R^2$ der Ort und Impuls eines Pendels.
Dann lässt sich die zugehörige Hamilton-Funktion $H \colon U \rightarrow \R$ angeben als:

```{math}
H(x,p) = \frac{p^2}{2m} + \frac{m}{2} \omega^2 x^2.
```

Hierbei bezeichnet $\omega = \sqrt{\frac{k}{m}}$ die Eigenfrequenz des Systems und $k > 0$ die Federkonstante.
````

Bisher haben wir noch nicht den Grund diskutiert, warum die Hamilton-Funktion eine besondere Rolle im Kontext dynamischer Systeme spielt.
Das wollen wir nun im folgenden Satz nachholen.

````{prf:theorem}
:label: satz:hamilton_konstant
Sei $n\in \N, U \subseteq \mathbb{R}^{2n}$ ein (offener) Phasenraum und $J= \begin{pmatrix} 0 & - \mathbf{1} \\ \mathbf{1} & 0 \end{pmatrix} \in \mathbb{R}^{2n \times 2n}$.
Ist die Hamilton-Funktion $H \in C^2(U; \mathbb{R})$, dann ist sie entlang der Lösungskurven der Hamiltonschen Differentialgleichung 
\begin{equation*}
\dot x = J \nabla H(x)
\end{equation*}
konstant.
````

````{prf:proof}
In der Hausaufgabe zu zeigen.
````

{prf:ref}`satz:hamilton_konstant` sagt uns also, dass die Orbits des kontinuierlichen Systems innerhalb der Niveaumengen der Hamilton-Funktion verlaufen.
Dies erlaubt es uns dynamische Systeme auf diese häufig auch *Energieschalen* genannten Niveaumengen $H^{-1}(E)$ für $E \in \R$ zu restringieren.
Diese Energieschalen bilden Untermannigfaltigkeiten des Phasenraums $U$.

Für den einfachen Fall eines Freiheitsgrades, d.h., für $n = 1$, lassen sich für eine gegebene Hamilton-Funktion $H$ die Orbits des dynamischen Systems bestimmen.
Für einen Punkt $x \in U$ im Phasenraum $U \subset \R^2$ unterscheiden wir zwei Fälle:

1. Ist $\nabla H(x) = 0$, so ist der Orbit wegem [](eq:hamilton_DGL) von der Form $O(x) = {x}$.

2. Ist $\nabla H(x) \neq 0$, so ist der Orbit $O(x)$ gegeben durch die zusammenhängende Menge

```{math}
O(x) = \{y \in U | H(y) = H(x), \nabla H(y) \neq 0\}
```

Die Orientierung des Orbits erhält man durch die Richtung, die orthogonal zum Gradienten $\nabla H$ steht, d.h., durch Drehung des Gradienten im Uhrzeigersinn um $\frac{\pi}{2}$.
Die Matrix $J$ entspricht eben einer solchen Drehung.

````{prf:remark}
Eine Formulierung der Bewegungsgleichungen eines dynamischen Systems als Hamiltonsche Differentialgleichungen hat den Vorteil, dass sie unter den sogenannten *kanonischen Transformationen* in manchen Fällen in eine einfachere, lösbare Form gebracht werden können.
````