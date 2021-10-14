# Stabilitätsanalyse

Anschaulich wird man ein stabilitätslage $x_s$ der DGL $\dot{x}(t) = F(t, x(t))$ dann stabil nennen, wenn benachbarte Lösungen nicht von $x_s$ wegstreben.

````{prf:definition}
:label: def:Stabilitaet

Die Gleichgewichtslage $x_s \in U \subseteq \R^n$ der DGL

```{math}
\dot{x}(t) = F(t, x(t)) , \qquad f\in C^1(U,\R^n)
```

* heißt **Lyapunov-stabil** , falls für jede Umgebung $W\subseteq U$ von $x_s$ eine Umgebung $V\subseteq U$ von $x_s$ existiert, sodass das AWP für alle Anfangswerte $x_0\in V$ und alle Zeiten $t \geq 0$ lösbar ist und die Lösungen $\phi$ in  $W$ bleiben.

* Andernfalls heißt sie **instabil**.
````