# Flüsse und Phasenportraits

Wir beginnen zunächst damit ein wichtiges Konzept einzuführen, welches die Beschreibung zeitabhängiger Systeme vereinfacht. Die folgende Definition ist zunächst sehr allgemein gehalten und wird später für unsere Anwendungen auf DGLs konkretisiert.

````{prf:Definition} Fluss
:label: def:Fluss

Sei $U$ eine Menge und $I=\R^+_0$, dann heißt eine Abbildung $\Phi:U\times I\rightarrow U$ **Fluss**, falls gilt,

* $\Phi(x,0) = x$ für alle $x\in U$,

* $\Phi(\Phi(x,s),t) = \Phi(x, s + t)$ für alle $x\in U$ und alle $s,t\in I$.
````

````{prf:remark} Notation
Anstatt beide Argument in Klammern wie in obiger Definition zu schreiben, benutzt man häufig folgende Darstellung, 

```{math}
\Phi_t(x) = \Phi(x, t).
```

````

In unserem Fall wollen wir speziell die Lösungen einer DGL als Fluss interpretieren. Hierbei definiert man dann die Funktion 

```{math}
$\phi(t) := \Phi_t(x_0)
```

für den Startwert $x_0$ welche dann das entsprechende AWP {eq}`eq:DGL` löst. Man kann in diesem Fall das erste Argument des Flusses also als Anfangswert interpretieren.

Ein Problem das hier allerdings unmittelbar auftritt, ist dass in {prf:ref}`def:Fluss` auf ganz $\R^+_0$ als Zeitintervall gearbeitet wird. Allerdings können wir für beliebige Anfangswerte $x_0\in U$ nur garantieren, dass die Lösung auf einem Intervall $I(x_0)\subset \R^+_0$ existiert. Deshalb benötigen wir zusätzlich den Begriff eines lokalen Flusses.

````{prf:Definition} Lokaler Fluss
:label: def:LokFluss


Sei $U$ eine Menge und die Menge $G\subset \R^+_0\times U$ sei gegeben als 

```{math}
G = \Cup_{x\in U} \{x\}\times I(x)
```

* $\Phi(x,0) = x$ für alle $x\in U$,

* $\Phi(\Phi(x,s),t) = \Phi(x, s + t)$ für alle $x\in U$ und alle $s,t\in I$.
````

````{prf:remark} Notation
Anstatt beide Argument in Klammern wie in obiger Definition zu schreiben, benutzt man häufig folgende Darstellung, 

```{math}
\Phi_t(x) = \Phi(x, t).
```

````


````{prf:definition}
Für ein Zeitintervall $I\subset\R$ und eine Teilmenge $G\subset I\times U$ heißt die Funktion 
$\Phi:G \rightarrow U$ Fluss oder dynamisches System von 
{eq}`eq:DGL` falls für jeden Anfangswert $(t,x_0)\in G$ gilt, dass

```{math}
\Phi_t(x_0) = x(t)
```
wobei $x$ eine Lösung des AWP {eq}`eq:DGL` ist.
````
