# Wiederholung: Gewöhnliche Differentialgleichungen

In diesem Abschnitt werden wir kurz die wichtigsten Definitionen und Ergebnisse zu gewöhnlichen Differentialgleichungen aus Kapitel 8 in {cite:p}`tenbrinck_2021` wiederholen und um neue Begriffe erweitern, mit denen wir die Theorie dynamischer Systeme mathematisch untersuchen können.

## Gewöhnliche Differentialgleichungen

Wir erinnern uns zunächst an die Definition eines gewöhnlichen Differentialgleichungssystems $m$-ter Ordnung als Grundlage für unsere weiteren Betrachtungen.

````{prf:definition} Gewöhnliches Differentialgleichungssystem
:label: def:DGL

Seien $n,m \in \N$.
Wir betrachten im Folgenden eine offene Teilmenge $U\subset (\R^n)^{m+1}$ und ein offenes Intervall $I\subset\R$. 
Es sei außerdem $F:I\times U\rightarrow\R^n$ eine stetige Funktion, dann nennen wir

```{math}
:label: eq:DGL
F(t,x(t),x'(t),\ldots,x^{(m)}(t)) = 0
```

ein **gewöhnliches Differentialgleichungssystem (DGL)** $m$-ter Ordnung von $n$ Gleichungen.
Gilt $n=1$, das heißt die Funktion $F$ ist skalarwertig, so sprechen wir von einer **gewöhnlichen Differentialgleichung**.

Eine Funktion $\phi\in C^m(I;\R^n)$ heißt **Lösung des Differentialgleichungssystems**, falls gilt,

```{math}
F(t, \phi(t), \phi'(t), \ldots, \phi^{(m)}(t)) = 0 \quad \forall t\in I.
```

Wenn wir die DGL nach der höchsten auftauchenden Ableitung auflösen können, so dass sie die folgende Form hat

```{math}
x^{(m)}(t) = F(t,x(t),x'(t),\ldots,x^{(m-1)}(t)),
```

so nennen wir die DGL **explizit**, ansonsten wird sie **implizit** genannt.
````

Folgende Bemerkung beschreibt eine alternative Notation von gewöhnlichen Differentialgleichungen 1. und 2. Ordnung, die häufig in der Literatur im Kontext dynamischer Systeme auftaucht.

````{prf:remark} Zeitableitungen bei gewöhnlichen Differentialgleichungen
Viele physikalische Phänomene können durch zeitabhängige gewöhnliche Differentialgleichungen 1. und 2. Ordnung beschrieben werden.
In diesen Fällen verwendet man häufig die Variable $t \in \R^+_0$ als unabhängige Variable anstatt einer Variable $x \in \R$.
Auch ändert sich häufig die Notation der Zeitableitungen der gesuchten Funktion $x$, so dass folgende Korrespondenz für die ersten beiden Ableitungen entsteht:
1. $x'(t) \ \ \hat{=} \ \ \dot{x}(t)$,
2. $x''(t) \ \ \hat{=} \ \ \ddot{x}(t)$.

Damit lässt sich das gewöhnliche Differentialgleichungssystem aus {eq}`eq:DGL` schreiben als

```{math}
:label: eq:DGLtime
F(t, x(t), \dot{x}(t), \ldots, x{(m)}(t)) = 0 \quad \forall t\in I.
```

````

## Autonome Differentialgleichungen

Im Fall von dynamischen Systemen erhält der Definitionsbereich der Funktion $F$ einer gewöhnlichen Differentialgleichung einen besonderen Namen, wie die folgende Bemerkung erklärt.

````{prf:remark} (Erweiterter) Phasenraum
Wird eine gewöhnliche Differentialgleichung als mathematisches Modell für ein kontinuierliches dynamisches System genutzt, so wird die offene Menge $U\subset (\R^n)^{m+1}$ auch als **Phasenraum** bezeichnet. 
Der Definitionsbereich $I\times U$ der stetigen Funktion $F$ wird auch als **erweiterter Phasenraum** bezeichnet.

Der Phasenraum beschreibt die Menge aller möglichen Zustände des dynamischen Systems.
Jeder Punkt des Phasenraums wird hierbei eindeutig einem Zustand des Systems zugeordnet.

In Kapitel {ref}`s:fluesse` werden wir spezielle Diagramme basierend auf dem Begriff des erweiterten Phasenraum betrachten (auch Phasenportraits genannt), um Lösungen von dynamischen Systemen mathematisch zu charakterisieren.
````

Im Fall von **kontinuierlichen dynamischen Systemen** spielt eine Familie von gewöhnlichen Differentialgleichungen eine wichtige Rolle, die wir im Folgenden definieren wollen.
Diese zeichnen sich dadurch aus, dass die Funktion $F$ in {eq}`eq:DGLtime` nicht explizit von der Zeit abhängt.

````{prf:definition} Autonome DGL
Hängt die Funktion $F$ in {prf:ref}`def:DGL` nicht explizit von der Zeit ab, d.h., wir haben $F:U\rightarrow\R^n$ dann heißt die Gleichung

```{math}
:label: eq:autonomeDGL
F(x(t), x'(t), \ldots, x^{(m)}(t)) = 0 \quad \forall t\in I
```

**autonome DGL**.

````

Im folgenden Beispiel wollen wir unterschiedliche gewöhnliche Differentialgleichungen darauf prüfen, ob sie autonom sind.

````{prf:example} Autonome Differentialgleichungen
Wir betrachten drei verschiedene gewöhnliche Differentialgleichungen und untersuchen diese auf ihre Zeitabhängigkeit.
Der Einfachheit-halber konzentrieren wir uns hierbei auf gewöhnliche Differentialgleichungen 1. Ordnung.
Sei hierzu  im Folgenden $I \subset \R$ ein offenes Intervall. 

1\. Die gewöhnliche Differentialgleichung

```{math}
2x'(t) = x(t)\cdot t \quad \forall t \in I
```

ist **nicht autonom**, da die rechte Seite der Gleichung durch die Funktion

```{math}
F(t,x(t)) = x(t) \cdot x
```

beschrieben wird und diese Funktion explizit vom Funktionsargument $t \in I$ abhängt.

<br />

2\. Die gewöhnliche Differentialgleichung

```{math}
2t\cdot \dot{x}(t) = x(t)\cdot t \quad \forall t \in I
```

ist hingegen **autonom**, da die Gleichung in folgende explizite Form überführt werden kann

```{math}
\dot{x}(t) = \frac{1}{2} x(t) \quad \forall t \in I
```

und somit die rechte Seite der Gleichung durch die Funktion 

```{math}
F(t,x(t)) = \frac{1}{2}x(t)
```

beschrieben wird, welche nicht explizit vom Funktionsargument $t \in I$ abhängt.

<br />

3\. Im Fall der gewöhnlichen Differentialgleichung

```{math}
2x'(t) = x(t)\cdot \sin(g(t)) \quad \forall t \in I
```

können wir für beliebige Funktionen $g \colon I \rightarrow \R$ **nicht entscheiden**, ob sie autonom ist wenn keine konkrete Form der Funktion $g$ gegeben ist.
````

## Anfangswertprobleme

Um gewöhnliche Differentialgleichungen zu lösen, betrachtet man in der Regel sogenannte Anfangswertprobleme.
Hierbei wählt man einen ausgezeichneten Zeitpunkt $t_0\in I$ aus dem Zeitintervall $I$, an welchem man die Lösung explizit durch einen Anfangswert $x_0\in U$ vorgibt.
Dieses Vorgehen wird in der folgenden Definition nochmal kurz wiederholt.

````{prf:definition}
:label: def:anfangswertproblem
Sei ein gewöhnliches Differentialgleichungssystem 1. Ordnung wie in {prf:ref}`def:DGL` gegeben, wobei $I \times U \subset \R_0^+ \times \R^n$ den erweiterten Phasenraum des Systems bezeichnet.
Sei außerdem $t_0 \in I$ ein Anfangszeitpunkt und $x_0 \in U$ der zugehörige Anfangszustand.

Dann nennen wir das Gleichungssystem

```{math}
:label: eq:AWP
\dot{x}(t) &= F(t, x(t))\quad\forall t\in I, \\
x(t_0) &= x_0
```

**Anfangswertproblem** des gewöhnlichen Differentialgleichungssystems. 
Sofern nicht explizit angegeben werden wir im Folgenden annehmen, dass ohne Beschränkung der Allgemeinheit $t_0=0$ gilt.
````

Die explizite Wahl des Anfangszeitpunkts und -zustands erlaubt es erst eine gewöhnliche Differentialgleichung eindeutig zu lösen.
Ohne diese zusätzlichen Informationen könnte man lediglich Funktionenscharen als Lösungsmenge angeben.
Dies wird durch das folgende Beispiel nochmal dargestellt.

````{prf:example}
Wir betrachten eine sehr einfache gewöhnliche Differentialgleichung erster Ordnung, die sich explizit in folgender Form schreiben lässt:

```{math}
x'(t) = x(t) \quad \forall t \in \R.
```

Man sieht leicht ein, dass Lösungen dieser Differentialgleichung Funktionen $x \colon \R \rightarrow \R$ von der Form

```{math}
x(t) = c\cdot e^t
```

für eine beliebige Konstante $c \in \R$ sein müssen.
Um diese Funktionenschar weiter einzuschränken und eine eindeutige Lösung zu erhalten, müssen wir noch Anfangswertbedindungen hinzunehmen.
Hierzu reicht es eine ausgewiesene Stelle $t_0 \in \R$ und einen Funktionswert $x_0 = x(t_0)$ festzulegen.

Wählen wir beispielsweise $t_0 = 0$ und $x_0 = x(0) = 2$, so erhalten wir als eindeutige Lösung der gewöhnlichen Differentialgleichung die Funktion

```{math}
x(t) = 2\cdot e^t.
```

Wir sehen also, dass durch das Festlegen eines Anfangswert die unbekannte Konstante $c \in \R$ als $c=2$ eindeutig bestimmt wurde.
````

## Existenz und Eindeutigkeit einer Lösung

Nicht jede gewöhnliche Differentialgleichung ist im Allgemeinen lösbar oder besitzt eindeutige Lösungen, wie das folgende Beispiel belegt.

````{prf:example}
Wir wollen im folgenden zwei Beispiele von autonomen, gewöhnlichen Differentialgleichungen erster Ordnung diskutieren, für die entweder die Existenz oder die Eindeutigkeit von Lösungen nicht gegeben ist.

1\. Die gewöhnliche Differentialgleichung

```{math}
e^{x'(t)} \equiv 0 \quad \forall t \in \R
```

besitzt keine Lösung, da die Exponentialfunktion strikt positiv ist und es somit keine Funktion $y \colon \R \rightarrow \R$ gibt, so dass die obige Gleichung erfüllt werden kann.

2\. Die gewöhnliche Differentialgleichung

```{math}
x'(t)(1-x'(t)) \equiv 0 \quad \forall t \in \R
```

besitzt auf Grund ihrer Symmetrieeigenschaften zwei unterschiedliche Funktionenscharen als Lösung, nämlich

```{math}
x_1(t) = c \quad \text{ und } \quad x_2(t) = t + c \quad \forall t \in \R,
```

wobei $c \in \R$ eine beliebige Konstante darstellt.
````

Die wichtigste Eigenschaft für die Existenz und Eindeutigkeit von Lösungen gewöhnlicher Differentialgleichungen ist die **(lokale) Lipschitzstetigkeit** der rechten Seite $F \colon I \times U \rightarrow U$.
Diese wollen wir der Vollständigkeit halber im Folgenden definieren.

```{margin} Rudolf Lipschitz
[Rudolf Otto Sigismund Lipschitz](https://de.wikipedia.org/wiki/Rudolf_Lipschitz) (Geboren 14. Mai 1832 in Königsberg i. Pr.; Gestorben 7. Oktober 1903 in Bonn) war ein deutscher Mathematiker und Hochschullehrer. Er betreute die Doktorarbeit von [Felix Klein](https://en.wikipedia.org/wiki/Felix_Klein), weswegen der österreichische Mathematiker [Martin Burger](https://www.math.fau.de/angewandte-mathematik-1/mitarbeiter/prof-dr-martin-burger/) in direkter Linie im akademischen Stammbaum von Lipschitz abstammt, siehe [Mathematics Genealogy Project](https://genealogy.math.ndsu.nodak.edu/index.php).
```

````{prf:definition} (Lokale) Lipschitzstetigkeit
Sei $F \colon G \to \R^n$ eine Funktion mit dem erweiterten Phasenraum $G \, \coloneqq \, I \times U \subset \R\times\R^n$.
Man sagt, dass $F$ in $G$ einer **globalen Lipschitz-Bedingung** genügt (bezüglich der Variablen $x \in U$) mit der Lipschitz-Konstanten $L\geq0$, wenn gilt

```{math}
\Vert F(t,x) - F(t,\widetilde{x}) \Vert \leq L \Vert x-\widetilde{x}\Vert\quad\text{ für alle }(t,x), (t,\widetilde{x})\in G\,.
```

Man sagt, $F$ genüge in $G$ einer **lokalen Lipschitz-Bedingung**, falls jeder Punkt $(t,x)\in G$ im erweiterten Phasenraum eine Umgebung $V$ besitzt, sodass $F$ in $G\cap V$ einer Lipschitzbedingung mit einer gewissen (von $V$ abhängigen) Konstanten $L\in\R_0^+$ genügt.
````

Für die **(lokale) Existenz von Lösungen** haben wir in Kapitel 8.4 {cite:p}`tenbrinck_2021` den Satz von Picard-Lindelöf formuliert, den wir im Folgenden wiederholen werden.

````{prf:theorem} Lokaler Existenzsatz nach Picard--Lindelöf
<<<<<<< HEAD
:label: satz:picardlindeloef_lokal
Sei $F\colon G\to\R^n$ eine stetige Funktion mit erweitertem Phasenraum $G \coloneqq I \times U \subset \R\times\R^n$, die lokal Lipschitz-stetig auf $G$ bezüglich der $y$-Variablen ist.
Dann existiert zu jedem Anfangswert $(t_0,y_0) \in G$ ein $\varepsilon>0$, sowie genau eine Lösung
=======
:label: thm:piclindlokal

Sei $F\colon G\to\R^n$ eine stetige Funktion mit erweitertem Phasenraum $G \coloneqq I \times U \subset \R\times\R^n$, die lokal Lipschitz-stetig auf $G$ bezüglich der $x$-Variablen ist.
Dann existiert zu jedem Anfangswert $(t_0,x_0) \in G$ ein $\varepsilon>0$, sowie genau eine Lösung
>>>>>>> main

```{math}
\phi \colon \left[t_0-\varepsilon, t_0+\varepsilon\right] \to \R^n
```

der gewöhnlichen Differentialgleichung 

```{math}
\dot{x}(t) \ = \ F(t,x(t))
```

unter der Anfangsbedingung $\phi(t_0)=x_0$.
````

```{margin} Ernst Lindelöf
[Ernst Leonard Lindelöf](https://en.wikipedia.org/wiki/Ernst_Leonard_Lindel%C3%B6f) (Geboren 7. März 1870 in Helsingfors (Helsinki), Großfürstentum Finnland; Gestorben 4. Juni 1946 in Helsinki) war ein finnischer Mathematiker.
```

```{margin} Émile Picard
[Charles Émile Picard](https://de.wikipedia.org/wiki/%C3%89mile_Picard) (Geboren 24. Juli 1856 in Paris; Gestorben 11. Dezember 1941 ebenda) war ein französischer Mathematiker.
```

````{prf:proof}
Siehe Kapitel 12, Satz 4 Kapitel 8.4 {cite:p}`forster_2017`
````

Bisher haben wir nur die Existenz und Eindeutigkeit von Lösungen gewöhnlicher Differentialgleichungen in lokalen Intervallen betrachtet.
Unter den strengeren Voraussetzungen einer rechten Seite $F$ der gewöhnlichen Differentialgleichung, die einer globalen Lipschitzbedingung genügt, lässt sich jedoch eine **globale Existenzaussage** formulieren, die besonders für konkrete Anwendungen sehr praktisch ist.

````{prf:theorem} Globaler Existenzsatz nach Picard-Lindelöf
:label: satz:picardlindeloef
Sei $F\colon G\to\R^n$ eine stetige Funktion mit erweitertem Phasenraum $G \, \coloneqq \, I \times U \subset \R\times\R^n$, die eine globale Lipschitzbedingung auf $G$ bezüglich der $x$-Variablen erfüllt.
Dann existiert zu jedem Anfangswert $(t_0,x_0) \in G$ eine globale Lösung

```{math}
\phi \colon I \to \R^n
```

der gewöhnlichen Differentialgleichung 

```{math}
\dot{x}(t) \ = \ F(t,x(t))
```

unter der Anfangsbedingung $\phi(t_0)=x_0$.
Es existieren außerdem keine weiteren (lokalen) Lösungen.
````

````{prf:proof}
Siehe Kapitel 2.3 {cite:p}`knabner_2013`
````

````{prf:corollary}
:label: cor:eindeutigkeitlinear
Das Anfangswertproblem jedes **linearen** gewöhnlichen Differentialgleichungssystems 1. Ordnung hat eine eindeutige globale Lösung.
````

````{prf:proof}
Siehe Theorem 2.25, Kapitel 2.3 {cite:p}`knabner_2013`
````

(s:lineare_dglsysteme)=
## Lösungen von linearen Differentialgleichungssystemen

Analog zu Kapitel 8 in {cite:p}`tenbrinck_2021` wollen wir uns mit Lösungen für **homogene lineare Differentialgleichungen** beschäftigen, jedoch dieses Mal nicht im skalaren Fall $n=1$, sondern für ein Anfangswertproblem von der Form

```{math}
:label: eq:linhomdglsystem

\dot{x}(t) &= A x(t), \quad \forall t \in I \subset \R^+_0, \\
x(t_0) &= x_0 \in U \subset \R^n.
```

Wir bemerken hierbei, dass im Gegensatz zum skalaren Fall hier die Koeffizientenmatrix $A \in \C^{n\times n}$ nicht von der Zeit abhängt, wir also ein autonomes Differentialgleichungssystem betrachten.

Bevor wir Lösungen von {eq}`eq:linhomdglsystem` angeben, wollen wir ein hilfreiches Funktionalkalkül einführen, dass die Notation im Fall von Differentialgleichungssystemen erleichtert.

````{prf:definition} Matrixexponential
Sei $n \in \N$ und $A \in \C^{n \times n}$ eine beliebige quadratische Matrix. 
Das **Matrixexponential** $e^A$ von $A$, ist diejenige $n\times n$-Matrix, welche durch die folgende Potenzreihe definiert ist:

```{math}
e^A \equiv \exp(A) \ \coloneqq \ \sum_{k=0}^\infty \frac{A^k}{k!} = I_n + A + \frac{A^2}{2} + \frac{A^3}{6} + \ldots.
```

Analog zur gewöhnlichen Exponentialfunktion konvergiert die Reihe für alle $A \in \C^{n \times n}$, woraus die Wohldefiniertheit der Definition folgt.
Für den Spezialfall $n=1$ entspricht das Matrixexponential der gewöhnlichen Exponentialfunktion.
````

````{prf:remark} Rechenregeln für das Matrixexponential
:label: rem:matrixexponentialregeln

Für das Matrixexponential gelten die gleichen Rechenregeln wie für die gewöhnliche Exponentialfunktion, wie zum Beispiel:

* $e^{tA}e^{sA} = e^{(t+s)A}, \quad$ für $s,t \in \R$

* $\frac{d}{dt} e^{tA} = Ae^{tA}, \quad$ für $t \in \R$

* $ e^{D} = \operatorname{diag}(e^{a_1}, \ldots, e^{a_n})$ ist Diagonalmatrix für eine Diagonalmatrix $D = \operatorname{diag}(a_1, \ldots, a_n)$.
````

Folgendes Lemma stellt einen interessanten Zusammenhang des Matrixexponentials zur Spektraltheorie her.

````{prf:lemma} Eigenwerte des Matrixexponentials
:label: lem:mpotew

Sei $A \in \C^{n\times n}$ eine beliebige quadratische Matrix und sei $\lambda \in \C$ ein Eigenwert von $A$ zum
Eigenvektor $v \in \C^n$.
Dann ist der Vektor $v$ auch Eigenvektor des Matrixexponentials $e^A$ zum zugehörigen Eigenwert $e^\lambda$.
````

````{prf:proof}
In der Hausaufgabe zu zeigen.
````

Mit Hilfe des Matrixexponentials lässt sich die Lösung des homogenen linearen Differentialgleichungssystems {eq}`eq:linhomdglsystem` kompakt angeben, wie uns folgendes Lemma zeigt.

````{prf:lemma}
Sei $n\in \N$, $I \subset \R^+_0$ und $A \in \C^{n\times n}$ eine beliebige quadratische Matrix.
Das Anfangswertproblem {eq}`eq:linhomdglsystem` hat die eindeutige Lösung

```{math}
x(t) = e^{A(t-t_0)}x_0, \quad \forall t \in I.
```
````

````{prf:proof}
Wir zeigen zunächst, dass die Lösung $x(t)$ die Anfangswertbedingung erfüllt:

```{math}
x(t_0) = e^{A(t_0-t_0)}x_0 = e^0x_0 = I_n x_0.
```

Um zu zeigen, dass $x(t)$ das lineare homogene Differentialgleichungssystem {eq}`eq:linhomdglsystem` löst, berechnen wir die entsprechende Zeitableitung als

```{math}
\dot{x}(t) = \frac{d}{dt}(e^{A(t-t_0)}x_0) = A \cdot e^{A(t-t_0)}x_0 = A x(t), \quad \forall t \in I.
```

Vergleichen wir die linke und rechte Seite dieser Gleichung so erkennen wir, dass $x(t)$ in der Tat eine Lösung des Differentialgleichungssystems ist.

Nach {prf:ref}`cor:eindeutigkeitlinear` ist die Lösung eindeutig, da es sich um ein lineares Differentialgleichungssystem 1. Ordnung handelt.
````

Im Allgemeinen kann man bei linearen Differentialgleichungssystemen nicht davon ausgehen, dass diese in der einfachsten Form wie in {eq}`eq:linhomdglsystem` vorliegen.
Außerdem ist die konkrete Berechnung des Matrixexponentials zur Bestimmung einer Lösungsfunktion $x(t)$ in der Regel ungeeignet.
Hierzu wollen wir die abschließende Bemerkung machen.

````{prf:remark}
1\. Zur Berechnung einer konkreten Lösung $x(t)$ des linearen homogenen Differentialgleichungssystems {eq}`eq:linhomdglsystem` bietet es sich an, die **Jordansche Normalform** $J = SAS^{-1}$ von $A$ aus Kapitel 2.7 in {cite:p}`tenbrinck_2021` auszunutzen, da für diese das Matrixexponential wie folgt berechnet werden kann:

```{math}
e^{tA} &=  \sum_{k=0}^\infty \frac{(t A)^k}{k!} = \sum_{k=0}^\infty \frac{(tS^{-1}JS)^k}{k!} 
\\&= 
S^{-1} \sum_{k=0}^\infty \frac{(tJ)^k}{k!} S = S^{-1} e^{tJ}S 
\\&= S^{-1} e^{t(D+N)}S = S^{-1} e^{tD} e^{tN} S
```

für eine Transformationsmatrix $S \in \C^{n \times n}$, eine Diagonalmatrix $D \in \C^{n \times n}$ mit den Eigenwerten von $A$ und einer nilpotenten Matrix $N \in \C^{n \times n}$, für die die Reihendarstellung des zugehörigen Matrixexponentials nach endlich vielen Summanden (entsprechend dem Nilpotenzindex von $N$) abbricht.

2\. Ist das vorliegende lineare Differentialgleichungssystem **inhomogen**, das heißt für eine stetige Störfunktion $b \colon I \rightarrow \R^n$ von der Form

```{math}
:label: eq:lininhomdglsystem

\dot{x}(t) &= A x(t) + b(t), \quad \forall t \in I \subset \R^+_0, \\
x(t_0) &= x_0 \in U \subset \R^n,
```

so lässt sich über die Variation der Konstanten aus Kapitel 8.2 in {cite:p}`tenbrinck_2021` eine eindeutige Lösung des Anfangswertproblems {eq}`eq:lininhomdglsystem` angeben als

```{math}
x(t) = e^{tA}x_0 + \int_0^t e^{(t-s)A}b(s) \, \mathrm{d}s.
```

3\. Im Falle eines homogenen, linearen Differentialgleichungssystems, das **nicht autonom** ist, das heißt die Koeffizientenmatrix $A = A(t)$ ist zeitabhängig, können wir nicht mehr die Spektraltheorie zur konkreten Berechnung von Lösungen nutzen.
Formal lassen sich dennoch Lösungen als sogenanntes **zeitgeordnetes Produkt** angeben, was jedoch den Rahmen dieser Vorlesung sprengen würde.
````
