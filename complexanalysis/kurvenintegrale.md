# Kurvenintegrale

## Wege und Kurven

Wir beginnen diesen Abschnitt mit der grundlegenden Definition von Wegen und Kurven.

````{prf:definition} Weg und Kurve
Sei $(X,\tau)$ ein topologischer Raum und $I = [a,b]$ ein reelles Intervall für $a,b \in \R$.
Wir nennen eine stetige Funktion $f \colon I \rightarrow X$ einen **Weg** in $X$.
Wir bezeichnen einen Weg $f$ als **glatt**, wenn er stetig differenzierbar ist und seine Ableitung für jeden Punkt $x \in I$ ungleich Null ist.
Außerdem bezeichnen wir einen Weg $f$ als **geschlossen**, wenn gilt $f(a) = f(b)$.
Schließlich nennen wir einen Weg $f$ **konstant**, wenn er für alle $t \in [a,b]$ auf den gleichen Punkt in $\C$ abbildet.

Die Bildmenge $f(I) \subset X$ nennen wir **Kurve** in $X$.
````

```{danger}
Normalerweise nennen wir eine Abbildung *glatt*, wenn sie unendlich oft differenzierbar ist.
Dies wird im Kontext von Wegen nicht gefordert und es genügt eine einfache stetige Differenzierbarkeit.
```

Wir wollen im Folgenden annehmen, dass $f$ eine holomorphe Funktion auf einer offenen Teilmenge $D \subset \C$ ist.
Wir betrachten $f(z) \mathrm{d}z$ als die zugehörige $1$-Form und außerdem sei $\gamma \colon I \rightarrow D$ für $I := [0,1]$ ein glatter Weg.
Wegen der Jacobischen Transformationsformel in {prf:ref}`thm:jacobitransformation` gilt dann für das Kurvenintegral von $f$ bezüglich $\gamma$

```{math}
:label: eq:kurvenintegral
\int_{\gamma} f(z) \, \mathrm{d}z = \int_I \gamma^*(f(z) \, \mathrm{d}z) = \int_0^1 f(\gamma(t)) \gamma'(t) \, \mathrm{d}t.
```

Häufig ist die Annahme eines global glatten Weges $\gamma$ eine zu starke Forderung.
Es genügt auch zu fordern, dass der Weg $\gamma$ stückweise glatt ist und aus endlich vielen Teilstücken besteht.
In diesem Fall lässt sich das Integral [](eq:kurvenintegral) als Summe der Integrale über die Teilstücke schreiben.

**ToDo: Abbildung von stückweise glatten Wegen / Kurven**

Wir definieren als Nächstes eine charakteristische Größe von geschlossenen Wegen in $\C$, den sogenannten Index.

````{prf:definition} Index
Sei $\gamma \colon [0,1] \rightarrow \C$ ein geschlossener Weg in $\C$ und $w \in \C \setminus \operatorname{Bild}(\gamma)$ ein beliebiger Punkt außerhalb der zugehörigen Kurve von $\gamma$.
Wir bezeichnen als **Index** von $w$ bezüglich des Wegs $\gamma$ folgende charakteristische Größe

```{math}
\operatorname{Ind}_\gamma(w) \ := \ \oint_\gamma \frac{1}{z - w} \frac{\mathrm{d}z}{2\pi i} \ = \ \int_0^1 \frac{\gamma'(t)}{\gamma(t - w)} \frac{\mathrm{d}z}{2\pi i} \in \mathbb{Z}.
```

Häufig wird der Index auch **Windungszahl** von $\gamma$ um $w$ genannt.
Sie ist eine *topologische Invariante*, die anschaulich beschreibt, wie häufig sich die zugehörige Kurve um den Punkt $w$ windet.

````

**ToDo: Abbildung mit Beispiel von [Wikipedia](https://de.wikipedia.org/wiki/Umlaufzahl_(Mathematik))**

````{prf:lemma}
Sei $\gamma \colon [0,1] \rightarrow \C$ ein geschlossener Weg in $\C$.
Dann ist die Abbildung, die jedem Punkt $w \in \C \setminus \operatorname{Bild}(\gamma)$ außerhalb der zugehörigen Kurve seinen Index $\operatorname{Ind_\gamma}(w)$ konstant auf jeder Zusammenhangskomponente bezüglich der Kurve von $\gamma$. 
````

````{prf:proof}
Schulz-Baldes S.318f.
````

## Homotopie

````{prf:definition} Homotopie
Sei $I := [0,1]$ ein reelles Intervall und $D \subset \C$ eine Teilmenge.
Wir nennen zwei Wege $\gamma, \Gamma \colon I \rightarrow D$ **homotop** in der Teilmenge $D$ genau dann, wenn eine stetige Abbildung $H \colon I \times I \rightarrow D$ existiert, so dass

```{math}
H(t,0) = \gamma(t), \qquad H(t,1) = \Gamma(t).
```

In diesem Fall nennen wir die Abbildung $H$ eine **Homotopie** zwischen den Wegen $\gamma$ und $\Gamma$.

````

Man kann zeigen, dass der Begriff der Homotopie zwischen Wegen in einer Teilmenge $D \subset \C$ eine *Äquivalenzrelation* auf Wegen in $D$ induziert.
Die zugehörigen Äquivalenzklassen werden auch *Homotopieklassen* genannt.

Für geschlossene Wege impliziert Homotopie eine besondere Eigenschaft bezüglich des Kurvenintegrals, wie folgendes Lemma festhält.

````{prf:lemma}
Sei $D \subset \C$ eine Teilmenge und seien $\gamma$ und $\Gamma$ geschlossene, homotope Wege in $D$.
Sei außerdem $f \colon D \rightarrow \C$ eine holomorphe Funktion.

Dann gilt

```{math}
\oint_\gamma f(z) \, \mathrm{d}z = \oint_\Gamma f(z) \, \mathrm{d}z.
```
````

````{prf:proof}
Schulz-Baldes S.321
````

Eine besondere Klasse von Wegen sind solche, die nullhomotop sind.

````{prf:definition} Nullhomotoper Weg
Wir nennen einen Weg $\gamma$ **nullhomotop** in einer Teilmenge $D \subset \C$ genau dann, wenn $\gamma$ homotop in $D$ zu einem konstanten Weg ist.
````

Wir realisieren also, dass sich nullhomotope Wege in einer Teilmenge $D \subset \C$ zu einem Punkt $w \in D$ zusammenziehen lassen.
Darüber hinaus zeigt der folgende Satz, dass das Kurvenintegral einer holomorphe Funktionen auf einem nullhomotopen Weg verschwindet.

````{prf:theorem} Satz von Cauchy
Sei $\gamma$ ein nullhomotoper Weg in einer Teilmenge $D \subset \C$, der sich zu einem Punkt $w \in D$ zusammenziehen lässt.
Sei darüber hinaus $f \colon D \rightarrow \C$ eine stetige Funktion, welche zudem holomorph auf der Menge $D \setminus \{w\}$ sei.

Dann gilt für das Kurvenintegral

```{math}
\oint_\gamma f(z) \, \mathrm{d}z = 0.
```
````

````{prf:proof}
Schulz-Baldes S.322
````

## Cauchyscher Integralsatz

Wir wollen nun einen der zentralen Aussagen der Funktionentheorie formulieren, die Cauchysche Integralformel.
Diese besagt, dass sich die Werte einer holomorphen Funktion im Inneren eines bestimmten Gebietes bereits durch die Werte auf dem Gebietsrand bestimmen lassen.

````{prf:theorem} Cauchyscher Integralsatz
Sei $D \subset \C$ ein Sterngebiet, d.h., $D$ ist eine offene Menge in der mindestens einen Punkt $z_0 \in \C$ gibt, so dass die Verbindungsstrecke jedes beliebigen Punktes $z \in D$ zu $z_0$ vollständig in $D$ liegt.
Sei außerdem $\gamma$ ein geschlossener Weg in $D$.

Dann lässt sich der Funktionswert von $f$ in jedem Punkt $z \in D \setminus \operatorname{Bild}(\gamma)$ darstellen durch das Kurvenintegral

```{math}
f(z) \ = \ \frac{1}{\operatorname{Ind}_\gamma(z)} \oint_\gamma \frac{f(\zeta)}{\zeta - z} \frac{\mathrm{d}\zeta}{2\pi i}.
```

````

````{prf:proof}
Schulz-Baldes S.323
````

Wir werden den Cauchyschen Integralsatz später noch in Form des sogenannten *Residuensatzes* stark verallgemeinern.
Für den Moment erlaubt uns dessen Aussage jedoch zu zeigen, dass jede holomorphe Funktion bereits analytisch ist, was die Umkehrung zu {prf:ref}`thm:analytischHolomorph` ist.

````{prf:theorem} Holomorphe Funktionen sind analytisch
Sei $\epsilon > 0$ und $z_0 \in D$ ein Punkt in einer offenen Teilmenge $D \subset \C$.
Sei außerdem $f \colon B_\epsilon(z_0) \rightarrow \C$ eine holomorphe Funktion.

Dann ist die Funktion $f$ für jeden Punkt $z \in B_\epsilon(z_0)$ durch eine konvergente Potenzreihe darstellbar (also analytisch) als

```{math}
f(z) = \sum_{n=1}^\infty a_n (z-z_0)^n,
```

deren Koeffizienten $(a_n)_{n\in\N}$ für alle $\epsilon' < \epsilon$ gegeben sind durch

```{math}
a_n \ = \ \oint_{\partial B_{\epsilon'}(z_0)} \frac{f(\zeta)}{(\zeta - z_0)^{n+1}} \frac{\mathrm{d}\zeta}{2\pi i}.
```

Insbesondere ist $f$ unendlich oft komplex differenzierbar und für alle $n \in \N$ gilt für die $n$-te Ableitung von $f$

```{math}
f^{(n)}(z_0) \ = \ n! \oint_{\partial B_{\epsilon'}(z_0)} \frac{f(\zeta)}{(\zeta - z_0)^{n+1}} \frac{\mathrm{d}\zeta}{2\pi i} = n! a_n.
```

````

````{prf:proof}
Schulz-Baldes S.325f.
````

Das folgende Korollar erlaubt eine direkte Abschätzung der $n$-ten Ableitung einer holomorphen Funktion.

````{prf:corollary} Cauchy-Abschätzungen

Sei $\epsilon > 0$ und $z_0 \in D$ ein Punkt in einer offenen Teilmenge $D \subset \C$.
Außerdem sei $f \colon B_\epsilon(z_0) \rightarrow \C$ eine holomorphe Funktion.
Dann gilt für alle $0 < \epsilon' < \epsilon$ die folgende genannte **Cauchy-Abschätzung**

```{math}
|f^{(n)}(z_0)| \ \leq \ \frac{n!}{\epsilon'^n} \max_{|z - z_0|=\epsilon'} |f(z)|.
```
````
