# Holomorphe Funktionen

Wir betrachten im Folgenden komplexe Funktionen $f:\C\to\C$. Der Begriff der Stetigkeit wird durch die Metrik induziert. Das Konzept der Differenzierbarkeit führt auf den zentralen Begriff der Funktionentheorie, sogenannte *holomorphen Funktionen*.

````{prf:definition} Holomorphe Funktion
:label: def:holomorph

Sei $U \subset \C$ eine offene Teilmenge, eine Funktion $f:U\to\C$ heißt **komplex differenzierbar** in $p\in\C$, falls der Grenzwert

```{math}
f'(p) = \lim_{h\rightarrow 0} \frac{f(p+h) - f(p)}{h}
```

existiert. Ist $f$ komplex differenzierbar für alle $p\in U$ so nennen wir $f$ **holomorph**.

````

````{prf:remark}
Beachte, dass im obigen Grenzwert $h\in\C$ gilt, der Limes existiert also, falls für eine beliebige Folge $h_k\in\C,k\in\N$ mit $\abs{h_k}\to 0$ gilt, dass

```{math}
\lim_{k\to\infty} \frac{f(p+h_k) - f(p)}{h_k} = f'(p).
```

Dies ist äquivalent dazu, dass für eine beliebige Folge $z_k\in\C,k\in\N$ mit $\abs{z_k-p}\to 0$ gilt, dass

```{math}
\lim_{k\to\infty} \frac{f(z_k) - f(p)}{z_k - p} = f'(p).
```
````

## Eigenschaften holomorpher Funktionen

Eine sehr nützliche Eigenschaft komplex differenzierbarer Funktionen liefert das folgende Lemma.

````{prf:lemma}
:label: lem:splitholo

Sei $U \subset \C$ eine offene Teilmenge, die Funktion $f:U\to\C$ ist genau dann komplex differenzierbar in $p\in U$, falls eine in $p$ stetige Funktion $h:U\to\C$ existiert, s.d.

```{math}
f(z) = f(p) + h(z)\cdot (z-p)\quad\forall z\in U.
```

Weiterhin gilt in diesem Fall $h(p) = f^\prime(p)$.
````

````{prf:proof}
Es sei $f$ komplex differenzierbar in $p$, dann definieren wir die Funktion

```{math}
h(z):=
\begin{cases}
\frac{f(z) - f(p)}{z-p}\text{ falls }z\neq p\\
f^\prime(p)\text{ sonst.}
\end{cases}
```

Da $f$ komplex differenzierbar in $p$ ist existiert der Grenzwert

```{math}
\lim_{z\to p} \frac{f(z) - f(p)}{z-p}
```

und ist gleich $f^\prime(p)$ und daher ist $h$ stetig in $p$. Weiterhin gilt

```{math}
h(z)\cdot (z-p) = f(z) - f(p)\quad\forall z\in U
```

und daher die Behauptung. 

Für die andere Richtung sei $h$ eine in $p$ stetige Funktion s.d.

```{math}
f(z) = f(p) + h(z)\cdot (z-p)\quad\forall z\in U.
```

Dann gilt

```{math}
\lim_{z\to p} \frac{f(z) - f(p)}{z-p} = \lim_{z\to p} h(z) = h(p)
```

wobei der Grenzwert existiert, da $h$ stetig in $p$ ist. Somit ist $f$ komplex differenzierbar in $p$.

````

Mithilfe des obigen Lemmas können wir sofort folgern, dass holomorphe Funktionen stetig sind.

````{prf:lemma}
Es sei $U\subset\C$ offen und $f:U\to\C$ sei komplex differenzierbar in $p\in U$, dann folgt $f$ ist stetig in $p$.
````

````{prf:proof}
Die Funktion $f$ sei komplex differenzierbar in $p$, dann existiert nach {prf:ref}`lem:splitholo` eine in $p$ stetige Funktion $h$, s.d., 

```{math}
f(z) = f(p) + h(z)\cdot(z-p)\quad \forall z\in U.
```

Die Polynome $z\mapsto f(p), z\mapsto (z-p)$ sind jeweils stetig in $p$, Addition und Multiplikation stetiger Funktionen erhält Stetigkeit und somit ist $f$ stetig in $p$.
````

Wir betrachten nun noch Ableitungsregeln, welche versichern, dass wir für die komplexe Ableitung die gewohnten Rechenregeln benutzten dürfen.

````{prf:lemma} Komplexe Ableitungsregeln
Es sei $U\subset\C$ offen und $f,g:U\to\C$ zwei holomorphe Funktionen, dann gilt

* $f+g$ ist holomorph, mit $(f+g)^\prime = f^\prime + g^\prime$,

* $f\cdot g$ ist holomorph, mit $(f\cdot g)^\prime = f^\prime g+ f g^\prime$.

Weiterhin seien $f:U\to V, g:V\to C$ zwei holomorphe Funktionen mit $V\subset\C$ offen, dann gilt

* $g\circ f$ ist holomorph mit $(g\circ f)^\prime = (g^\prime \circ f)\, f^\prime$.

Zusätzlich gilt 

* $\frac{1}{f}: U\setminus f^{-1}(0)\to \C$ ist holomorph, mit $(\frac{1}{f})^\prime = \frac{f^\prime}{f^2}$.
````

````{prf:proof}
ToDo
````

## Die Cauchy--Riemannschen Differentialgleichungen

Da die komplexen Zahlen auch einen zweidimensionalen reellen Vektorraum bilden, stellt sich die Frage wie komplexe Differenzierbarkeit mit der bekannten totalen Differenzierbarkeit im $\R^n$ zusammenhängt.

````{prf:definition}
Es sei $U\subset\R^n$ offen, eine Funktion $F:U\to\R^m$ heißt **total differenzierbar** in $a\in U$, falls ein reell lineares Funktional $df(a):\R^n\to\R^m$ existiert, s.d.,

```{math}
\lim_{x\to a} \frac{\abs{f(x)-f(a) - df(a)(x-a)}}{\abs{x-a}} = 0.
```
````

Im Falle von totaler Differenzierbarkeit, wissen wir, dass $F$ in alle Richtung partiell differenzierbar ist, und dass das Differential $df(a)$ durch die Jacobi-Matrix am Punkt $a$ gegeben ist. Falls $F$ andererseits in alle Richtungen **stetig** partiell differenzierbar ist, so ist es auch total Differenzierbar.

Sei nun $f\C\to\C$ eine komplexe Funktion wobei wir mit $u:=\Re(f),v:=\Im(f)$ jeweils der Real- und Imaginärteil von $f$ sind. Dann ist ist $f$ natürlicherweise auch eine Funktion $f:\R^2\to\R^2$, denn

```{math}
f = u+iv = \begin{pmatrix} u\\ v\end{pmatrix}.
```

Somit können wir auch für $f:\C\to\C$ den Begriff der totalen Differenzierbarkeit betrachten. Der folgende Satz setzt nun Holomorphie und Totale Differenzierbarkeit in Beziehung und führt auf natürliche Weise auf die **Cauchy--Riemannschen Differentialgleichungen**.

````{prf:remark}
Der konzeptionelle Unterschied zwischen totaler Differenzierbarkeit und Holomorphie ist, dass der Grenzwert in {prf:ref}`def:holomorph` durch den Quotienten die komplexe Multiplikation benutzt, während wir bei totaler Differenzierbarkeit die Beträge von Vektoren betrachten. Allgemein unterscheidet sich $\C$ als Körper nur durch die zusätzlich definierte komplexe Multiplikation vom reellen Vektorraum $\R^2$. Genau diese komplexe Multiplikation die hier einfließt, führt dazu, dass der Begriff der Holomorphie nicht gleich dem der klassischen Differenzierbarkeit auf $\R^2$ ist.
````

Dafür setzen wir Voraus, dass die Komponenten $u,v$, stetig partiell differenzierbar sind und somit das totale Differential in $p\in U\subset\C$ gegeben ist durch

```{math}
df(p) = 
\begin{pmatrix} 
\partial_x u &\partial_y u\\
\partial_x v &\partial_y v
\end{pmatrix}.
```

Wir erkennen, dass das totale Differential auch eine Abbildung $df(p):\C\to\C$ definiert

```{math}
df(p)(z)= df(p)(x+iy):= 
\begin{pmatrix} 
\partial_x u &\partial_y u\\
\partial_x v &\partial_y v
\end{pmatrix}
\begin{pmatrix}
x\\y
\end{pmatrix}
```

welche offensichtlich linear über $\R$ aber **nicht notwendigerweise** linear über $\C$ ist.

````{prf:theorem}
Es sei $U\subset \C$ offen und $f=u+iv:\C\to\C$ eine Funktionen mit **stetig partiell differenzierbaren** Funktionen $u,v:\C\to\R$, dann sind folgende Aussagen äquivalent,

1. $f$ ist holomorph,

2. die Abbildung $df(p):\C\to\C$ ist linear über dem Körper $\C$,

3. es gelten die Cauchy--Riemannschen Differentialgleichungen

```{math}
\partial_x u = \partial_y v, \qquad \partial_y u = -\partial_x v.
```

````

````{prf:proof}
ToDo, siehe [Video](https://www.fau.tv/clip/id/40944) ab Minute 32:30.
````

````{prf:example} Holomorphe Funktionen
Ableitung eines komplexen Monoms -> Beispiel 10.4 auf S.314 in Schulz-Baldes

$f(z) := \overline{z}$ ist nicht holomorph -> Beispiel 10.7 auf S.315 in Schulz-Baldes
````
