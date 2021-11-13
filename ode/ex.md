# Aufgaben

````{admonition} Aufgabe: DGL höherer Ordnung
:class: hint

Gegeben sei folgende gewöhnliche Differentialgleichung 4.~Ordnung:

```{math}
x^{(4)}(t) = 7 x^{(3)}(t) - \dot x(t) + 5 x(t) + t^2
```

Überführen Sie diese in ein System gewöhnlicher Differentialgleichungen 1.Ordnung.

````

````{admonition} Aufgabe: Autonome gewöhnliche Differentialgleichungen
:class: hint

Entscheiden und begründen Sie mathematisch, ob die folgenden gewöhnlichen Differentialgleichungen **autonom** sind.

**a)** Differentialgleichung für harmonischen Oszillator:

```{math}
\ddot x(t) + \lambda x(t) = 0
```

für eine Konstante $\lambda \in \mathbb{R}$.

**b)** Newtonsche Kraftgleichung:

```{math}
m \ddot x(t) = F(t, x(t))
```

für eine Konstante $m > 0$, eine Kraft $F: \mathbb{R} \times \mathbb{R}^3 \rightarrow \mathbb{R}^3$, welche von der Position im Raum $x: \mathbb{R} \rightarrow \mathbb{R}^3$ und der Zeit $t \in \mathbb{R}$ abhängt.

**c)** Newtonsche Kraftgleichung:

```{math}
m \ddot x(t) = F(t, x(t))
```

für eine Konstante $m > 0$, eine Kraft $F: \mathbb{R}^3 \rightarrow \mathbb{R}^3$, welche im Gegensatz zur Situation in b) lediglich von der Position im Raum $x: \mathbb{R} \rightarrow \mathbb{R}^3$ abhängt.

**d)** Mathieusche Differentialgleichung:

```{math}
\ddot x(t) + [\lambda + \gamma \cos(t)] ~ x(t) = 0
```

für Konstanten $\lambda, \gamma \in \mathbb{R}$.
````

````{admonition} Flüsse
:class: hint

Für $I = \mathbb{R}^0_+$ und $U = \mathbb{R}^2$ betrachten wir die Abbildung $\phi: I \times U \rightarrow U$ mit 

```{math}
\phi(t, x) = 
\begin{pmatrix} \frac{x_2}{2} ~ \sin(\omega t) + x_1 ~ \cos(\omega t) \\ x_2 ~ \cos(\omega t) - 2 x_1 ~ \sin(\omega t) \end{pmatrix}, 
```
wobei $x = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}$ gilt.
Zeigen Sie, dass diese Abbildung die mathematischen Eigenschaften eines Flusses erfüllt.
````

````{admonition} Phasenporträt gedämpfter Oszillator
:class: hint

Wir betrachten die Bewegungsgleichung für den harmonischen Oszillator 

```{math}
m ~ \ddot x(t) + r ~ \dot x(t) + k ~ x(t) = 0
```

mit Masse $m = 1  ~ kg$, Dämpfungskonstante $r = 0.5 ~ \frac{kg}{s}$ und Federkonstante $k = 1.5 ~ \frac{kg}{s^2}$.

Wie in Beispiel 1.3 im Skript führen wir den Impuls $p(t) = m ~ \dot x(t)$ ein und erhalten das Differentialgleichungssystem erster Ordnung

```{math}
\dot x(t) &= \frac{1}{m} ~ p(t)\\
\dot p(t) &= -k ~ x(t) - \frac{r}{m} ~ p(t).
```

Zeichnen Sie händisch ein Phasenporträt für dieses System in den Unbekannten $x$ und $p$, indem Sie für die folgenden Punkte $(x,p)$ die durch das Differentialsystem gegebene Steigung berechnen und einzeichnen:

```{math}
(-1, 0) \quad  (1, 0) \quad (0, -1) \quad  (0, 1) \quad (-0.75, -0.75) \quad  (-0.75, 0.75) \quad (0.75, -0.75) \quad (0.75, 0.75)
```

````

````{admonition} Aufgabe: Eigenschaften Hamilton-Funktion
:class: hint

Beweisen Sie die folgende Aussage:

Sei $P \subseteq \mathbb{R}^{2m}$ ein (offener) Phasenraum und $\mathbb{J} = \begin{pmatrix} 0 & - 𝟙 \\ 𝟙 & 0 \end{pmatrix} \in Mat(2m, \mathbb{R})$. Ist die Hamilton-Funktion $H \in C^2(P, \mathbb{R})$, dann ist sie entlang der Lösungskurven der Hamiltonschen Differentialgleichung $\dot x = \mathbb{J} \nabla H(x)$ konstant.
````

````{admonition} Aufgabe: Hamilton-Funktion
:class: hint

Zeigen Sie mathematisch, dass die Hamilton-Funktion eines eindimensionalen harmonischen Oszillators gegeben ist durch:

```{math}
H(x,p) = \frac{p^2}{2m} + \frac{m}{2} w^2 x^2,
```

wobei $w = \sqrt{\frac{k}{m}}$ gilt.

````
