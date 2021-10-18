# Stabilitätsanalyse

In diesem Abschnitt schauen wir uns das Verhalten von dynamischen Systemen um Ruhelagen an. Diese sind oftmals von besonderes Interesse, da man in vielen technischen Anwendungen daran interessiert ist das System in eine oder nahe einer Gleichgewichtslage zu bringen.

Zur Erinnerung $x\in U $ heißt Ruhelage, wenn $\Phi_t(x) = x$ für alle $t$ ein Fixpunkt des Flusses ist.

## Stabilität von Lösungen

Anschaulich versteht man unter der stabilitätsanalyse von Ruhelagen ob benachbarte Lösungen von der Ruhelage wegstreben oder nicht. Ist nun die Ruhelage stabil, dann ist auch in Zukunft das System nahe bei der Ruhelage, sonst im Allgemeinen nicht.

````{prf:definition} Stabilität von Lösungen
:label: def:Stabilitaet

Sei $\Phi$ der Fluss zu dem Vektorfeld $f\in C^1(U,\R^n)$ auf $U$.

i) Eine Lösung $ t \in [0,\infty) \mapsto \Phi_t(x)$ heißt **(Lyapunov) stabil**, wenn zu jedem $\epsilon > 0$ ein $\delta>0$ existiert mit:

```{math}
\|x-y\|<\delta \Rightarrow \sup_{t\geq0}\|\Phi_t(x)-\Phi_t(y)\|<\epsilon.
```

ii) Eine Lösung $ t \in [0,\infty) \mapsto \Phi_t(x)$ heißt **asymptotisch stabil**, wenn ein $\delta > 0$ existiert mit:

```{math}
\|x-y\|<\delta \Rightarrow \lim_{t\to\infty}\|\Phi_t(x)-\Phi_t(y)\|=0.
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

## Ruhelagen bei lineare dynamischen Systemen

Zuerst wollen wir uns Ruhelagen für allgemeine lineare DGL anschauen. Diese art von DGL haben wir schon genauer kennen gelernt.

````{prf:theorem}

Sei $A\in \C^{n\times n}$ eine Matrix mit Eigenwerten $ z_1,\dots, z_k\in \C $.
Der Fluss $\Phi_t$ zur linearen DGL  $\dot{x}(t) = Ax(t)$ hat eine Ruhelage $0\in \C^n$ (welche eindeutig ist, wenn alle $z_k\neq0$).

Setze $\gamma = \max_{k=1,\dots,K} \mathcal{R}e(z_k)$

i) Falls $\gamma <0$, ist die Ruhelage 0 asymptotisch stabil

i) Falls $\gamma >0$, ist die Ruhelage 0 instabil.

````

````{prf:proof}

Zu beliebiger Anfangsbedingung $x$ und $\epsilon > 0$ erhalten wir die Abschätzung

```{math}
\begin{align*}
\|\Phi_t(x)\| &= \|e^{tA}x\|=\|M^{-1}e^{tD}e^{tJ}Mx\|\leq \|M^{-1}\|\|e^{tD}\|\|e^{tJ}\|\|M\|\|x\|\\
&\leq C_1\|e^{td}\|C_2 e^{\epsilon t}C_3C_4 = Ce^{\gamma t} e^{\epsilon t}.
\end{align*}
```
Weil $ e^{tJ}$ ein Polynom in $t$ ist gilt die Abschätzung $ \|e^{tJ}\|\leq \|e^{\epsilon t}\|$ und $\|e^{tD}\|\leq e^{t\gamma}$ wegen der Definiton von $\gamma$. <br />
Das verhalten der Norm des Flusses hängt vom Vorzeichen von $\gamma$ ab. <br />
Wenn $\gamma >0$, existiert $v$ mit $e^{tA}\lambda v = \lambda e^{t\gamma}v \to \infty $ für alle $\lambda>0$. Also enthällt jede Umgebung von 0 Punkte, die explodieren. <br />
Falls $\gamma <0$, dann gilt $0\leq \|\Phi_t(x)-0\|\leq Ce^{\gamma t} \|e^{tJ}\| \to 0$. Also asymptotische stabilität des Ruhepunktes 0.
````

## Linearisierung um Ruhelage

In diesem Abschnitt wollen wir unsere Erkentnisse 