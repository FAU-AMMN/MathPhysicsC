# Wiederholung: Gewöhnliche Differentialgleichungen

In diesem Abschnitt werden wir kurz die wichtigsten Definitionen und Ergebnisse zu gewöhnlichen Differentialgleichungen aus Kapitel 8 in {cite:p}`tenbrinck_2021` wiederholen und um neue Begriffe erweitern, mit denen wir die Theorie dynamischer Systeme mathematisch untersuchen können.

## Gewöhnliche Differentialgleichungen

Wir erinnern uns zunächst an die Definition eines gewöhnlichen Differentialgleichungssystems $m$-ter Ordnung als Grundlage für unsere weiteren Betrachtungen.

````{prf:definition} Gewöhnliches Differentialgleichungssystem
:label: def:DGL
Seien $n,m \in \N$.
Wir betrachten im Folgenden eine offene Teilmenge $U\subset (\R^n)^{m+1}$ und ein offenes Intervall $I\subset\R^+_0$. 
Es sei außerdem $F:I\times U\rightarrow\R^n$ eine stetige Funktion, dann nennen wir

```{math}
:label: eq:DGL
F(x,y,y',\ldots,y^{(m)}) = 0
```

ein **gewöhnliches Differentialgleichungssystem (DGL)** $m$-ter Ordnung von $n$ Gleichungen.
Gilt $m=1$, das heißt die Funktion $F$ ist skalarwertig, so sprechen wir von einer **gewöhnlichen Differentialgleichung**.

Eine Funktion $\phi\in C^m(I;\R^n)$ heißt **Lösung des Differentialgleichungssystems**, falls gilt,

```{math}
F(t, \phi(t), \phi'(t), \ldots, \phi^{(m)}) = 0 \quad \forall t\in I.
```

Wenn wir die DGL nach der höchsten auftauchenden Ableitung auflösen können, so dass sie die folgende Form hat

```{math}
y^{(m)} = F(x,y,y',\ldots,y^{(m-1)}),
```

so nennen wir die DGL **explizit**, ansonsten wird sie **implizit** genannt.
````

Folgende Bemerkung beschreibt eine alternative Notation von gewöhnlichen Differentialgleichungen 1. und 2. Ordnung, die häufig in der Literatur im Kontext dynamischer Systeme auftaucht.
````{prf:remark} Zeitableitungen bei gewöhnlichen Differentialgleichungen
Viele physikalische Phänomene können durch zeitabhängige gewöhnliche Differentialgleichungen 1. und 2. Ordnung beschrieben werden.
In diesen Fällen verwendet man häufig die Variable $t \in \R^+_0$ als unabhängige Variable anstatt einer Variable $x \in \R$.
Auch ändert sich häufig die Notation der Zeitableitungen der gesuchten Funktion $y$, so dass folgende Korrespondenz für die ersten beiden Ableitungen entsteht:
1. $y'(x) \ \hat{=} \ \dot{y}(t)$,
2. $y''(x) \ \hat{=} \ \ddot{y}(t)$.
````

## Autonome Differentialgleichungen

Im Fall von dynamischen Systemen erhält der Definitionsbereich der Funktion $F$ einer gewöhnlichen Differentialgleichung einen besonderen Namen, wie die folgende Bemerkung erklärt.
````{prf:remark} (Erweiterter) Phasenraum
Wird eine gewöhnliche Differentialgleichung als mathematisches Modell für ein kontinuierliches dynamisches System genutzt, so wird die offene Menge $U\subset (\R^n)^{m+1}$ auch als **Phasenraum** bezeichnet. 
Der Definitionsbereich $I\times U$ der stetigen Funktion $F$ wird auch als **erweiterter Phasenraum** bezeichnet.

Der Phasenraum beschreibt die Menge aller möglichen Zustände des dynamischen Systems.
Jeder Punkt des Phasenraums wird hierbei eindeutig einem Zustand des Systems zugeordnet.

In Kapitel \xxx werden wir spezielle Diagramme basierend auf dem Begriff des erweiterten Phasenraum betrachten (auch Phasenportraits genannt), um Lösungen von dynamischen Systemen mathematisch zu charakterisieren.
````

Im Fall von **kontinuierlichen dynamischen Systemen** spielt eine Familie von gewöhnlichen Differentialgleichungen eine wichtige Rolle, die wir im Folgenden definieren wollen. 
Diese zeichnen sich dadurch aus, dass die Funktion $F$ in [](eq:DGL) nicht explizit von der Zeit abhängt.

````{prf:definition} Autonome DGL
Hängt die Funktion $F$ in {prf:ref}`def:DGL` nicht explizit von der Zeit ab, d.h., wir haben $F:U\rightarrow\R^n$ dann heißt die Gleichung

```{math}
:label: eq:autonome_DGL
y^{(m)}(x) = F(y(x), y'(x), \ldots, y^{(m-1)}(x)) \quad \forall t\in I
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

<!-- ## Anfangswertprobleme

Üblicherweise betrachtet man nicht nur DGLs sondern sogenannte Anfangswertprobleme. Hierbei wählt man einen ausgezeichneten Zeitpunkt $t_0\in I$ aus dem Zeitintervall $I$ an welchem man die Lösung explizit durch einen Anfangswert $x_0\in U$ vorgibt. Im Setting von {prf:ref}`def:DGL` heißt
das Gleichungssystem

```{math}
:label: eq:AWP
\dot{x}(t) = F(t, x(t))\quad\forall t\in I
x(t_0) = x_0
```

**Anfangswertproblem**. Sofern nicht explizit angegeben werden wir im folgenden annehmen, dass ohne Beschränkung der Allgemeinheit $t_0=0$ gilt.

## Existenz und Eindeutigkeit einer Lösung

Wir wiederholen die wichtigsten Existenzaussagen zu Anfangswertproblem. Die wichtigste Eigenschaften in diesem Kontext ist die Lipschitzstetigkeit der rechten Seite $F$.

````{prf:definition} Lipschitzstetigkeit
$F$
```` -->
