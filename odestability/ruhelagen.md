# Stabilität von Ruhelagen

Zunächst wollen wir die Stabilität von dynamischen System im einfachen Fall von Ruhelagen für allgemeine **lineare** Differentialgleichungssysteme untersuchen.
Diese Familie von gewöhnlichen Differentialgleichungssystemen haben wir schon in Kapitel 8 in {cite:p}`tenbrinck_2021` kennen gelernt.

Das folgende Theorem beschreibt die Existenz und Eindeutigkeit einer Ruhelage eines dynamischen System, das durch ein lineares Differentialgleichungssystem charakterisiert wird und gibt Bedingungen für die Stabilität der Ruhelage.

````{prf:theorem}
:label: thm:stablin

Sei $A\in \C^{n\times n}$ eine Matrix mit den Eigenwerten $\lambda_1,\dots, \lambda_n\in \C$.
Dann beschreibt der zugehörige Phasenfluss $\Phi$ zum homogenen linearen Differentialgleichungssystem

```{math}
\dot{x}(t) = Ax(t)
```

eine Ruhelage in $\mathbf{0} \in \C^n$.
Diese ist sogar eindeutig, falls $\lambda_i\neq 0, i=1,\ldots,n$ gilt.

Für 

```{math}
\gamma \coloneqq \max_{i=1,\dots,n} \mathcal{Re}(\lambda_i)
```

kann die Stabilität der Ruhelage wie folgt charakterisiert werden:

1. Falls $\gamma <0$ gilt, ist die Ruhelage $\mathbf{0}$ *asymptotisch stabil*

2. Falls $\gamma >0$ gilt, ist die Ruhelage $\mathbf{0}$ *instabil*.

````

````{prf:proof}

Wir wissen, dass für einen beliebigen Startpunkt $x_0 \in U$ im Phasenraum der Phasenfluss $\Phi \colon I \times U \rightarrow U$ eine Lösung des Differentialgleichungssystems realisiert.
Für homogene, lineare Differentialgleichungssysteme haben wir bereits in {ref}`s:lineare_dglsysteme` Lösungen mittels des *Matrixexponentials* hergeleitet.

Sei $J = S^{-1}AS$ die Jordansche Normalform von $A$ mit Transformationsmatrizen $S^{-1},S \in \C^{n \times n}$, so erhalten wir die Abschätzung

```{math}
\|\Phi_t(x_0)\| &= \|e^{tA}x_0\| = \|S^{-1}e^{tJ}Sx_0\| = \|S^{-1}e^{tD}e^{tN}Sx_0\| \\
&\leq \|S^{-1}\| \cdot \|e^{tD}\| \cdot \|e^{tN}\| \cdot \|S\| \cdot \|x_0\| \leq C_1 \cdot \|e^{tD}\| \cdot \|e^{t N}\|,
```

für eine Konstante $C_1 > 0$, die unabhängig von $t$ ist.
Hierbei haben wir ausgenutzt, dass sich die Jordannormalform $J$ von $A$ als Summe einer Diagonalmatrix $D$ mit den Eigenwerten $\lambda_i \in \C$, $i=1,\ldots,n$ von $A$ und einer nilpotenten Matrix $N$ schreiben lässt als $J = D + N$.
Diese Matrizen kommutieren, d.h., $D \cdot N = N \cdot D$.

Wir sehen nun ein, dass $e^{tN}$ wegen der Nilpotenz von $N$ eine endliche Reihe bildet der Form

```{math}
e^{tN} = \sum_{k=0}^m \frac{(tN)^k}{k!} = \sum_{k=0}^m t^k\frac{N^k}{k!},
```

welches ein Polynom vom Grad $m$ darstellt, wobei $m \in \N$ der Nilpotenzindex der Matrix $N$ ist.

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
:label: eq:abschaetzungew
\|\Phi_t(x_0)\| \leq C_1 \cdot \|e^{tN}\| \cdot \|e^{tD}\| \leq C_1 \cdot C_2 e^{t \epsilon} \cdot C_3 e^{t\gamma} = C e^{t \epsilon} e^{t\gamma}.
```

Da $\epsilon > 0$ beliebig klein ist, können wir $|\epsilon| < |\gamma|$ wählen.
Damit hängt das Verhalten der Norm des Flusses nur noch vom Vorzeichen von $\gamma$ ab.
Wir unterscheiden daher zwei Fälle:

1\. Wenn $\gamma >0$ ist, so existiert zum Eigenwert $\gamma$ von $A$ ein zugehöriger Eigenvektor $v\in U$, so dass die Eigenwertgleichung $A v = \gamma v$ gilt.
Nach {prf:ref}`lem:mpotew` ist dann $e^{t\gamma}$ ein Eigenwert des Matrixexponentials $e^{tA}$ mit zugehörigem Eigenvektor $v$.
Insgesamt erhalten wir also

```{math}
||\Phi_t(\alpha v)|| = ||e^{tA}\alpha v|| = ||\lambda e^{t\gamma} \alpha v|| \to \infty, \quad \text{ für } \ t \to \infty, \quad  \forall \alpha>0. 
```

Also enthält jede beliebig kleine Umgebung der Ruhelage $0$ Punkte, für die die entsprechenden Lösungen divergieren.
In diesem Fall ist die Ruhelage also **instabil**.

2\. Falls $\gamma <0$ gilt, so gilt auch $\gamma + \epsilon <0$ und wir können abschätzen,

```{math}
0\leq \|\Phi_t(x_0)-0\|\leq C e^{t (\gamma + \epsilon)} \to 0 \quad \text{ für } \ t \to \infty.
```

Dies liefert uns also **asymptotische Stabilität** der Ruhelage $\mathbf{0}$.
````

Wir haben also gesehen, dass im Fall eines homogenen, linearen Differentialgleichungssystems die $\mathbf{0}$ immer eine Ruhelage des zugehörigen dynamischen Systems darstellt, deren Stabilität einzig vom Vorzeichen des größten Eigenwerts abhängt.

(s:linearisierung_ruhelage)=
## Linearisierung um Ruhelage

In diesem Abschnitt wollen wir unsere Erkentnisse zur Stabilitätsanalysie vom Fall eines linearen Differentialgleichungssystems auf den allgemeinen Fall übertragen, da man es in den meisten Anwendungen leider nur selten mit linearen Differentialgleichungen zu tun hat.
Darüber hinaus ist es erstrebenswert Stabilitätsaussagen zu Differentialgleichungen zu machen, deren Lösungen man nicht explizit analytisch herleiten kann.
Daher betrachten wir im Folgenden das Anfangswertproblem eines **allgemeinen Differentialgleichungssystem erster Ordnung** auf dem Phasenraum $U\in \R^n$, das nicht notwendigerweise linear sein muss und für ein Vektorfeld $F\in C^1(U;\R^n)$ wie folgt formuliert ist

```{math}
:label: eq:awpallg

\dot{x}(t) &= F(x(t)), \quad \forall t \in I \subset \R^+_0\\
x(0) &= x_0.
```

Wir nehmen an, dass $x_F \in U$ eine Ruhelage des dynamischen Systems ist, so dass dementsprechend $F(x_F) = 0$ gilt.
Durch einfache Translation der Koordinaten des Systems um $x_F \in U$, können wir ohne Beschränkung der Allgemeinheit annehmen, dass die Ruhelage sich im Nullpunkt befindet.

Im Folgenden definieren wir zwei wichtige Werkzeuge zur Untersuchung der Stabilität von Ruhelagen für allgemeine Differentialgleichungssysteme.

````{prf:definition} Linearisierung und Abweichung
:label: def:linearisierung

Sei $F\in C^1(U;\R^n)$ ein Vektorfeld auf dem Phasenraum $U \subset \R^n$ und $0$ eine Ruhelage des dynamischen Systems, dass durch das allgemeine Differentialgleichungssystem in {eq}`eq:awpallg` charakterisiert wird.
Sei nun $(DF)(x)$ die Jacobi-Matrix der Funktion $F$ im Punkt $x \in U$ (vgl. Kapitel 6.2 in {cite:p}`tenbrinck_2021`).
Dann bezeichnen wir mit $A := (DF)(0)$ die **Linearisierung** von $F$ in der Ruhelage $0 \in U$.
Außerdem bezeichnen wir die Funktion $R \in C^1(U; \R^n)$ mit

```{math}
R(x) \ \coloneqq \ F(x) - Ax
```

als die **Abweichung** (auch **Residuum** genannt) des Vektorfeldes $F$ von seiner Linearisierung $A$ in der Ruhelage.

````

Mit diesen Hilfswerkzeugen werden wir im Folgenden zeigen, dass die Lösung des Differentialgleichungssystem in führender Ordnung durch die Linearisierung $A$ von $F$ kontrolliert werden, solange wir uns nah genug zur Ruhelage befinden. Dies wird durch das folgende Lemma ausgedrückt.

````{prf:lemma}
:label: lem:intexpglgn

Wir betrachten das Anfangswertproblem aus {eq}`eq:awpallg` auf dem Phasenraum $U \subset \R^n$ für ein Vektorfeld $F\in C^1(U;\R^n)$.
Außerdem sei $A \coloneqq (DF)(0)$ die Linearisierung des Vektorfelds in der Ruhelage $0$ des dynamischen Systems und $R(x) \coloneqq F(x) - Ax$ die Abweichung von $F$ von seiner Linearisierung $A$ im Nullpunkt.

Dann lassen sich Lösungen des Differentialgleichungssystems mittels der Linearisierung $A$ und der Abweichung $R$ explizit angeben als

```{math}
x(t) = e^{At}x_0 + \int_0^t e^{A(t-s)} R(x(s))\, \mathrm{d}s, \quad \forall t \in I.
```

````

````{prf:proof}
Wir setzen zunächst die unbekannte Lösung $x(t)$ des Anfangswertproblems {eq}`eq:awpallg` in der allgemeinen Form
```{math}
x(t) = e^{At}c(t),\quad \text{mit }c(0) = x_0
```
an, und suchen eine Bestimmungsgleichung für die unbekannte Funktion $c(t)$ mittels **Variation der Konstanten** (vgl. Kapitel 8.2 in {cite:p}`tenbrinck_2021`).

Mittels der Rechenregeln für das Matrixexponentials in {prf:ref}`rem:matrixexponentialregeln` können wir die Ableitung der Funktion $x$ mittels Produktregel angeben als

```{math}
\dot{x}(s) = A e^{As}c(s)+ e^{As}\dot{c}(s) = Ax(s) + e^{As}\dot{c}(s).
```

Aus der Definition des Residuums in {prf:ref}`def:linearisierung` folgt aber auch

```{math}
\dot{x}(s) = F(x(s)) = Ax(s) + R(x(s)).
```

Vergleichen wir die beiden Gleichungen, so sieht man ein, dass 

```{math}
e^{As}\dot{c}(s) = R(x(s))
```

gelten muss.
Äquivalent können wir auch folgern, dass $\dot{c}(s) = e^{-As}R(x(s))$ gilt.

Nach dem Hauptsatz der Differential- und Integralrechnung (vgl. Theorem 5.3 in {cite:p}`tenbrinck_2021`) gilt dann für die unbekannte Funktion $c$ der folgende Zusammenhang
```{math}
c(t) = c(0) + \int_0^t \dot{c}(s)\, \mathrm{d}s = x_0+ \int_0^t e^{-As}R(x(s)) \, \mathrm{d}s.
```

Setzen wir dies in die erste Gleichung unserer Ansatzfunktion ein und nutzen die Rechenregeln des Matrixexponnentials aus {prf:ref}`rem:matrixexponentialregeln`, so erhalten wir schließlich die Aussage des Lemmas

```{math}
x(t) = e^{At}x_0+ \int_0^t e^{A(t-s)}R(x(s)) \, \mathrm{d}s.
```

````

Auf den ersten Blick nützt uns die Identität in {prf:ref}`lem:intexpglgn` nicht viel, denn auch auf der rechten Seite taucht $x(s)$, also die unbekannte Lösung des Anfangswertproblems {eq}`eq:awpallg` auf.
Es stellt sich jedoch heraus, dass wir die **Gronwall-Ungleichung** auf diese Integralgleichung anwenden können.
Diese wichtige Abschätzung in der Theorie von Differentialgleichungen ähnelt Münchhausens Methode, sich an den eigenen Haaren aus dem Sumpf zu ziehen.

```{margin} Thomas Gronwall
[Thomas Hakon Gronwall](https://de.wikipedia.org/wiki/Thomas_Hakon_Gr%C3%B6nwall) (Geboren 16. Januar 1877 in Dylta Bruk bei Axberg/Gemeinde Örebro; Gestorben 9. Mai 1932 in New York, NY) war ein schwedischer Mathematiker.
```

````{prf:lemma} Gronwall-Ungleichung
:label: lemma:Gronwall

Für zwei stetige Funktionen $f,g\in C([t_0,t_1]; \R^+)$ gelte für eine Konstante $a \geq 0$ die Ungleichung

```{math}
f(t) \leq a + \int_{t_0}^t f(s)g(s)\, \mathrm{d}s \quad \forall t\in [t_0,t_1].
```

Dann lässt sich der Wert der Funktion $f$ durch die Funktion $g$ wie folgt abschätzen

```{math}
f(t) \leq a \exp{ \left(\int_{t_0}^t g(s)\, \mathrm{d}s \right)} \quad \forall t\in [t_0,t_1].
```

````

````{prf:proof}
Wir definieren zunächst eine Hilfsfunktion

```{math}
h(t) \ \coloneqq \ a + \int_{t_0}^t f(s)g(s)\, \mathrm{d}s
```

und bemerken, dass $0 \leq f(t) \leq h(t)$ nach Voraussetzung gilt für alle $t \in [t_0, t_1]$.
Nun führen wir eine einfache Fallunterscheidung durch:

1\. Ist $h(t)=0$, so folgt mit der Abschätzung $f(t) \leq h(t)$ schon, dass $f(t) = 0$ gelten muss, so dass die Behauptung des Lemmas trivialerweise erfüllt ist.

2\. Sei also im Folgenden $h(t) > 0$.
Aus dem Haupsatz der Integral- und Differentialrechnung wissen wir, dass $h'(t) = f(t)g(t)$ gilt.
Wegen $f(t) \leq h(t)$ für alle $t \in [t_0, t_1]$ folgt sofort, dass

```{math}
f(t)g(t) \leq h(t)g(t) \quad \forall t \in [t_0,t_1].
```

Kombinieren wir diese Abschätzung mit der Identität der Ableitung $h'(t)$, so erhalten wir durch Umstellen

```{math}
\frac{h'(t)}{h(t)} \leq g(t) \quad \forall t \in [t_0, t_1].
```

Da wir $h(t) > 0$ angenommen haben erhalten wir durch Integration beider Seiten die Abschätzung

```{math}
\int_{t_0}^t \frac{h'(s)}{h(s)} \, \mathrm{d}s \leq \int_{t_0}^t g(s) \, \mathrm{d}s 
```

für alle $t \in [t_0, t_1]$.
Für die linke Seite können wir das Integral explizit angeben als

```{math}
\int_{t_0}^t \frac{h'(s)}{h(s)} \, \mathrm{d}s = \ln(h(t)) - \ln(h(t_0)) = \ln(h(t)) - \ln(a) = \ln\left(\frac{h(t)}{a}\right).
```

Es gilt also nun

```{math}
\ln \left(\frac{h(t)}{a}\right) \leq \int_{t_0}^t g(s)\, \mathrm{d}s.
```

Durch Anwenden der Exponentialfunktion auf beiden Seiten und Ausnutzen der Voraussetzung $f(t) \leq h(t)$ erhalten wir schließlich die Behauptung des Lemmas

```{math}
 f(t) \leq h(t)\leq a \exp{\left( \int_{t_0}^t g(s)\, ds \right)} \quad \forall t \in [t_0,t_1].
```

````

Wir wollen folgende Bemerkungen zur Gronwall-Ungleichung festhalten.

````{prf:remark}
1\. Die in {prf:ref}`lemma:Gronwall` beschriebene Gronwall-Ungleichung ist eigentlich ein Spezialfall für eine konstante Funktion $a(t) \equiv a \geq 0$.
Die ursprünglich bewiesene Aussage gilt auch für allgemeinere Funktionen.

2\. Man kann sich die Abschätzung in der Gronwall-Ungleichung leicht merken wenn man Gleichheit der beiden Seiten annimmt. 
Die Integralgleichung

```{math}
f(t) = a + \int_{t_0}^t f(s)g(s)\, \mathrm{d}s \quad t\in [t_0,t_1]
```

entspricht nämlich dem **linearen Anfangswertproblem** 

```{math}
\dot{f}(t) &= f(t)\cdot g(t) \quad \forall t \in [t_0, t_1], \\
f(t_0) &= a,
```

welches für alle $t \in [t_0, t_1]$ die folgende explizite Lösung besitzt 

```{math}
f(t) = a \exp{\left( \int_{t_0}^t g(s)\, \mathrm{d}s \right)}.
```

````

Wir werden die Resultate der beiden Lemmata in den folgenden Abschnitten anwenden, um die Stabilität von Ruhelagen eines allgemeinen dynamischen Systems durch eine Linearisierung zu untersuchen.

## Asymptotische Stabilität von Ruhelagen

Durch die explizite Darstellung von Lösungen allgemeiner Differentialgleichungssysteme basierend auf der Linearisierung und Abweichung des Vektorfeldes $F \colon U \rightarrow \R^n$ in {prf:ref}`lem:intexpglgn` und der Gronwall-Ungleichung in {prf:ref}`lemma:Gronwall` sind wir nun in der Lage die Stabilität einer Ruhelage eines dynamischen Systems zu analysieren.

Wir formulieren direkt das Hauptresultat, dass uns ein hinreichendes Kriterium für **asymptotische Stabilität** der Ruhelage basierend auf den Eigenwerten der Linearisierung liefert.

````{prf:theorem} Asymptotische Stabilität von Ruhelagen
:label: thm:stabasymallg

Sei $F \in C^1(U; \R^n)$ ein Vektorfeld auf dem offenen Phasenraum $U \subset \R^n$.
Eine Ruhelage $x_F \in  U \subset \R^n$ des dynamischen Systems, das durch das allgemeine Differentialgleichungssystem

```{math}
\dot{x}(t) = F(x(t)), \quad \forall t \in \R^+_0
```

charakterisiert wird, ist **asymptotisch stabil** wenn für die Eigenwerte $\lambda_i \in \C, i=1,\ldots,n$ der Linearisierung $A \, \coloneqq \, (Df)(x_F)$ gilt

```{math}
\mathcal{Re}(\lambda_i)<0, \quad \text{für } i=1,\ldots,n.
```

````

````{prf:proof}
Wie bereits in {ref}`s:linearisierung_ruhelage` diskutiert können wir durch Translation der Koordinaten des dynamischen Systems annehmen, dass ohne Beschränkung der Allgemeinheit $x_F = 0 \in U$ gilt.
Da $U\subseteq\R^n$ nach Vorraussetzung offen ist, können wir eine offene Kugel $B_{{r^\ast}}(0) \coloneqq \{y \in U \colon ||y|| < {r^\ast}\}$ mit Radius ${r^\ast} > 0$ als Umgebung der Ruhelage $0$ finden, so dass $B_{r^\ast}(0) \subset U$ gilt.

Wir nehmen im Folgenden an, dass der Realteil der Eigenwerte $\lambda_i \in \C, i=1,\ldots,n$ der Linearisierung $A \, \coloneqq \, Df(0)$ echt negativ ist, d.h., für ein geeignetes $\Lambda > 0$ gilt die Abschätzung 

```{math}
\mathcal{Re}(\lambda_i)< -\Lambda, \quad \text{für } i=1,\ldots,n. 
```

Dann gibt es analog zum Beweis von {prf:ref}`thm:stablin` eine Konstante $c>0$, so dass gilt

```{math}
:label: eq:normexp

\|e^{At}\| \leq c\cdot e^{-\Lambda t}\quad \forall t\in \R^+_0.
```

Hierbei haben wir ausgenutzt, dass wir die Konstante $\epsilon > 0$ in {eq}`eq:abschaetzungew` so klein wählen können, dass $\gamma + \epsilon < -\Lambda$ gilt.


Wir können nun einen Radius $r\in (0,{r^\ast})$ bestimmen, so dass die folgende Abschätzung gilt

```{math}
:label: eq:residuum

\|R(x)\| \leq \frac{\Lambda}{2c} \|x\|, \quad \forall \|x\| \leq r.
```

Dies liegt an der totalen Differenzierbarkeit des Vektorfelds $F$ in der Ruhelage (vgl. Kapitel 6.2 in {cite:p}`tenbrinck_2021`), denn dies bedeutet, dass das Residuum in der Nähe der Ruhelage schnell genug gegen Null konvergiert, so dass gilt

```{math}
\lim_{x\to 0} \frac{\|R(x)\|}{\|x\|} = \lim_{x\to 0}\frac{\|F(x)- (DF)(0)\cdot x\|}{\|x\|} = 0.
```

Wir wollen im Folgenden zeigen, dass wenn der Anfangswert unserer unbekannten Lösung des Differentialgleichungssystems beschränkt ist durch

```{math}
\|x(0)\| \leq \epsilon <\frac{r}{c},
```

dann soll schon für die Norm der Lösung für beliebiges $t \geq 0$ gelten
```{math}
\|x(t)\| \leq c\epsilon e^{-\frac{\Lambda t}{2}}.
```

Da $c\epsilon e^{- \frac{\Lambda t}{2}} \leq c\epsilon < r <\tilde{r}$ gilt, liegt die Lösung somit noch in der offenen Kugel $B_{{r^\ast}}(0) \subset U$ und konvergiert für $t \rightarrow \infty$ gegen 0, was den Satz beweist.

Nehmen wir also an, dass $\|x(0)\| \leq \epsilon <\frac{r}{c}$ gelte.
Nun können wir nach {prf:ref}`lem:intexpglgn` die unbekannte Lösung durch ihre Linearisierung darstellen als

```{math}
x(t) = e^{At}x_0 + \int_0^t e^{A(t-s)} R(x(s))\, \mathrm{d}s.
```

Nehmen wir also die Norm der unbekannten Lösung in dieser Darstellung und nutzen die Abschätzungen {eq}`eq:normexp` und {eq}`eq:residuum`, so erhalten wir 

```{math}
\|x(t)\|\leq ce^{-\Lambda t}\|x_0\| + \int_0^tce^{-\Lambda (t-s)}\frac{\Lambda}{2c}\|x(s)\|\, \mathrm{d}s, \quad \forall \|x\| \leq r.
```

Multiplizieren wir beide Seiten der Ungleichung mit $e^{\Lambda t}$ und definieren uns eine Hilfsfunktion $f(t):=e^{\Lambda t}\|x(t)\|$, dann erhalten wir

```{math}
f(t)\leq \underbrace{c\|x_0\|}_{=:a} + \int_0^t \underbrace{\frac{\Lambda}{2}}_{=:g(s)} f(s)\, \mathrm{d}s.
```

Für diese Form der Ungleichung bietet es sich an das {prf:ref}`lemma:Gronwall` zur Gronwall-Ungleichung anzuwenden, durch das wir schließlich folgendes Resultat bekommen
```{math}
f(t) \leq c \|x_0\| \exp{\left( \frac{1}{2} \int_0^t \Lambda \, \mathrm{d}s \right) }
\leq c \epsilon e^{\frac{\Lambda}{2} t} \leq r e^{\frac{\Lambda}{2} t}.
```

Durch Multiplikation beider Seiten mit $e^{-\Lambda t}$ führt dies zur finalen Abschätzung

```{math}
 \|x(t)\|\leq re^{-\frac{\Lambda}{2}t}, \quad \forall t\in\R^+_0.
 ```
 
 Wir sehen also ein, dass die unbekannte Lösung für alle nicht-negativen Zeiten in der offenen Kugel $B_r(0) \subset B_{{r^\ast}}(0) \subset U$ enthalten ist und offensichtlich gegen Null konvergiert.
 Damit ist die Ruhelage $0 \in U$ asymptotisch stabil.
````

Folgende Bemerkung geht speziell auf ein Detail des Beweises ein, das eine Aussage zum Konvergenzradius der Lösungen eines dynamisches Systems zulässt.

````{prf:remark} Attraktionsbassin
Der Beweis von {prf:ref}`thm:stabasymallg` liefert zusätzlich die Aussage, dass alle Punkte $x\in U$ im Phasenraum mit 

```{math}
\|x\| < \frac{r}{c}
```

 zu Orbits gehören, die gegen die Ruhelage $0 \in U$ konvergieren.
 Diesen attraktiven Einzugsbereich der Ruhelage nennt man auch das **Attraktionsbassin** der Ruhelage.
````

## Lyapunov-Stabilität von Ruhelagen

Während ein hinreichendes Kriterium für das Vorliegen *asymptotischer Stabilität* die strikte Ungleichung $Re(\lambda_i)<0$ für die Eigenwerte $\lambda_i$ der Jacobi-Matrix war, ist die Situation bezüglich der Lyapunov-Stabilität einer Ruhelage **komplizierter**.
Hierzu wollen wir ein Resultat für den Fall von linearen dynamischen Systemen im Folgenden formulieren.

````{prf:theorem} Lyapunov-Stabilität von Ruhelagen
:label: thm:stablyaplinear

Sei $A\in \R^{n\times n}$ eine Matrix mit den Eigenwerten $\lambda_1,\dots, \lambda_n\in \C$.
Besitzen die Eigenwerte $\lambda_i \in \C, i=1,\ldots,n$ von $A$ einen nicht-positiven Realteil $Re(\lambda_i) \leq 0$, und ist im Fall $Re(\lambda_i)=0$ die geometrische Vielfachheit gleich der algebraischen Vielfachheit des Eigenwerts, dann ist $0\in \R^n$ eine **Lyapunov-stabile** Ruhelage des dynamischen Systems, dass durch das lineare Differentialgleichungssystem

```{math}
\dot{x}(t) = Ax(t), \quad  \forall t \in I \subset \R^+_0
```

charakterisiert wird.
````

````{prf:proof}
Aus {prf:ref}`thm:stablin` wissen wir bereits, dass im Fall eines linearen dynamischen Systems $\vec{0} \in U$ eine Ruhelage im Phasenraum $U \subset \R^n$ ist.
Seien $\lambda_1, \ldots, \lambda_k \in \C$ für $k \leq n$ die paarweise verschiedenen Eigenwerte der Matrix $A$. 
Wir betrachten wieder die Jordansche Normalform $J = S^{-1}AS$ der Matrix $A$ für Transformationsmatrizen $S,S^{-1} \in \C^{n \times n}$ und 

```{math}
J=
\begin{pmatrix}
J_{r_1}(\lambda_1)& & & 0\\
 & J_{r_2}(\lambda_2) & & \\
 & & \ddots & \\
 0 & & & J_{r_k}(\lambda_k)
\end{pmatrix}.
```

Hierbei bezeichnen $r_i \in \N, i=1,\ldots, k$ die algebraischen Vielfachheiten der zugehörigen Eigenwerte und jeder Jordanblock (vgl. Kapitel 2.7 in {cite:p}`tenbrinck_2021`)) hat die Gestalt

```{math}
 J_r(\lambda) \ \coloneqq \ \begin{pmatrix}
\lambda & 1 & & 0\\
 & \ddots & \ddots & \\
 & & \ddots & 1\\
 0 & & & \lambda
 \end{pmatrix} \in \C^{r\times r}
```

Mit den Rechenregeln für das Matrixexponential aus {prf:ref}`rem:matrixexponentialregeln` folgt

```{math}
e^{Jt} = \begin{pmatrix}
\exp{(J_{r_1}(\lambda_1)t)} & & 0\\
 & \ddots & \\
 0& & \exp{(J_{r_k}(\lambda_k)t)}
 \end{pmatrix}.
```

Betrachten wir nun die Norm der Lösungen des homogenen, linearen Differentialgleichungssystems für einen Startwert $x_0 \in U$ mit

```{math}
\| \Phi_t(x_0) \| = \|e^{At}x_0\| = \|S^{-1}e^{Jt}S x_0\| \leq \|S^{-1}\| \|e^{Jt}\| \|S\| \|x_0\|,
```

so sehen wir ein, dass die Ruhelage $\vec{0} \in U$ **Lyapunov-stabil** ist wenn für alle Jordanblöcke $J_{r_i}(\lambda_i), i=1,\ldots,k$ von $J$ der Ursprung $0\in \C^{r_i}$ eine Lyapunov-stabile Ruhelage des folgenden linearen Differentialgleichungssystems ist

```{math}
 \dot{y}(t) = J_{r_i}(\lambda_i) y(t), \quad t \in I \subset \R^+_0.
```

Dies ist bereits gegeben falls für einen Eigenwert $Re(\lambda_i)<0$ gilt, denn damit folgt aus {prf:ref}`thm:stablin` sogar schon **asymptotische Stabilität**, welche Lyapunov-Stabilität induziert.

Betrachten wir also nun einen komplexen Eigenwert $\lambda_i \in \C$ von $A$ mit $Re(\lambda_i)=0$ und für den die geometrische Vielfachheit nach Vorraussetzung gleich der algebraischen Vielfachheit ist.
In diesem Fall ist der ihm zugeordnete Jordanblock eine Diagonalmatrix auf deren Hauptdiagonale der Eigenwert $\lambda_i \in \C$ steht, da alle Jordankästchen eindimensional sind. 
In diesem Fall sehen wir, dass die Norm des Matrixexponentials beschränkt ist und wir dadurch **Lyapunov-Stabilität** der Ruhelage gezeigt haben, da gilt
```{math}
\|e^{J_{r_i}(\lambda_i)t)}\| = |e^{\lambda_i t}| = |e^0e^{\mathcal{Im}(\lambda_i) t}| = |\cos{(\mathcal{Im}(\lambda_i)t)} + i \sin{(\mathcal{Im}(\lambda_i)t)}| = 1.
```
Für diese Umformung haben wir die Definition der komplexen Exponentialfunktion genutzt, für die gilt:

```{math}
e^z = e^{x+iy} = e^xe^iy = e^x(\cos(y) + i\sin(y)), \quad \text{für } z = x+iy \in \C.
```

````

Das folgende Beispiel illustriert, dass eine Ruhelage instabil werden kann, wenn die geometrische Vielfachheit nicht mit der algebraischen Vielfachheit übereinstimmt für einen Eigenwert $\lambda =0$ der Koeffizientenmatrix $A$.

````{prf:example}
Sei $U \subset \R^2$ der Phasenraum und wir betrachten das homogene, lineare Differentialgleichungssystem

```{math}
\dot{x}(t) = A x(t), \quad \forall t \in \R_0^+
```

für eine Koeffizientenmatrix

```{math}
A = \begin{pmatrix} 0&1\\0&0\end{pmatrix}.
```

Wie man leicht nachrechnet besitzt diese Matrix den Eigenwert $\lambda = 0$ mit algebraischer Vielfachheit $2$ und geometrischer Vielfachheit $1$ zum Eigenvektor $v = (1,0)^T \in \R^2$.
Die Vielfachheiten des Eigenwert **stimmen** also **nicht überein**.

Aus {prf:ref}`thm:stablin` wissen wir, dass eine Ruhelage in $\vec{0} \in \R^2$ existiert.
Man sieht jedoch leicht ein, dass sogar jeder Punkt $x_0 = (y, 0) \in U$ eine Ruhelage des Systems darstellt, da diese Punkte ein Vielfaches des Eigenvektors zum Eigenwert $\lambda = 0$ darstellen und somit im Kern der Matrix $A$ liegen, d.h., für diese Punkte ist die rechte Seite des Differentialgleichungssystems $\vec{0} \in \R^2$ und somit liegt eine Ruhelage vor.

Wir wollen die Stabilität dieser Ruhelagen im Folgenden untersuchen.
Hierzu betrachten wir die Norm des Phasenflusses $\Phi \colon I \times U \rightarrow U$, der für einen gegebenen Anfangswert $x_0 = (y,z) \in U$ mit $z \neq 0$ der die Lösung des Differentialgleichungssystems beschreibt mit

```{math}
\| \Phi_t(x_0) \| &= \| e^{At}x_0 \| = \| \sum_{k=0}^\infty \frac{(At)^k}{k!} x_0\| = \| [\underbrace{(At)^0}_{=I_2} + (At)^1] x_0\| \\
&= \| \begin{pmatrix} 1 & t \\ 0 & 1\end{pmatrix}\begin{pmatrix} y \\ z \end{pmatrix} \| = \| \begin{pmatrix} y + tz \\ z\end{pmatrix} \| \overset{t\to \infty}{\longrightarrow} \infty.
```

Wir sehen also, dass für jeden Anfangswert $x_0 = (y,z)$ mit $z \neq 0$ die Lösung des Differentialgleichungssystems divergiert und somit ist jede Ruhelage des dynamischen Systems **instabil**.
````

Leider kann man nicht wie im Fall der asymptotischen Stabilität vom linearen auf den nichtlinearen Fall schließen, wie das folgende Beispiel zeigt.

````{prf:example}
Wir betrachten eine gewöhnliche Differentialgleichung 1. Ordnung der Form

```{math}
\dot{x}(t) = \alpha x(t) + \beta x^3(t), \forall t \in \R^+_0.
```

mit freien Parametern $\alpha, \beta \in \R$.

Wie man einsieht ist $0$ eine Ruhelage des dynamischen Systems, das durch diese Differentialgleichung charakterisiert wird.
Wir betrachten die Linearisierung der Differentialgleichung in der Ruhelage mit $A := (DF)(0) = \alpha$ und erhalten

```{math}
\dot{x}(t) = A x(t) = \alpha x(t), \quad \forall t \in \R^+_0.
```
 
Folgende Fallunterscheidung zeigt nun das Stabilitätsverhalten der Ruhelage in Abhängigkeit der gewählten Parameter $\alpha, \beta \in \R$:
|            | linearisierte Gleichung | nicht lineare Gleichung |
| :--------- |:------------------------|:----------------------- |
| $\alpha<0$ | asymptotisch stabil     | asymptotisch stabil     |
| $\alpha>0$ | instabil                | instabil |
| $\alpha=0$ | Lyapunov-stabil         | asymptotisch stabil für $\beta<0$ |
|            |                         | stabil für $\beta =0 $            | 
|            |                         | instabil $\beta > 0$               |

Wie man sieht hängt die Stabilität im nichtlinearen Fall nicht nur vom Parameter $\alpha$, sondern ebenfalls von $\beta$ ab, was eine Stabilitätsanalyse deutlich komplizierter macht.

````
