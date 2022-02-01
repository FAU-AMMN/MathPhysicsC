# Integrationstechniken

In diesem Abschnitt beschäftigen wir uns mit Rechenmethoden und Rechenregeln, die es uns erlauben Funktionen mehrerer Variablen bezüglich des Lebesgue-Maßes zu integrieren. Insbesondere lernen wir dadurch Verfahren kennen um Volumina und Flächen zu berechnen. Um diese Regeln formal zu zeigen benötigen wir zunächst etwas Theorie.

## Produktmaße

Für zwei Messräume $(\Omega_1,\Sigma_1), (\Omega_2,\Sigma_2)$ wollen wir nun einen Produktraum erhalten. Hierbei werden wir auf Konzepte des **Tensorproduktes** zurückgreifen und benutzen deshalb die gleiche Notation. Wir definieren dann die Produkt-$\sigma$-Algebra,

```{math}
\Sigma_1\otimes\Sigma_2 := \sigma\left( \{A_1\times A_2: A_1\in\Sigma_1, A_2\in\Sigma_2 \}.
```

Wir arbeiten nicht auf Vektorräumen darum konstruieren wir **kein** Tensorprodukt im Sinnen von Kapitel ??, aber die grundlegenden Konzepte
sind ähnlich, weshalb es üblich ist, hier diese Notation zu verwenden. Weiterhin erkenn wir, dass mit dieser Konstruktion $\Sigma_1\otimes\Sigma_2 $ eine $\sigma$-Algebra auf $\Omega_1\times\Omega_2$ ist.

````{prf:definition} Produktmaß
Es seien $(\Omega_1,\Sigma_1,\mu_1), (\Omega_2,\Sigma_2,\mu_2)$ zwei Maßräume, dann heißt ein Maß $\mu$ auf dem Messraum $(\Sigma_1\otimes\Sigma_2, \Omega_1\times\Omega_2)$ **Produktmaß**, falls 

```{math}
\mu(A_1\times A_2) = \mu_1(A_1)\mu_2(A_2)\quad\forall A_1\in\Sigma_1, A_2\in\Sigma_2.
```

````

Man kann zeigen, dass ein Produktmaß stets existiert siehe ??. Allerdings ist es nicht notwendigerweise eindeutig bestimmt, hierfür benötigt man die sogennate $\sigma$-Endlichkeit.

````{prf:definition}
Es sei $(\Omega,\Sigma,\mu)$ ein Maßraum, das Maß $\mu$ heißt $\sigma$**-endlich**, falls ene Folge von Mengen $A_i\in\Sigma,i\in\N$ existiert, s.d., $\mu(A_i)<\infty$ und 

```{math}
\bigcup_{i\in\N} A_i = \Omega.
```
````

````{prf:remark}
Das wichtigste Beispiel für uns ist das Lebesgue-Maß auf $\R^d$ welches bezüglich der Borelschen $\sigma$-Algebra zwar nicht endlich aber $\sigma$-endlich ist. Insbesondere ist es damit auch $\sigma$-endlcih bezüglich der Lebesgue $\sigma$-Algebra $\mathcal{A}$.
````

## Der Satz von Fubini

Der Satz von Fubini erlaubt es die Berechnung mehrdimensionaler Integrale auf die Berechnung niederdimensionaler Integrale zurück zu führen.
Um diesen zentralen Satz zu formulieren benötigen wir jedoch zunächst den Begriff von doppelintegrierbaren Funktionen.

````{prf:definition} Doppelintegrierbare Funktion

Wir nennen eine Funktion $f \colon \R^n \times \R^k \rightarrow \overline{\R}$ **doppelintegrierbar** oder **iteriert integrierbar**,
wenn die folgende Aussagen gelten:

1\. Für fast alle Punkte $x \in \R^n$ ist die Funktion

```{math}
f_x \colon \R^k &\rightarrow \overline{\R},\\
f_x(y) &:= f(x,y).
```

über $\R^k$ Lebesgue-integrierbar.
In diesem Fall definieren wir eine Funktion

```{math}
F(x) := \int_{\R^k} f_x(y) \, \mu_k(\mathrm{d}y).
```

2\. Die Funktion $F \colon \R^k \rightarrow \overline{\R}$ ist über $\R^n$ Lebesgue-integrierbar.
In diesem Fall können wir das **Doppelintegral** von $f$ berechnen als

```{math}
\mu_n(\mu_k(f)) := \int_{\R^n}\int_{\R^k} f(x,y) \, \mu_n(\mathrm{d}x) \mu_k(\mathrm{d}y) = \int_{\R^k} F(x) \, \mu_k(\mathrm{d}y).
```

3\. Die beiden ersten Aussagen gelten auch für vertauschte Rollen der Variablen $x$ und $y$.

````

````{prf:lem}
:label: lem:doppelintegrierbar

1\. Die Menge der doppelintegrierbaren Funktionen bilden einen Vektorraum $V_D$.
Doppelintegrale sind *linear*, d.h., für zwei doppelintegrierbare Funktionen $f,g \in V_D$ und beliebige Skalare $\lambda \in \R$ gilt

```{math}
\mu_n(\mu_k(f + \lambda g)) = \mu_n(\mu_k(f)) + \lambda \mu_n(\mu_k(g)),\\
\mu_k(\mu_n(f + \lambda g)) = \mu_k(\mu_n(f)) + \lambda \mu_k(\mu_n(g)).
```

2\. Sei $(f_j)_j\in\N$ eine Folge von doppelintegrierbaren Funktionen, die nichtnegativ sind, d.h., $f_j \geq 0$ für $j\in\N$.
Die Folge konvergiere von unten gegen eine Funktion $f$ und es existiere eine Konstante $C < \infty$ mit

```{math}
\mu_n(\mu_k(f_n)) \leq C, \qquad \mu_k(\mu_n(f_n)) \leq C.
```

Dann ist die Funktion $f$ ebenfalls doppelintegrierbar und es gilt

```{math}
\lim_{j\to\infty} \mu_n(\mu_k(f_j)) = \mu_n(\mu_k(f)), \quad \lim_{j\to\infty} \mu_k(\mu_n(f_j)) = \mu_k(\mu_n(f)).
```

````

````{prf:proof}
Schulz-Baldes S.153f.
````

````{prf:remark}
Die Aussage aus {prf:ref}`lem:doppelintegrierbar` gilt analog für nichtnegative Funktionenfolgen $(f_j)_{j\in\N}$, die von oben gegen die Funktion $f$ konvergieren. 
````

````{prf:theorem} Das Prinzip von Cavalieri

Sei $A \subset \R^{n+k}$ eine messbare Menge für die gilt $\mu_{n+k}(A) < \infty$.

Dann gilt, dass die Menge

```{math}
A_x := \lbrace y \in \R^k | (x,y) \in A \rbrace
```

ebenfalls messbar ist mit endlichem Maß $\mu_k(A_x)$.

Außerdem ist jede Funktion $x \mapsto \mu_k(A_x)$ messbar und es gilt

```{math}
\mu_{n+k}(A) = \int \mu_n(\mathrm{d}x) \mu_k(A_x).
```

Die Aussage gilt für Vertauschung der Variablen $x$ und $y$ analog.
````

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
