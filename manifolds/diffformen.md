# Differentialformen auf Mannigfaltigkeiten

Die vorhergehenden Abschnitte liefern nun die nötigen Grundlagen um **Differentialformen** zu betrachten. Insbesondere werden wir diese über eine Unterstruktur der bekannten Tensorfelder erhalten. Dieser Schritt isr konzeptionell sehr ähnlich zum Schritt von allgemeinen Tensoren zu den Antisymmetrischen, bzw. alternierenden Tensoren. Dieser Zusammenhang erklärt auch die Begrifflichkeit alternierende Differentialform welche in de Literatur häufig vorkommt.

Differentialformen sind ein wichtiges Konzept in verschieden Bereichen der Mathematik und Physik. Auch wenn wir diese Thematik hier nicht betrachten, sei erwähnt, dass Differentialformen die Integration auf speziellen glatten Mannigfaltigkeiten erlauben.

(s:difformen)=
## Differentialformen

In Kapitel ?? haben wir symmetrische und antisymmetrische Tensoren kennengelernt. Dieses Konzept werden wir nun auf Tensorfelder übetragen um somit Differntialformen zu erhalten. Hierfür betrachten wir für eine glatte Mannigfaltigkeit die Menge

```{math}
\Lambda^k T^\ast\M := \bigsqcup_{p\in\M} \Lambda^k (T^\ast_p\M)
```

der alternierenden Tensorfelder. Antisymmetrische Tensoren bilden direkt eine Teilmenge aller Tensoren und es bleibt lediglich zu zeigen, dass die Vektorraumstruktur erhalten bleibt. Die Situation hier ist nun anders, man benötigt den abstrakten Begriff des **Untervektorbündels**.

````{prf:definition}
Es seien $\pi_E:E\to B$ und $\pi_D:D\to B$ zwei Vektorbündel, wobei für jedes $p\in\M$ die Untervektorraumrelation 

```{math}
\pi_D^{-1}(p) = D_p\subset E_p = \pi_E^{-1}(p)
```

gelte, dann heißt $D$ Untervektorbündel von $E$.
````

```{figure} ../img/subbundle.png
---
height: 300px
name: "fig:subbundle"
---
Visualisierung eines Untervektorbündels, siehe {cite:p}`lee2003` Kapitel 10.
```

In diesem Fall erhält man also ein Untervektorbündel.

````{prf:lemma}
Sei $\M$ eine glatte $n$-dimensionale Mannigfaltigkeit, dann ist $\Lambda^k T^\ast\M$ ein glattes Untervektorbündel vom Rang $\begin{pmatrix} n k \end{pmatrix}$.
````

````{prf:proof}
ToDo.
````

Dank der Bündelstruktur können wir erneut glatte Schnitte betrachten, welche nun auf das Konzept der Differentialform führen.

````{prf:definition}
Es sei $\M$ eine glatte Mannigfaltigkeit, dann nennt man einen glatten Schnitt

```{math}
\omega\in \Gamma(\Lambda^k T^\ast\M)
```

eine $k$-Differentialform oder auch $k$-Form. Den Vektorraum der Differentialformen notieren wir durch 

```{math}
\Omega^k(\M) := \Gamma(\Lambda^k T^\ast\M).
```
````

## Das äußere Produkt

In {numref}`s:symtensoren` haben wir das äußere Produkt $\wedge$ kennengelernt, welches wir nun auf Differentialformen übertragen. Dazu seien $\omega\in \Omega^k(\M), \eta\in \Omega^l(\M)$ zwei Differentialformen für $k,l\in\N$, dann setzten wir

```{math}
\omega \wedge \eta:\M &\to \Lambda^{k+l}T^\ast\M\\
p&\mapsto \omega_p \wedge \eta_p
```

was in der Tat eine Differentialform definiert, also $\omega\wedge\eta \in \Omega^{k+l}(\M)$. Zusätzlich überträgt sich auch die Darstellung in einer lokalen Karte von {prf:ref}`cor:tensorfieldchart` auf diese Situation, wobei das Tensorprodukt, durch das äußere Produkt ersetzt werden kann.

````{prf:lemma}
Es sei $\M$ eine glatte Mannigfaltigkeit, $(\varphi,U)$ eine Karte und $\omega\in\Omega^l(\M)$ eine Differentialform, dann gilt lokal in $U$ 

```{math}
\omega = \sum_{1\leq i_1,\ldots,i_k \leq n}\omega_{i_1\ldots i_k}
dx_{i_1}\wedge\ldots\wedge dx_{i_k},
```

wobei $\omega_{i_1\ldots i_k}\in C^\infty(\M)$ für alle $i_1,\ldots,i_k\in\{1,\ldots,n\}$ gilts

````

````{prf:proof}
Siehe z.B. {cite:p}`lee2003` Kapitel 14.
````

````{prf:example}


1\. Für $k=0$ und $\M$ eine glatte Mannigfaltigkeit erhalten wir 

```{math}
\Omega^0(\M) = C^\infty(\M).
```

<br/>

2\. Für $k=1$ und $\M$ eine glatte Mannigfaltigkeit erhalten wir 

```{math}
\Omega^1(\M)
```

gerade die Kovektorfelder aus {numref}`s:kotangbundel`.

<br/>

3\. Für $k=3$ und $\M=\R^3$ ist z.B., 

```{math}
\omega(xy) := \sin(xy) dx\wedge dy
```

eine Differentialform.

````

## Die äußere Ableitung

Wir wenden uns nun einer wichtigen Operation auf Differentialformen zu, der äußeren Ableitung. Aus {prf:ref}`ex:totdiff` kennen wir schon das totale Differential $df\in \Omega^1(\M)$, für eine glatte Funktion $f\in C^\infty(\M)$. Hierbei haben wir für ein glattes Vektorfeld $X\in \Gamma(T\M)$ die Abbildung

```{math}
df(X) := X(f)
```

definiert, wobei die rechte Seite über die Wirkung des Vektorfelds definiert ist. Wir können dieses Konzept verallgemeinern, indem wir die äußere Ableitung definieren.

````{prf:definition}
Es sei $\M$ eine glatte Mannigfaltigkeit und $f\in C^\infty(\M)$, dann definieren wir die lineare Abbildung 

```{math}
d:\Omega^k(\M)\to \Omega^{k+1}(\M)\\
d(f\, dx^{i_1}\wedge\ldots\wedge dx^{i_k}):= df \wedge dx^{i_1}\wedge\ldots\wedge dx^{i_k}.
```
````

````{prf:remark}
Beachte, dass die obige Abbildung nur jeweils für lokale Koordinaten definiert ist. Wegen der Kartenunabängigkeit führt dies aber auf eine eindeutig definierte Funktion, siehe z.B. {cite:p}`lee2003` Kapitel 14. Da wir $d$ auf den Elementen $dx^{i_1}\wedge\ldots\wedge dx^{i_k}$ definiert haben erhalten wir jeweils lokal eine eindeutige lineare Fortsetzung, da jedes $\omega\in \Omega^k(\M)$ lokal die Darstellung 

```{math}
\omega = \sum_{1\leq i_1,\ldots,i_k \leq n}\omega_{i_1\ldots i_k}
dx_{i_1}\wedge\ldots\wedge dx_{i_k}
```

hat und somit 

```{math}
d\omega &= \sum_{1\leq i_1,\ldots,i_k \leq n} d(\omega_{i_1\ldots i_k}
dx_{i_1}\wedge\ldots\wedge dx_{i_k})\\ 
&= \sum_{1\leq i_1,\ldots,i_k \leq n} d(\omega_{i_1\ldots i_k})\wedge
dx_{i_1}\wedge\ldots\wedge dx_{i_k}
```
````

````{prf:example} Äußere Ableitung
:label: ex:10.14

1\. Für $\omega\in\Omega^0(\R^3)$ ist $d\omega = \frac{\partial\omega}{\partial x_1}dx_1+
\frac{\partial\omega}{\partial x_2}dx_2+\frac{\partial\omega}{\partial x_3}dx_3$.

<br/>

2\. Für $\omega = \omega_1dx_1+\omega_2dx_2+\omega_3dx_3\in\Omega^1(\R^3)$ ist

```{math}
d\omega &=& (d\omega_1)\wedge dx_1+(d\omega_2)\wedge dx_2+(d\omega_3)\wedge
dx_3\\
&=& \left(\frac{\partial\omega_2}{\partial x_1}-\frac{\partial\omega_1}{\partial x_2}\right)
dx_1\wedge dx_2+ \left(\frac{\partial\omega_3}{\partial x_2}-\frac{\partial\omega_2}{\partial x_3}\right)
dx_2\wedge dx_3\\
&& + \left(\frac{\partial\omega_1}{\partial x_3}-\frac{\partial\omega_3}{\partial x_1}\right)
dx_3\wedge dx_1.
```

<br/>

3\. Für $\omega = \omega_{12}dx_1\wedge dx_2+\omega_{23}dx_2\wedge dx_3
+\omega_{31}dx_3\wedge dx_1 \in\Omega^2(\R^3)$ ist
```{math}
d\omega = \left(\frac{\partial\omega_{12}}{\partial x_3} + \frac{\partial\omega_{23}}{\partial x_1}
+ \frac{\partial\omega_{31}}{\partial x_2}\right)dx_1\wedge dx_2\wedge dx_3.
```

<br/>

4\. Für $\omega\in\Omega^3(\R^3)$ ist $d\omega=0$.
````

Für die äußere Ableitung können wir zusätzlich folgende Eigenschaften zeigen.

````{prf:lemma}
:label: lem:outeprop

Es sei $\M$ eine glatte Mannigfaltigkeit, dann haben wir folgende Eigenschaften.

<br/>

1\. Für $f,g\in C^\infty(\M)$ gilt 

```{math}
d(fg) = d(f)\,g + f\, d(g).
```

<br/>

2\. Für $\omega\in\Omega^k(\M),\eta\in\Omega^l(\M)$ gilt 

```{math}
d(\omega\wedge\eta) = (d\omega)\wedge \eta + (-1)^k \omega\wedge (d\eta).
```

<br/>

3\. Es gilt $d\circ d = 0$.
````

````{prf:remark}
Da $d$ Eigenschaft 2 erfüllt, nennt man $d$ auch Antiderivation.
````

Eine interessante Anwendung finden Differntialformen im sog. Poincaré-Lemma. Hierfür benötigen wir folgenden Begriffe

````{prf:definition}
:label: def:geschlossenexakt

Es sei $\M$ eine glatte Mannigfaltigkeit, eine Differentialform $v\in\Omega^k(\M)$ heißt
* **geschlossen**, wenn $dv=0$, 
* **exakt**, wenn $v=d\eta$ für ein $\eta\in\Omega^{k-1}(\M)$ gilt.
````

Nach Satz {prf:ref}`lem:outer:prop` sind exakte Differentialformen geschlossen, da für $v=d\eta$ gilt,

```{math}
dv = d(d\eta) = (d\circ d)\eta = 0.
```

Das Poincaré-Lemma besagt nun, dass auf sternförmigen offenen Mengen $U\subseteq \R^n$ auch die Umkehrung gilt.

````{prf:lemma} Poincaré-Lemma
Es sei $U\subset\R^n$ eine offene sternförmige Menge, dann gilt für $\omega\in \Omega^k(\M)$, 

```{math}
\omega\text{ ist geschlossen}\Leftrightarrow \omega\text{ ist exakt.}
```

````

````{prf:proof}
Siehe z.B. {cite:p}`lee2003` Theorem 11.49.
````

## Der Pullback

Die letzte Operation die wir in diesem Kapitel betrachten ist der sogenannte **Pullback**. Hierbei betrachten wir zwei glatte Mannigfaltigkeiten $\M,\mathcal{N}$ und eine glatte Funktion $F:M\to\mathcal{N}$. Das Ziel ist es nun eine Differentialform auf $N$, $\omega\in\Omega^k(\mathcal{N})$ mithilfe von $F$ auf eine Differentialform auf $\M$ zurückzuziehen. Ausgewertet an $p\in\M$ ergibt eine Differentialform $\eta\in\Omega^k(\M)$ ein Element aus $L^k(T_p^\ast\M)$,

```{math}
\eta_p\in \Omega^k(T_p\M) \subset L^k(T_p^\ast\M)
```

also eine Linearform, welche auf $k$ Elemente $v_1,\ldots,v_k\in T_p^\ast\M$ des Kotangentialraums in $p$ an $\M$ wirkt. Haben wir nun a priori $\omega\in\Omega^k(\mathcal{N})$ gegeben brauchen wir deshalb zunächst eine Methode mit der wir Tangentialvektoren über $F$ von $\M$ nach $\N$ vorschieben können, der sogennante **Pushforward**.

````{prf:definition}
Es seien $\M,\mathcal{N}$ zwei glatte Mannigfaltigkeiten und $F\in C^\infty(\M,\mathcal{N})$, dann definieren wir für $p\in\M$ 

```{math}
F_\ast:T_p\M\to T_{F(p)}\mathcal{N}\\
D\mapsto \big[f\mapsto D(f\circ F)]
```

den sogenannten **Pushforward**.
````

Da wir nun Tangentialvektoren von $T_p\M$ auf $T_{F(p)}\mathcal{N}$ schieben können, sind wir in der Lage damit den Pullback von Kotangentialvektoren zu definieren.

````{prf:definition}
Es seien $\M,\mathcal{N}$ zwei glatte Mannigfaltigkeiten und $F\in C^\infty(\M,\mathcal{N})$, dann definieren wir für $p\in\M$ 

```{math}
F^\ast: T_{F(p)}^\ast\mathcal{N}\to \big[T^p_\M\mapsto\R\big]\\
v \mapsto \big[D\mapsto v(F_\ast(D)) \big]
```

den **Pullback**
````

````{prf:remark}
Es gilt insbesondere, dass $F^\ast v \in T_p^\ast\M$ für jedes $v\in T_{F(p)}^\ast\mathcal{N}$.
````

Dieses Konzept können wir nun auf Formen übertragen in dem wir eine neue Differentialform punktweise an $p$ definieren am Punkt $F(p)$. Konkret seien $v_1,\ldots, v_k\in T_p\M$, dann definiere

```{math}
(F^\ast\omega)_p (v_1,\ldots,v_k) := \omega_F(p)\big(F_\ast(v_1),\ldots,F_\ast(v_k)\big).
```

Die so definierte Abbildung bildet tatsächlich zwischen den passenden Räumen ab

```{math}
F^\ast:\Omega^k(\mathcal{N})\to\Omega^k(\mathcal{M})\\
\omega\mapsto \big[ p\mapsto (F^\ast\omega)_p \big].
```

Zusätzlich erhält man folgende Eigenschaften.

````{prf:lemma}
Es seien $\M,\mathcal{N}$ glatte Mannigfaltigkeiten und $F\in C^\infty(\M,\mathcal{N})$, dann gilt, 

1. $F^\ast$ ist linear,

2. $F^\ast(\omega\wedge\eta) = F^\ast(\omega) \wedge F^\ast(\eta)$ für $\omega,\eta\in\Omega^k(\mathcal{N})$.

3. Für lokale Koordinaten Kovektorfelder $dy^1,\ldots,dy^m$ und $f\in C^\infty(\mathcal{N})$ gilt 

```{math}
F^\ast(f dy^{i_1}\wedge\ldots\wedge dy^{i_k}) = (f \circ F) d(y^{i_1}\circ F)\wedge\ldots\wedge d(y^{i_k}\circ F).
```
````

````{prf:proof}

Für 1. und 2. siehe Hausaufgaben, Für 3. siehe {cite:p}`lee2003` Lemma 14.16.

````
