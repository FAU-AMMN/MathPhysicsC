# Lebesgue-Integral

Anhand des in ?? konstruirten MAßes wollen wir nun einen neuen Begriff des Integrals herleiten. Unsere Motivation hierbei war anstatt den Definitionsbereich, den Bildbereich einer Funktion $f:\Omega\to\R$ zu zerteilen. Dies führt auf das Problem, dass man Urbildern

```{math}
f^{-1}(I)
```

für Mengen $I\subset\R$ ein Maß zuordnen muss. Dies soll im Folgenden mithilfe des Lebesgue-Maßes geschehen. Um $f^{-1}(I)$ allerdings im Lebesgue-Maß auswerten zu können, müssen wir voraussetzen, dass diese Menge messbar ist. Dies führt auf spezielle Anforderungen an die Funktion $f$.

## Messbare Funktionen

Wir beginnen mit der Definition von messbaren Funktionen. Wir benutzen hierbei den Begriff eines **Messraums** der anders als ein MAßraum nur eine Grundmenge und eine $\sigma$-Algebra voraussetzt und kein Maß beinhaltet.

````{prf:definition} Messbarkeit von Funktionen
Es seien $(\Omega_1,\Sigma_1), (\Omega_1,\Sigma_1)$ zwei Messräume und $f:\Omega_1\to\Omega_2$ eine Funktion, dann nennen wir $f$ **messbar**, falls

```{math}
f^{-1}(A)\in\Sigma_1\quad\forall A\in\Sigma_2
```

````

Für ein Teilmengensystem $\mathcal{C}\subset 2^{\Omega_2}$ benutzten wir auch die Schreibweise

```{math}
f^{-1}(\mathcal{C}) = \{ f^{-1}(C): C\in\mathcal{C}\},
```

womit sich die Messbarkeit einer Funktion äquivalent auch durch die Bedingung

```{math}
f^{-1}(\Sigma_2)\subset\Sigma_1
```

schreiben lässt. In diesem Kapitel wollen wir speziell Funktionen $f:\Omega\to\overline{\R}$ betrachten wobei $\Omega\subset\R^d$. Hierbei nennen wir $f$ **Borel-messbar**, falls

```{math}
f^{-1}(\mathcal{B}(\overline{\R}))\subset \mathcal{B}(\R^d).
```

Analog nennen wir $f$ **Lebesgue-messbar**, falls

```{math}
f^{-1}(\mathcal{B}(\overline{\R}))\subset \mathcal{A}.
```

Eine wichtige Aussage in dem Kontext von messbaren Funktionen ist die Tatsache, dass sich Urbild mit dem $\sigma$-Operator vertauschen lässt, wobei für $\mathcal{C}\subset 2^\Omega$ die Menge $\sigma(\mathcal{C})$ gerade die kleinste $\sigma$-Algebra ist welche $\mathcal{C}$ enthält siehe ??.

````{prf:lemma}
Es sei $f:\Omega_1\to\Omega_2$ eine Funktion und $\mathcal{C}\subset 2^{\Omega_2}$ ein Teilmengensystem, dann gilt

```{math}
f^{-1}(\sigma(\mathcal{C})) = \sigma(f^{-1}(\mathcal{C})).
```
````

````{prf:proof}
ToDo
[Vorlesung](https://www.fau.tv/clip/id/40563) ab 29:52.
````

Mit diesem Lemma können wir folgende Beziehungen zeigen.

````{prf:lemma}
1. Borel-messbare Funktionen sind Lebesgue-messbar
2. Stetige Funktionen sind Borel-messbar. 
````

````{prf:proof}
ToDo
[Vorlesung](https://www.fau.tv/clip/id/40563) ab 17:12
````

## Charakterisierung über Niveaumengen


````{prf:remark}

1\. Konkatenation von messbaren Funktionen ist wieder eine messbare Funktion.

2\. Summen, Produkte, Quotienten, Maxima und Minima endlich vieler reellwertiger messbarer Funktionen sind wieder messbar.

3\. Sei $(f_n)_{n \in \N}$ mit $f_n \colon \Omega \subset \R^n \rightarrow \R$ eine Folge von messbaren Funktionen.
Dann sind $\inf(f_n), \sup(f_n), \lim\inf (f_n)$ und $\lim\sup (f_n)$ auch messbar.

````

## Das Lebesgue-Integral

ToDo Definition

````{prf:lemma}
:label: lem:simplefun

Sei $f \colon \Omega \subset \R^n \rightarrow [0,\infty]$ eine Lebesgue-messbare Funktion.
Dann existiert eine monoton wachsende Folge $(T_n)_{n_\in N}$ von Treppenfunktionen mit

```{math}
T_n|_{D^c} = 0 \qquad \text{ und } \qquad T_n \nearrow f,
```

d.h., es gilt

```{math}
\lim_{n\rightarrow \infty} T_n(x) = f(x) \qquad \text{ und } \qquad T_{n+1}(x) \geq T_n(x).
```

````

````{prf:proof}
ToDo
````


````{prf:definition} Lebesgue-Integral für nichtnegative Funktionen
1\. Für Lebesgue-messbare Mengen $A_i, i=1,\ldots,N$ und nicht-negative Koeffizienten $\alpha_i, i=1,\ldots,N$ definieren wir das **Lebesgue-Integral** einer positiven *Treppenfunktion* $T = \sum_{i=1}^N \alpha_i \chi_{A_i}$ als

```{math}
\int \mu(\mathrm{d}x) f(x) = \sum_{i=1}^N \alpha_i \mu(A_i).
```

2\. Sei $(T_n)_{n\in\N}$ eine monoton wachsende Folge von Treppenfunktionen mit

```{math}
T_n|_{D^c} = 0 \qquad \text{ und } \qquad T_n \nearrow f
```

und $f \colon D \rightarrow \overline{R}$ eine positive, *Lebesgue-messbare Funktion*.
Dann ist das **Lebesgue-Integral** von $f$ definiert als

```{math}
\int_D \mu(\mathrm{d}x) f(x) = \lim_{n\rightarrow \infty} \int \mu(\mathrm{d}x) f_n(x) = \sup_n \int \mu(\mathrm{d}x) f_n(x) \in [0,\infty].
```

````

````{prf:theorem} Eigenschaften des Lebesgue-Integrals
Das Lebesgue-Integral ist *wohldefiniert*, d.h., sein Wert ist unabhängig von der gewählten Folge von Treppenfunktionen $(T_n)_{n\in\N}$.
Darüber hinaus ist das Lebesgue-Integral *linear* und *monoton*, d.h., für nichtnegative, Lebesgue-messbare Funktionen $f,g \geq 0$ gilt

```{math}
\int \mu(\mathrm{d}x)(f(x) + \lambda g(x)) = \left( \int \mu(\mathrm{d}x) f(x) \right) + \lambda \left( \int \mu(\mathrm{d}x) g(x) \right)\\
f \leq g \quad \Rightarrow \quad \int \mu(\mathrm{d}x) f(x) \leq \int \mu(\mathrm{d}x) g(x).
```

````

````{prf:proof}
ToDo
````

````{prf:lemma} Satz von Beppo Levi
:label: lem:levi

````

````{prf:definition} Allgemeines Lebesgue-Integral
Sei $f \colon \R^n \rightarrow \R$ eine Lebesgue-messbare Funktion.
Wir nennen die Funktion $f$ **Lebesgue-integrierbar**, genau dann wenn gilt

```{math}
\mu(|f|) < +\infty
```

Falls die Funktion $f$ Lebesgue-integrierbar ist, definieren wir entsprechende positive integrierbare Funktionen

```{math}
f_+ := \max \lbrace f, 0 \rbrace, \qquad f_- := \max{-f, 0},
```

so dass gilt $f = f_+ - f_-$.
Dann können wir das **Lebesgue-Integral** von $f$ definieren als

```{math}
\mu(f) := \mu(f_+) - \mu(f_-).
```

Häufig vewenden wir die äquivalenten Schreibweisen

```{math}
\mu(f) \hat{=} \int \mu(\mathrm{d}x) f(x) \hat{=} \int f(x) \mathrm{d}x.
```

````

````{prf:lemma}
Das Lebesgue-Integral ist eine linearer und monotoner Operator auf der Menge der Lebesgue-integrierbaren Funktionen.
````

````{prf:proof}
ToDo
````

````{prf:definition}
Seien $f,g \colon \R^n \rightarrow \overline{\R}$ Lebesgue-messbare Funktionen.
Wir sagen $f = g$ **fast sicher** bezüglich des Lebesgue-Maßes genau dann, wenn eine Lebesgue-Nullmenge $N$ existiert, so dass gilt

```{math}
f(x) = g(x) \quad \forall x \in \R^n \setminus N.
```

````
