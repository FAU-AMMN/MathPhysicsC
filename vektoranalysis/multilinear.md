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
Dann nennen wir die Menge 

```{math}
\V^\prime := \{\varphi:\V\rightarrow\R: \varphi\text{ ist linear und stetig}\}
```

den **topologischer Dualraum** zu $V$.
````

```{danger}
Der algebraische Dualraum ist im Allgemeinen nicht gleich dem topologischen Dualraum.
Der Hauptzweck dieses Abschnitts ist es diese Tatsache klar zu machen und die Unterschiede der beiden Definitionen herauszustellen.
```

Der Integraloperator ist ein typisches Beispiel für einen linearen stetigen Operator.
````{prf:example} Integraloperator
Es sei $\V := C([0,1])$ der Funktionenraum der stetigen Funktionen auf dem Intervall $[0,1] \subset \R$.
Dann ist der durch $T \colon C([0,1]) \rightarrow \R$ definierte Integraloperator mit

```{math}
T(f) := \int_0^1 f(x) \, \mathrm{d}x
```

ein Element des *topologischen Dualraums*, d.h. $T \in \V^\prime$, da man zeigen kann, dass er linear und stetig ist.

````

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
Sei $\V := C^1([0,1])$ der Vektorraum der stetig differenzierbaren Funktionen auf dem Intervall $[0,1] \subset \R$.
Wir betrachten im Folgenden den *Differentialoperator*

```{math}
D \colon V &\rightarrow \R \\
(Df)(x) &\mapsto f'(x), \quad \forall x \in [0,1].
```

Bekanntermaßen ist der Differentialoperator $D$ **linear** und ist somit ein Element des algebraischen Dualraums, d.h., $D \in V^\ast$.
Statten wir den Vektorraum $C^1([0,1])$ mit der *Supremumsnorm* 

```{math}
||f||_\infty := \sup_{x \in [0,1]} |f(x)|
```

aus und betrachten die Funktionenfolge $f_n(x) := x^n$, dann sehen wir ein, dass die Supremumsnorm der Folge konstant ist mit $||f_n||_\infty \equiv 1$ für alle $n\in\N$.
Für den Differentialoperator $D$ gilt jedoch

```{math}
||Df_n||_\infty = \sup_{x \in [0,1]} |(Df_n)(x)| = \sup_{x \in [0,1]} |f_n'(x)| = \sup_{x \in [0,1]} |nx^{n-1}| = n.
```

Um die *Stetigkeit* des Differentialoperators zu untersuchen betrachten wir die konstante Nullfunktion $F_0 \in V$ mit $F_0(x) \equiv 0$ für alle $x \in [0,1]$.
Vergleichen wir nun den Abstand der konstanten Nullfunktionen zum ersten Folgenglied $f_1$ unserer Funktionenfolge, so erhalten wir erwartungsgemäß

```{math}
||f_1 - F_0||_\infty = ||f_1||_\infty = ||x^1||_\infty = 1 < \frac{3}{2} =: \delta.
```

Für den Differenzialoperator erhalten wir analog
```{math}
||Df_1 - DF_0||_\infty = ||Df_1||_\infty = ||1||\infty < \frac{3}{2} =: \epsilon.
```

Wäre der Differenzialoperator $D$ stetig, so müsste nach dem $\epsilon-\delta$-Kriterium nun für jedes Folgenglied $f_n$ unserer Funktionenfolge $||Df_n - DF_0|| < \epsilon$ gelten, da der Abstand kleiner $\delta$ ist wegen

```{math}
||f_n - F_0||_\infty = ||f_n||_\infty = ||x^n||_\infty = 1 < \delta.
```

Jedoch sehen wir, dass die Folge der Ableitungen divergiert, d.h.,

```{math}
||Df_n - DF_0||_\infty = ||Df_n||_\infty = ||nx^{n-1}||_\infty = n > \epsilon \quad \text{für } n\geq 2.
```

Wir sehen also ein, dass der Differentialoperator **nicht stetig** ist und somit kein Element des topologischen Dualraums $V'$ sein kann.
Damit haben wir gezeigt, dass in unendlich-dimensionalen Räumen $V' \subsetneq V^\ast$ gilt.
````

## k-Multilinearformen

Nachdem wir uns den Begriff der Linearität ins Gedächtnis zurückgerufen haben und Dualräume erklärt haben, wollen wir was Konzept linearer Abbildungen in der folgenden Definition verallgemeinern.

````{prf:definition} k-Multilinearität
:label: def:multilinear

Sei $k \in \N$ und es seien $\V_i, i=1,\ldots,k$, sowie $W$ reelle Vektorräume. 

Wir nennen eine Abbildung 

```{math}
\varphi : \V_1\times\ldots\times \V_k\ \to W
``` 

**k-(multi)linear**, falls alle zugehörigen partiellen Abbildungen $\varphi_i$ für $i\in\{1,\ldots,k\}$ mit

```{math}
\varphi_i \colon V_i &\to W\\
x&\mapsto \varphi_i(x):= \varphi(z_1,\ldots, z_{i-1}, x, z_{i+1},\ldots,z_k)
```

*linear* sind.

Die Menge aller $k$-linearen Abbildungen wird mit $L^k(\V_1\times\ldots\times \V_k; W)$ bezeichnet.
Falls alle Vektorräume übereinstimmen, d.h., $\V_i = \V$ für alle $i=1,\ldots,k$ gilt, so schreibt man auch $L^k(\V\times\ldots\times \V; W) =: L^k(\V; W)$.
````

````{prf:remark}
Ausgeschrieben bedeutet die Bedingung in der obigen Definition, dass für beliebige Vektoren $x,y\in \V_i$ und Skalare $\lambda \in \R$ gilt

```{math}
\varphi(z_1,\ldots,z_{i-1},\lambda \cdot x, z_{i+1},\ldots,z_k) = \lambda \cdot \varphi(z_1,\ldots,z_{i-1}, x, z_{i+1}, \ldots,z_k)
```

und

```{math}
\varphi(z_1,\ldots,z_{i-1},x+y,z_{i+1},\ldots,z_k) = \varphi(z_1,\ldots,x,\ldots,z_k) + \varphi(z_1,\ldots,y,\ldots,z_k).
```

für jedes Argument $i = 1,\ldots,k$ der Abbildung $\varphi \colon V_1 \times \ldots \times \V_k \rightarrow W$.

````

Viele multilineare Abbildungen kennen wir bereits aus der Linearen Algebra ohne sie bisher so bezeichnet zu haben.
Im folgenden Beispiel wiederholen wir einige bekannte Beispiele unter dem Aspekt der Multilinearität.

````{prf:example}
:label: ex:multilinear

Wir betrachten im Folgenden Beispiele für $k$-lineare Abbildungen mit verschiedenen $k\in\N$.

**$k=1$**: In diesem einfachen Fall sind alle Linearformen $1$-linear.
Daher ist der Raum der $1$-Linearformen gerade der algebraische Dualraum aus {prf:ref}`def:algebraischerDualraum`, d.h. es gilt $L^1(\V; \R) = \V^\ast$.

<br/><br/>
**$k=2$**: Es sei $\V=\R^n$ der Euklidische Vektorraum mit kanonischem innerem Produkt $\langle\cdot,\cdot\rangle$. 
Für $A\in\R^{n,n}$ ist 

```{math}
\varphi:\V\times \V &\to\R\\ 
(x,y) &\mapsto \varphi(x, y) :=\langle x,A y \rangle
```

eine **Bilinearform** bzw. eine $2$-Linearform nach {prf:ref}`def:multilinear`. 
Sie heißt _symmetrisch_, falls

```{math}
\varphi(x, y) = \varphi(y, x), \quad \forall x, y\in \V
```

und _antisymmetrisch_ falls

```{math}
\varphi(x, y) = -\varphi(y, x), \quad \forall x, y\in \V.
```

<br/><br/>
**$k=n$**: Es sei $n\in \N$ und $\V=\R^n$ der Euklidische Vektorraum.
Die $n$-lineare Abbildung

```{math}
\varphi :\V \times \ldots \times \V &\to\R\\ 
(z_1, \ldots, z_n) &\mapsto \varphi(z_1,\ldots,z_n) := \det([z_1,\ldots,z_n])
```

heißt **Determinantenform**.
Wir beachten, dass hierbei jedes $z_i \in \R^n$ für $i=1,\ldots,n$ ein Vektor ist und es sich bei $[z_1,\ldots,z_n] \in \R^{n\times n}$ um eine Matrix handelt.
Die Determinantenform gibt das orientierte Volumen des von den Vektoren $z_1,\ldots,z_n$ aufgespannten Parallelotops an.
````

## Der Vektorraum der Multilinearformen

Die Menge der $k$-linearen Abbildung $L^k(V_1,\ldots,V_k; W)$ für $\R$-Vektorräume $V_1,\ldots,V_k$ und $W$ besitzt mehr Struktur als wir ihr bisher angesehen haben.
Mit den entsprechenden Verknüpfungen handelt es sich ebenfalls um einen Vektorraum, wie das folgende Lemma zeigt.

````{prf:lemma}
Sei $k \in \N$ und es seien $\V_1,\ldots,\V_k$ sowie $W$ reelle Vektorräume.
Dann ist die Menge $L^k(\V_1\times\ldots\V_k; W)$ ein Vektorraum über $\R$ bezüglich der Addition 

```{math}
(\varphi_1+\varphi_2)(z_1,\ldots,z_k) := \varphi_1(z_1,\ldots,z_k) +
\varphi_2(z_1,\ldots,z_k),
```
für $k$-lineare Abbildungen $\varphi_1,\varphi_2\in L^k(\V_1, \ldots, V_k;W)$ und der Multiplikation mit Skalaren $\lambda \in \R$

```{math}
(\lambda\varphi)(z_1,\ldots,z_k) := \lambda\big(\varphi(z_1,\ldots,z_k)\big),\quad\varphi\in L^k(\V_1, \ldots, V_k;W).
```

````

````{prf:proof}
In der Hausaufgabe zu zeigen.
````

Wir wir bereits in {prf:ref}`ex:multilinear` gesehen haben erhalten wir einen wichtigen Spezialfall für $k=1$, nämlich den algebraischen Dualraum $V^\ast = L^1(\V;\R)$. 
Für diesen Vektorraum können wir eine spezielle Basis angeben, wie das folgende Lemma zeigt.

````{prf:lemma} Duale Basis
:label: lem:dualeBasis
Es sei $\V$ ein $n$-dimensionaler $\R$-Vektorraum mit einer endlichen Basis $B = (b_1,\ldots,b_n)$.
Für beliebige Vektoren $z \in V$ bilden die Abbildungen $\eta_i:\V\rightarrow\R$ für $i=1,\ldots,n$ mit

```{math}
\eta_i(z) := \eta_i\left(\sum_{i=1}^n \alpha_i b_i\right) := \alpha_i
```

eine Basis des algebraischen Dualraums $\V^\ast$.
Diese spezielle Basis wird auch die **duale Basis** zur Basis $B$ genannt. 

````

````{prf:proof}
Wir zeigen zunächst, dass $\eta_i\in\V^\ast$ für $i=1,\ldots,n$. 
Dazu seien $x,y\in\V$ beliebige Vektoren.
Dann existieren Koeffizienten $\alpha_i^x,\alpha_i^y \in \R$ für $i=1,\ldots,n$, so dass es eine eindeutige Darstellung als Linearkombination der Basisvektoren gibt mit

```{math}
x = \sum_{i=1}^n \alpha_i^x b_i, \qquad y = \sum_{i=1}^n \alpha_i^y b_i.
```

Somit haben wir also für die Summe der Vektoren

```{math}
\eta_i(x+y) &= 
\eta_i\left(\sum_{i=1}^n \alpha_i^x b_i + \sum_{i=1}^n \alpha_i^y b_i\right) = 
\eta_i\left(\sum_{i=1}^n \alpha_i^x b_i + \alpha_i^y b_i\right) = 
\eta_i\left(\sum_{i=1}^n (\alpha_i^x + \alpha_i^y) b_i\right) 
\\&= \alpha_i^x + \alpha_i^y = 
\eta_i\left(\sum_{i=1}^n \alpha_i^x b_i\right)  + \eta_i\left(\sum_{i=1}^n \alpha_i^y b_i\right) = 
\eta_i(x) + \eta_i(y).
```

Weiterhin gilt für beliebige Skalare $\lambda\in\R$ 

```{math}
\eta_i(\lambda x) = \eta_i\left(\lambda \sum_{i=1}^n \alpha_i^x b_i\right) = 
\eta_i\left(\sum_{i=1}^n (\lambda \alpha_i^x) b_i\right) =
\lambda \alpha_i^x =
\lambda \eta_i(x).
```

Damit haben wir also gezeigt, dass die Elemente der dualen Basis $\eta_i$ linear sind und somit gilt $\eta_i \in V^\ast$ für $i=1,\ldots,n$. 

Sei nun $\phi\in \V^\ast$, dann gilt 

```{math}
\phi(x) = \phi\left(\sum_{i=1}^n \alpha_i^x b_i\right) = \sum_{i=1}^n \alpha_i^x \phi(b_i) = 
\sum_{i=1}^n \eta_i(x) \phi(b_i),
```

insbesondere gilt also $\phi = \sum_{i=1}^n \phi(b_i) \eta_i$.

Somit bilden die Abbildungen $\eta_i$ ein Erzeugendensystem von $V^\ast$, da jede lineare Abbildung $\phi \in V^\ast$ als Linearkombination dargestellt werden kann. 

Um zu zeigen, dass es sogar um eine Basis des algebraischen Dualraums handelt, müssen wir noch zeigen, dass das Nullelement des Vektorraums eine eindeutige Darstellung besitzt.
Seien also Koeffizienten $a_i\in\R$ gegeben, so dass $0 = \sum_{i=1}^n a_i \eta_i$ die Nullabbildung realisiert.
Dann folgt schon für jedes $j=1,\ldots,n$

```{math}
0 = \left(\sum_{i=1}^n a_i \eta_i\right)(b_j) = \sum_{i=1}^n a_i \underbrace{\eta_i(b_j)}_{=\delta_{ij}} = a_j.
```

Offensichtlich kann die Nullabbildung nur erzeugt werden, wenn für alle Koeffizienten $a_i=0$ gilt für $i=1,\ldots,n$ und damit ist die Aussage bewiesen.

````

Durch obiges Lemma bemerken wir, dass der algebraische Dualraum isomorph zum zu Grund liegenden Vektorraum ist.
````{prf:remark}
Die Aussage aus {prf:ref}`lem:dualeBasis` zeigt insbesondere, dass im **endlich-dimensionalen** Fall $\dim(\V) = \dim(\V^\ast)$.
Die Vektorräume sind also isomorph zueinander.

Die Aussage lässt sich ebenfalls auf den Fall eines **unendlich-dimensionalen** Vektorraums übertragen.
Hierfür erinnern wir daran, dass für einen Vektorraum $V$ stets eine Basis $B^V = \{b_i^v:i\in I\}\subset V$ existiert, wobei $I$ eine (nicht notwendigerweise endliche) Indexmenge ist.
Insbesondere bemerken wir, dass wir hier von einer **Hamelbasis** sprechen, d.h., für jedes Element $v\in V$ gibt es eindeutig bestimmte Koeffizienten $\alpha_i, i\in I$, so dass gilt

```{math}
v = \sum_{i\in I} \alpha_i b_i.
```

Der wichtige Punkt hierbei ist, dass nur **endlich viele** Koeffizienten $\alpha_i$ ungleich null sind und die Summation somit keine eigentlich unendliche Reihe beschreibt, sondern nur eine endliche Summe.
Diese Konzept ist insbesondere verschieden vom Begriff der [Schauderbasis](https://de.wikipedia.org/wiki/Schauderbasis)
````

```{margin} Georg Hamel
[Georg Karl Wilhelm Hamel](https://de.wikipedia.org/wiki/Georg_Hamel) (Geboren 12. September 1877 in Düren; Gestorben 4. Oktober 1954 in Landshut) war ein deutscher Mathematiker.
```

```{margin} Juliusz Schauder
[Juliusz Paweł Schauder](https://de.wikipedia.org/wiki/Juliusz_Schauder) (Geboren 21. September 1899 in Lemberg; Gestorben September 1943) war ein polnischer Mathematiker.
```

Wir wollen uns das Konzept der dualen Basis mit Hilfe des Euklidischen Vektorraums klar machen im Folgenden.
````{prf:example} Duale Basis
Sei $V = \R^n$ der Euklidische Vektorraum ausgestattet mit der Standard Einheitsbasis $B = (e_i)_{i=1,\ldots,n}$.
Dann lässt sich jeder Vektor $x \in V$ eindeutig als Linearkombination der Einheitsvektoren schreiben mit

```{math}
x = \sum_{i=1} \alpha_i^x e_i = \sum_{i=1} x_i e_i.
```

Wir sehen also ein, dass die Koeffizienten $\alpha_i^x$ gerade die Einträge des Vektors $x$ selbst sind.
Da die duale Basis des algebraischen Dualraums $V^\ast$ zur Basis $B$ nach {prf:ref}`lem:dualeBasis` gerade die Koeffizienten $\alpha_i^x$ liefern soll, ist klar, dass die entsprechenden linearen Abbildungen durch eine **Linksmultiplikation mit den transponierten Einheitsvektoren** gegeben sind, d.h., $\eta_j(x) := e_j^T x = \langle e_j, x \rangle$, denn es gilt

```{math}
\eta_j(x) = 
\eta_j \left( \sum_{i=1} \alpha_i^x e_i \right) = 
\langle e_j, \sum_{i=1} x_i e_i\rangle =
\sum_{i=1} x_i \underbrace{\langle e_j, e_i\rangle}_{= \delta_{ij}} =  
x_j = \alpha_j^x, \quad \forall j=1,\ldots,n.
```

````

Wir halten abschließend fest, dass sich der **Bidualraum** $(V^\ast)^\ast$, d.h., der duale Raum des Dualraums $V^\ast$, im endlich-dimensionalen Fall leicht charakterisieren lässt.

````{prf:remark}
:label: rem:doubledual

Für $n \in \N$ sei $\V$ ein $n$-dimensionaler reeller Vektorraum.
Dann gilt, dass die Abbildung 

```{math}
\Psi :\V &\rightarrow \V^{\ast\ast}\\
x &\mapsto \Psi_x \quad \text{ mit } \quad \Psi_x(\varphi) := \varphi(x).
```

ein Isomorphismus ist.

````