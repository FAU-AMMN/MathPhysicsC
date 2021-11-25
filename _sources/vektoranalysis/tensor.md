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
:label: def:tensor

Es seien $V$ und $W$ zwei reelle Vektorräume.
Ein reeller Vektorraum $X$ heißt **Tensorproduktraum** falls eine bilineare Abbildung $\otimes:V\times W\rightarrow X$ existiert, so dass die folgende **universelle Eigenschaft** gilt:

Für jede Bilinearform $\phi\in L^2(V\times W; Y)$ in einen beliebigen reellen Vektorraum $Y$, existiert eine eindeutige lineare Abbildung 
$p \in L^1(X; Y)$, so dass gilt 

```{math}
:label: eq:universell
\phi(v,w) = p(v\otimes w) = p(\otimes(v,w))\quad\forall (v,w)\in V\times W.
```

Das bedeutet, dass die Vektorräume $L^2(V \times W; Y)$ und $L^1(X; Y)$ isomorph zueinander sind.
In diesem Fall schreibt man auch $X = V \otimes W$.
Wir nennen die bilineare Abbildung $\otimes$ **Tensorprodukt** und verwenden häufig für sie die Infix-Schreibweise $\otimes(v,w)=:v\otimes w$.
````

Diese Definition erscheint auf den ersten Blick abstrakt und unverständlich. 
Was ist jetzt also genau ein Tensorprodukt?

**Das Tensorprodukt ist universell:**

Wir haben in der {prf:ref}`def:tensor` das kartesische Produkt $\times$ benutzt welches eindeutig definiert ist. 
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

Wie wir weiter unten noch genauer beschreiben werden, stellt die universelle Eigenschaft eine wichtige Beziehung zwischen dem Raum der bilinearen Abbildungen auf $V\times W$ und dem Raum der linearen Abbildungen von $X = V\otimes W$ nach $Y$ für ein Tensorprodukt $\otimes$ her. 
Für den Spezialfall $Y = \R$ ist letzterer gerade der algebraische Dualraum des Tensorproduktraums.
Sofern wir das Tensorprodukt gegeben haben erhalten wir alle Bilinearformen also schon über einfache Linearformen auf $V\otimes W$.

Das folgende einfache Beispiel soll uns helfen diese Beziehung besser zu verstehen.

````{prf:example} Universelle Eigenschaft
:label: ex:universelleEigenschaft
Im Folgenden betrachten wir wieder den Euklidischen Vektorraum $V=W=\R^2$ und zwei Vektoren $x, y \in \R^2$.
Wie wir in {prf:ref}`ex:tensorproduktVarianten` festgestellt haben realisiert das dyadische Produkt 

```{math}
\otimes \colon \R^2 \times \R^2 \rightarrow \R^2 \otimes \R^2 = \R^{2 \times 2} =: X
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

Wir stellen fest, dass es für zwei beliebige $\R$-Vektorräume $V$ und $W$ immer ein Tensorprodukt gibt, und dass wir dieses Tensorprodukt konkret konstruieren können indem wir uns auf die Basis der Vektorräume $V$ und $W$ zurückziehen. 
Diese Tatsache formulieren wir in der folgenden Aussage.

````{prf:theorem} Existenz des Tensorprodukts
:label: thm:existenzTensorprodukt

Für zwei reelle Vektorräume $V, W$ existiert stets mindestens ein Tensorprodukt $\otimes\in L^2(V\times W; V\otimes W)$.
````

````{prf:proof}
Der folgende Beweis ist ein sogenannter *konstruktiver Beweis*, d.h., wir zeigen die Existenz eines Objekts indem wir es explizit angeben. 
Im Gegensatz hierzu gibt es auch nicht-konstruktive Existenzbeweise.

Es sei $B^V = \{b_i^V: i\in I^V\}$ eine Basis von $V$ und es sei analog $B^W = \{b_i^W: i\in I^W\}$ eine Basis von $W$ für zwei Indexmengen $I^V$ und $I^W$.
Wir betrachten zunächst das kartesische Produkt der beiden Indexmengen

```{math}
J := I^V \times I^W = \{(i,j): i\in I^V, j\in I^W\}.
```

Es sei nun $X$ ein reeller Vektorraum dessen Basis sich durch $J$ indizieren lässt, das heißt es existiert eine Menge 

```{math}
B^X = \{b_{ij}^X: (i,j)\in J\},
```

so dass $B^X$ eine Hamel-Basis von $X$ ist.
Ein solcher Vektorraum existiert immer, da zum Beispiel das kartesische Produkt $V\times W$ der beiden Vektorräume $V$ und $W$ diese Eigenschaft schon erfüllt.

Wir definieren nun eine bilineare Abbildung $\otimes: V\times W \to X$ über 

```{math}
\otimes (b_i^V, b_j^W) = b_i^V \otimes b_j^W := b_{ij}^X \quad \forall (i,j)\in J.
```

Es sei darauf hingewiesen, dass die bilineare Abbildung $\otimes$ durch eine Definition über die Indexmenge $J$ eindeutig festgelegt ist.
Dies liegt daran, dass für beliebige Paare $(v,w)\in V\times W$ endlich viele Koeffizienten $\alpha_{i_1},\ldots,\alpha_{i_n}$ und $\beta_{j_1},\ldots, \beta_{j_m}$ existieren, so dass für die Vektoren $v \in V$ und $w \in W$ eine Darstellung in den jeweiligen Hamel-Basen existiert mit

```{math}
v = \sum_{k=1}^n \alpha_{i_k} b_{i_k}^V, \quad w = \sum_{l=1}^m \beta_{j_l} b_{j_l}^W.
```

Durch diese Darstellung erhalten wir für die bilineare Abbildung $\otimes: V\times W \to X$ nun eine **explizite Vorschrift** als
```{math}
\otimes(v,w) 
= 
\otimes\big(\sum_{k=1}^n \alpha_{i_k} b_{i_k}^V, \sum_{l=1}^m \beta_{j_l} b_{j_l}^W\big) = 
\sum_{k=1}^n \sum_{l=1}^m \alpha_{i_k} \beta_{j_l} \otimes\left(b_{i_k}^V, b_{j_l}^W\right) =
\sum_{k=1}^n \sum_{l=1}^m \alpha_{i_k} \beta_{j_l} b_{i_kj_l}^X.
```

Wir müssen nun noch die **universelle Eigenschaft** der bilinearen Abbildung $\otimes$ nachweisen, um zu zeigen, dass es sich um ein Tensorprodukt handelt.
Sei dazu $\phi\in L^2(V\times W; Y)$ eine Bilinearform auf einen beliebigen reellen Vektorraum $Y$.
Dann können wir eine Linearform auf $p: X\to Y$ explizit definieren durch Angabe ihrer Wirkung auf die Basiselemente mit

```{math}
p(b_{ij}^X) := \phi(b_i^V, b_j^W) \quad \forall (i,j) \in J.
```

Dann gilt nämlich, unter Ausnutzung der Linearität von $p$ und der obigen Rechnung, dass gilt

```{math}
p(\otimes(v,w))
&= p \left( \sum_{k=1}^n \sum_{l=1}^m \alpha_{i_k} \beta_{j_l} b_{i_kj_l}^X \right)
= \sum_{k=1}^n \sum_{l=1}^m \alpha_{i_k} \beta_{j_l} p(b_{i_kj_l}^X) \\
&= \sum_{k=1}^n \sum_{l=1}^m \alpha_{i_k} \beta_{j_l} \phi\left(b_{i_k}^V, b_{j_l}^W\right)
= \phi\big(\sum_{k=1}^n \alpha_{i_k} b_{i_k}^V,\sum_{l=1}^m \beta_{j_l} b_{j_l}^W\big)
= \phi(v,w)
```

Wir sehen also, dass $\otimes$ die universelle Eigenschaft erfüllt und zwar insbesondere dadurch, dass die Linearform $p$ durch die obige Definition eindeutig festgelegt ist.

````

Als Korollar aus {prf:ref}`thm:existenzTensorprodukt` erhalten wir somit, dass eine Basis des Tensorproduktraums durch das kartesische Produkt der ursprünglichen Basen konstruiert werden kann. 
Hieran sieht man den qualitativen Unterschied zwischen $V \times W$ und $V\otimes W$.

````{prf:corollary}
Für zwei reelle Vektorräume $V$ und $W$ mit zugehörigen Basen 

```{math}
B^V = \{b_i^V: i\in I^V\}, \quad B^W = \{b_i^W: i\in I^W\},
```

 und einem Tensorprodukt $\otimes:V\times W \to V\otimes W$ ist 

```{math}
B^X \, \coloneqq \, \{b_i^V \otimes b_j^W: i\in I^V, j\in I^W\}
```

eine Basis von $X = V\otimes W$.
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

**Das Tensorprodukt?**

Die letzte Aussage zeigt also, dass obwohl es verschiedene Arten gibt Tensorprodukte auf Vektorräumen $V,W$ zu definieren, diese stets isomorph zueinander sind. Deshalb spricht man auch von **dem** Tensorprodukt $V\otimes W$ was so klingt als gäbe es nur ein einziges. In der Tat gibt es zwar mehrere Tensorprodukte aber man kann sie alle miteinander identifizieren.

Deshalb werden wir im folgendem auch von **dem** Tensorprodukt sprechen.

## Natürliche Isomorphismen und Eigenschaften des Tensorprodukts

Die Definition über die universelle Eigenschaft erlaubt es uns relativ direkt folgende Isomorphismen zu erhalten.

````{prf:lemma} Isomorphismen

Es seien $V_1,V_2,V_3$ reelle Vektorräume, dann haben wir folgende Isomorphismen.

1. $V_1\otimes V_2 \cong V_2\otimes V_1$,

2. $(V_1\otimes V_2)\otimes V_3 \cong V_1 \otimes (V_2 \otimes V_3)$,

3. $\R \otimes V_1 \cong V_1$,

4. $L(V_1, L(V_2, V_3))\cong L(V_1\otimes V_2, V_3)$.

````

````{prf:proof}
Siehe Übung.
````

Die zweite Eigenschaft erlaubt es uns das Tensorprodukt über $k$-viele reelle Vektorräume $V_1,\ldots, V_k$ zu bilden, wir notieren

```{math}
\bigotimes_{i=1}^k=V_1\otimes\ldots\otimes V_k
```

und sehen, dass diese Objekt wohldefiniert ist. Insbesondere ist äquivalent das Tensorprodukt über $k$-Vektorräume mithilfe einer
$k$-Multilinearform zu definieren anstatt der Bilinearform in {prf:ref}`def:tensor`.

Die letzte Eigenschaft wird insbesondere wichtig um Tensorprodukte von Dualräumen zu charakterisieren. Dafür benötigen wir zusätzlich folgendes Prinzip, was man in der Algebra unter [Funktoren](https://de.wikipedia.org/wiki/Funktor_(Mathematik)) kennt. Konkret wollen wir nun für reelle Vektorräume $V_1,V_2, W_1, W_2$ das Tensorprodukt

```{math}
\mathrm{Hom}(V_1, W_1) \otimes \mathrm{Hom}(V_2, W_2)
```

untersuchen.

````{prf:lemma}
Es seinen $V_1,V_2, W_1,W_2$ reelle Vektorräume und $\phi_1\in \mathrm{Hom}(V_1, W_1), \phi_2 \in \mathrm{Hom}(V_2, W_2)$, dann existiert **genau ein** Tensorprodukt, s.d., 

```{math}
(\phi_1 \otimes \phi_2)
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
