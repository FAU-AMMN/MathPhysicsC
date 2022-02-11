# Der Integralsatz von Cauchy

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
