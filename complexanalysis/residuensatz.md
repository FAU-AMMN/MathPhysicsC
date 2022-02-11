# Laurententwicklung und Residuensatz

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


## Singularitäten homomorpher Funktionen

In diesem Abschnitt beschäftigen wir uns mit speziell ausgezeichneten Punkten, den sogenannten Singularitäten.

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
:label: lem:pole

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

## Laurent-Reihe

Die Beobachtung aus {prf:ref}`lem:pole` motiviert die folgende Definition der Laurent-Reihe, die nach {prf:ref}`` immer an einem Pol von Ordnung $m$ existiert.

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

## Cauchyscher Residuensatz

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
