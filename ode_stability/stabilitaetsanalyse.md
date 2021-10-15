# Stabilitätsanalyse

In diesem Abschnitt schauen wir uns das Verhalten von dynamischen Systemen um Ruhelagen an. 
Zur Erinnerung $x\in U $ heißt Ruhelage, wenn $\Phi_t(x) = x$ für alle $t$ ein Fixpunkt des Flusses ist.
Anschaulich versteht man unter der stabilitätsanalyse von Ruhelagen ob benachbarte Lösungen von der Ruhelage wegstreben oder nicht.


````{prf:definition} Stabilität von Lösungen
:label: def:Stabilitaet

Sei $\Phi$ der Fluss zu dem Vektorfeld $f\in C^1(U,\R^n)$ auf $U$.

i) Eine Lösung $ t \in [0,\infty) \mapsto \Phi_t(x)$ heißt **(Lyapunov) stabil**, wenn zu jedem $\epsilon > 0$ ein $\delta>0$ existiert mit:

```{math}
\|x-y\|<\delta \Rightarrow \sup_{t\geq0}\|\Phi_t(x)-\Phi_t(y)\|<\epsilon.
```

ii) Eine Lösung $ t \in [0,\infty) \mapsto \Phi_t(x)$ heißt **asymptotisch stabil**, wenn ein $\delta > 0$ existiert mit:

```{math}
\|x-y\|<\delta \Rightarrow \lim{t\to\infty}\|\Phi_t(x)-\Phi_t(y)\|=0.
```

iii) Eine Lösung heißt **instabil**, wenn sie nicht stabil ist.
````

````{prf:example} harmonischer Oszillator

Der Fluss für den harmonischen Oszillator im ungedämpfte Fall ist, wie wir im vorherigem Beispiel herausgefunden haben, gegeben durch $ \Phi(t, (x,p)) = \begin{pmatrix}
\frac{p}{\omega m}\sin(\omega t) + x~\cos(\omega t)\\
p \cos(\omega t) - m x \sin(\omega t)
\end{pmatrix} \stackrel{!}{=}\begin{pmatrix}
x\\p\end{pmatrix}
 $. Wir sehen, dass eine Ruhelage sich bei
$\begin{pmatrix}
x\\p\end{pmatrix} = \begin{pmatrix}
0\\0\end{pmatrix}$ befindet.

Diese Ruhelage ist stabil.
Sie ist sogar asymptotisch stabil für den Fall mit Reibung $(r>0)$ und instabil, falls die Reibung negativ ist (Hausuafgabe?).

````