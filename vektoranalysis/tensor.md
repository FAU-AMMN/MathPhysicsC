# Tensoren und Tensorprodukte

In diesem Kapitel widmen wir uns einem wichtigen aber komplizierten Thema der Vektoranalysis, nämlich Tensoren und Tensorprodukten.
Der Begriff hat sehr viele verschiedene Anschauungsmöglichkeiten (siehe [Wikipedia](https://de.wikipedia.org/wiki/Tensorprodukt)) weshalb es nicht leicht ist eine Einführung zu geben die gleichzeitig allgemein, aber auch verständlich ist. Da Tensoren aber eine wichtige Rolle in der Physik spielen werden wir uns hier damit beschäftigen.

## Motivation

Wir betrachten zwei Beispiele aus der Physik, welche auf Tensoren zurückgreifen.

````{prf:remark}
Der Begriff Tensor wurde von Hamilton in der Mitte des 19. Jahrhunderts eingeführt. Er leitete die Bezeichnung vom latinischen _tendere_ (spannen) ab, da die ursprüngliche Anwendung derartiger Objekte in der Elastizitätstheorie Anwendung fand.
````

### Der Cauchy Spannungstensor

```{margin}
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

### Quantenverschränkung

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