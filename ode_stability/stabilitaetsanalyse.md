# Stabilitätsanalyse

In diesem Abschnitt schauen wir uns das Verhalten von dynamischen Systemen um Ruhelagen an. Diese sind oftmals von besonderes Interesse, da man in vielen technischen Anwendungen daran interessiert ist das System in eine oder nahe einer Gleichgewichtslage zu bringen.

Zur Erinnerung $x\in U $ heißt Ruhelage, wenn $\Phi_t(x) = x$ für alle $t$ ein Fixpunkt des Flusses ist. Für spezielle autonome DGL mit
```{math}
\dot{x} = F(x)
```
ist $x$ auch eine Ruhelage, falls $F(x) = 0$ gilt. Das ist einfach zu verstehen, da die Geschwindigkeit 0 ist und somit die Funktion $F$ die nur vom Ort abhängt sich nicht ändern kann.

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
\end{pmatrix}
 $. Nun suchen wir einen Fixpunkt der unabhängig ist von $t$. Wir sehen, dass eine Ruhelage sich bei
$\begin{pmatrix}
x\\p\end{pmatrix} = \begin{pmatrix}
0\\0\end{pmatrix}$ befindet.

Diese Ruhelage ist stabil, denn wie wir im Phasenporträt gesehen habe ist jeder Anfangswert um (0,0) periodisch. Damit kann das System nicht wegstreben von der Ruhelage.
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
Falls $\gamma <0$, dann gilt $0\leq \|\Phi_t(x)-0\|\leq Ce^{\gamma t} \|e^{tJ}\| \to 0$. Also asymptotische Stabilität des Ruhepunktes 0.
````
````{prf:example}

Wir führen das Beispiel vom vorherigen Abschnitt weiter. 

````

## Linearisierung um Ruhelage

In diesem Abschnitt wollen wir unsere Erkentnisse aus dem linearen Fall auf den allgemeinen übertragen. Man möchte Stabilitätsfragen auch für DGLn klären, deren Lösungen man nicht direkt hinschreiben kann.

Wie betrachten nun eine nicht notwendig lineare DGL auf $U\in \R^n$

```{math}
\dot{x} = F(x), \quad f\in C^1(U,\R^n)
```

in einer Umgebung einer Gleichgewichtslage $x_f$. Von dieser können wir (durch Einführung verschobener Koordinaten $x-x_f$) o.B.d.A. annehmen, dass sie sich im Nullpunkt befindet.
Mit $A := Df(0)$ bezeichne 

```{math}
R\in C^1(U, \R^n),\quad R(x):=f(x) -Ax
```
die Abweichung des Vektorfeldes von seiner Linearisierung an der Gleichgewichtslage.

Wir wollen zeigen, dass die Lösung der DGL in führender Ordnung durch die Linearisierung von $f$ kontrolliert werden, soweit wir uns in der Nähe der Gleichgewichtslage befinden. Dazu benutzen wir das folgende Lemma.

````{prf:lemma}
```{math}
x(t) = e^{At}x_0 + \int_0^t e^{A(t-s)} R(x(s))\, ds
```
````
````{prf:proof}
Wir setzen die Lösung $x(t)$ des AWP $\dot{x} = F(x), x(0) = x_0$ in der Form
```{math}
x(t) = e^{At}c(t),\quad \text{mit }c(0) = x_0
```
an, und suchen eine Bestimmugsgleichung für den Vektor $c(t)$(sog. Variation der Konstanten).
Es gilt
```{math}
\dot{x}(s) =A e^{As}c(s)+ e^{As}\dot{c}(s) = Ax(s) + e^{As}\dot{c}(s)
```
und 
```{math}
\dot{x}(s) = Ax(s) + e^{As}\dot{c}(s) +R(x(s)),
```
also
```{math}
e^{As}\dot{c}(s) = R(x(s))\quad \text{oder}\quad \dot{c}(s) = e^{-As}R(x(s)).
```
Damit ist
```{math}
c(t) = c(0) + \int_0^t \dot{c}(s)\, ds=x_0+ \int_0^t e^{-As}R(x(s)) \, ds
```
und
```{math}
x(t) = e^{At}x_0+ \int_0^t e^{A(t-s)}R(x(s)) \, ds.
```
````
Scheinbar nützt uns diese Identität nicht viel, denn auch auf der rechten Seite taucht $x(s)$, also die unbekannte Lösung des AWP auf.

Wir können aber die Gronwall-Ungleichung auf diese Integralgleichung anwenden. Diese in der Differentialgleichungstheorie wichtige Abschätzung ähnelt Münchhausens Methode, sich an den eigenen Haaren aus dem Sumpf zu ziehen.

````{prf:lemma} Gronwall-Ungleichung
Für $f,g\in C^0([t_0,t_1), [0,\infty))$ gelte mit einem geeigneten $a \geq 0$ die Ungleichung
```{math}
f(t)\leq a + \int_{t_0}^t f(s)g(s)\, ds\quad (t\in [t_0,t_1)).
```
Dann ist
```{math}
f(t)\leq a \exp{ \left(\int_{t_0}^t g(s)\, ds\right)}\quad (t\in [t_0,t_1)).
```
````

````{prf:proof}

- Ist $a>0$, dann gilt für die rechte Seite
```{math}
h(t)\leq a + \int_{t_0}^t f(s)g(s)\, ds\quad (t\in [t_0,t_1))
```
mit der Vorraussetzung $h(t)\geq 0$ und $h'(t) = f(t)g(t)$, also $\frac{h'(t)}{h(t)}\leq g(t)$.\\
Integration ergibt $\ln \left(\frac{h(t)}{a}\right)\leq \int_{t_0}^t g(s)\, ds$, oder $h(t)\leq a \exp{\left( \int_{t_0}^t g(s)\, ds \right)}$, also die Behauptung.

- Ist $a=0$, dann gelten Voraussetzung und Resultat für alle $\hat{a} :=\epsilon >0$, also ist $f=0$.
````

````{prf:remark} Zur Gronwall-Ungleichung
Man kann sich die Abschätzung leicht merken, wenn man Gleichheit annimmt. Die Integralgleichung
```{math}
f(t) = a + \int_{t_0}^t f(s)g(s)\, ds\quad (t\in [t_0,t_1)).
```
entspricht ja dem Anfangswertproblem $\dot{f} = f\cdot g,\ f(t_0) = a$ mit der Lösung $f(t) = a \exp{\left( \int_{t_0}^t g(s)\, ds \right)}$.

````
