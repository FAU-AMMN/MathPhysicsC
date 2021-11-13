# Tensoren und Tensorprodukte

In diesem Kapitel widmen wir uns einem wichtigen aber komplizierten Thema der Vektoranalysis, nämlich Tensoren und Tensorprodukten.
Der Begriff hat sehr viele verschiedene Anschauungsmöglichkeiten (siehe [Wikipedia](https://de.wikipedia.org/wiki/Tensorprodukt)) weshalb es nicht leicht ist eine Einführung zu geben die gleichzeitig allgemein, aber auch verständlich ist. Da Tensoren aber eine wichtige Rolle in der Physik spielen werden wir uns hier damit beschäftigen.

## Motivation

Wir betrachten zwei Beispiele aus der Physik, welche auf Tensoren zurückgreifen.

````{prf:remark}
Der Begriff Tensor wurde von Hamilton in der Mitte des 19. Jahrhunderts eingeführt. Er leitete die Bezeichnung vom latinischen _tendere_ (spannen) ab, da die ursprüngliche Anwendung derartiger Objekte in der Elastizitätstheorie Anwendung fand.
````

### Der Cauchy Spannungstensor

```{margin} Augustin Cauchy
[Augustin-Louis Cauchy](https://de.wikipedia.org/wiki/Augustin-Louis_Cauchy) (Geboren 21. August 1789 in Paris; Gestorben 23. Mai 1857 in Sceaux) war ein französischer Mathematiker.
```

Mechanische Spannung beschreibt die innere Beanspruchung und Kräfte in einem Volumen $V\subset\R^3$ die aufgrund einer äußeren Belastungen auftreten. Die grundlegende Idee ist das **Euler-Cauchy Stress Prinzip**, welches beschreibt, dass auf jede Schnittfläche $A\subset\R^2$ welche ein Volumen in zwei Teile trennt, von diesen zwei Komponenten eine Spannung auf $A$ ausgewirkt wird, welche durch den **Spannungsvektor** $\mathbf{T}^n$ beschrieben wird. Der Spannungsvektor ist hierbei von der Dimension "Kraft pro Fläche".

```{figure} ../img/stress_vector.png
---
height: 250px
name: "fig:stress"
---
Visualisierung für Normal- und Scherspannung an einer Schnittfläche. Quelle: [Wikipedia; Cauchy Stress Tensor](https://en.wikipedia.org/wiki/Cauchy_stress_tensor).
```

Wie in {numref}`fig:stress` visualisiert teilt sich die Spannung in zwei Komponenten auf:

**Normalspannung:**

Dieser Teil des Spannungsvektor zeigt in Richtung der normalen $\mathbf{n}$ welche orthogonal auf der Schnittfläche stehen.

**Scherspannung:**

Dieser Teil des Spannungstensors ist parallel zur Schnittfläche.

Man erkennt nun, dass die Spannung in $V$ nicht durch einen einzigen Vektor ausgedrückt werden kann. Einerseits hängt sie vom betrachteten Punkt $P\in V$ ab und zudem von der Orientierung der Schnittfläche. Allerdings hat Cauchy gezeigt, dass ein Tensorfeld $\mathbf{\sigma}(x)$ existiert, s.d.,

```{math}
T^{\mathbf{n}}(x) = \mathbf{n}\cdot \mathbf{\sigma}(x),
```

d.h. in jedem Punkt $x\in V$ ist der Stressvektor linear im Normalenvektor $\mathbf{n}$.

```{figure} ../img/stress_tensor_comp.png
---
height: 250px
name: "fig:stress-comp"
---
Quelle: [Wikipedia; Spannungstensor](https://de.wikipedia.org/wiki/Spannungstensor).
```

Hierfür betrachtet man einen freigeschnittenen Würfel wie in {numref}`fig:stress-comp` und definiert für die drei verschiedenen Flächen (orthogonal zu den Einheitsvektoren) den Stresstensor

```{math}
\mathbf{T}^{e_i}:= \sum_{j=1}^3 \sigma_{ij} e_j.
```

So haben wir z.B. für $\mathbf{T}^{e_1}$ die Normalspannung gegeben durch $\sigma_{11} e_1$ und die zwei Scherspannungskomponenten $\sigma_{12} e_2, \sigma_{13} e_3$. Insgesamt erhält man neun Komponenten $\sigma_{ij}$ welche über die Definition

```{math}
\mathbf{\sigma} := \sum_{i=1}^3 e_i \otimes \mathbf{T}^{e_i} = \sum_{i=1}^3\sum_{j=1}^3 \sigma_{ij} (e_i\otimes e_j)
```

den Cauchy Stresstensor $\mathbf{\sigma}$ ergebene. Hierbei bezeichnet $\otimes$ das **dyadische Produkt** zweier Vektoren. Für $x\in\R^n,y\in\R^m$ definieren wir

```{math}
x \otimes y := 
\begin{pmatrix}
x_1y_1 &\ldots &x_1 y_m\\
\vdots &\ddots & \vdots\\
x_n y_1&\ldots& x_n y_m
\end{pmatrix}.
```

Wir werden später sehen, dass man die Idee $\sigma$ über das dyadische Produkt zu definieren abstrahieren kann, was auf den allgemeinen Tensorbegriff führt.

### Quantenverschränkung

## Das Tensorprodukt

Wir wollen nun das Tensorprodukt von Vektorräumen abstrakt einführen und es später konkret realisieren.

````{prf:definition} Tensorprodukt
Es seien $V,W$ zwei reelle Vektorräume. Ein reeler Vektorraum $X$ heißt **Tensorproduktraum** falls eine bilineare Abbildung $\otimes:V\times W\rightarrow X$ existiert, s.d., die folgende **universelle Eigenschaft** gilt:

Für jede Bilinearform $\phi\in L^2(V\times W, Y)$ in einen beliebigen reellen Vektorraum $Y$, existiert eine eindeutige lineare Abbildung 
$p \in L^1(X, Y)$, s.d. gilt 

```{math}
\phi(v,w) = p((v\otimes w)) = p(\otimes(v,w))\quad\forall (v,w)\in V\times W.
```

In diesem Fall schreibt man auch $X = V\otimes X$, $\otimes$ heißt Tensorprodukt und zusätzlich ist die Schreibweise $\otimes(v,w)=:v\otimes w$ üblich.
````

**Was bedeutet das?**

Diese Definition erscheint auf den ersten Blick abstrakt und unverständlich. Was ist jetzt also ein Tensorprodukt?

**Das Tensorprodukt ist universell:**

Wir haben benutzten in der Definition oben das kartesische Produkt $\times$ welches eindeutig definiert ist. Im Gegensatz dazu gibt es nicht _ein_ Tensorprodukt $\otimes$ oder _einen_ Tensorproduktraum $V\otimes W$. Wir haben die Freiheit $\otimes$ zu wählen und wann immer die universelle Eigenschaft erfüllt ist, heißt dann $V\otimes W$ Tensorproduktraum. Derartige Konzepte nennt man in der Algebra _universell_.

**Was bedeutet die universelle Eigenschaft?**

Wie wir weiter unten noch genauer beschreiben werden, stellt die universelle Eigenschaft eine wichtige Beziehung zwischen dem Raum der bilinearen Abbildungen auf $V\times W$ und dem Dualraum von $V\otimes W$ her. Sofern wir das Tensorprodukt gegeben haben erhalten wir alle Bilinearformen schon über einfache Linearformen auf $V\otimes W$.

## Existenz und Konstruktion

Wir können ein Tensorprodukt konkret konstruieren indem wir uns auf die Basis der Vektorräume $V$ und $W$ zurückziehen. Diese Tatsache formulieren wir in der folgenden Aussage.

````{prf:theorem}
Für zwei reelle Vektorräume $V, W$ existiert stets mindestens ein Tensorprodukt $\otimes\in L^2(V\times W, V\otimes W)$.
````

````{prf:proof}
Der folgende Beweis ist ein sogenannter konstruktiver Beweis, d.h., wir zeigen die Existenz eines Objekts indem wir es explizit angeben. Es gibt auch nicht-konstruktive Existenzbeweise.

Es sei $B^V = \{b_i^V: i\in I^V\}$ eine Basis von $V$ und analog $B^W = \{b_i^W: i\in I^W\}$  eine Basis von $W$ für Indexmengen $I^V, I^W$. Wir betrachten das kartesische Produkt 

```{math}
J := I^V \times I^W = \{(i,j): i\in I^V, j\in I^W\}.
```

Es sei nun $X$ ein Vektorraum dessen Basis sich durch $J$ indizieren lässt, d.h., es existiert eine Menge 

```{math}
B^X = \{b_{ij}^X: (i,j)\in J\}
```

s.d. $B^X$ eine Basis von $X$ ist. Ein solcher Vektorraum existiert, da z.B. das kartesische Produkt $V\times W$ diese Eigenschaft erfüllt.

Wir definieren nun eine bilineare Abbildung $\otimes: V\times W\to X$ über 

```{math}
b_i^V \otimes b_j^W := b_{ij}^X\quad\forall (i,j)\in J.
```

Beachte, $\otimes$ ist durch die Definition auf $J$ eindeutig festgelegt, da für beliebige $(v,w)\in V\times W$ endlich viele Faktoren 
$\alpha_{i_1},\ldots,\alpha_{i_m}$ und $\beta_{j_1},\ldots, \beta_{j_n}$ existieren s.d.

```{math}
\otimes(v,w) 
&= 
\otimes\big(\sum_{k=1}^n \alpha_{i_k} b_{i_k}^V, \sum_{l=1}^m \beta_{j_l} b_{j_l}^W\big) 
\\&= 
\sum_{k=1}^n \sum_{l=1}^m \otimes\left(b_{i_k}^V, b_{j_l}^W\right)
\\&=
\sum_{k=1}^n \sum_{l=1}^m b_{i_kj_l}^X.
```

Wir müssen nun die universelle Eigenschaft zeigen, sei dazu $\phi\in L^2(V\times W, Y)$ eine Bilinearform auf einen reellen Vektorraum $Y$, dann können wir eine Linearform auf $p:X\to Y$ definieren durch (analog reicht es die Definition auf den Basiselementen anzugeben)

```{math}
p(b_{ij}^X) := \phi(b_i^V, b_j^W).
```

Dann gilt nämlich, unter Ausnutzung der Linearität von $p$ und obiger Rechnung, dass 

```{math}
p(\otimes(v,w)) 
&=
\sum_{k=1}^n \sum_{l=1}^m p(b_{i_kj_l}^X)
\\&=
\sum_{k=1}^n \sum_{l=1}^m \phi\left(b_{i_k}^V, b_{j_l}^W\right)
\\&
\phi\big(\sum_{k=1}^n  b_{i_k}^V,\sum_{l=1}^m b_{j_l}^W\big)
\\&
\phi(v,w)
```

und somit gilt die universelle Eigenschaft. Insbesondere, da $p$ durch die obige Definition eindeutig festgelegt ist.

````

Als Korollar erhalten wir somit, dass eine Basis des Tensorproduktraums durch das kartesische Produkt der ursprünglichen Basen konstruiert werden kann. Hieran sieht man qualitativ den Unterschied zwischen $V\otimes W$ und $V\otimes W$.

````{prf:corollary}
Für zwei reelle Vektorräume $V,W$ mit Basen $B^V = \{b_i^V: i\in I^V\}, B^W = \{b_i^W: i\in I^W\}$ und ein Tensorprodukt $\otimes:V\times W\to V\otimes W$ ist 

```{math}
\{b_i^V\otimes b_j^W: i\in I^V, j\in I^W\}
```

eine Basis von $V\otimes W$.
````

Wir wissen nun, dass mindestens ein Tensorprodukt existiert, es stellt sich also die Frage inwiefern sich verschiedene derartige Abbildungen auf den gleichen Vektorräumen $V,W$ unterschieden. Seien dazu $\otimes_1, \otimes_2$ je zwei Tensorprodukte auf $V\times W$. Wegen der universellen Eigenschaft gibt es lineare Abbildungen $p_1: V\otimes_1 W\to W\otimes_2 V$ und $p_2: V\otimes_2 W\to W\otimes_1 V$, s.d.,

```{math}
\otimes_2 &= p_1 \circ \otimes_1\\
\otimes_1 &= p_2 \circ \otimes_2.
```

und somit

```{math}
\otimes_2 &= p_1\circ p_2 \circ \otimes_2\\
\otimes_1 &= p_2\circ p_1 \circ \otimes_1.
```

Da wir aber die Basis von $V\otimes_2 W$ über Elemente $\otimes_2(b_i^V, b_j^W)$ charakterisieren können, und aus der ersten Gleichung folgt, dass

```{math}
p_1\circ p_2(\otimes(b_i^V,b_j^W)) = \otimes(b_i^V, b_j^W)
```

wissen wir dass $p_1\circ p_2 = \mathrm{Id}$. Das folgt da $p_1\circ p_2$ als lineare Abbildung schon ganz auf den Basiselementen festgelegt ist. 
Analog folgt $p_2\circ p_1 = \mathrm{Id}$ und somit sind $p_1, p_2$ isomorph zueinander. D.h. wir haben insgesamt gezeigt, dass verschiedene Tensorprodukte stets isomorph zueinander sind.

````{prf:lemma}
Es seien $V,W$ zwei reelle Vektorräume und $\otimes_1,\otimes_2$ zwei Tensorprodukte. Dann existiert genau ein Isomorphismus $p:V\otimes_1 W\to V\otimes_2 W$, s.d.

```{math}
\otimes_2 = p\circ \otimes_1.
```

````

## Tensoren als Linearformen

Als Einleitung in das Thema wollen wir Tensoren zunächst als Linearformen auf $\V_1\times\ldots\times\V_k$
betrachten wobei für $i=1,\ldots,k$ $\V_i$ reelle endlich dimensionale Vektorräume sind.
Man schreibt in diesem Fall auch

```{math}
\V_1\otimes\ldots\otimes\V_k = L(\V_1\times\ldots\V_k,\R)
```

wobei $\otimes$ das Tensorprodukt bezeichnet.

Der wichtige Spezialfall ist hier allerdings nun nicht $\V^k$ sondern ein kartesisches Produkt der Form

```{math}
(V^\ast)^r\times V^s.
```

````{prf:definition}
Es sei $\V$ ein reeller endlich-dimensionaler Vektorraum, dann nennt man 

```{math}
T^r_s(V) := L((V^\ast)^r\times V^s, \R)
```

Menge der $r$-fach **kontravarianten** und $s$-fach **kovarianten** Tensoren, oder alternativ Tensoren der Stufe $(r,s)$. 

````

Wir wollen diese abstrakte Definition nun mit einfachen Beispielen veranschaulichen zunächst für $r+s=1$.

````{prf:example}
Tensoren der Stufe $(1,0)$ können mit Elementen des Vektorraums selbst identifiziert werden, denn 

```{math}
T^1_0(V) = L((V^\ast), \R) = \V^{\ast\ast}\cong \V
```

mit der Identifikation aus {prf:ref}`lem:doubledual`. Weiterhin sind Tensoren der Stufe $(0,1)$ Elemente des 
Dualraums, also einfach Linearformen auf $\V$, sogenannte _Kovektoren_.


````

Als weiteren Spezialfall erhalten wir Multilinearformen.

````{prf:example}
Tensoren der Stufe $(0,k)$ sind $k$-Linearformen, da $T^0_k(V) = L^k(V)$. 


````

````{prf:example}
Aus einer linearen Abbildung $A:\V\to\V$ erhält man direkt einen Tensor der Stufe $(1,1)$ über die Abbildung 

```{math}
\varphi, v \mapsto \varphi(Av).
```

````
