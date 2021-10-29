
# Hamiltonsche Differentialgleichungen

Ein wichtiges Prinzip für viele physikalischen Anwendungen und dynamische System sind *Erhaltungssätze* und die dazugehörigen *Erhaltungsgrößen*. 
Aus der klassichen Mechanik kennen wir beispielsweise die *Energieerhaltung* oder die *Impulserhaltung*. 

In []{s:fluesse} haben wir Bewegungslgleichungen als System von DGLs hergeleitet und gelöst, deshalb wollen wir nun die nötige Theorie entwickeln, die es uns erlaubt Erhaltungsgrößen direkt aus der Formulierung des Differentialgleichungssystems abzulesen.
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
In dieser Vorlesung verzichten wir auf diesen Zugang zur Hamilton-Funktion und verweisen die interessierten Leser\*innen auf {cite}.
2. Im Folgenden werden wir annehmen, dass die Hamilton-Funktion $H$ nicht explizit von der Zeitvariable $t \in I$ abhängt, was jedoch im Allgemeinen sein kann.
````

Basierend auf der Hamilton-Funktion aus {prf:ref}`def:hamiltonsch` können wir nun die Hamiltonschen Differentialgleichungen definieren.

````{prf:definition} Hamiltonsche Differentialgleichung
Sei $x(t) = (p(t),q(t)) \in U$ eine Bahnkurve des Phasenraums $U \subset \R^{2n}$.
Wird das hamiltonsche Vektorfeld auf der linken Seite von [](eq:hamilton_Gleichung) als 

```{math}
X = \dot{x}(t) = \begin{pmatrix} \dot{p} \\ \dot{q} \end{pmatrix} (t)
```

gewählt, so lässt sich die Gleichung schreiben als

```{math}
:label: hamilton_DGL
\dot{x}(t) = J \nabla H(x(t)).
```

In dieser Form wird die entstehende Differentialgleichung in []{eq:hamilton_DGL} **Hamiltonsche Differentialgleichung** genannt.
````

Für diesen einfachen Fall lässt sich beobachten, dass die Lösungskurven der Hamiltonschen Differentialgleichungen sich nicht schneiden und durch jeden Punkt des Phasenraums eine Lösungskurve verläuft. 

Die Hamilton-Funktion $H$ als Funktion des Phasenraumes kann als die Energie eines Systems von Teilchen aufgefasst werden.
Wir wollen uns die Rolle der Hamilton-Funktion $H$ an Hand eines physikalischen Beispiels klar machen.

````{prf:example} Newtonsche Kraftgleichung
Im folgenden Beispiel wollen wir die Bewegung eines Teilchens mit Masse $m>0$ in einem Kraftfeld $F \colon \R^3 \rightarrow \R^3$  untersuchen, welches nur vom Ort $q \in \R^3$ abhängt.
Nach dem 2. Newtonschen Gesetz erhalten wir die Bewegungsgleichung

```{math}
:label: eq:newton
m\ddot{q}(t) = F(q(t)).
```

Die gewöhnliche Differentialgleichung 2. Ordnung in []{eq:newton} lässt sich durch die Definition des Impulses des Teilchens $p(t) \, \coloneqq \, m \dot{q(t)}$ in ein gewöhnliches Differentialgleichungssystem 1. Ordnung überführen:

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

Definieren wir nun die **Hamilton-Funktion** aus {prf:ref}`def:hamiltonsch`

```{math}
H(p,q) \, \coloneqq \, \frac{||p||^2}{2m} + V(q),
```

so erkennen wir, dass diese sich aus *kinetischer* und *potentieller Energie* zusammensetzt. 
Durch diese Hamilton-Funktion $H$ lässt sich []{eq:newton} als **Hamiltonsche Differentialgleichung** schreiben mit

```{math}
X = \begin{pmatrix}\dot{p} \\ \dot{q} \end{pmatrix} = \begin{pmatrix} -\nabla V(q) \\ \frac{p}{m} \end{pmatrix} = \begin{pmatrix}0 & -\mathbf{1}\\ \mathbf{1} & 0 \end{pmatrix} \begin{pmatrix} \frac{p}{m} \\ \nabla V(q) \end{pmatrix} = J \nabla H(p,q).
```

````

Ergänzend wollen wir noch folgendes Beispiel einer Hamilton-Funktion nennen im Folgenden nennen.


````{prf:example}
Im Fall des eindimensionalen harmonischen Oszillators aus []{ex:oscillations} lässt sich ebenfalls eine Hamilton-Funktion des dynamischen Systems angeben. 
Sei $(x,p) \in U$ als Punkt des Phasenraums $U \subset \R^2$ der Ort und Impuls eines Pendels.
Dann lässt sich die zugehörige Hamilton-Funktion $H \colon U \rightarrow \R$ angeben als:

```{math}
H(x,p) = \frac{p^2}{2m} + \frac{m}{2} \omega^2 x^2.
```

Hierbei bezeichnet $\omega = \sqrt{\frac{k}{m}}$ die Eigenfrequenz des Systems.
````


