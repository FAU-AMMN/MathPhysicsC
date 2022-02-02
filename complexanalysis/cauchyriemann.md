# Cauchy-Riemann Gleichungen

Der zentrale Begriff der Funktionentheorie ist der einer *holomorphen Funktion*.

````{prf:definition} Holomorphe Funktion
:label: def:holomorph

Sei $D \subset \C$ eine offene Teilmenge und $f \colon D \rightarrow \C$ eine stetige Funktion.

Wir nennen die Funktion $f$ **holomorph** auf der Teilmenge $D$, wenn es für jeden Punkt $z \in D$ eine komplexe Ableitung der Funktion $f$ gibt mit

```{math}
f'(z) = \lim_{h\rightarrow 0} \frac{f(z+h) - f(z)}{h}.
```

````

Der Differentialquotient in {prf:ref}`def:holomorph` erinnert sehr an die Definition der Ableitung einer reellen Funktion.
Der grundlegende Unterschied ist hier jedoch, dass $h \in \C$ komplex ist.
Interpretiert man den Körper der komplexen Zahlen als zweidimensionalen reellen Vektorraum, so muss für die beiden Richtungsableitungen $x := \operatorname{Re}(z)$ und $y := \operatorname{Im}(z)$ gelten

```{math}
\partial_x f(z) = \lim_{\epsilon \rightarrow 0} \frac{f(z+\epsilon) - f(z)}{\epsilon} = \lim_{\epsilon \rightarrow 0} \frac{f(z+i\epsilon) - f(z)}{i\epsilon} = -i \partial_y f(z), \quad \epsilon \in \R.
```

Dieser Zusammenhang ist charakteristisch für holomorphe Funktionen und wird im folgenden Satz präzisiert.

````{prf:theorem} Cauchy-Riemann Gleichungen
Sei $D \subset \C$ eine offene Teilmenge und $f \colon D \rightarrow \C$ eine stetige Funktion für die gilt

```{math}
f(z) = u(z) + i v(z), \qquad u,v \colon D \rightarrow \R.
```

Dann ist die Funktion $f$ genau dann holomorph auf der Teilmenge $D$, wenn die folgenden **Cauchy-Riemann Gleichungen** auf ganz $D$ gelten:

```{math}
\partial_x u = \partial_y v, \qquad \partial_y u = -\partial_x v.
```

````

````{prf:proof}
Schulz-Baldes S.313
````

````{prf:example} Holomorphe Funktionen
Ableitung eines komplexen Monoms -> Beispiel 10.4 auf S.314 in Schulz-Baldes

$f(z) := \overline{z}$ ist nicht holomorph -> Beispiel 10.7 auf S.315 in Schulz-Baldes
````

Eine besondere Klasse von Funktionen sind *analytische Funktonen*, die sich lokal mit Hilfe von Reihen darstellen lassen.

````{prf:definition} Analytische Funktion
Sei $D \subset \C$ eine Teilmenge und $f \colon D \rightarrow \C$ eine Funktion.

Wir nennen die Funktion $f$ **analytisch** in einem Punkt $z_0 \in D$ genau dann, wenn ein $\epsilon > 0$ existiert, so dass sich jeder Funktionswert $f(z) \in \C$ in einer entsprechenden lokalen Umgebung durch eine absolut konvergente Reihe darstellen lässt mit 

```{math}
f(z) = \sum_{n \geq 0} a_n (z-z_0)^n, \qquad \forall |z - z_0| < \epsilon,
```

wobei $(a_n)_{n_\in\N}$ eine Folge in $\C$ ist.

Wir nennen die Funktion $f$ analytisch auf der Teilmenge $D$, wenn sie analytisch ist für alle Punkte $z_0 \in D$.

````

Der folgende Satz beschreibt den Zusammenhang zwischen analytischen und holomorphen Funktionen.

````{prf:theorem}
:label: thm:analytischHolomorph
Jede analytische Funktion $f$ auf einer Teilmenge $D \subset \C$ ist auch holomorph auf $D$.
````

````{prf:proof}
Vertauschung des Limes $h \rightarrow 0$ und der Summe.
````

Wie wir später im Hauptsatz der Funktionentheorie sehen werden gilt auch die Umkehrung.