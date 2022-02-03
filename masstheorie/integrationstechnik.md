# Integrationstechniken

In diesem Abschnitt beschäftigen wir uns mit Rechenmethoden und Rechenregeln, die es uns erlauben Funktionen mehrerer Variablen bezüglich des Lebesgue-Maßes zu integrieren. Insbesondere lernen wir dadurch Verfahren kennen um Volumina und Flächen zu berechnen. Um diese Regeln formal zu zeigen benötigen wir zunächst etwas Theorie.

## Produktalgebren

Für zwei Messräume $(\Omega_1,\Sigma_1), (\Omega_2,\Sigma_2)$ wollen wir nun einen Produktraum erhalten. Hierbei werden wir auf Konzepte des **Tensorproduktes** zurückgreifen und benutzen deshalb die gleiche Notation. Wir definieren dann die Produkt-$\sigma$-Algebra,

```{math}
\Sigma_1\otimes\Sigma_2 := \sigma\left(\Sigma_1\times\Sigma_2\right),
```

wobei

```{math}
\Sigma_1\times\Sigma_2 = \left\{A_1\times A_2: A_1\in\Sigma_1, A_2\in\Sigma_2\right\}.
```

Wir arbeiten nicht auf Vektorräumen darum konstruieren wir **kein** Tensorprodukt im Sinnen von {numref}`s:Tensoren`, aber die grundlegenden Konzepte sind ähnlich, weshalb es üblich ist, hier diese Notation zu verwenden. Weiterhin erkennen wir, dass mit dieser Konstruktion $\Sigma_1\otimes\Sigma_2 $ eine $\sigma$-Algebra auf $\Omega_1\times\Omega_2$ ist.

```{figure} ../img/schnitte.jpg
---
width: 600px
name: "fig:schnitte"
---

Visualisierung von Mengenschnitten.
```

Für eine Menge $E\subset\Omega_1\times\Omega_2$ betrachtet man in diesem Kontext oft sogenannte **Schnitte**

```{math}
E_x := \{y\in \Omega_2: (x,y)\in E\}\subset\Omega_2\\
E^y := \{x\in \Omega_1: (x,y)\in E\}\subset\Omega_1
```

wofür man folgende Aussage hat.

````{prf:lemma}
:label: lem:secmeasure

Es seien $(\Omega_1,\Sigma_1), (\Omega_2,\Sigma_2)$ Messräume, dann gilt für eine Produktmessbare Menge $E\in \Sigma_1\otimes\Sigma_2$, dass $E_x\in \Sigma_2, E_y\in\Sigma_1$ für alle $x\in\Omega_1,y\in\Omega_2$.
````

````{prf:proof}
Wir betrachten das Teilmengensystem

```{math}
\M = \{E\subset\Omega_1\times\Omega_2:  E_x\in\Sigma_2, E^y\in\Sigma_1,\quad\forall x\in\Omega_1,  y\in\Omega_2\}
```

d.h. alle Mengen, welche die gewünschte Bedingung erfüllen. Wir sehen, dass für $A\in\Sigma1,B\in\Sigma_2$ gilt

```{math}
(A\times B)_x = 
\begin{cases}
B &\text{ falls }x\in A\\
\emptyset &\text{ sonst}
\end{cases}
```

und daher $(A\times B)_x\in\Sigma_2$ für alle $x\in\Omega_1$. Analog zeigt man $(A\times B)^y\in\Sigma_1$ für alle $y\in\Omega_2$ und daher gilt

```{math}
\Sigma_1\times\Sigma_2\subset \M.
```

Weiterhin ist $\M$ eine $\sigma$-Algebra. Es gilt $\emptyset\M$, weiterhin $(E^C)_x = (E_x)^C$und analog $(E^C)^y= (E^y)^C$ und daher
gilt

```{math}
E\in\M\Rightarrow E^C\in\M.
```

Weiterhin gilt für eine Folge von Mengen $E_i\in\M,i\in\N$

```{math}
\left(\bigcup_{i\in\N} E_i\right)_x = \bigcup_{i\in\N} (E_i)_x
```

analog für den anderen Schnitt und daher

```{math}
\bigcup_{i\in\N} E_i\in\M.
```

Somit folgt 

```{math}
\Sigma_1\otimes\Sigma_2=\sigma(\Sigma_1\times\Sigma_2)\subset \sigma(\M) = \M.
```
````

Speziell für $\Omega_1=\R^n, \Omega_1=\R^m$ könnte man sich nun fragen wie sich die Produkt-Algebra für die bekannten Borel und Lebesgue Algebren verhält. Zumindest für die Borel $\sigma$-Algebra haben wir folgende Aussage.

````{prf:lemma}
Für $n,m\in\N$ gilt 

```{math}
\B(\R^n)\otimes \B(\R^m) = \B(\R^{n+m}).
```
````

````{prf:proof}
Offensichtlich gilt für den Mengen-Ring

```{math}
\mathcal{R}(\R^{n+m})=\left\{\bigcup_{i=1}^N Q_i: Q_i\subset\R^{n+m}\text{ ist halboffener Quader} \right\},
```

dass

```{math}
\mathcal{R}(\R^{n+m})\subset \B(\R^n)\otimes \B(\R^m).
```

Weiterhin wissen wir aber auch nach ??, dass $\sigma(\mathcal{R}(\R^{n+m})) = \B(\R^{n+m})$ und somit

```{math}
\B(\R^{n+m})\subset \B(\R^n)\otimes \B(\R^m).
```

Für die andere Richtung sei $A_1\in\B(\R^n) A_2\in\B(\R^m)$, dann gilt 

```{math}
A_1\times A_2 = \left(A_1\times\R^m\right) \cap (\R^n\times A_2) =\pi_1^{-1}(A_1) \cap \pi_2^{-1}(A_2)
```

wobei $\pi_1:\R^{n+m}\to\R^n,\pi_2:\R^{n+m}\to\R^m$ die Projektionen

```{math}
\pi_1(z_1,\ldots,z_{n+m})&= (z_1,\ldots, z_n)\\
\pi_2(z_1,\ldots,z_{n+m})&= (z_{n+1},\ldots, z_{n+m})
```

sind. Da Projektionen stetig sind, sind sie Borel-messbar nach ?? und daher gilt

```{math}
\pi_1^{-1}(A_1)\in B(\R^{n+m})\\
\pi_2^{-1}(A_2)\in B(\R^{n+m}).
```

Daraus folgern wir, dass

```{math}
A_1\times A_2 \in \B(\R^{n+m})
```

und somit

```{math}
\B(\R^n)\otimes \B(\R^m)\subset\B(\R^{n+m}).
```

````

Für die Lebesgue $\sigma$-Algebren gilt diese Identität nicht, allgemein kann man zeigen, dass

```{math}
\mathcal{A}(\R^n)\otimes\mathcal{A}(\R^m)\subset \mathcal{A}(\R^{n+m})
```

allerdings ist die Menge auf der rechten Seite echt größer wie das folgende Beispiel zeigt.

````{prf:example}
:label: ex:prodsig

Wir betrachten die zwei Lebesgue-Algebren für $n=m=1$, dh. $\mathcal{A}(\R)$. Nach {numref}`s:vitali` gibt es Mengen $V\subset\R$ sogenannte Vitali-Mengen s.d. $V\not\in\mathcal{A}(\R)$. Weiterhin erkennen wir, dass für das Lebesgue-Maß auf $\R^2$ folgt, dass

```{math}
\lambda^{2}(V\times\{0\}) = 0
```

dies folgt mit der Argumentation aus Aufgabe??. Daher ist $V\times\{0\}\in \mathcal{A}(\R^2)$ da es eine Nullmenge ist.

Wir erkennen aber, dass sich $V$ als Schnitt dieser Produkt-Menge darstellen lässt, nämlich

```{math}
V = (V\times\{0\})^0
```

wäre nun $(V\times\{0\})^0\in \mathcal{A}(\R)\otimes\mathcal{A}(\R)$ so würde mit {prf:ref}`lem:secmeasure` folgen, dass auch der Schnitt $V\in\mathcal{A}(\R)$ gilt, was ein Widerspruch ist, daher

```{math}
(V\times\{0\})^0 \not\in  \mathcal{A}(\R)\otimes\mathcal{A}(\R).
```

````

Das abstrakte Konzept, welches sich hinter diesem Beispiel verbirgt wir mit dem Begriff Vollständigkeit eines Maßes bezeichnet.

````{prf:definition}
Ein Maßraum $(\Omega,\Sigma,\mu)$, falls für jede $\mu$-Nullmenge $N\in\Sigma, \mu(N)=0$ gilt

```{math}
A\subset N \Rightarrow A\in \Sigma.
```
````

```{prf:remark}
Wir wissen, dass jede Menge die bezüglich des äußeren Maßes $\lambda^\ast$ eine Nullmenge ist auch Lebesgue-messbar ist. Daher ist das Lebesgue-Maß ein vollständiges Maß.
```
````

Weiterhin lässt sich ein beliebiges Maß vervollständigen, indem wir die $\sigma$-Algebra

```{math}
\overline{\Sigma}:=\{A\cup N: A\in\Sigma, N\subset B\in\Sigma\text{ mit }\mu(B)=0\}
```

betrachten zusammen mit dem Maß

```{math}
\overline{\mu}(B)= \overline{\mu}(A\cup N):= \mu(A).
```

Hier lässt sich nun folgendes zeigen.

````{prf:lemma}
:label: lem:completelebesgue

Für $n,m\in\N$ gilt

```{math}
\overline{\mathcal{A}(\R^n)\otimes\mathcal{A}(\R^m)}= \mathcal{A}(\R^{n+m}).
```
````

````{prf:proof}
Siehe z.B. {cite:p}`boga_2007` Theorem 1.5.6.
````

## Produktmaße

Wir wollen nun Maße auf der Produktalgebra betrachten.

````{prf:definition} Produktmaß
Es seien $(\Omega_1,\Sigma_1,\mu_1), (\Omega_2,\Sigma_2,\mu_2)$ zwei Maßräume, dann heißt ein Maß $\mu$ auf dem Messraum $(\Sigma_1\otimes\Sigma_2, \Omega_1\times\Omega_2)$ **Produktmaß**, falls 

```{math}
\mu(A_1\times A_2) = \mu_1(A_1)\cdot\mu_2(A_2)\quad\forall A_1\in\Sigma_1, A_2\in\Sigma_2.
```

````

````{prf:remark}
In {ref}`s:grass` haben wir das Tensorprodukt zweier lineare Abbildungen $T_1,T_2$ definiert über

```{math}
(T_1\otimes T_2)(v_1,V_2) := T_1(v_1)\cdot T_2(v_2).
```

Es sei hier erwähnt, dass das Maß **keine** lineare Abbildung ist, insbesondere haben wir keinen Vektorraum gegeben. Die Produktstruktur ist trotzdem ähnlich, weshalb eine gewisse Analogie zwischen dem Tensorprodukt und dem Produktmaß herrscht.
````

````{prf:remark}
In den obigen Produkten können einzelnen Terme jeweils unendlich werden, hierbei benutzt man die Konvention

```{math}
0 * a = 0\quad\forall a\in\overline{\R}.
```
````

Man kann zeigen, dass ein Produktmaß stets existiert siehe ??. Allerdings ist es nicht notwendigerweise eindeutig bestimmt, hierfür benötigt man die sogennate $\sigma$-Endlichkeit.

````{prf:definition}
Es sei $(\Omega,\Sigma,\mu)$ ein Maßraum, das Maß $\mu$ heißt $\sigma$**-endlich**, falls eine Folge von Mengen $A_i\in\Sigma,i\in\N$ existiert, s.d., $\mu(A_i)<\infty$ und 

```{math}
\bigcup_{i\in\N} A_i = \Omega.
```
````

````{prf:remark}
Das wichtigste Beispiel für uns ist das Lebesgue-Maß auf $\R^d$ welches bezüglich der Borelschen $\sigma$-Algebra zwar nicht endlich aber $\sigma$-endlich ist. Insbesondere ist es damit auch $\sigma$-endlich bezüglich der Lebesgue $\sigma$-Algebra $\mathcal{A}$.
````

Für $\sigma$-endliche Maße kann man zeigen, dass ein eindeutig bestimmtes Produktmaß existiert.

````{prf:theorem}
Es seien $(\Omega_1,\Sigma_1,\mu_1), (\Omega_2,\Sigma_2,\mu_2)$ zwei $\sigma$-endliche Maßräume, dann existiert eine eindeutig bestimmtes Produktmaß

```{math}
\mu_1\otimes \mu_2:\Sigma_1\otimes\Sigma_2\to[0,\infty],
```

s.d. die Bedingung

```{math}
(\mu_1\otimes\mu_2)(A\times B) = \mu_1(A)\cdot\mu_2(B)\quad\forall A\in\Sigma_1, B\in\Sigma_2,
```

erfüllt ist.
````

````{prf:proof}
See Bogachev ref missing.
````

Anhand von {prf:ref}`ex:prodsig` haben wir gesehen, dass die Lebesgue $\sigma$-Algebra auf $\R^{n+m}$ größer ist als die Produkt $\sigma$-Algebra. Allerdings kann man zeigen, dass das Produktmaß zumindest auf der kleineren Produktalgebra übereinstimmt.

````{prf:lemma}
:label: lem:lebesguecomp

Es gilt

```{math}
\lambda^{n+m} = \overline{\lambda^n\otimes\lambda^m},
```

insbesondere folgt damit für eine beliebige Menge $E\in \mathcal{A}(\R^n)\otimes\mathcal{A}(\R^m)$

```{math}
\lambda^{n+m}(E) = (\lambda^n\otimes\lambda^m)(E).
```

````

````{prf:proof}
Siehe z.B. {cite:p}`boga_2007` Theorem 1.5.6.
````

Speziell für $A_1\in\mathcal{A}(\R^n), A_2\in\mathcal{A}(\R^m)$ folgt damit

```{math}
\lambda^{n+m}(A^1\times A^2)=\lambda^{n}(A^1)\cdot\lambda^{m}(A^2).
```

## Das Prinzip von Cavalieri

Im vorherigen Abschnitt haben wir Produkte von Maßen betrachtet. Insbesondere haben wir erkannt, dass wir für Mengen der Form $A\times B$, dass Lebesgue-Maß multiplikativ aufteilen können,

```{math}
\lambda^{n+m}(A\times B) = \lambda^n(A)\,\lambda^m(B).
```

Unser Ziel ist es nun das Lebesgue-Maß beliebige messbare Mengen $E\subset\R^{n+m}$ mithilfe der niedrigdimesnionaleren Lebesgue-Maße auszudrücken. Dies führt auf das sogenannte Prinzip von Cavalieri.

```{margin} Bonaventura Cavalieri
[Bonaventura Francesco Cavalieri](https://de.wikipedia.org/wiki/Bonaventura_Cavalieri) (Geboren 1598 wahrscheinlich in Mailand; Gestorben 3. Dezember oder 30. November 1647 in Bologna; mit Gelehrtennamen Cavalerius) war ein italienischer Jesuat, Mathematiker und Astronom.
```

```{figure} ../img/cavalieri.jpg
---
width: 400px
name: "fig:cavalieri"
---

Visualisierung für das Prinzip von Cavalieri, beide Objekte haben die gleiche Fläche.
```

Das Prinzip beruht auf der Intuition, dass zwei Körper, das gleiche Volumen haben, sofern alle ihre Schnittflächen welche parallel zu einer Grundfläche verlaufen gleich sind. Für $\R^2$ ist dieses Prinzip in {numref}`fig:cavalieri` dargestellt. Formal bedeutet das, dass wir für eine messbare Menge $E$, den Inhalt über das Integral der Schnitte ausdrücken wollen, es gibt hier also drei Größen

```{math}
\lambda^{n+m}(E), \int_{\R^n} \lambda^m(E_x) d\lambda^n(x), \int_{\R^m} \lambda^m(E_y) d\lambda^m(y)
```

welche wir in Beziehung zueinander setzten wollen. Dazu benötigen wir aber zunächst die folgenden Konzepte.



Ein weiteres Konzept was man in diesem Kontext benötigt, sind sogenannte monotone Klassen.

````{prf:definition} Monotone Klasse
Es sei $\Omega$ eine Menge, ein Teilmengensystem $\mathcal{C}\subset 2^\Omega$ heißt **monotone Klasse**, falls

1\. Für eine aufsteigende Folge von Mengen $A_i\in\mathcal{C}, A_i\subset A_{i+1}, i\in\N$ gilt auch 

```{math}
\bigcup_{i\in\N} A_i\in\mathcal{C}.
```

1\. Für eine absteigende Folge von Mengen $A_i\in\mathcal{C}, A_i\supset A_{i+1}, i\in\N$ gilt auch 

```{math}
\bigcap_{i\in\N} A_i\in\mathcal{C}.
```
````

Offensichtlich ist jede $\sigma$-Algebra eine monotone Klasse,die Umkehrung dieser Aussage gilt nicht im Allgemeinen. Betrachtet man aber analog zur kleinsten von $\mathcal{C}$ erzeugten $\sigma$-Algebra die kleinste von $\mathcal{C}$ erzeugt monotone Klasse $\text{M}\big[\mathcal{C}\big]$ so gilt folgendes technisches Lemma.

````{prf:lemma} Monotone Klassen Lemma
:label: lem:monclass

Es sei $\mathcal{C}$ ein Mengen-Ring, dann gilt

```{math}
\sigma(\mathcal{C}) = \text{M}\big[\mathcal{C}\big].
```
````

````{prf:proof}
Siehe z.B. {cite:p}`tao_2011` Lemma 1.7.14.
````

Für zwei $\sigma$-Algebren ist das kartesische Produkt $\Sigma_1\times\Sigma_2$ i.A. kein Mengen-Ring, die Menge

```{math}
\Sigma_1\diamond\Sigma_2:= \left\{\bigcup_{i=1}^N A^1_i\times A^2_i: A^1_i\in\Sigma_1, A^2_i\in\Sigma_2\quad i=1,\ldots,n\right\}
```

allerdings schon und sie erzeugt offensichtlich auch die Produkt-$\sigma$-Algebra,

```{math}
\sigma(\Sigma_1\diamond\Sigma_2) = \Sigma_1\otimes\Sigma_2.
```

Auf $\Sigma_1\diamond\Sigma_2$ können wir dann auch das monotone Klasse Lemma anwenden, womit wir nun das Prinzip von Cavalieri beweisen.

````{prf:theorem} Das Prinzip von Cavalieri
:label: thm:cavalieri

Sei $E \in \mathcal{A}(\R^n)\otimes\mathcal{A}(\R^m)$ mit $\lambda^{n}\otimes\lambda^{m}(E) < \infty$,
dann gilt für fast alle $x\in\R^n,y\in\R^m$, dass die Schnitte $E_x, E^y$ auch Lebesgue-messbar sind, die Funktionen

```{math}
x \mapsto \lambda^m(E_x)\\
y \mapsto \lambda^n(E^y)
```

sind messbar und es gilt

```{math}
\lambda^{n}\otimes\lambda^{m}(E) &= \int_{\R^n} \lambda^m(E_x) d\lambda^n(x)\\
&=
\int_{\R^m} \lambda^n(E^y) d\lambda^m(y).
```

````

````{prf:proof}
Es sei $\mathcal{C}\subset\mathcal{A}(\R^n)\otimes\mathcal{A}(\R^m)$ das System aller Mengen s.d. die Aussage gilt. Dann ist $\mathcal{C}$ eine monotone Klasse und

```{math}
\mathcal{A}(\R^n)\diamond\mathcal{A}(\R^m)\subset \mathcal{C}.
```

Mit dem monotone Klassen Lemma ({prf:ref}`lem:monclass`) folgt dann

```{math}
\mathcal{A}(\R^n)\otimes\mathcal{A}(\R^m) = \sigma(\mathcal{A}(\R^n)\diamond\mathcal{A}(\R^m)) = 
\text{M}\big[\mathcal{A}(\R^n)\diamond\mathcal{A}(\R^m)\big] \subset 
\text{M}\big[\mathcal{C}\big] = \mathcal{C}.
```

````

Ein Korollar aus der obigen Aussage ist, dass fast alle Schnitte einer $\lambda^n\otimes\lambda^m$ Nullmenge selbst Nullmengen bezüglich $\lambda^n$, bzw. $\lambda^m$ sind.

````{prf:corollary}
Es sei $E\in\mathcal{A}(\R^n)\otimes\mathcal{A}(\R^m)$ eine Nullmenge, dann folgt, dass für fast alle $x\in\R^n,y\in\R^m$ auch $\lambda^m(E_x)=0=\lambda^n(E^y)$ gilt.
````

````{prf:proof}
Für die Funktion $f:x\mapsto \lambda^m(E_x)$ gilt mit dem Prinzip von Cavalieri, dass 

```{math}
0 = \lambda^{n}\otimes\lambda^{m}(E) = \int_{\R^n} f(x)d\lambda^n(x)
```

und daher mit ??, dass 

```{math}
f(x)=\lambda^m(E_x)=0
```

für fast alle $x\in\R^n$. Die Aussage für $\lambda^n(E^y)$ folgt analog.

````

Diese Korollar erlaubt es uns die Aussage von Cavalieri auf alle Mengen $E\in \mathcal{A}(\R^{n+m})$ zu verallgemeinern.

````{prf:lemma}
Die Aussagen von {prf:ref}`thm:cavalieri` gelten auch für Mengen $E\in \mathcal{A}(\R^{n+m})$.
````

````{prf:proof}
Es sei $E\in \mathcal{A}(\R^{n+m})$, nach {prf:ref}`lem:completelebesgue` existieren Mengen $\tilde{E}\in\mathcal{A}(\R^n)\otimes\mathcal{A}(\R^m)$, $N\subset \tilde{N}$, s.d.

```{math}
E = \tilde{E}\cup N\\
(\lambda^n\otimes\lambda^m)(\tilde{N}) = 0.
```

Insbesondere ist dann

```{math}
E\setminus \tilde{N} = \left(\tilde{E}\setminus \tilde{N} \right)\cup \underbrace{\left(N\setminus \tilde{N}\right)}_{=\emptyset} = 
\tilde{E}\setminus \tilde{N}\in \in\mathcal{A}(\R^n)\otimes\mathcal{A}(\R^m)
```

daher können wir {prf:ref}`thm:cavalieri` auf $E\setminus \tilde{N}$ anwenden. Da aber fast alle Schnitte $\tilde{N}_x,\tilde{N}^y$ Nullmengen sind, gilt die Aussage, dann für fast alle $x,y\in E$.
````

Mit dieser Aussage können wir nun ein Beispiel betrachten, in welchem wir die Fläche eines Kreises berechnen.

```{figure} ../img/ball.jpg
---
width: 600px
name: "fig:ball"
---

Visualisierung für {prf:ref}`ex:ball`.
```

````{prf:example}
:label: ex:ball

Wir betrachten den $2$-dimensionale Ball

```{math}
B_r^2:=\{x\in\R^2: |x|\leq r\},
```

wir erkennen, dass sich ein Schnitt für $\abs{y}\leq r$ jeweils ergibt durch

```{math}
(B_r^2)_y = \{x:(x,y)\in B_r^2\} = \{x\leq\sqrt{r^2-y^2}\} = [-\sqrt{r^2-y^2},\sqrt{r^2-y^2}]
```

und ansonsten leer ist.

Somit erhalten wir 

```{math}
\lambda^1((B_r^2)_y) = 
\begin{cases}
2 \sqrt{r^2-y^2}&\text{ falls }y\leq r\\
\emptyset\text{ sonst}
\end{cases}.
```

Damit erhalten wir mithilfe des Prinzips von Cavalieri

```{math}
\lambda^2(B_r^2) &= \int_{\R} \lambda^1((B_r^2)_y) d\lambda^1(y) = 
\int_{[-r,r]} 2 \sqrt{r^2-y^2} d\lambda^1(y)\\
&= 
2\int_{-r}^r \sqrt{r^2 - y^2} dy = 
\lim_{t\to r}\left[y \sqrt{r^2-y^2} +r^2\arctan\left(\frac{y}{\sqrt{r^2-y^2}}\right)\right]^t_{-t}\\
&=
r^2\pi.
```
````

Das Volumen einer Kugel in $n$-Dimensionen lässt sich mithilfe des folgenden Lemmas berechnen.

````{prf:lemma}
Für die $n$-dimensionale Kugel

```{math}
B_r^n:=\{x\in\R^n: |x|\leq r\}
```

gilt

```{math}
\lambda^n(B_r^n) =
r^d\,
\begin{cases}
\frac{1}{(n/2)!} \pi^{n/2}&\text{ falls }n gerade\\
\frac{2}{1\cdot 3\cdot\ldots n} \pi^{(n-1)/2}&\text{ falls }n gerade\\
\end{cases}
```
````

````{prf:proof}
Siehe Hausaufgabe.
````

## Der Satz von Fubini




Dazu zeigen wir ein allgemeineres Resultat für messbare Funktionen.

````{prf:lemma}
Es sei $f:\R^{m+n}\to\overline{\R}$ messbar bezüglich $\mathcal{A}(\R^n)\otimes\mathcal{A}(\R^m)$, dann gilt für die Funktionen

```{math}
f_x:x \mapsto f(x,y),\\
f_y:y \mapsto f(x,y),
```

dass $f_x$ messbar bezüglich $\mathcal{A}(\R^m)$ und $f_y$ messbar bezüglich $\mathcal{A}(\R^n)$ ist.

````

````{prf:proof}
Siehe Hausaufgabe.
````





Der Satz von Fubini erlaubt es die Berechnung mehrdimensionaler Integrale auf die Berechnung niederdimensionaler Integrale zurück zu führen. Unser Ziel ist es also für eine Funktion $f:\R^{n+m}\to\overline{R}$ das Integral

```{math}
\int_{\R^{n+m}} f(z) d\lambda^{n+m}(z)
```

mithilfe von Inetgration bezüglich $d\lambda^n$ und $\lambda^m$ aufzuteilen. Hierfür definieren analog zu den Mengenschnitten aus {prf:ref}`lem:secmeasure` für alle $x\in\R^n$ die Funktion

```{math}
f_x:\R^m&\to\overline{R}\\
y&\mapsto f(x,y)
```

und für alle $y\in\R^m$ die Funktion

```{math}
f^y:\R^n&\to\overline{R}\\
x&\mapsto f(x,y).
```

Wäre $f_x$ für fast alle $x\in\R^n$ integrierbar bezüglich $\lambda^m$, so kann man das Integral

```{math}
I_x(f) := \int_{\R^m} f_x(y) d\lambda^m(y)
```

betrachten. Da $x\in\R^n$ bei dieser Überlegung variabel ist, definiert dies eine neue Funktion $x\mapsto I_x(f)$, welche im Falle erneuter Integrierbarkeit auf

```{math}
\int_{\R^n} I_x(f) d\lambda^n(x) = \int_{\R^n}\int_{\R^m} f(x,y) d\lambda^m(y)d\lambda^n(x).
```

Gleichermaßen sollen diese Schritte aber auch für $f^y$ funktionieren, deshalb definieren wir doppelintegrierbare Funktionen.

````{prf:definition} Doppelintegrierbare Funktion

Eine Funktion $f \colon \R^{n+m} \to \overline{\R}$ heißt **doppelintegrierbar** falls 
für fast alle Punkte $x \in \R^n, y\in\R^m$ die Funktionen $f_x,f^y$ integrierbar sind und zusätzlich die Funktionen

```{math}
x\mapsto I_x(f) =\int_{\R^m} f(x,y) d\lambda^m(y)\\
y\mapsto I^y(f) =\int_{\R^n} f(x,y) d\lambda^n(x)\\
```

integrierbar sind.
````

Für die Menge der doppelintegrierbaren Funktionen

```{math}
V_{\text{D}} := \{f:\R^{n+m}\to\overline{\R}: f\text{ ist doppelintegrierbar}\}
```

können wir folgende Aussage zeigen.

````{prf:lemma}
:label: lem:doppelintegrierbar

1\. Die Menge der doppelintegrierbaren Funktionen bilden einen Vektorraum $V_D$.

2\. Doppelintegrale sind *linear*, d.h., für zwei doppelintegrierbare Funktionen $f,g \in V_D$ und beliebige Skalare $\lambda \in \R$ gilt

```{math}
\int_{\R^n}\int_{\R^m} (f + \lambda g)\,d\lambda^m d\lambda^n = 
\int_{\R^n}\int_{\R^m} f d\lambda^m d\lambda^n + 
\lambda\,\int_{\R^n}\int_{\R^m} g d\lambda^m d\lambda^n
```

und analog für das andere Doppelintegral


```{math}
\int_{\R^m}\int_{\R^n} (f + \lambda g) d\lambda^n d\lambda^m = 
\int_{\R^n}\int_{\R^m} f d\lambda^n d\lambda^m + 
\lambda\,\int_{\R^n}\int_{\R^m} g d\lambda^n d\lambda^m
```

3\. Sei $(f_j)_j\in\N$ eine Folge von nichtnegativen, doppelintegrierbaren Funktionen und sei $f:\R^{n+m}\to\overline{\R}$ eine Funktion, s.d.,

```{math}
f_j\leq f\quad\forall j\in\N,\qquad \lim_{j\to\infty} f_j =f.
```

Falls beide Doppelintegrale für die $f_j$ gleichmäßig beschränkt sind, so gilt $f\in V_{\text{D}}$ und 

```{math}
\lim_{j\to\infty} \int_{\R^n}\int_{\R^m} f_j\,d\lambda^m d\lambda^n = \int_{\R^n}\int_{\R^m} f\,d\lambda^m d\lambda^n\\ 
\lim_{j\to\infty} \int_{\R^m}\int_{\R^n} f_j\,d\lambda^n d\lambda^m= \int_{\R^m}\int_{\R^n} f\,d\lambda^n d\lambda^m.
```

````

````{prf:proof}
Schulz-Baldes S.153f.
````

````{prf:remark}
Die Aussage aus {prf:ref}`lem:doppelintegrierbar` gilt analog für nichtnegative Funktionenfolgen $(f_j)_{j\in\N}$, die von oben gegen die Funktion $f$ konvergieren. 
````

Der Wunsch ist natürlich zeigen zu können, dass beide Doppelintegrale übereinstimmen und insbesondere, dass

```{math}
\int_{\R^{n+m}} f\,d\lambda^{n+m}
```

gleich dem Doppelintegral ist.

````{prf:proof}
Es sei $E\in \mathcal{A}(\R^{n+m})$, nach {prf:ref}`lem:completelebesgue` existieren Mengen $\tilde{E}\in\mathcal{A}(\R^n)\otimes\mathcal{A}(\R^m)$, $N\subset \tilde{N}$, s.d.

```{math}
E = \tilde{E}\cup N\\
(\lambda^n\otimes\lambda^m)(\tilde{N}) = 0.
```

Insbesondere ist dann

```{math}
E\setminus \tilde{N} = \left(\tilde{E}\setminus \tilde{N} \right)\cup \underbrace{\left(N\setminus \tilde{N}\right)}_{=\emptyset} = 
\tilde{E}\setminus \tilde{N}\in \in\mathcal{A}(\R^n)\otimes\mathcal{A}(\R^m)
```

daher können wir {prf:ref}`thm:cavalieri` auf $E\setminus \tilde{N}$ anwenden. Da aber fast alle Schnitte $\tilde{N}_x,\tilde{N}^y$ Nullmengen sind, gilt die Aussage, dann für fast alle $x,y\in E$.
````

Mit dieser Aussage können wir nun ein Beispiel betrachten, in welchem wir die Fläche eines Kreises berechnen.

```{figure} ../img/ball.jpg
---
width: 600px
name: "fig:ball"
---

Visualisierung für {prf:ref}`ex:ball`.
```

````{prf:example}
:label: ex:ball

Wir betrachten den $2$-dimensionale Ball

```{math}
B_r^2:=\{x\in\R^2: |x|\leq r\},
```

wir erkennen, dass sich ein Schnitt für $\abs{y}\leq r$ jeweils ergibt durch

```{math}
(B_r^2)_y = \{x:(x,y)\in B_r^2\} = \{x\leq\sqrt{r^2-y^2}\} = [-\sqrt{r^2-y^2},\sqrt{r^2-y^2}]
```

und ansonsten leer ist.

Somit erhalten wir 

```{math}
\lambda^1((B_r^2)_y) = 
\begin{cases}
2 \sqrt{r^2-y^2}&\text{ falls }y\leq r\\
\emptyset\text{ sonst}
\end{cases}.
```

Damit erhalten wir mithilfe des Prinzips von Cavalieri

```{math}
\lambda^2(B_r^2) &= \int_{\R} \lambda^1((B_r^2)_y) d\lambda^1(y) = 
\int_{[-r,r]} 2 \sqrt{r^2-y^2} d\lambda^1(y)\\
&= 
2\int_{-r}^r \sqrt{r^2 - y^2} dy = 
\lim_{t\to r}\left[y \sqrt{r^2-y^2} +r^2\arctan\left(\frac{y}{\sqrt{r^2-y^2}}\right)\right]^t_{-t}\\
&=
r^2\pi.
```
````

Das Volumen einer Kugel in $n$-Dimensionen lässt sich mithilfe des folgenden Lemmas berechnen.

````{prf:lemma}
Für die $n$-dimensionale Kugel

```{math}
B_r^n:=\{x\in\R^n: |x|\leq r\}
```

gilt

```{math}
\lambda^n(B_r^n) =
r^d\,
\begin{cases}
\frac{1}{(n/2)!} \pi^{n/2}&\text{ falls }n gerade\\
\frac{2}{1\cdot 3\cdot\ldots n} \pi^{(n-1)/2}&\text{ falls }n gerade\\
\end{cases}
```
````

````{prf:proof}
Siehe Hausaufgabe.
````

## Der Satz von Fubini




Dazu zeigen wir ein allgemeineres Resultat für messbare Funktionen.

````{prf:lemma}
Es sei $f:\R^{m+n}\to\overline{\R}$ messbar bezüglich $\mathcal{A}(\R^n)\otimes\mathcal{A}(\R^m)$, dann gilt für die Funktionen

```{math}
f_x:x \mapsto f(x,y),\\
f_y:y \mapsto f(x,y),
```

dass $f_x$ messbar bezüglich $\mathcal{A}(\R^m)$ und $f_y$ messbar bezüglich $\mathcal{A}(\R^n)$ ist.

````

````{prf:proof}
Siehe Hausaufgabe.
````





Der Satz von Fubini erlaubt es die Berechnung mehrdimensionaler Integrale auf die Berechnung niederdimensionaler Integrale zurück zu führen. Unser Ziel ist es also für eine Funktion $f:\R^{n+m}\to\overline{R}$ das Integral

```{math}
\int_{\R^{n+m}} f(z) d\lambda^{n+m}(z)
```

mithilfe von Inetgration bezüglich $d\lambda^n$ und $\lambda^m$ aufzuteilen. Hierfür definieren analog zu den Mengenschnitten aus {prf:ref}`lem:secmeasure` für alle $x\in\R^n$ die Funktion

```{math}
f_x:\R^m&\to\overline{R}\\
y&\mapsto f(x,y)
```

und für alle $y\in\R^m$ die Funktion

```{math}
f^y:\R^n&\to\overline{R}\\
x&\mapsto f(x,y).
```

Wäre $f_x$ für fast alle $x\in\R^n$ integrierbar bezüglich $\lambda^m$, so kann man das Integral

```{math}
I_x(f) := \int_{\R^m} f_x(y) d\lambda^m(y)
```

betrachten. Da $x\in\R^n$ bei dieser Überlegung variabel ist, definiert dies eine neue Funktion $x\mapsto I_x(f)$, welche im Falle erneuter Integrierbarkeit auf

```{math}
\int_{\R^n} I_x(f) d\lambda^n(x) = \int_{\R^n}\int_{\R^m} f(x,y) d\lambda^m(y)d\lambda^n(x).
```

Gleichermaßen sollen diese Schritte aber auch für $f^y$ funktionieren, deshalb definieren wir doppelintegrierbare Funktionen.

````{prf:definition} Doppelintegrierbare Funktion

Eine Funktion $f \colon \R^{n+m} \to \overline{\R}$ heißt **doppelintegrierbar** falls 
für fast alle Punkte $x \in \R^n, y\in\R^m$ die Funktionen $f_x,f^y$ integrierbar sind und zusätzlich die Funktionen

```{math}
x\mapsto I_x(f) =\int_{\R^m} f(x,y) d\lambda^m(y)\\
y\mapsto I^y(f) =\int_{\R^n} f(x,y) d\lambda^n(x)\\
```

integrierbar sind.
````

Für die Menge der doppelintegrierbaren Funktionen

```{math}
V_{\text{D}} := \{f:\R^{n+m}\to\overline{\R}: f\text{ ist doppelintegrierbar}\}
```

können wir folgende Aussage zeigen.

````{prf:lemma}
:label: lem:doppelintegrierbar

1\. Die Menge der doppelintegrierbaren Funktionen bilden einen Vektorraum $V_D$.

2\. Doppelintegrale sind *linear*, d.h., für zwei doppelintegrierbare Funktionen $f,g \in V_D$ und beliebige Skalare $\lambda \in \R$ gilt

```{math}
\int_{\R^n}\int_{\R^m} (f + \lambda g)\,d\lambda^m d\lambda^n = 
\int_{\R^n}\int_{\R^m} f d\lambda^m d\lambda^n + 
\lambda\,\int_{\R^n}\int_{\R^m} g d\lambda^m d\lambda^n
```

und analog für das andere Doppelintegral


```{math}
\int_{\R^m}\int_{\R^n} (f + \lambda g) d\lambda^n d\lambda^m = 
\int_{\R^n}\int_{\R^m} f d\lambda^n d\lambda^m + 
\lambda\,\int_{\R^n}\int_{\R^m} g d\lambda^n d\lambda^m
```

3\. Sei $(f_j)_j\in\N$ eine Folge von nichtnegativen, doppelintegrierbaren Funktionen und sei $f:\R^{n+m}\to\overline{\R}$ eine Funktion, s.d.,

```{math}
f_j\leq f\quad\forall j\in\N,\qquad \lim_{j\to\infty} f_j =f.
```

Falls beide Doppelintegrale für die $f_j$ gleichmäßig beschränkt sind, so gilt $f\in V_{\text{D}}$ und 

```{math}
\lim_{j\to\infty} \int_{\R^n}\int_{\R^m} f_j\,d\lambda^m d\lambda^n = \int_{\R^n}\int_{\R^m} f\,d\lambda^m d\lambda^n\\ 
\lim_{j\to\infty} \int_{\R^m}\int_{\R^n} f_j\,d\lambda^n d\lambda^m= \int_{\R^m}\int_{\R^n} f\,d\lambda^n d\lambda^m.
```

````

````{prf:proof}
Schulz-Baldes S.153f.
````

````{prf:remark}
Die Aussage aus {prf:ref}`lem:doppelintegrierbar` gilt analog für nichtnegative Funktionenfolgen $(f_j)_{j\in\N}$, die von oben gegen die Funktion $f$ konvergieren. 
````

Der Wunsch ist natürlich zeigen zu können, dass beide Doppelintegrale übereinstimmen und insbesondere, dass

```{math}
\int_{\R^{n+m}} f\,d\lambda^{n+m}
```

gleich dem Doppelintegral ist.

````{prf:proof}
Schulz-Baldes S.156-160
````

````{prf:remark}
Das Prinzip von Cavalieri besagt, dass jede charakteristische Funktion $\chi_A$ einer messbaren Menge $A$ doppelintegrierbar ist und es gilt

```{math}
\mu_{n+k}(\chi_A) = \mu_n(\mu_k(\chi_A)) = \mu_k(\mu_n(\chi_A)). 
```

````

````{prf:theorem} Satz von Fubini-Tonelli
Sei $f \colon \R^{n} \times \R^k \rightarrow \overline{\R}$ eine Lebesgue-integrierbare Funktion.
Dann ist $f$ doppelintegrierbar und es gilt

```{math}
\mu_{n+k}(f) = \mu_n(\mu_k(f)) = \mu_k(\mu_n(f)). 
```

````

````{prf:proof}
S.164
````

````{prf:example}
Aus Doppelintegrierbarkeit einer Funktion folgt nicht notwendigerweise deren Lebesgue-Integrierbarkeit.

(Website)[https://www.geometrie-und-logik.de/studium/analysis-la-ws-2020/saetze-ueber-lebesgueintegrierbare-funktionen/]

````

Die Aussage gilt jedoch unter einer zusätzlichen Voraussetzung.

````{prf:theorem}
Sei $f \colon \R^{n} \times \R^k \rightarrow \overline{\R}$ eine doppelintegrierbare Funktion, die *nichtnegativ* ist, d.h., es gilt $f \geq 0$.
Dann ist $f$ Lebesgue-integrierbar.
````

````{prf:proof}
Schulz-Baldes S.166
````

## Die Jacobische Transformationsformel

Abschließend wollen wir noch ein wichtiges Theorem formulieren, dass für die mehrdimensionale Integration sehr nützlich ist.

````{prf:theorem} Jacobische Transformationsformel
:label: thm:jacobitransformation
Seien $U, V \subset \R^n$ offene Teilmengen und die Abbildung

```{math}
\Phi \colon U \rightarrow V := \Phi(U)
```

sei ein $C^1$-Diffeomorphismus, d.h., dass die Abbildung $\Phi$ invertierbar ist, und dass sowohl $\Phi$ als auch die Umkehrabbildung $\Phi^{-1}$ stetig differenzierbar sind.
Sei außerdem $f \colon V \rightarrow \R$ eine Lebesgue-integrierbare Funktion.

Dann gilt, dass die Verknüpfung $f \circ \Phi \colon U \rightarrow \R$ auch Lebesgue-integrierbar ist und es gilt die folgende Integrationsregel

```{math}
\int_{\Phi(U)} f(y) \mu(\mathrm{d}y) = \int_U (f \circ \Phi)(x) \cdot |\det(D\Phi(x))|\mu(\mathrm{d}x). 
```

Hierbei nennt man $\det(D\Phi(x))$ die **Jacobi-Determinante**.

````

````{prf:proof}
Schulz-Baldes S.168-174
````