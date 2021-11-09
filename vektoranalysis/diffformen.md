# Differentialformen

In diesem Kapitel werden wir nun [Differentialformen](https://de.wikipedia.org/wiki/Differentialform) einführen. Die entscheidende Neuerung im Vergleich zum vorhergehenden Kapitel, ist 
dass wir zusätzlich zur Vektorraumstruktur nun ein Konzept von Räumlichkeit einführen, speziell betrachten wir eine offene Menge $U\subset\R^n$. Ein weiterer wichtiger Aspekt, ist dass wir im Folgenden mit glatten Funktion arbeiten wollen, d.h., mit dem Raum $C^\infty(U,\R^n)$.


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
Eine Differentialform $\vv\in\Omega^*(U)$ heißt
* **geschlossen**, wenn $d\vv=0$, ***exakt**, wenn $\vv=d\psi$ für ein $\psi\in\Omega^*(U)$ gilt.

%
Nach Satz {prf:ref}`thm:dd` sind exakte Differentialformen geschlossen.\\ Für $k$--Formen auf konvexen offenen Teimengen $U\subseteq \R^n$ gilt für $k\ge 1$auch die Umkehrung (sog.
[**Poincaré-Lemma**](https://de.wikipedia.org/wiki/Poincar%c3%a9-Lemma) ),  siehe Kapitel {prf:ref}`sect:Poinca`).
%