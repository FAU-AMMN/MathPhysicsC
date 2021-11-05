# Stabilität von Ruhelagen

Zunächst wollen wir uns den einfachen Fall von Ruhelagen für allgemeine **lineare** Differentialgleichungssysteme anschauen. 
Diese Familie von gewöhnlichen Differentialgleichungssystemen haben wir schon in Kapitel 8 in {cite:p}`tenbrinck_2021` kennen gelernt.

Das folgende Theorem beschreibt die Existenz und Eindeutigkeit einer Ruhelage eines dynamischen System, das durch ein lineares Differentialgleichungssystem charakterisiert wird und gibt Bedingungen für die Stabilität der Ruhelage.

````{prf:theorem}

Sei $A\in \C^{n\times n}$ eine Matrix mit den Eigenwerten $\lambda_1,\dots, \lambda_n\in \C$.
Dann beschreibt der zugehörige Phasenfluss $\Phi$ zum homogenen linearen Differentialgleichungssystem

```{math}
\dot{x}(t) = Ax(t)
```

eine Ruhelage in $\vec{0} \in \C^n$.
Diese ist sogar eindeutig, falls $\lambda_i\neq 0, i=1,\ldots,n$ gilt.

Für 

```{math}
\gamma \coloneqq \max_{i=1,\dots,n} \mathcal{Re}(\lambda_i)
```

kann die Stabilität der Ruhelage wie folgt charakterisiert werden:

1. Falls $\gamma <0$ gilt, ist die Ruhelage $\vec{0}$ *asymptotisch stabil*

2. Falls $\gamma >0$ gilt, ist die Ruhelage $\vec{0}$ *instabil*.

````

````{prf:proof}

Wir wissen, dass für einen beliebigen Startpunkt $x_0 \in U$ im Phasenraum der Phasenfluss $\Phi \colon I \times U \rightarrow U$ eine Lösung des Differentialgleichungssystems realisiert.
Für homogene, lineare Differentialgleichungssysteme haben wir bereits in {prf:ref}`s:lineare_dglsysteme` Lösungen mittels des *Matrixexponentials* hergeleitet.

Sei $J = S^{-1}AS$ die Jordansche Normalform von $A$ mit Transformationsmatrizen $S^{-1},S \in \C^{n \times n}$, so erhalten wir die Abschätzung

```{math}
\begin{align*}
\|\Phi_t(x_0)\| &= \|e^{tA}x_0\| = \|S^{-1}e^{tJ}Sx\| = \|S^{-1}e^{tD}e^{tN}Sx\| \\
&\leq \|S^{-1}\| \cdot \|e^{tD}\| \cdot \|e^{tN}\| \cdot \|S\| \cdot \|x\| \leq C_1 \cdot \|e^{tD}\| \cdot \|e^{t N}\|,
\end{align*}
```
für eine Konstante $C_1 > 0$, die unabhängig von $t$ ist.
Hierbei haben wir ausgenutzt, dass sich die Jordannormalform $J$ von $A$ als Summe einer Diagonalmatrix $D$ mit den Eigenwerten $\lambda_i \in \C$, $i=1,\ldots,n$ von $A$ und einer nilpotenten Matrix $N$ schreiben lässt als $J = D + N$.
Diese Matrizen kommutieren, d.h., $D \cdot N = N \cdot D$.

Wir sehen nun ein, dass $e^{tN}$ wegen der Nilpotenz von $N$ eine endliche Reihe bildet der Form

```{math}
e^{tN} = \sum_{k=0}^m \frac{(tN)^k}{k!} = \sum_{k=0}^m t^k\frac{N^k}{k!},
```

welches ein Polynom vom Grad $m$ darstellt, wobei $m$ der Nilpotenzindex der Matrix $N$ ist.

Sei nun $\epsilon > 0$ beliebig klein gewählt.
Dann lässt sich die Norm des Polynoms mit einer genügend großen Konstanten $C_2 > 0$, die von $\epsilon$ jedoch nicht von $t$ abhängt, durch eine gewöhnliche Exponentialfunktion abschätzen mit  

```{math}
 \|e^{tN}\| = \| \sum_{k=0}^m t^k\frac{N^k}{k!} \| \leq \sum_{k=0}^m t^k \frac{\|N^k\|}{k!} \leq C_2  e^{t \epsilon}.
 ```

Wählen wir nun $\gamma \coloneqq \max_{i=1,\dots,n} \mathcal{Re}(\lambda_i)$, so folgt direkt, dass gilt

```{math}
||e^{tD}|| \leq C_3 e^{t\gamma}.
```

Insgesamt erhalten wir also für die Norm des Phasenflusses

```{math}
\|\Phi_t(x_0)\| \leq C_1 \cdot \|e^{tN}\| \cdot \|e^{tD}\| \leq C_1 \cdot C_2 e^{t \epsilon} \cdot C_3 e^{t\gamma} = C e^{t \epsilon} e^{t\gamma}.
```

Da $\epsilon > 0$ beliebig klein ist, können wir $|\epsilon| < |\gamma|$ wählen.
Damit hängt das Verhalten der Norm des Flusses nur noch vom Vorzeichen von $\gamma$ ab.
Wir unterscheiden daher zwei Fälle:

1\. Wenn $\gamma >0$ ist, so existiert zum Eigenwert $\gamma$ von $A$ ein zugehöriger Eigenvektor $v\in U$, so dass die Eigenwertgleichung $A v = \gamma v$ gilt.
Nach Lemma {prf:ref}`lem:matrixexponential_ew` ist dann $e^{t\gamma}$ ein Eigenwert des Matrixexponentials $e^{tA}$ mit zugehörigem Eigenvektor $v$.
Insgesamt erhalten wir also

```{math}
||\Phi_t(\alpha v)|| = ||e^{tA}\alpha v|| = ||\lambda e^{t\gamma} \alpha v|| \to \infty, \quad \text{ für } \ t \to \infty, \quad  \forall \alpha>0. 
```

Also enthält jede beliebig kleine Umgebung der Ruhelage $0$ Punkte, für die die entsprechenden Lösungen divergieren.
In diesem Fall ist die Ruhelage also **instabil**.

2\. Falls $\gamma <0$ gilt, so können wir abschätzen, dass 

```{math}
0\leq \|\Phi_t(x)-0\|\leq C e^{t\epsilon} e^{t \gamma} \to 0 \quad \text{ für } \ t \to \infty.
```

Dies liefert uns also **asymptotische Stabilität** der Ruhelage $0$.
````

Wir haben also gesehen, dass im Fall eines homogenen, linearen Differentialgleichungssystems die $0$ immer eine Ruhelage des zugehörigen dynamischen Systems darstellt, deren Stabilität einzig vom Vorzeichen des größten Eigenwerts abhängt.

## Linearisierung um Ruhelage

In diesem Abschnitt wollen wir unsere Erkentnisse zur Stabilitätsanalysie vom Fall eines linearen Differentialgleichungssystems auf den allgemeinen Fall übertragen, da man es in den meisten Anwendungen leider nur selten mit linearen Differentialgleichungen zu tun hat.
Darüber hinaus wäre es erstrebenswert Stabilitätsaussagen zu Differentialgleichungen zu machen, deren Lösungen man nicht analytisch explizit herleiten kann.
Daher betrachten wir im Folgenden ein allgemeines Differentialgleichungssystem erster Ordnung auf dem Phasenraum $U\in \R^n$, das nicht notwendigerweise linear sein muss und wie folgt formuliert wird

```{math}
\dot{x} = F(x), \quad F\in C^1(U;\R^n).
```

Wir nehmen an, dass $x_F \in U$ eine Ruhelage ist, so dass $F(x_F) = 0$ gilt.
in einer Umgebung einer Gleichgewichtslage $x_f$. Von dieser können wir (durch Einführung verschobener Koordinaten $x-x_f$) o.B.d.A. annehmen, dass sie sich im Nullpunkt befindet.
Mit $A := Df(0)$ bezeichne 

```{math}
R\in C^1(U, \R^n),\quad R(x):=f(x) -Ax
```
die Abweichung des Vektorfeldes von seiner Linearisierung an der Gleichgewichtslage.

Wir wollen zeigen, dass die Lösung der DGL in führender Ordnung durch die Linearisierung von $f$ kontrolliert werden, soweit wir uns in der Nähe der Gleichgewichtslage befinden. Dazu benutzen wir das folgende Lemma.

````{prf:lemma}
:label: lemma:intexpglgn

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
:label: lemma:Gronwall
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

## Asymptotische Stabilität von Ruhelagen

````{prf:theorem} Asymptotische stabilität von Ruhelagen
Eine Gleichgewichtslage $x_s\in  U\subset \R^n$ der DGL
```{math}
\dot{x} = F(x), \quad f\in C^1(U,\R^n)
```
ist asymptotisch stabil, wenn für die Eigenwerte $\lambda$ von $Df(x_s)$ gilt: $Re(\lambda)<0$.
````

````{prf:proof}

- Wieder können wir durch eine Verschiebung $x_s = 0$ erreichen. Da $U\subseteq\R^n $ offen ist, gehört eine Kugelumgebung vom positiven Radius $\vec{r}$ zu $U$.

- Für die Eigenwerte $\lambda_i$ von $A:=Df(x_s)$ gelte die Abschätzung $Re(\lambda_i)< -\Lambda,\ \Lambda>0$ geeignet. Dann gibt es ein $c>0$, sodass gilt

```{math}
\|e^{At}\| \leq c\cdot e^{-\Lambda t}\quad (t\geq 0).
```
Das ersieht man aus der Tatsache, dass die Einträge von $e^{At}$ Summen von $\lambda_i$-Quasipolynomen $e^{\lambda_i t}p_i(t)$ sind und dass wegen $Re(\lambda_i) + \Lambda <0$
```{math}
\lim_{t\to\infty} \exp((\lambda_i + \Lambda)t)p_i(t) = 0
```
ist.

- Nun existiert ein Radius $r\in (0,\vec{r})$ mit
```{math}
\|R(x)\|\leq \frac{\Lambda}{2c} \|x\|, \quad \text{falls } \|x\|\leq r,
```
denn $\lim_{x\to 0} \frac{\|Re(x)\|}{\|x\|} = \lim_{x\to}\frac{\|f(x)- Df(0)\cdot x\|}{\|x\|} = 0$.

- Wenn wir nun zeigen können, dass aus
```{math}
:label: eq:residuumabsch
\|x(0)\|\leq \epsilon <\frac{r}{c}
```
folgt, dass für $t\geq 0$ gilt:
```{math}
\|x(t)\|\leq c\epsilon e^{-\Lambda t/2},
```
dann haben wir den Satz bewiesen, denn für die rechte Seite gilt: $c\epsilon e^{-\Lambda t/2} \leq c\epsilon<r<\tilde{r}$, und für $t\to \infty$ strebt sie gegen Null.

Nun gilt nach Lemma \ref{lemma:intexpglgn}: $x(t) = e^{At}x_0 + \int_0^t e^{A(t-s)} R(x(s))\, ds$ woraus mit \ref{eq:residuumabsch} die Ungleichung
```{math}
\|x(t)\|\leq ce^{-\Lambda t}\|x_0\| + \int_0^tce^{-\Lambda (t-s)}\frac{\Lambda}{2c}\|x(s)\|\, ds
```
folgt, soweit $\|x\|\leq r$.

Setzt man $F(t):=e^{\Lambda t}\|x(t)\|$, dann gilt
```{math}
F(t)\leq \underbrace{c\|x_0\|}_{=:a} + \int_0^t \underbrace{\frac{\Lambda}{2}}_{=:g(s)} F(s)\, ds,
```
also nach dem Gronwall-Lemma \ref{lemma:Gronwall}
```{math}
F(t) \leq c \|x_0\| + \exp{\left( \frac{1}{2} \int_0^t \Lambda \, ds \right) }
\leq c \epsilon e^{\frac{\Lambda}{2} t} \leq r e^{\frac{\Lambda}{2} t}
```
oder $\|x(t)\|\leq re^{-\frac{\Lambda}{2}t}$. Die Lösungskurve bleibt also für alle positiven Zeiten in der Vollkugel $\{x\in \R^n|\|x\|\leq r\}$ und konvergiert gegen Null.
````

````{prf:remark}
Der Beweis liefert zusätzlich die Aussage, dass alle $x\in U$ mit $\|x\|<\frac{r}{c}$ zu gegen die Gleichgewichtslage konvergierenden Orbits gehören, also in deren Einzugsbereich, dem so genannten *Bassin*, liegen.
````

### Lyapunov-Stabilität von Ruhelagen

Während ein hinreichendes Kriterium für das Vorliegen *asymptotischer Stabilität* die strikte Ungleichung $Re(\lambda_i)<0$ für die Eigenwerte $\lambda_i$ der Jacobi-Matrix war, ist die Situation bezüglich der Liapunov-Stabilität komplizierter.

````{prf:theorem}
Besitzen die Eigenwerte $\lambda_i$ von $A\in \R^{n\times n}$ Realteil $Re(\lambda_i) \leq 0$, und ist im Fall $Re(\lambda_i)=0$ die geometrische Vielfachheit gleich der algebraischen, dann ist $0\in \R^n$ Liapunov-stabile Gleichgewichtslage der DGL $\dot{x} = Ax$.
````
````{prf:proof}

- Aus der **Jordan Normalform** $A=VJV^{-1}$ mit Jordan-Matrix $J$ der Form
```{math}
J=
\begin{pmatrix}
J_{r_1}(\lambda_1)& & & 0\\
 & J_{r_2}(\lambda_2) & & \\
 & & \ddots & \\
 0 & & J_{r_k}(\lambda_k)
\end{pmatrix}, \quad J_r(\lambda_r):=\begin{pmatrix}
\lambda_r & 1 & & 0\\
 & \ddots & \ddots & \\
 & & \ddots & 1\\
 0 & & & \lambda_r
 \end{pmatrix} \in \C^{r\times r}
```
folgt mit
```{math}
\exp{(Jt)} = \begin{pmatrix}
\exp{(J_{r_1}(\lambda_1)t)} & & 0\\
 & \ddots & \\
 0& & \exp{(J_{r_k}(\lambda_k)t)}
 \end{pmatrix}
```
die Liapunov-Stabilität der Gleichgewichtslage aus
```{math}
\|\exp{(At)}\|= \|V\exp{(Jt)}V^{-1}\|\leq \|V\|\|V^{-1}\|\|\exp{(Jt)}\|,
```
wenn für alle Jordanblöcke $J_{r_i}(\lambda_i)$ von $J$ der Ursprung $0\in \C^{r_i}$ Liapunov-stabile Gleichgewichtslage der DGL $\dot{y} = J_{r_i}(\lambda_i)y$ ist.

- Aus $Re(\lambda_i)<0$ folgt sogar asymptotische Stabilität.

- Da für einen komplexen Eigenwert $\lambda$ von $A$ mit $Re(\lambda)=0$ die geometrische Vielfachheit nach Vorraussetzung gleich der algebraischen ist, sind die ihm zugeordneten Jordanblöcke alle eindimensional: $J_{r_i}(\lambda_i) = \lambda$. Damit ist in diesem Fall
```{math}
\|exp{(J_{r_i}(\lambda_i)t)}\|= |\cos{(Im(\lambda)t)} + i \sin{(Im(\lambda)t)}|=1.
```
````

````{prf:remark}
Dass man die Gleichheit von geoemtrischer und algebraischer Vielfachheit fordern muss, sieht man schon am Beispiel von
```{math}
A = \begin{pmatrix} 0&1\\0&0\end{pmatrix} \quad \text{mit} \quad e^{At} = \begin{pmatrix} 0&t\\0&0\end{pmatrix}.
```
````

Leider kann man nicht wie im Fall der asymptotischen Stabilität vom linearen auf dern nicht linearen Fall folgern.
````{prf:example}
DGL $\dot{x} = \alpha x+ \beta x^3$ mit Parametern $\alpha, \beta\in \R$. \\
Die Null ist Gleichgewichtslage der DGL und ihre Linearisierung $\dot{y} = \alpha y$.

|          | linearisierte Gleichung | nicht lineare Gleichung |
| :------- |:------------------------|:----------------------- |
| $\alpha<0$ | asymptotisch stabil | asymptotisch stabil |
| $\alpha>0$ | instabil | instabil |
| $\alpha=0$ | Liapunov-stabil | <table><tbody><tr><td>asymptotisch stabil für</td><td>&beta; &lt; 0</td></tr><tr><td>stabil für</td><td>&beta; =0</td></tr><tr><td> instabil für</td><td>&beta; &gt; 0</td></tr></tbody></table> |

````
````{prf:remark}
Anschaulich gesprochen kann asymptotische Stabilität nur vorliegen, wenn der Fluss in der Nähe der Gleichgewichtslage das Phasenraumvolumen verkleinert. Daher kann man in physikalischen Situationen ohne Reibungseffekte höchstens Liapunov-Stabilität erwarten. das hat z.B. zur Folge, dass die Frage der **Stabilität des Sonnensystems** sehr subtil ist.
````