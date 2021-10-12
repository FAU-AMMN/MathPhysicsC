# Flüsse und Phasenportraits

In diesem Abschnitt führen wir zunächst grundlegende Konzepte ein und betrachten danach geometrische Interpretation von DGLs.

Untenstehend die wichtigsten Schlagwörter:

* Fluss {prf:ref}`def:Fluss`,
* lokaler Fluss{prf:ref}`def:LokFluss`,
* Fluss einer DGL,
  * Bahnkurve,
  * Orbit,
  * Ruhelage

## Flüsse

Wir beginnen zunächst damit ein wichtiges Konzept einzuführen, welches die Beschreibung zeitabhängiger Systeme vereinfacht. Die folgende Definition ist zunächst sehr allgemein gehalten und wird später für unsere Anwendungen auf DGLs konkretisiert.

````{prf:definition} Fluss
:label: def:Fluss

Sei $U$ eine Menge und $I=\R^+_0$, dann heißt eine Abbildung $\Phi:I\times U\rightarrow U$ **Fluss**, falls gilt,

1. $\Phi(0, x) = x$ für alle $x\in U$,

2. $\Phi(t, \Phi(x,s)) = \Phi(s + t, x)$ für alle $x\in U$ und alle $s,t\in I$.
````

````{prf:remark} Notation
Anstatt beide Argument in Klammern wie in obiger Definition zu schreiben, benutzt man häufig folgende Darstellung, 

```{math}
\Phi_t(x) = \Phi(t, x).
```

````

In unserem Fall wollen wir speziell die Lösungen einer autonomen DGL

```{math}
\dot{x} = F(x).
```

für $F\in C^1(U;\R^n)$ als Fluss interpretieren. Hierbei soll das zweite Argument jeweils den Anfangswert
$x_0\in U$ angeben und $\Phi(x_0) = \Phi(\cdot, x_0)$ dann eine Lösung der DGL sein, d.h., $\frac{\d}{\d t} \Phi(x_0) = F(\Phi(x_0))$.

Nach dem Satz von Picard-Lindelöf (Kapitel 7, {cite:p}`tenbrinck_2021`) wissen wir, dass für jeden Anfangswert $x_0\in U$ ein $\epsilon(x_0) >0$ existiert, s.d., es eine eindeutige Lösung $\phi: [-\epsilon(x_0), \epsilon(x_0)]$ gibt. In diesem Fall wählen wir also $I(x_0)=[-\epsilon(x_0), \epsilon(x_0)]$. Wir können also nicht wie in {prf:ref}`def:Fluss` auf ganz $\R^+_0$ als Zeitintervall arbeiten. Stattdessen können wir nur Tupel der Form $(x_0, t)$ betrachten, wobei $x_0\in U$ fixiert ist und $t$ aus $I(x_0)$ gewählt werden kann, was wir mithilfe des kartesischen Produkts

\begin{align*}
\{x_0\}\times I(x_0)
\end{align*}

dargestellt werden kann. Dies führt uns auf den Begriff des lokalen Flusses.

````{prf:definition} Lokaler Fluss
:label: def:LokFluss


Sei $U$ eine Menge und die Menge $G\subset \R^+_0\times U$ sei gegeben als 

```{math}
G = \bigcup_{x\in U} \{x\}\times I(x),
```

wobei $0\in I(x)\subset \R^+_0$ für jedes $x\in U$.

Dann heißt eine Abbildung $\Phi: G\rightarrow U$ **lokaler Fluss**, falls

1. $\Phi(0,x) = x$ für alle $x\in U$,

2. $\Phi(t, \Phi(s, x)) = \Phi(s+t, x)$ für alle $x\in U$ und alle $s,t$ s.d. $s, s+t\in I(x)$ und $t\in I(\Phi(x,s))$.

````

Im nächsten Lemma wollen wir nun sehen, dass die Lösung einer DGL tatsächlich als lokaler Fluss interpretiert werden kann.

````{prf:Lemma}
Sei $U\subset\R^n$, $F:U \rightarrow \R^n$ lokal Lipschitz stetig, dann existieren Intervalle $I(x_0)$, sodass es für 

```{math}
G = \bigcup_{x_0\in U} I(x_0)\times\{x_0\},
```

eine Funktion $\Phi:G\rightarrow \R^n$ gibt, mit folgenden Eigenschaften

1. $\frac{\d}{\d t} \Phi(t, x_0) = F(\Phi(t, x_0))$ für alle $(t,x_0)\in G$,

2. $\Phi$ ist ein lokaler Fluss auf $G$.

````

````{prf:remark}
Die Abbildung $\Phi$ bezeichnet man hier auch als**Fluss einer DGL**.
````

````{prf:proof}

Nach dem Satz von Picard-Lindelöf existiert für jedes $x_0\in U$ ein $\epsilon(x_0)>0$ s.d., die Lösung der DGL 
auf $[-\epsilon(x_0),\epsilon(x_0)]$ mit AW $x_0$ existiert. Daher können wir 

```{math}
G = \bigcup_{x_0\in U} [-\epsilon(x_0),\epsilon(x_0)] \times\{x_0\}
```

wählen und $\Phi$ so definieren, dass 

```{math}
\frac{\d}{\d t} \Phi(t, x_0) &= F(\Phi(t, x_0))\\
\Phi(0, x_0) &= x_0
```

für alle $(t, x_0)\in G$. Damit haben wir 1. und die erste Flusseigenschaft gezeigt. Die zweite Flusseigenschaften ist eine direkte Folgerung aus der Eindeutigkeit der Lösung der DGL. Wir führen den Beweis trotzdem explizit aus. Es sei $x_0\in U, s\in [-\epsilon(x_0), \epsilon(x_0)]$ und weiterhin $t$, s.d., $s+t \in [-\epsilon(x_0), \epsilon(x_0)]$ und $t\in [-\epsilon(\Phi(s,x_0)), \epsilon(\Phi(s,x_0))]$. 
Per Definition löst die Funktion

```{math}
\phi_1(\tau) := \Phi(s + \tau, x_0)
```

sowie auch die Funktion 

```{math}
\phi_2(\tau) := \Phi(\tau, \Phi(s,x_0))
```
die DGL auf dem Intervall $[t, \epsilon(x_0)]$. Weiterhin wissen wir, dass 

```{math}
\phi_1(0) = \Phi(s, x_0) = \Phi(0, \Phi(s, x_0)) = \phi_2(0),
```

somit stimmen also beide Funktionen an einem Punkt überein und sind somit schon auf dem gesamten Intervall $[t, \epsilon(x_0)]$ gleich, was 
eine Folgerung aus dem Eindeutigkeitssatz ({cite:p}`tenbrinck_2021`, Kapitel 7) ist. Wir haben also 

```{math}
\Phi(s + \tau, x_0) = \phi_1(\tau) = \phi_2(\tau) = \Phi(\tau, \Phi(s,x_0))
```
für jedes $\tau\in [t, \epsilon(x_0)]$.
````

## Phasenportraits

Die teilweise abstrakten Begriffe zu Flüssen werden nun mit einfachen geometrische Anschauung unterlegen. Dafür benötigen wir zunächst die folgenden Definitionen.

````{prf:definition}
Es sei $\Phi:G\rightarrow U$ ein Fluss einer DGL, mit $G\subset \R^+_0\times U$.

* Für jedes $x_0\in U$ heißt die Funktion $t\mapsto \Phi(t, x_0)$ **Bahnkurve** durch $x_0$.

* Die Menge $\mathcal{O}(x_0) := \{\Phi(t, x_0): (t, x_0)\in G}$ heißt **Orbit** oder **Trajektorie** durch $x_0$.

* Ein Orbit heißt **Ruhelage**, falls $\mathcal{O}(x_0) = \{x_0\}$.

* Ein Anfangswert $x_0\in U$ heißt **periodisch** mit Periode $T>0$, falls $\Phi(T, x_0) = x_0$.
````
