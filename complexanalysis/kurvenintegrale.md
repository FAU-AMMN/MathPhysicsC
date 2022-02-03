# Kurvenintegrale

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

````{prf:definition}
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

Nun beschäftigen wir uns mit speziell ausgezeichneten Punkten, den sogenannten Singularitäten.

````{prf:definition} Singularitäten
Sei $D \subset \C$ eine offene Teilmenge und $z_0 \in D$ ein Punkt.

1\. Wenn $f \colon D \setminus \{z_0\} \rightarrow \C$ eine holomorphe Funktion ist.
Dann nennen wir den Punkt $z_0$ eine **isolierte Singularität** von $f$.

2\. Wir nennen den Punkt $z_0$ eine **hebbare Singularität**, wenn $z_0$ eine isolierte Singularität einer holomorphen Funktion $f \colon D \setminus \{z_0\} \rightarrow \C$ ist und es eine holomorphe Funktion $g \colon D \rightarrow \C$ gibt, so dass $g(z) = f(z)$ gilt für alle $z \in D \setminus \{z_0\}$.

3\. Wir nennen den Punkt $z_0$ einen **Pol**, wenn für alle Folgen $z_n \rightarrow z_0$ gilt

```{math}
\lim_{n\rightarrow \infty} |f(z_n)| = \infty.
```

4\. Wir nennen den Punkt $z_0$ eine **wesentliche Singularität**, wenn $z_0$ weder hebbar noch Pol ist.
````

Der Satz von Casorati-Weierstraß erlaubt es wesentliche Singularitäten zu charakterisieren.

````{prf:remark} Casorati-Weierstraß
Sei $D \subset \C$ eine offene Teilmenge und $z_0 \in D$ ein Punkt.

Der Punkt $z_0$ ist genau dann eine wesentliche Singularität einer holomorphen Funktion $f \colon D \setminus \{z_0\} \rightarrow \C$, wenn für alle $\epsilon > 0$ die Menge der Funktionswerte $f(B_\epsilon(z_0)) \setminus \{z_0\})$ dicht in $\C$ liegt.

````

**ToDo: Hier Beispiel zu Singularitäten? Schulz-Baldes S.329**

````{prf:theorem} Riemannscher Hebbarkeitssatz

Sei $D \subset \C$ eine offene Teilmenge und $z_0 \in D$ ein Punkt.
Sei außerdem $f \colon D \setminus \{z_0\} \rightarrow \C$ eine holomorphe Funktion.
Falls eine Umgebung $U \subset D$ von $z_0$ gibt, so dass $f$ auf $U \setminus \{z_0\}$ beschränkt ist, so kann man einen Funktionswert $f(z_0)$ in $z_0$ so wählen, dass die Funktion $f$ auf der gesamten Teilmenge $D$ holomorph ist, d.h., der Punkt $z_0$ ist eine hebbare Singularität.

````

````{prf:proof}
Schulz-Baldes S.327
````

Das folgende Lemma charakterisiert Pole einer holomorphen Funktion.

````{prf:lemma}
Sei $D \subset \C$ eine offene Teilmenge und $z_0 \in D$ eine isolierte Singularität einer holomorphen Funktion $f \colon D \setminus \{z_0\} \rightarrow \C$.

Dann sind folgende Aussagen äquivalent:

1\. Der Punkt $z_0$ ist ein Pol der Funktion $f$.

2\. Es existiert ein $m \in \N$, so dass die Funktion $(z - z_0)^m f(z)$ beschränkt in einer lokalen Umgebung von $z_0$ ist, jedoch die Funktion $(z - z_0)^{m-1} f(z)$ unbeschränkt ist.

Die Ordnung der Funktion $f$ im Pol $z_0$ ist dann definiert als

```{math}
\operatorname{Ord}_{z_0}(f) := -m.
```

````

````{prf:proof}
Schulz-Baldes S.330
````

Dieser Begriff von Ordnung setzt den Begriff der Ordnung von Polynomen für holomorphe Funktionen fort.
Häufig spricht man jedoch nur von der Ordnung $m > 0$ eines Pols.

Diese Beobachtung motiviert die folgende Definition der Laurent-Reihe, die nach {prf:ref}`` immer an einem Pol von Ordnung $m$ existiert.

````{prf:definition} Laurent-Reihe

Sei $D \subset \C$ eine offene Teilmenge und $z_0 \in D$ Pol von Ordnung $m$ einer holomorphen Funktion $f \colon D \setminus \{z_0\} \rightarrow \C$.

Dann definieren wir die **Laurent-Reihe** von $f$ um den Pol $z_0$ durch

```{math}
f(z) := \sum_{n=-m}^\infty a_n (z-z_0)^n.
```

Als **Hauptteil** der Laurent-Reihe bezeichnen wir den Term

```{math}
\sum_{n=-m} a_n (z-z_0)^n
```

und das **Residuum** von $f$ bei $z_0$ als

```{math}
\operatorname{Res}_{z_0}(f) = a_{-1}.
```

````{prf:definition} Meromorphe Funktion
Sei $D \subset \C$ eine offene Teilmenge.
Wir nennen eine Funktion $f \colon D \rightarrow \C$ **meromorph** auf $D$ genau dann, wenn eine lokalendliche Menge $P$ existiert, so dass die Funktion $f$ holomorph auf $D \setminus P$ mit Polen in $P$ ist. 
````

````{prf:example} Meromorphe Funktionen
Rationale Funktionen oder konkretes Beispiel

Schulz-Baldes S.332

````

Das folgende Lemma erlaubt die explizite Berechnung des Residuums.

````{prf:lemma} Berechnung des Residuums

Sei $D \subset \C$ eine offene Teilmenge und $z_0 \in D$ Pol einer holomorphen Funktion $f \colon D \setminus \{z_0\} \rightarrow \C$.

Für genügend kleine $\epsilon > 0$ lässt sich das Residuum von $f$ bei $z_0$ angeben als

```{math}
\operatorname{Res}_{z_0}(f) = \oint_{\partial B_\epsilon(z_0)} f(z) \frac{\mathrm{d}z}{2\pi i}.
```

Falls der Pol von Ordnung $-m$ ist, lässt sich das Residuum von $f$ bei $z_0$ sogar angeben als

```{math}
\operatorname{Res}_{z_0}(f) = \partial_z^{m-1}\left( (z-z_0)^m \frac{f(z)}{(m-1)!}\right)|_{z=z_0}.
```

````

````{prf:proof}
Schulz-Baldes S.333f.
````

````{prf:example} Berechnung des Residuums
Rationale Funktion bei Schulz-Baldes S.335
````

Der folgende Residuensatz von Cauchy stellt eine zentrale Aussage der Funktionentheorie vor.

````{prf:theorem} Cauchyscher Residuensatz
Sei $D \subset \C$ eine offene Teilmenge und $f \colon D \rightarrow \C$ eine meromorphe Funktion mit endlicher Menge $P \subset D$ von Polstellen.
Sei außerdem $\gamma$ ein geschlossener und zusammenziehbarer Weg in $D$ mit $\operatorname{Bild}(\gamma) \cap P = \emptyset$.

Dann gilt der folgende Zusammenhang

```{math}
\int_\gamma f(z) \frac{\mathrm{d}z}{2\pi i} = \sum_{z_0 \in P} \operatorname{Ind}_\gamma(z_0) \operatorname{Res}_{z_0}(f).
```
````

````{prf:proof}
Schulz-Baldes S.337
````

````{prf:remark}
Für holomorphe Funktionen $f$ entspricht der Residuensatz gerade dem Cauchyschen Integralsatz.
Wenn $D$ als Sterngebiet angenommen wird ist die Zusammenziehbarkeit des Wegs $\gamma$ immer erfüllt. 
````

````{prf:example}
Viele konkrete Beispiele in Schulz-Baldes S.338-344
````
