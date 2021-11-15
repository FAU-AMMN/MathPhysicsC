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
\Psi&:\V\rightarrow \V^{\ast\ast}\\
\Psi(x)&:= (\varphi\mapsto \varphi(x))
```

ein Isomorphismus ist.

````
