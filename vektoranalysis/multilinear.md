# Multilinearformen

In diesem Abschnitt wollen wir die Definition der sogenannten *Multilinearformen* einführen.
Für beliebige Vektorräume $\V, W$ über einem Körper $\K$ haben Sie bereits den Begriff der *Linearform*, also einer linearen Abbildung $\varphi:\V\rightarrow W$ kennengelernt.
Die Idee der Multilinearform ist anstatt nur einem, gleich $k$-viele Vektorräume $V_1,\ldots,V_k$ für $k \in \N$ über $\K$ zu betrachten und das Konzept der Linearität auf eine Abbildung $\varphi:\V_1\times\ldots\V_k\rightarrow W$ zu übertragen. 

Zur Vereinfachung werden wir im Folgenden nur den Körper $\K=\R$ betrachten, in den meisten Fällen lassen sich die hier beschriebenen Konzepte aber direkt auf allgemeine Körper übertragen.
Wir beginnen zunächst mit einer Wiederholung und betrachten die schon bekannten Linearformen. 
Insbesondere soll der nächste Abschnitt die verschiedenen Begriffe des Dualraums abgrenzen.

## Dualräume

Für einen reellen Vektorraum $\V$ wollen wir lineare Abbildungen $\varphi:V\to\R$ betrachten.
Diese lassen sich mit Hilfe der folgenden Definition zum algebraischen Dualraum zusammenfassen.
````{prf:definition} Algebraischer Dualraum
:label: def:algebraischerDualraum
Es sei $\V$ ein beliebiger $\R$-Vektorraum. 
Dann nennen wir die Menge 

```{math}
\V^\ast := \{\varphi:\V\rightarrow\R: \varphi\text{ ist linear}\}
```

den **algebraischer Dualraum** zu $V$.
````

Aus {cite:p}`tenbrinck_2021` ist bereits der Begriff des *topologischen Dualraums* bekannt, welcher allerdings eine etwas restriktivere Definition hat. 
Sie fordert nämlich noch zusätzlich die Stetigkeit der linearen Abbildungen.

````{prf:definition} Topologischer Dualraum
:label: def:topologischerDualraum
Es sei $\V$ ein normierter $\R$-Vektorraum für einen Körper $\R$. 
Dann nenne wir die Menge 

```{math}
\V^\prime := \{\varphi:\V\rightarrow\R: \varphi\text{ ist linear und stetig}\}
```

den **topologischer Dualraum** zu $V$.
````

```{danger}
Der algebraische Dualraum ist im Allgemeinen nicht gleich dem topologischen Dualraum.
Der Hauptzweck dieses Abschnitts ist es diese Tatsache klar zu machen und die Unterschiede der beiden Definitionen herauszustellen.
```

Folgende Bemerkung sagt etwas über die minimale Struktur, die der Vektorraum $V$ haben muss, damit die Definition des topologischen Dualraums sinnvoll ist.
````{prf:remark}
Damit die {prf:ref}`def:topologischerDualraum` sinnvoll ist, ist es in der Tat nicht notwendig, dass $V$ ein normierter Raum ist. Es reicht anzunehmen, dass $\V$ ein *topologischer Vektorraum* ist.
````

 Durch Vergleichen von {prf:ref}`def:algebraischerDualraum` und {prf:ref}`def:topologischerDualraum` erkennt man sofort, dass stets $\V^\prime\subset \V^\ast$ gilt. 
 Außerdem stellt man fest, dass die beiden Räume im endlich-dimensionalen Fall überein stimmen, wie folgendes Lemma aussagt.
````{prf:lemma}
Für $n\in\N$ sei $\V$ ein $n$-dimensionaler $\R$-Vektorraum, dessen Norm durch das Standardskalarprodukt induziert ist.
Dann gilt 

```{math}
V^\prime = V^\ast.
```

````
````{prf:proof}
In der Hausaufgabe zu zeigen.
````

Das folgende Beispiel aus der Funktionalanalysis erklärt, dass die Gleichheit von algebraischen und topologischen Dualräumen nicht mehr in unendlich-dimensionalen Räumen gilt.
````{prf:example} Differentialoperator
Wir betrachten im Folgenden den *Differentialoperator*

```{math}
D \colon C^1[0,1] &\rightarrow C^1[0,1] \\
(Df)(x) &\mapsto f'(x), \quad \forall x \in [0,1]
```

der auf dem Raum der stetig differenzierbaren Funktionen auf dem Intervall $[0,1]$ definiert ist.

Offensichtlich ist der Differentialoperator $D$ **linear** und ist somit ein Element des algebraischen Dualraums, d.h., $D \in (C^1[0,1])^\ast$.
Statten wir den Vektorraum $C^1[0,1]$ mit der *Supremumsnorm* 

```{math}
||f||_\infty := \sup_{x \in [0,1]} |f(x)|
```

aus und betrachten die Funktionenfolge $f_n(x) := x^n$, dann sehen wir ein, dass die Supremumsnorm der Folge konstant ist mit $||f_n||_\infty \equiv 1$ für alle $n\in\N$, jedoch für den Differentialoperator $D$ gilt

```{math}
||Df_n||_\infty = \sup_{x \in [0,1]} |(Df_n)(x)| = \sup_{x \in [0,1]} |f_n'(x)| = \sup_{x \in [0,1]} |nx^{n-1}| = n.
```

Wir sehen also ein, dass 

```{math}
\frac{||Df_n||_\infty}{||f_n||_\infty} \overset{n\rightarrow \infty}{\longrightarrow} \infty
```

gilt und somit der der Differentialoperator **nicht stetig** ist und somit kein Element des topologischen Dualraums $(C^1[0,1])'$ sein kann.
Damit haben wir gezeigt, dass in unendlich-dimensionalen Räumen $(C^1[0,1])' \subsetneq (C^1[0,1])^\ast$ gilt.

````

## k-Multilinearformen

Wir verallgeminern nun den Begriff der Linearität in der folgenden Definition.

````{prf:definition}
:label: def:multilinear

Für $i=1,\ldots,k$ sei $\V_i$, sowie $W$ ein reeller Vektorraum. Eine Abbildung 

```{math}
\varphi:\V_1\times\ldots\times \V_k\ \to W
``` 

heißt k-**(multi)linear**, wenn für beliebige $z_i\in\V_i$ und jede Komponente $i\in\{1,\ldots,k\}$ die Abbildung 

```{math}
V_i &\to W\\
x&\mapsto \varphi_i(x):= \varphi(z_1,\ldots, z_{i-1}, x, z_{i+1},\ldots,z_k)
```

linear ist. Die Menge aller $k$-linearen Abbildungen wird mit $L^k(\V_1\times\ldots\times \V_k, W)$ bezeichnet.
````

````{prf:remark}
Ausgeschrieben bedeutet die Bedingung in der obigen Definition, dass für alle $z_i\in V_i$, $\lambda\in\R$, 
und insbesondere für jedes $i\in\{1,\ldots,k\}$, $x,y\in \V_i$  gilt,

```{math}
\varphi(z_1,\ldots,z_{i-1},\lambda x, z_{i+1},\ldots,z_k) = \lambda
\varphi(z_1,\ldots,z_{i-1}, x, z_{j+1}, \ldots,z_k)
```

und


```{math}
&\varphi(z_1,\ldots,z_{i-1},x+y,z_{j+1},\ldots,z_k)\\
= 
&\varphi(z_1,\ldots,x,\ldots,z_k) + \varphi(z_1,\ldots,y,\ldots,z_k).
```

````

Falls alle Vektorräume übereinstimmen, d.h., $\V_i = \V$ für alle $i=1,\ldots,k$, so schreibt man auch $L^k(\V\times\ldots\times \V,W) = L^k(\V,W)$.

Viele multilineare Abbildungen sind schon aus der Linearen Algebra vertraut. Im folgenden Beispiel wiederholen wir einige bekannte Beispiele unter dem Aspekt der Multilinearität.

````{prf:example}
:label: ex:multi

Wir betrachten Beispiele für verschiedene $k\in\N$.

**$k=1$**:

In diesem Fall haben wir bereits gesehen, dass $L^1(\V,\R) = \V^\ast$.

**$k=2$**:

Es sei $\V=\R^n$ mit kanonischem innerem Produkt $\langle\cdot,\cdot\rangle$. Für $A\in\R^{n,n}$ ist 

```{math}
\varphi:\V\times \V\to\R\\ 
\varphi(x, y) :=\langle x,A y \rangle
```

eine **Bilinearform**. Sie heißt _symmetrisch_,
falls

```{math}
\varphi(x, y) = \varphi( y, x)\qquad (x, y\in \V)
```

und _antisymmetrisch_ falls

```{math}
\varphi(x, y) = -\varphi( y, x)\qquad (x, y\in \V).
```

**$k=n$**:

Es sei $\V=\R^n$. Die $n$-lineare Abbildung

```{math}
\varphi(z_1,\ldots,z_n) := \det((z_1,\ldots,z_n))
```

heißt **Determinantenform**. Wir beachten, dass hierbei jedes $z_i\in\R^n$ ein Vektor und $(z_1,\ldots,z_n)$ eine Matrix ist.
Die Form gibt das orientierte Volumen des von $z_1,\ldots,z_n$ aufgespannten Parallelotops an.
````

## Der Vektorraum der Multilinearformen

Die Definition einer $k$-linearen Abbildung ermöglicht es uns sehr direkt eine Vektorraumstruktur zu definieren.

````{prf:lemma}
Es seien $\V_1,\ldots,\V_k$ sowie $W$ reelle Vektorräume, dann ist die Menge $L^k(\V_1\times\ldots\V_k,W)$ ein Vektorraum über $\R$ bezüglich der Addition 

```{math}
(\varphi_1+\varphi_2)(z_1,\ldots,z_k) := \varphi_1(z_1,\ldots,z_k) +
\varphi_2(z_1,\ldots,z_k),\quad \varphi_1,\varphi_2\in L^k(\V,\R)
```
und der Skalarmultiplikation

```{math}
(\lambda\varphi)(z_1,\ldots,z_k) := \lambda\big(\varphi(z_1,\ldots,z_k)\big),\quad\varphi\in L^k(\V,\R), \lambda\in\R.
```

````

````{prf:proof}
Siehe Übung.
````

Als wichtigen Spezialfall erhalten wir für $k=1$ den Dualraum $L^1(\V,\R)$. Für diesen Vektorraum können wir eine spezielle Basis charakterisieren, die sogenannte **duale Basis**.

````{prf:lemma} Duale Basis
Es sei $\V$ ein $n$-dimensionaler $\R$-Vektorraum mit einer Basis $B = (b_1,\ldots,b_n)$, die Abbildungen 
$\eta_i:\V\rightarrow\R$ für $i=1,\ldots,n$,

```{math}
\eta_i(z) = \eta_i\left(\sum_{i=1}^n \alpha_i b_i\right) := \alpha_i
```

bilden einen Basis von $\V^\ast$, die sogenannte **duale Basis** zu $B$. 

````

````{prf:example} Duale Basis
Rn mit Standardbasis ist es Multiplikation von rechts mit Transponierter Standardbasis.
````

````{prf:remark}
Insbesondere zeigt diese Aussage, dass $\dim(\V) = \dim(\V^\ast)$.
````

````{prf:proof}
Wir zeigen zunächst, dass $\eta_i\in\V^\ast$. Dazu sei $x,y\in\V$, dann existieren skalare 
$\alpha_i^x,\alpha_i^y\in\R$ für $i=1,\ldots,n$, s.d., 

```{math}
x &= \sum_{i=1}^n \alpha_i^x b_i\\
y &= \sum_{i=1}^n \alpha_i^y b_i.
```

Somit haben wir 

```{math}
\eta_i(x+y) &= \eta_i\left(\sum_{i=1}^n \alpha_i^x b_i + \alpha_i^y b_i\right) 
\\&=
\eta_i\left(\sum_{i=1}^n (\alpha_i^x + \alpha_i^y) b_i\right) 
\\&=
\alpha_i^x + \alpha_i^y
\\&=
\eta_i\left(\sum_{i=1}^n \alpha_i^x b_i\right)  + \eta_i\left(\sum_{i=1}^n \alpha_i^y b_i\right)
\\&=
\eta_i(x) + \eta_i(y).
```

Weiterhin gilt für $\lambda\in\R$ 

```{math}
\eta_i(\lambda x) &= \eta_i\left(\lambda \sum_{i=1}^n \alpha_i^x b_i\right) 
\\&=
\eta_i\left(\sum_{i=1}^n (\lambda \alpha_i^x) b_i\right) 
\\&=
\lambda \alpha_i^x
\\&=
\lambda \eta_i(x)
```

und damit ist $\eta_i$ linear. 
Sei nun $\phi\in\V^\ast$, dann gilt 

```{math}
\phi(x) = \phi\left(\sum_{i=1}^n \alpha_i^x b_i\right) = \sum_{i=1}^n \alpha_i^x \phi(b_i) = 
\sum_{i=1}^n \eta_i(x) \phi(b_i),
```

insbesondere gilt also $\phi = \sum_{i=1}^n \eta_i \phi(b_i$).

Somit bilden die Abbildungen $\eta_i$ ein Erzeugenden System, da jedes $\phi$ als Linearkombination dargestellt werden kann. 
Weiterhin seien $a_i\in\R$ gegeben, s.d., $0 = \sum_{i=1}^n a_i \eta_i$, damit folgt für jedes $j=1,\ldots,n$,  

```{math}
0 = \left(\sum_{i=1}^n a_i \eta_i\right)(b_j) = \sum_{i=1}^n a_i \eta_i(b_j) = a_j
```

und damit ist die Aussage bewiesen.

````

````{prf:remark}
Die Aussage lässt sich auf den Fall eines unendlich-dimensionalen Vektorraums übertragen. Hierfür erinnern wir daran, dass für einen Vektorraum $V$ stets eine Basis $B^V = \{b_i^v:i\in I\}\subset V$ existiert wobei $I$ eine (nicht notwendigerweise endliche) Indexmenge ist. Insbesondere bemerken wir, dass wir hier von einer **Hamelbasis** sprechen, d.h., für jedes Element $v\in V$ gibt es eindeutig bestimmte Koeffizienten $\alpha_i, i\in I$ s.d.

```{math}
v = \sum_{i\in I} \alpha_i b_i.
```

Der wichtige Punkt ist aber, dass nur **endlich viele** $\alpha_i$ ungleich null sind und die Summation somit keine eigentlich unendliche Reihe beschreibt sondern nur eine endliche Summe. Diese Konzept ist insbesondere verschieden vom Begriff der [Schauderbasis](https://de.wikipedia.org/wiki/Schauderbasis)
````

```{margin} Georg Hamel
[Georg Karl Wilhelm Hamel](https://de.wikipedia.org/wiki/Georg_Hamel) (Geboren 12. September 1877 in Düren; Gestorben 4. Oktober 1954 in Landshut) war ein deutscher Mathematiker.
```

```{margin} Juliusz Schauder
[Juliusz Paweł Schauder](https://de.wikipedia.org/wiki/Juliusz_Schauder) (Geboren 21. September 1899 in Lemberg; Gestorben September 1943) war ein polnischer Mathematiker.
```

Wir halten weiterhin fest, dass sich der doppelt duale Raum im endlich-dimensionalen Fall leicht charakterisieren lässt.

````{prf:lemma}
:label: lem:doubledual

Es sei $\V$ ein $n$-dimensionaler reeller Vektorraum, dann gilt, dass die Abbildung 

```{math}
\Psi:\V\rightarrow \V^{\ast\ast}
\Psi(x) := (\varphi\mapsto \varphi(x))
```

ein Isomorphismus ist.

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