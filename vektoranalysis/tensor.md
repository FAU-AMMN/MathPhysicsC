# Tensoren und Tensorprodukte

In diesem Kapitel widmen wir uns einem für die Physik sehr wichtigen aber relativ abstrakten Thema der Vektoranalysis, nämlich *Tensoren* und *Tensorprodukten*.
Der Begriff hat sehr viele verschiedene Anschauungsmöglichkeiten (siehe [Wikipedia](https://de.wikipedia.org/wiki/Tensorprodukt)) weshalb es nicht leicht ist eine Einführung zu geben die gleichzeitig allgemein, aber auch verständlich ist. Da Tensoren aber eine wichtige Rolle in der Physik spielen werden wir uns hier damit beschäftigen.

## Motivation

Wir betrachten zunächst ein konkretes Anwendungsbeispiel aus der Physik, welches auf Tensoren zurückgreift.
Hier wird der sogenannte *Cauchy Spannungstensor* verwendet.

````{prf:remark} Begriffsherkunft
Der Begriff Tensor wurde von Hamilton in der Mitte des 19. Jahrhunderts eingeführt. Er leitete die Bezeichnung vom lateinischen _tendere_ (spannen) ab, da die ursprüngliche Anwendung derartiger Objekte in der Elastizitätstheorie Anwendung fand.
````

```{margin} Augustin Cauchy
[Augustin-Louis Cauchy](https://de.wikipedia.org/wiki/Augustin-Louis_Cauchy) (Geboren 21. August 1789 in Paris; Gestorben 23. Mai 1857 in Sceaux) war ein französischer Mathematiker.
```

Mechanische Spannung ist eine physikalische Größe, die die innere Beanspruchung und Kräfte in einem Volumen $V\subset\R^3$ angibt, welche aufgrund einer äußeren Belastungen auftreten.
Die grundlegende Idee ist das **Euler-Cauchy Spannungsprinzip**, welches beschreibt, dass auf jede Schnittfläche $A\subset\R^2$, die ein Volumen in zwei Teile trennt, von diesen zwei Volumenteilen eine Spannung auf $A$ ausgeübt wird, welche durch einen sogenannten **Spannungsvektor** $\mathbf{T}^{(n)}$ beschrieben wird. 
Der Komponenten des Spannungsvektors haben hierbei die Dimension "Kraft pro Fläche".

```{figure} ../img/stress_vector.png
---
height: 250px
name: "fig:stress"
---
Visualisierung für Normal- und Scherspannung an einer Schnittfläche. Quelle: [Wikipedia; Cauchy Stress Tensor](https://en.wikipedia.org/wiki/Cauchy_stress_tensor).
```

Wie in {numref}`fig:stress` visualisiert teilt sich die Spannung in zwei Komponenten auf:

**Normalspannung:**

Die Normalspannung $\sigma_n$ ist der Teil des Spannungsvektors, der in Richtung der Normalen $\mathbf{n}$ zeigt, welche orthogonal auf der Schnittfläche steht.

**Scherspannung:**

Die Scherspannung $\tau_n$ ist der Teil des Spannungstensors, der parallel zur Schnittfläche liegt.

Man erkennt nun, dass die Spannung in $V$ nicht durch einen einzigen Vektor ausgedrückt werden kann. Einerseits hängt sie vom betrachteten Punkt $x\in V$ ab und zudem von der Orientierung der Schnittfläche. Allerdings hat Cauchy gezeigt, dass ein linearer Operator $\mathbf{\sigma}(x)$ existiert, so dass

```{math}
\mathbf{T}^{(n)}(x) = \mathbf{\sigma}(x) \cdot n,
```

d.h. in jedem Punkt $x\in V$ ist der Stressvektor linear im Normalenvektor $n$.

```{figure} ../img/stress_tensor_comp.png
---
height: 250px
name: "fig:stress-comp"
---
Quelle: [Wikipedia; Spannungstensor](https://de.wikipedia.org/wiki/Spannungstensor).
```

Der lineare Operator $\mathbf{\sigma}$ wird auch **Cauchy Spannungstensor** genannt.
Um diesen besser zu verstehen betrachtet man für einen fixen Punkt $x$ des Volumens einen infinitesimal kleinen, freigeschnittenen Würfel wie in {numref}`fig:stress-comp`.
Nun definieren wir für die drei verschiedenen Flächen (orthogonal zu den Einheitsvektoren $e_1, e_2$ und $e_3$) die Spannungsvektoren

```{math}
\mathbf{T}^{(e_i)}:= \sum_{j=1}^3 \sigma_{ij} e_j, \quad i \in \lbrace 1,2,3 \rbrace.
```

So setzt sich beispielsweise der Spannungsvektor $\mathbf{T}^{(e_1)}$ zusammen aus der Summe der Normalspannung $\sigma_{11} e_1$ und den zwei Scherspannungskomponenten $\sigma_{12} e_2$ und $\sigma_{13} e_3$.

Insgesamt erhält man neun Spannungskomponenten $\sigma_{ij}$ für $i,j=1,2,3$ welche insgesamt den Spannungszustand im Punkt $x$ als Spannungsvektoren in Richtung der Einheitsvektoren vollständig beschreiben.
Dies liegt daran, dass wir jeden Spannungsvektor in $x$ als Linearkombination der drei Spannungsvektoren $\mathbf{T}^{(e_i)}, i=1,2,3$ darstellen können.

Wir führen nun eine *multilineare Abbildung* $\otimes \colon \R^n \times \R^m \rightarrow \R^{n \times m}$ für zwei beliebige Vektoren $x\in\R^n$ und $y\in\R^m$ ein, die das **dyadische Produkt** der Vektoren genannt wird und wie folgt definiert ist

```{math}
x \otimes y := 
\begin{pmatrix}
x_1y_1 &\ldots &x_1 y_m\\
\vdots &\ddots & \vdots\\
x_n y_1&\ldots& x_n y_m
\end{pmatrix}.
```

Fassen wir nun zeilenweise die Spannungsvektoren $\mathbf{T}^{(e_i)}, i=1,2,3$ in einer Matrix zusammen, so erhalten wir den Cauchy Spannungstensor $\mathbf{\sigma}$ für den Punkt $x$ des Volumens als

```{math}
:label: eq:cauchySpannungstensor

\mathbf{\sigma} := 
\begin{pmatrix}
\sigma_{11} & \sigma_{12} & \sigma_{13} \\
\sigma_{21} & \sigma_{22} & \sigma_{23} \\
\sigma_{31} & \sigma_{32} & \sigma_{33}
\end{pmatrix} 
&= 
\begin{pmatrix}
\mathbf{T}^{(e_1)} \\
\mathbf{T}^{(e_2)} \\
\mathbf{T}^{(e_3)}
\end{pmatrix}
= 
\begin{pmatrix}
\mathbf{T}^{(e_1)} \\
0 \\
0
\end{pmatrix}
+
\begin{pmatrix}
0 \\
\mathbf{T}^{(e_2)} \\
0
\end{pmatrix}
+
\begin{pmatrix}
0 \\
0 \\
\mathbf{T}^{(e_3)} \\
\end{pmatrix}\\
&=
\sum_{i=1}^3 e_i \otimes \mathbf{T}^{(e_i)} = \sum_{i=1}^3 e_i\otimes ( \sum_{j=1}^3 \sigma_{ij} e_j) =
\sum_{i=1}^3\sum_{j=1}^3 \sigma_{ij} (e_i\otimes e_j).

```

Wir werden später sehen, dass man die Idee, den Operator $\sigma$ über das dyadische Produkt zu definieren, abstrahieren kann, was auf den allgemeinen Tensorbegriff führt.

````{prf:remark}
In der Tat handelt es sich bei dem Operator $\sigma \colon \R^3 \rightarrow \R^3$ in {eq}`eq:cauchySpannungstensor` nicht nur um einen Tensor, sondern genauer um ein **Tensorfeld**, dass jedem Punkt $x$ des Volumens einen Spannungstensor zuordnet.
````

## Das Tensorprodukt

Wir wollen nun das Tensorprodukt von Vektorräumen abstrakt einführen und es an späterer Stelle für konkrete Realisierungen diskutieren.
Hierbei wollen wir uns zunächst auf einen Spezialfall einschränken, der lediglich *zwei Vektorräume* berücksichtigt, um die zu Grunde liegenden wichtigen Konzepte klarer herauszustellen.
Es ist wichtig zu verstehen, dass die folgenden Definitionen sich mit dem Konzept der $k$-Multilinearität in {ref}`s:multilinearformen` auf $k \in \N$ verschiedene $\R$-Vektorräume direkt verallgemeinern lassen.

````{prf:definition} Tensorprodukt
:label: def:tensorprodukt

Es seien $V$ und $W$ zwei reelle Vektorräume.
Ein reeller Vektorraum $X$ heißt **Tensorproduktraum** falls eine bilineare Abbildung $\otimes:V\times W\rightarrow X$ existiert, so dass die folgende **universelle Eigenschaft** gilt:

Für jede Bilinearform $\phi\in L^2(V\times W; Y)$ in einen beliebigen reellen Vektorraum $Y$, existiert eine eindeutige lineare Abbildung 
$p \in L^1(X; Y)$, so dass gilt 

```{math}
:label: eq:universell
\phi(v,w) = p(v\otimes w) = p(\otimes(v,w))\quad\forall (v,w)\in V\times W.
```

In diesem Fall schreibt man auch $X = V \otimes W$.
Wir nennen die bilineare Abbildung $\otimes$ **Tensorprodukt** und verwenden häufig für sie die Infix-Schreibweise $\otimes(v,w)=:v\otimes w$.
````

Diese Definition erscheint auf den ersten Blick abstrakt und unverständlich. 
Was ist jetzt also genau ein Tensorprodukt?

**Das Tensorprodukt ist universell:**

Wir haben in der {prf:ref}`def:tensorprodukt` das kartesische Produkt $\times$ benutzt welches eindeutig definiert ist. 
Im Gegensatz dazu gibt es jedoch nicht _ein_ Tensorprodukt $\otimes$ oder _einen_ Tensorproduktraum $V\otimes W$. 
Wir haben die Freiheit $\otimes$ zu wählen und wann immer die universelle Eigenschaft erfüllt ist, heißt dann $X = V\otimes W$ Tensorproduktraum.
Derartige Konzepte nennt man in der Algebra _universell_.
Betrachten wir hierzu ein kurzes Beispiel für unterschiedliche Realisierungen eines Tensorproduktes.

````{prf:example} Varianten eines Tensorprodukts
:label: ex:tensorproduktVarianten

Wir betrachten in diesem Beispiel den Euklidischen Vektorraum $V=W=\R^2$ und zwei Vektoren $x, y \in \R^2$.
Nehmen wir zunächst das Tensorprodukt, dass durch das **dyadische Produkt** $\otimes : \R^2 \times \R^2 \rightarrow \R^{2 \times 2}$ gegeben ist mit

```{math}
x \otimes y \, \coloneqq \,
\begin{pmatrix}
x_1y_1 & x_1y_2 \\
x_2y_1 & x_2y_2
\end{pmatrix}.
```

Man sieht ein, dass der zugehörige *Tensorproduktraum* also $\R^{2 \times 2} = \R^2 \otimes \R^2$ sein muss.
Anderseits erhält man den gleichen Tensorproduktraum, wenn man ein **alternatives Tensorprodukt** $\otimes^*$ zum dyadischen Produkt definiert, welches lediglich die Reihenfolge der Komponenten von $y$ vertauscht mit

```{math}
x \otimes^* y \, \coloneqq \,
\begin{pmatrix}
x_1y_2 & x_1y_1 \\
x_2y_2 & x_2y_1
\end{pmatrix}.
```

````

**Was bedeutet die universelle Eigenschaft?**

Wie wir weiter unten noch genauer beschreiben werden, stellt die universelle Eigenschaft eine wichtige Beziehung zwischen dem Raum der bilinearen Abbildungen auf $V\times W$ und dem Dualraum von $X = V\otimes W$ für ein Tensorprodukt $\otimes$ her. 
Sofern wir das Tensorprodukt gegeben haben erhalten wir alle Bilinearformen schon über einfache Linearformen auf $V\otimes W$.

Das folgende einfache Beispiel soll uns helfen diese Beziehung besser zu verstehen.

````{prf:example} Universelle Eigenschaft
:label: ex:universelleEigenschaft
Im Folgenden betrachten wir wieder den Euklidischen Vektorraum $V=W=\R^2$ und zwei Vektoren $x, y \in \R^2$.
Wie wir in {prf:ref}`ex:tensorproduktVarianten` festgestellt haben realisiert das dyadische Produkt 

```{math}
\otimes \colon \R^2 \times \R^2 \rightarrow \R^2 \otimes \R^2 = \R^{2 \times 2} =: X$
```

mit

```{math}
x \otimes y \, \coloneqq \,
\begin{pmatrix}
x_1y_1 & x_1y_2 \\
x_2y_1 & x_2y_2
\end{pmatrix}.
```

ein *Tensorprodukt* der Vektorräume $V=W=\R^2$.
Wegen der *universellen Eigenschaft* muss nun gelten, dass für jede Bilinearform $\Phi \in L^2(V \times W; Y)$ für beliebige $\R$-Vektorräume $Y$ eine eindeutige lineare Abbildung $p \in L^1(X; Y)$ existiert, die äquivalent im Sinne von {eq}`eq:universell` ist.

Nehmen wir also beispielsweise das Skalarprodukt $\langle \cdot, \cdot \rangle \colon V \times W \rightarrow \R$ als eine mögliche Bilinearform $\Phi \in L^2(V \times W; Y)$ mit

```{math}
\langle x, y \rangle = x^T \cdot y = x_1y_1 + x_2y_2.
```

Wir müssen nun einen linearen Operator $p \in L^1(X; Y)$ finden, der eine äquivalente Berechnung wie das Skalarprodukt auf dem Tensorproduktraum $X = \R^{2 \times 2}$, der durch das dyadische Produkt induziert wird, durchführt.
Hierzu wählen wir die Spur $p(A) \coloneqq \operatorname{Spur}(A)$ einer Matrix $A \in \R^{2 \times 2}$, denn diese ist **linear** und es gilt:

```{math}
\operatorname{Spur}
\begin{pmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{pmatrix}
= a_{11} + a_{22}.
```

Überprüfen wir mit dieser Wahl nun die **universelle Eigenschaft des dyadischen Produkts**, so erhalten wir

```{math}
\Phi(x,y) = \langle x, y \rangle = x_1y_1 + x_2y_2 = \operatorname{Spur}
\begin{pmatrix}
x_1y_1 & x_1y_2 \\
x_2y_1 & x_2y_2
\end{pmatrix}
 = \operatorname{Spur}(x \otimes y) = p(x \otimes y).
```

Es sei angemerkt, dass wir nicht gezeigt haben, dass der Spur-Operator der *einzige* lineare Operator ist, der diese Äquivalenz erfüllt.
Betrachten wir statt dessen die alternative Variante $\otimes^*$ des dyadischen Produkts aus {prf:ref}`ex:tensorproduktVarianten`, so bleibt der Tensorproduktraum gleich, jedoch ändert sich der eindeutig bestimmte, lineare Operator $p \in L^1(X; Y)$.
Durch die Vertauschung der Elemente der Matrix $x \otimes^* y$ nimmt man nicht mehr die Summe der Hauptdiagonalelemente realisiert durch den Operator $\operatorname{Spur}(A) = a_{11} + a_{22}$, sondern die **Summe der Gegendiagonalelemente** realisiert durch einen linearen Operator $\operatorname{Spur}^*(A) \coloneqq a_{21} + a_{12}$, d.h., die Diagonale von links unten nach rechts oben in der Matrix.
In diesem Fall erhält man nämlich analog

```{math}
\Phi(x,y) = \langle x, y \rangle = x_1y_1 + x_2y_2 = \operatorname{Spur}^*
\begin{pmatrix}
x_1y_2 & x_1y_1 \\
x_2y_2 & x_2y_1
\end{pmatrix}
 = \operatorname{Spur}^*(x \otimes^* y) = p(x \otimes^* y).
```

Dies Veranschaulicht die Beziehung der involvierten Vektorräume und die zu Grunde liegende universelle Eigenschaft des Tensorprodukts.

````

```{danger}
Wir haben in {prf:ref}`ex:universelleEigenschaft` lediglich die universelle Eigenschaft zur Veranschaulichung überprüft für ein konkretes Beispiel.
Wir haben jedoch **nicht** gezeigt, dass das dyadische Produkt die *universelle Eigenschaft* erfüllt.
Dafür hätten wir die Äquivalenz für **alle möglichen** Bilinearformen $\Phi \in L^2(V \times W; Y)$ für **beliebige Vektorräume** $Y$ beweisen müssen.
```


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

## Äußere Formen

In {prf:ref}`ex:multi` haben wir für $k=2$ bereits den Begriff der Antisymmetrie kennengelernt. Dieser Fall lässt sich auf beliebige $k\in\N$ verallgemeinern, was zur Definition der äußeren Form führt.

````{prf:definition} Äußere Form
:label: aeussere_Form

Es sei $\V$ ein $n$--dimensionaler $\R$-Vektorraum und $k\in\N$. Dann heißt $\varphi\in L^k(E,\R)$ 
**äußere** $k$**-Form**,wenn sie **antisymmetrisch** ist, d.h., für alle $1\leq i<l\leq k$ und
$z\in \V^k$ gilt

```{math}
\varphi(z_1,\ldots,z_i,\ldots,z_l,\ldots,z_k) =-\varphi(z_1,\ldots,z_l,\ldots,z_i,\ldots,z_k).
```

Der Unterraum der äußeren $k$-Formen wird mit $\Lambda^k(\V)\subset L^k(\V,\R)$ bezeichnet.
````

````{prf:example}

$k=1$:

Hier fallen alle bisherigen Definitionen zusammen, d.h., 

```{math}
\Lambda^1(\V) = L^1(\V,\R)= \V^\ast
```

$k=2$:

Für $A\in\R^{2,2}$ definiert die Abbildung $(x,y)\mapsto\langle x,A y\rangle$ eine äußere $2$-Form auf $\R^n$ genau dann, wenn die Matrix $A$ antisymmetrisch ist. D.h., falls $A^T=-A$ gilt.

$k=n$:

Die Determinantenform ist bis auf ihre Vielfachen die einzige äußere $n$-Form auf dem $\R^n$.
````

Wir beweisen zwei kleine Hilfsaussagen zu äußeren Formen

````{prf:lemma}
Es sein $\V$ ein reeller Vektorraum und $\varphi\in\Lambda^k(V)$.
* Für jede Permutation $\pi:\{1,\ldots,k\}\rightarrow\{1,\ldots,k\}$ gilt 

```{math}
\varphi(z_{\pi(1)},\ldots,z_{\pi(k)}) = \sign(\pi) \varphi(z_1,\ldots,z_k).
```

* Sind $z_1,\ldots, z_k$ linear abhängig, so gilt $\varphi(z_1,\ldots,z_k) = 0$.

````

````{prf:proof}
Die erste Behauptung folgt direkt aus der Tatsache, dass sich jede Permutation als Verkettung endlich vieler Transpositionen schreiben lässt.
Für die zweite Behauptung sehen wir zunächst, dass 

```{math}
\varphi(z_1,\ldots,x,\ldots, x,\ldots,z_k) = -\varphi(z_1,\ldots,x,\ldots,x,\ldots,z_k)
```

und somit $\varphi(z_1,\ldots,x,\ldots,x,\ldots,z_k)=0$. Sind die $z_i$ nun linear abhängig, so existieren Skalare $\alpha_i$, s.d., 
ein $j$ existiert mit $\alpha_j\neq 0$ und 

```{math}
\sum_{i=1}^n \alpha_i z_i = 0 \Leftrightarrow z_j = 
\frac{1}{\alpha_j} \sum_{i\neq j} \alpha_i z_i.
```

Somit folgt

```{math}
\varphi(z_1,\ldots,z_j,\ldots,z_k) = 
\sum_{i\neq j} \alpha_i \varphi(z_1,\ldots,z_{j-1},z_i,z_{j+1},\ldots,z_k) = 0.
```

````

Wir werden nun eine Methode kennelernen die es uns erlaubt eine äußere $k$-Form als sogenanntes **äußeres Produkt** von $k$ vielen Linearformen zu erhalten.

````{prf:definition} Äußeres Produkt
Für einen Vektorraum $\V$ ist das **äußere Produkt** von $\omega_1,\ldots,\omega_k\in\Lambda^1(\V)$
durch

```{math}
\omega_1\wedge\ldots\wedge\omega_k:V^k&\to\R\\
(z_1,\ldots,z_k)&\mapsto 
\det
\begin{pmatrix}
\omega_1(z_1)&\ldots&\omega_k(z_1)\\ 
\vdots&&\vdots\\
\omega_1(z_k)&\ldots&\omega_k(z_k)
\end{pmatrix}
```

definiert.
````

````{prf:lemma}
Für einen Vektorraum $\V$ ist das äußere Produkt von $\omega_1,\ldots,\omega_k\in\Lambda^1(\V)$ eine $k$-Linearform. 
````

````{prf:proof}
Siehe Übung.
````

Insbesondere gilt damit für die Dualbasis $\eta_1,\ldots,\eta_n$ von $\V^*$, dass

```{math}
\eta_{i_1}\wedge\ldots\wedge\eta_{i_k}\in\Lambda^k(\V)
```

für beliebige Indexkombinationen $i_1,\ldots,i_k \in \{1,\ldots,n \}$. Wegen der Eigenschaften der Determinante gilt

```{math}
\eta_{i_1}\wedge\ldots\wedge\eta_{i_k} = \sign(\pi)\, \eta_{\pi(i_1)}\wedge\ldots\wedge\eta_{\pi(i_k)} 
```

wobei $\pi:\{i_1,\ldots,i_k\}\rightarrow\{i_1,\ldots,i_k\}$ eine Permutation ist, s.d.,

```{math}
\pi(i_1) <= \ldots <= \pi(i_j) <= \ldots <= \pi(i_k).
```

Desweiteren gilt auch

```{math}
\eta_{i_1}\wedge\ldots\wedge\eta_{i_k} &\neq 0\\
&\Leftrightarrow \\
i_{j}\neq i_l&\text{ für } j\neq l.
```

Wir können nun jede $k$-Form $\omega\in\Lambda^k(E)$ eindeutig als Linearkombination
```{math}
\omega = \sum_{1\leq i_1<\ldots<i_k\leq n}\omega_{i_1\ldots i_k}
\alpha_{i_1}\wedge\ldots\wedge\alpha_{i_k}
```
mit Koeffizienten
```{math}
\omega_{i_1\ldots i_k} := \omega(e_{i_1},\ldots,e_{i_k})\in\R
```
darstellen. Da
die Indexmengen $\{i_1,\ldots ,i_k\}$ die $k$--elementigen Teilmengen von$\{1,\ldots,n\}$ durchlaufen, gilt
für $\dim(E)=n$
```{math}
\dim\left(\Lambda^k(E)\right) = {n\choose k}.
```
Das  *äußere Produkt*
Produkt der $k$--Form $\omega$ mit einer $l$--Form
```{math}
\psi := \sum_{1\leq j_1<\ldots<j_{l}\leq n}\psi_{j_1\ldots j_l}\,
\alpha_{j_1}\wedge\ldots\wedge\alpha_{j_l}
```
wird nun distributiv als $\omega\wedge\psi\in\Lambda^{k+l}(E)$,
```{math}
\omega\wedge\psi := \sum_{1\leq i_1<\ldots<i_k\leq n} \sum_{1\leq
j_1<\ldots<j_l\leq n} \omega_{i_1\ldots i_k} \psi_{j_1\ldots j_l}
\alpha_{i_1}\wedge\ldots\wedge\alpha_{i_k}\wedge\alpha_{j_1}\wedge
\ldots\wedge\alpha_{j_l}
```
definiert. All diejenigen Summanden, bei denen ein Indexpaar $i_r=j_s$vorkommt, sind gleich Null, denn $\alpha_l\wedge\alpha_l = -\alpha_l\wedge\alpha_l=0$.

* Das äußere Produkt ist *assoziativ*, d.h. für beliebige äußere Formen auf $E$ gilt
```{math}
(\omega\wedge\psi)\wedge\rho = \omega\wedge(\psi\wedge\rho).
```
* Weiter gilt für eine $k$--Form $\omega$ und eine $l$--Form $\psi$
```{math}
\omega\wedge\psi = (-1)^{k\cdot l}\psi\wedge\omega,
```
denn wir müssen $k\!\cdot\! l$--mal Eins--Formen kommutieren, um von der einen
zur anderen Gestalt zu gelangen.


````{prf:example} [Wikipedia](https://de.wikipedia.org/wiki/Symplektischer_Vektorraum) *Symplektische Form*
:label: symplektische Form auf dem $\R^{2n}$
```{math}
\omega := \sum_{i=1}^n\alpha_i\wedge\alpha_{i+n}\in\Lambda^2(\R^{2n}).
```
Für $n=2$ ergibt sich
```{math}
\omega = \alpha_1\wedge\alpha_3+\alpha_2\wedge\alpha_4,
```
also
```{math}
\omega\wedge\omega &=& (\alpha_1\wedge\alpha_3+\alpha_2\wedge\alpha_4)
\wedge(\alpha_1\wedge\alpha_3+\alpha_2\wedge\alpha_4)\\
&=& \underbrace{\alpha_1\wedge\alpha_3\wedge\alpha_1\wedge\alpha_3}_0 +
\alpha_2\wedge\alpha_4\wedge\alpha_1\wedge\alpha_3\\
&& + \alpha_1\wedge\alpha_3\wedge\alpha_2\wedge\alpha_4 + \underbrace
{\alpha_2\wedge\alpha_4\wedge\alpha_2\wedge\alpha_4}_0\\
&=& (-1)^3\alpha_1\wedge\alpha_2\wedge\alpha_3\wedge\alpha_4 +
(-1)^1\alpha_1\wedge\alpha_2\wedge\alpha_3\wedge\alpha_4\\
&=& -2\alpha_1\wedge\alpha_2\wedge\alpha_3\wedge\alpha_4.
```
Die symplektische Form $\omega$ hat eine Schlüsselrolle in der Klassischen Mechanik. Dort bezeichnet man die Koordinaten $x_1,\ldots,
x_n$ als Impulskoordinaten, die Koordinaten $x_{n+1},\ldots, x_{2n}$ als
Ortskoordinaten.
````

````{prf:example} Vektoren und äußere Formen
Wir ordnen nun Vektoren
$v = \begin{pmatrix} v_1\\ \vdots\\ v_n \end{pmatrix} =\sum_{k=1}^nv_ke_k\in\R^n$ verschiedene äußere Formen zu.

* Das kanonische innere Produkt im $\R^n$ vermittelt einen Isomorphismus
```{math}
v\mapsto v^*,\ v^*(u) :=\, < v,u > \qquad(u\in\R^n)
```
des $\R^n$ und seines Dualraumes. Die Eins--Form $v^*$ besitzt dabei die Gestalt
```{math}
v^* = \sum_{i=1}^nv_i\alpha_i
\in\Lambda^1(\R^n).
```
* $v\in\R^n$ wird auch eine $(n-1)$--Form $\omega_v\in\Lambda^{n-1}(\R^n)$,
```{math}
\omega_v(u_2,\ldots,u_n) := \det(v,u_2,\ldots,u_n) \qquad (u_2,\ldots,u_n\in\R^n)
```
zugeordnet. Speziell im $\R^3$ finden wir die $2$--Form
```{math}
\omega_v = v_1\alpha_2\wedge\alpha_3+v_2\alpha_3\wedge\alpha_1+v_3
\alpha_1\wedge\alpha_2.
```
* Wir betrachten jetzt speziell den (physikalisch wichtigen) $\R^3$.
Das äußere Produkt zweier solcher $1$--Formen ergibtauf dem $\R^3$ die $2$--Form
```{math}
v^*\wedge u^* &=& (v_1\alpha_1+v_2\alpha_2+v_3\alpha_3)
\wedge(u_1\alpha_1+u_2\alpha_2+u_3\alpha_3)\\
&=& (v_1u_2-v_2u_1)\alpha_1\wedge\alpha_2+(v_2u_3-v_3u_2)\alpha_2\wedge
\alpha_3\\
&& + (v_3u_1-v_1u_3)\alpha_3\wedge\alpha_1\\
&=& \omega_{v\times u}.
```
Wir haben auf diese Weise das [*Kreuzprodukt*](https://de.wikipedia.org/wiki/Kreuzprodukt)
```{math}
v\times u=\begin{pmatrix} v_2u_3-v_3u_2\\v_3u_1-v_1u_3 \\ v_1u_2-v_2u_1 \end{pmatrix} \in\R^3
```
zweier Vektoren $v,u\in\R^3$ gewonnen.
````

````{prf:theorem}
Die Vektoren $w_1,\ldots,w_k\in E^*$ sind genau dann linear abhängig, wenn
```{math}
w_1\wedge\ldots\wedge w_k=0.
```
````

````{prf:proof}
* Wenn sie linear abhängig sind, können wir einen Index $i\in\{1,\ldots, k\}$ finden, für den $w_i$ eine Linearkombination $w_i=\sum_{\stackrel{l=1}{l\neq i}}^k c_l w_l$ ist. Damit gilt aber 
```{math}
w_1\wedge\ldots\wedge w_k = \sum_{\stackrel{l=1}{l\neq i}}^kc_l\, w_1 \wedge \ldots \wedge w_{i-1}\wedge w_l\wedge w_{i+1 \wedge\ldots\wedge w_k = 0,
```
denn in jedem Summanden kommt $w_l$ doppelt vor.
* Andernfalls können wir die Vektoren $w_1,\ldots,w_k$ zu einer Basis
```{math}
w_1,\ldots,w_n \text{ mit } n:=\dim(E^*)
```
ergänzen, sodass $w_1\wedge\ldots\wedge w_n\neq0$ ist.
Dann ist aber auch $w_1\wedge\ldots\wedge w_k\neq0$.
````
%
````{prf:definition} Grassmannalgebra
:label: Grassmannalgebra "uber $E$.
Für einen endlich-dimensionalen $\R$-Vektorraum $E$ heißt der reelle Vektorraum
```{math}
\Lambda^*(E) := \bigoplus_{k=0}^{\dim(E)}\Lambda^k(E)
```
(mit $\Lambda^0(E):=\R$) mit der durch das Dachprodukt
gegebenen Multiplikation die **äußere** oder
[**Grassmann-Algebra**](https://de.wikipedia.org/wiki/Gra%C3%9Fmann-Algebra)
````
````{prf:remark}
* $\dim(\Lambda^*(E)) = 2^{\dim(E)}$, denn $\sum_{k=0}^n{n\choose k} = 2^n$.
* Für beliebige $k,l\in\N_0$ ist für alle $\omega\in\Lambda^k(E)$ und
$\varphi\in\Lambda^l(E)$:\\ $\omega\wedge\varphi\in\Lambda^{k+l}(E)$, aber für
$m>\dim(E)$ ist $\dim(\Lambda^m(E))=0$.
````

````{prf:definition}
:label: pull-back von $\omega$ mit $f$.
Für eine lineare Abbildung $f:E\to F$ endlichdimensionaler $\R$--Vektorräume und $\omega\in\Lambda^k(F)$ heißt die durch
```{math}
f^*(\omega)( v_1,\ldots, v_k) := \omega \big(f( v_1),\ldots,f( v_k)\big)
\qquad (v_1,\ldots,v_k\in E)
```
definierte $k$--Form $f^*(\omega)$ die **Zurückziehung** (engl.
**pull--back**).
````
%
Es gilt offensichtlich $f^*(\omega)\in\Lambda^k(E)$, denn $f^*(\omega)$
ist $k$--linear und antisymmetrisch.
%
````{prf:theorem}
* Die Abbildung $f^*:\Lambda^*(F)\to\Lambda^*(E)$ ist linear.
* Für $g\in L(F,G)$ ist $(g\circ f)^*=f^*\circ g^*$.
* Für die identische Abbildung $Id_E:E\to E$ ist $Id_E^* = Id_{\Lambda^*(E)}$.
* Für eine invertierbare Abbildung $f\in {\rm GL}(E,F)$ ist $(f^*)^{-1}=(f^{-1})^*$.
* $f^*(\alpha\wedge\beta) = f^*(\alpha)\wedge f^*(\beta)$.
````

````{prf:proof}
Für alle Vektoren $v_1,\ldots,v_k\in E$ gilt
* Mit $\alpha, \beta\in\Lambda^k(F)$ und $c_1,c_2\in\R$ ist
```{math}
f^*(c_1\alpha+c_2\beta)(v_1,\ldots,v_k)
 &=& (c_1\alpha+c_2\beta) \big(f(v_1),\ldots,f(v_k)\big)\\
&=& c_1\alpha\big(f(v_1),\ldots,f(v_k)\big) + c_2\beta\big(f(v_1),\ldots,f(v_k)\big)\\
&=& c_1f^*\alpha(v_1,\ldots,v_k)+c_2f^*\beta(v_1,\ldots,v_k).
```
* $(g\circ f)^*\alpha( v_1,\ldots, v_k) = \alpha\big(g\circ f( v_1),\ldots, g\circ f( v_k)\big)= g^*\alpha\big(f( v_1),\ldots,f( v_k)\big)\\=  f^*\circ g^*\alpha( v_1,\ldots, v_k)$
* $Id_E^*(\alpha)(v_1,\ldots,v_k) = \alpha\big(Id_E(v_1),\ldots,Id_E(v_k)\big)
= \alpha(v_1,\ldots,v_k)$.
* Folgt aus 2. und 3.: $(f^{-1})^*f^* = (f\circ f^{-1})^* = Id_F^* =
Id_{\Lambda^*(F)}$.
* Hausaufgabe.

