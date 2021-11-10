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

Der Stresstensor spielt eine wichtige Rolle in der Kontinuumsmechanik, insbesondere bei der Beschreibung von Spannungen und Stress. Hierbei betrachten man zwei Komponenten.

**Normalspannung:**
Für ein Volumen $V\subset\R^3$ betrachten wir Schnittflächen $A \subset V$ auf welche eine **äußere** Kraft $F$ wirkt mit $A$-orthogonaler Komponente $F_n$.
_Formal_ ergibt sich die Normalspannung als

```{math}
\sigma = \lim_{\Delta A\rightarrow 0}\frac{\Delta F_n}{A}.
```

**Scherspannung**

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