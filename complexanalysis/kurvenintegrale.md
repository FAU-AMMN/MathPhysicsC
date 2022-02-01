# Kurvenintegrale

Wir beginnen diesen Abschnitt mit der grundlegenden Definition von Wegen und Kurven.

````{prf:definition} Weg und Kurve
Sei $(X,\tau)$ ein topologischer Raum und $I = [a,b]$ ein reelles Intervall für $a,b \in \R$.
Wir nennen eine stetige Funktion $f \colon I \rightarrow X$ einen **Weg** in $X$.
Wir bezeichnen einen Weg $f$ als **glatt**, wenn er stetig differenzierbar ist und seine Ableitung für jeden Punkt $x \in I$ ungleich Null ist.
Außerdem bezeichnen wir einen Weg $f$ als **geschlossen** wenn gilt $f(a) = f(b)$.

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

````{prf:definition} Homotopie
Sei $I := [0,1]$ ein reelles Intervall und $D \subset \C$ eine Teilmenge.
Wir nennen zwei Wege $\gamma, \Gamma \colon I \rightarrow D$ **homotop** in der Teilmenge $D$ genau dann, wenn eine stetige Abbildung $H \colon I \times I \rightarrow D$ existiert, so dass

```{math}
H(t,0) = \gamma(t), \qquad H(t,1) = \Gamma(t).
```

In diesem Fall nennen wir die Abbildung $H$ eine **Homotopie** zwischen den Abbildungen $\gamma$ und $\Gamma$.

````