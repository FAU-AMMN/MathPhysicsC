# Maßtheorie

Ein [**Maß**](https://de.wikipedia.org/wiki/Ma%c3%9f_(Mathematik)) $\mu$ auf einer Menge $M$ wie z.B.\ dem $\R^n$
ordnet geeigneten Teilmengen $A\subseteq M$
Zahlen
```{math}
\mu(A)\in[0,\infty]:=[0,\infty)\cup\{\infty\}
```
zu, eben das Maß von $A$. Diese Teilmengen heißen *messbar*.
Die Leere Menge ist dabei messbar, mit $\mu(\emptyset) = 0$.
Sind die messbare Teilmengen $A_1$ und $A_2$ disjunkt, dann gilt 
außerdem 
```{math}
\mu(A_1\cup A_2)= \mu(A_1)+\mu(A_2).
```
(sog. *Additivität* von $\mu$). 
Das Buch \cite{Ba}
von {\sc Bauer} gibt eine Einführung in die allgemeine Maß-und Integrationstheorie.
Siehe auch das Skript 
[Analysis III](https://www.math.fau.de/wp-content/uploads/2020/02/knauf_analysis_III_2019.pdf).
Wichtige Maße sind z.B. die folgenden.

1. Das [**Zählmaß**](https://de.wikipedia.org/wiki/Z%c3%a4hlma%c3%9f_(Ma%c3%9ftheorie)) $m$ auf einer endlichen Menge $M$, mit 
```{math}
m(A):=|A|\qquad (A\subseteq M).
````
Hier sind insbesondere alle Teilmengen messbar.

2. Das *Lebesgue--Maß* $\lambda^n$ auf dem $\R^n$, das wir bald kennen lernen,
