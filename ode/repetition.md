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
F(x,y(x),y'(x),\ldots,y^{(m)}(x)) = 0
```

ein **gewöhnliches Differentialgleichungssystem (DGL)** $m$-ter Ordnung von $n$ Gleichungen.
Gilt $n=1$, das heißt die Funktion $F$ ist skalarwertig, so sprechen wir von einer **gewöhnlichen Differentialgleichung**.

Eine Funktion $\phi\in C^m(I;\R^n)$ heißt **Lösung des Differentialgleichungssystems**, falls gilt,

```{math}
F(x, \phi(x), \phi'(x), \ldots, \phi^{(m)}(x)) = 0 \quad \forall x\in I.
```

Wenn wir die DGL nach der höchsten auftauchenden Ableitung auflösen können, so dass sie die folgende Form hat

```{math}
y^{(m)}(x) = F(x,y(x),y'(x),\ldots,y^{(m-1)}(x)),
```

so nennen wir die DGL **explizit**, ansonsten wird sie **implizit** genannt.
````

Folgende Bemerkung beschreibt eine alternative Notation von gewöhnlichen Differentialgleichungen 1. und 2. Ordnung, die häufig in der Literatur im Kontext dynamischer Systeme auftaucht.
````{prf:remark} Zeitableitungen bei gewöhnlichen Differentialgleichungen
Viele physikalische Phänomene können durch zeitabhängige gewöhnliche Differentialgleichungen 1. und 2. Ordnung beschrieben werden.
In diesen Fällen verwendet man häufig die Variable $t \in \R^+_0$ als unabhängige Variable anstatt einer Variable $x \in \R$.
Auch ändert sich häufig die Notation der Zeitableitungen der gesuchten Funktion $y$, so dass folgende Korrespondenz für die ersten beiden Ableitungen entsteht:
1. $y'(x) \ \ \hat{=} \ \ \dot{y}(t)$,
2. $y''(x) \ \ \hat{=} \ \ \ddot{y}(t)$.

Damit lässt sich das gewöhnliche Differentialgleichungssystem aus [](eq:DGL) schreiben als
```{math}
:label: eq:DGL_time
F(z, y(t), \dot{y}(t), \ldots, y{(m)}(t)) = 0 \quad \forall t\in I.
```
````

## Autonome Differentialgleichungen

Im Fall von dynamischen Systemen erhält der Definitionsbereich der Funktion $F$ einer gewöhnlichen Differentialgleichung einen besonderen Namen, wie die folgende Bemerkung erklärt.
````{prf:remark} (Erweiterter) Phasenraum
Wird eine gewöhnliche Differentialgleichung als mathematisches Modell für ein kontinuierliches dynamisches System genutzt, so wird die offene Menge $U\subset (\R^n)^{m+1}$ auch als **Phasenraum** bezeichnet. 
Der Definitionsbereich $I\times U$ der stetigen Funktion $F$ wird auch als **erweiterter Phasenraum** bezeichnet.

Der Phasenraum beschreibt die Menge aller möglichen Zustände des dynamischen Systems.
Jeder Punkt des Phasenraums wird hierbei eindeutig einem Zustand des Systems zugeordnet.

In Kapitel {ref}s:fluesse werden wir spezielle Diagramme basierend auf dem Begriff des erweiterten Phasenraum betrachten (auch Phasenportraits genannt), um Lösungen von dynamischen Systemen mathematisch zu charakterisieren.
````

Im Fall von **kontinuierlichen dynamischen Systemen** spielt eine Familie von gewöhnlichen Differentialgleichungen eine wichtige Rolle, die wir im Folgenden definieren wollen. 
Diese zeichnen sich dadurch aus, dass die Funktion $F$ in [](eq:DGL_time) nicht explizit von der Zeit abhängt.

````{prf:definition} Autonome DGL
Hängt die Funktion $F$ in {prf:ref}`def:DGL` nicht explizit von der Zeit ab, d.h., wir haben $F:U\rightarrow\R^n$ dann heißt die Gleichung

```{math}
:label: eq:autonome_DGL
F(y(x), y'(x), \ldots, y^{(m)}(x)) = 0 \quad \forall t\in I
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
2y'(x) = y(x)\cdot x \quad \forall x \in I
```
ist **nicht autonom**, da die rechte Seite der Gleichung durch die Funktion
```{math}
F(x,y(x)) = y(x) \cdot x
```
beschrieben wird und diese Funktion explizit vom Funktionsargument $x \in I$ abhängt.

<br />

2\. Die gewöhnliche Differentialgleichung
```{math}
2t\cdot \dot{y}(t) = y(t)\cdot t \quad \forall t \in I
```
ist hingegen **autonom**, da die Gleichung in folgende explizite Form überführt werden kann
```{math}
\dot{y}(t) = \frac{1}{2} y(t) \quad \forall t \in I
```
und somit die rechte Seite der Gleichung durch die Funktion 
```{math}
F(t,y(t)) = \frac{1}{2}y(t)
```
beschrieben wird, welche nicht explizit vom Funktionsargument $t \in I$ abhängt.

<br />

3\. Im Fall der gewöhnlichen Differentialgleichung
```{math}
2y'(x) = y(x)\cdot \sin(g(x)) \quad \forall x \in I
```
können wir für beliebige Funktionen $g \colon I \rightarrow \R$ **nicht entscheiden**, ob sie autonom ist wenn keine konkrete Form der Funktion $g$ gegeben ist.
````

## Anfangswertprobleme
Um gewöhnliche Differentialgleichungen zu lösen, betrachtet man in der Regel sogenannte Anfangswertprobleme.
Hierbei wählt man einen ausgezeichneten Zeitpunkt $t_0\in I$ aus dem Zeitintervall $I$, an welchem man die Lösung explizit durch einen Anfangswert $y_0\in U$ vorgibt.
Dieses Vorgehen wird in der folgenden Definition nochmal kurz wiederholt.

````{prf:definition}
:label: def:anfangswertproblem
Sei ein gewöhnliches Differentialgleichungssystem 1. Ordnung wie in {prf:ref}`def:DGL` gegeben, wobei $I \times U \subset \R_0^+ \times \R^n$ den erweiterten Phasenraum des Systems bezeichnet.
Sei außerdem $t_0 \in I$ ein Anfangszeitpunkt und $y_0 \in U$ der zugehörige Anfangszustand.

Dann nennen wir das Gleichungssystem

```{math}
:label: eq:AWP
\dot{y}(t) &= F(t, y(t))\quad\forall t\in I, \\
y(t_0) &= y_0
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
y'(x) = y(x) \quad \forall x \in \R.
```

Man sieht leicht ein, dass Lösungen dieser Differentialgleichung Funktionen $y \colon \R \rightarrow \R$ von der Form

```{math}
y(x) = c\cdot e^x
```

für eine beliebige Konstante $c \in \R$ sein müssen.
Um diese Funktionenschar weiter einzuschränken und eine eindeutige Lösung zu erhalten, müssen wir noch Anfangswertbedindungen hinzunehmen.
Hierzu reicht es eine ausgewiesene Stelle $x_0 \in \R$ und einen Funktionswert $y_0 = y(x_0)$ festzulegen.

Wählen wir beispielsweise $x_0 = 0$ und $y_0 = y(0) = 2$, so erhalten wir als eindeutige Lösung der gewöhnlichen Differentialgleichung die Funktion

```{math}
y(x) = 2\cdot e^x.
```

Wir sehen also, dass durch das Festlegen eines Anfangswert die unbekannte Konstante $c \in \R$ als $c=2$ eindeutig bestimmt wurde.
````

## Existenz und Eindeutigkeit einer Lösung

Nicht jede gewöhnliche Differentialgleichung ist im Allgemeinen lösbar oder besitzt eindeutige Lösungen, wie das folgende Beispiel belegt.
````{prf:example}
Wir wollen im folgenden zwei Beispiele von autonomen, gewöhnlichen Differentialgleichungen erster Ordnung diskutieren, für die entweder die Existenz oder die Eindeutigkeit von Lösungen nicht gegeben ist.

1\. Die gewöhnliche Differentialgleichung

```{math}
e^{y'(x)} \equiv 0 \quad \forall x \in \R
```

besitzt keine Lösung, da die Exponentialfunktion strikt positiv ist und es somit keine Funktion $y \colon \R \rightarrow \R$ gibt, so dass die obige Gleichung erfüllt werden kann.

2\. Die gewöhnliche Differentialgleichung

```{math}
y'(x)(1-y'(x)) \equiv 0 \quad \forall x \in \R
```

besitzt auf Grund ihrer Symmetrieeigenschaften zwei unterschiedliche Funktionenscharen als Lösung, nämlich

```{math}
y_1(x) = c \quad \text{ und } \quad y_2(x) = x + c \quad \forall x \in \R,
```

wobei $c \in \R$ eine beliebige Konstante darstellt.
````

Die wichtigste Eigenschaft für die Existenz und Eindeutigkeit von Lösungen gewöhnlicher Differentialgleichungen ist die **(lokale) Lipschitzstetigkeit** der rechten Seite $F \colon I \times U$.
Diese wollen wir der Vollständigkeit halber im Folgenden definieren.

````{prf:definition} (Lokale) Lipschitzstetigkeit
Sei $F \colon G \to \R^n$ eine Funktion mit dem erweiterten Phasenraum $G \, \coloneqq \, I \times U \subset \R\times\R^n$.
Man sagt, dass $F$ in $G$ einer **globalen Lipschitz-Bedingung** genügt (bezüglich der Variablen $y \in U$) mit der Lipschitz-Konstanten $L\geq0$, wenn gilt

```{math}
\Vert F(t,y) - F(t,\widetilde{y}) \Vert \leq L \Vert y-\widetilde{y}\Vert\quad\text{ für alle }(t,y), (t,\widetilde{y})\in G\,.
```

Man sagt, $F$ genüge in $G$ einer **lokalen Lipschitz-Bedingung**, falls jeder Punkt $(a,b)\in G$ im erweiterten Phasenraum eine Umgebung $V$ besitzt, sodass $F$ in $G\cap V$ einer Lipschitzbedingung mit einer gewissen (von $V$ abhängigen) Konstanten $L\in\R_+$ genügt.
%\end{definition}
````

Für die (lokale) Existenz von Lösungen haben wir in Kapitel 8.4 {cite:p}`tenbrinck_2021` den **Satz von Picard-Lindelöf** formuliert, den wir im Folgenden wiederholen werden.

````{prf:theorem} (Lokaler) Existenzsatz nach Picard-Lindelöf
:label: satz:picardlindeloef_lokal
Sei $F\colon G\to\R^n$ eine stetige Funktion mit erweitertem Phasenraum $G \coloneqq I \times U \subset \R\times\R^n$, die lokal Lipschitz-stetig auf $G$ bezüglich der $y$-Variablen ist.
Dann existiert zu jedem Anfangswert $(t_0,y_0) \in G$ ein $\varepsilon>0$, sowie eine Lösung

```{math}
\phi \colon \left[t_0-\varepsilon, t_0+\varepsilon\right] \to \R^n
```

der gewöhnlichen Differentialgleichung 

```{math}
\dot{y}(t) \ = \ F(t,y(t))
```

unter der Anfangsbedingung $\phi(t_0)=y_0$.
````
````{prf:proof}
Siehe \cite[§12, Satz 4]{forster}.
````