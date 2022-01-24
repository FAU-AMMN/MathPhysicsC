# Lebesgue-Integral

S.121-145. Schulz-Baldes

Wir beginnen mit der Definition von verschiedenen Klassen von messbaren Funktionen.
Hierzu wollen wir uns die in [] hergeleitete Maßtheorie zu Nutze machen.

````{prf:definition} Messbare Funktionen
Es sei $\Omega \subset \R^n$ eine Borel-messbare Teilmenge.
Wir betrachten eine Funktion

```{math}
f \colon D \rightarrow \overline{R} = \R \cup \lbrace -\infty, \infty \rbrace.
```

Dann können wir $f$ im Folgenden in verschiedene Klassen einteilen.

1\. Wir nennen $f$ **Borel-messbar** genau dann, wenn die Urbilder aller Borel-messbaren Teilmengen von $\B(\overline{R})$ unter $f$ auch wieder Borel-messbarbare Teilmengen in $\B(\R^n)$ sind, d.h., wenn gilt

```{math}
\forall B \in \B(\overline{\R}): f^{-1}(B) \in \B(\R^n).
```

2\. Wir nennen $f$ **Lebesgue-messbar** genau dann, wenn die Urbilder aller Borel-messbaren Teilmengen von $\B(\overline{R})$ unter $f$ Lebesgue-messbare Teilmengen von $\R^n$ sind, d.h., wenn gilt

```{math}
\forall B \in \B(\overline{\R}): f^{-1}(B) \subset \R^n \text{ ist Lebesgue-messbar}.
```

3\. Wir nennen $f$ **Treppenfunktion** genau dann, wenn sie sich als stückweise konstante Funktion mit Hilfe von Indikatorfunktionen von Lebesgue-messbaren Mengen darstellen lässt, d.h., es existiert ein $N \in \N$ eine endliche Menge von Lebesgue-messbaren Teilmengen $A_i, i=1,\ldots,N$ und Koeffizienten $\alpha_i \in \overline{\R}$, so dass 

```{math}
f = \sum_{i=1}^N \alpha_i \chi_{A_i},
```

wobei $\chi_A$ die *Indikatorfunktion* einer Teilmenge $A \subset \R^n$ ist mit:

```{math}
\chi_A(x) = \begin{cases} 1, \quad x \in A, \\ 0, \quad x \not \in A. \end{cases}
```

````

````{prf:lemma}
Jede stetige Funktion $f \colon \R^n \rightarrow \overline{R}$ ist Borel-messbar. 
````

````{prf:proof}
Schulz-Baldes S.122
````

````{prf:remark}
Es lässt sich zeigen, dass alle Treppenfunktionen und Borel-messbaren Funktionen (und mit `prf:ref`{lem:stetigBorelMessbar} auch stetige Funktionen) schon Lebesgue-messbar sind.
````

Verallgemeinerung auf Messräume?

Illustration hier von Treppenfunktionen (siehe S.37 in Knauf)!

Erweiterung einer Funktion, die auf einer Lebesgue-messbaren Menge $\Omega \subset \R^n$ definiert ist auf ganzen Raum durch Fortsetzung mit Null.

````{prf:remark}

1\. Konkatenation von messbaren Funktionen ist wieder eine messbare Funktion.

2\. Summen, Produkte, Quotienten, Maxima und Minima endlich vieler reellwertiger messbarer Funktionen sind wieder messbar.

3\. Sei $(f_n)_{n \in \N}$ mit $f_n \colon \Omega \subset \R^n \rightarrow \R$ eine Folge von messbaren Funktionen.
Dann sind $\inf(f_n), \sup(f_n), \lim\inf (f_n)$ und $\lim\sup (f_n)$ auch messbar.

````

````{prf:theorem}
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
Schulz-Baldes S.127
````

````{prf:definition} Lebesgue-integrierbare Funktionen
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
Schulz-Baldes S.137
````