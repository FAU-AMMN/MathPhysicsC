# Gewöhnliche Differentialgleichungen

## Gewöhnliche Differentialgleichungen

Im Folgenden bezeichnet $U\subset\R^n$ stets eine **offene** Teilmenge des $\R^n$

````{prf:definition} Gewöhnliche Differentialgleichung und Phasenraum
:label: def:DGL
Es sei $I\subset\R^+_0$ eine offenes Intervall und $F:I\times U\rightarrow\R^n$ eine **stetige** Funktion, dann nennen wir

```{math}
:label: eq:DGL
\dot{x}(t) = F(t, x(t))\quad\forall t\in I
```

gewöhnliche Differentialgleichung (DGL) erster Ordnung. Eine Funktion $\phi\in C^1(I,\R^n)$ heißt **Lösung** der DGL, falls gilt,

```{math}
\dot{\phi}(t) = F(t, \phi(t))\quad\forall t\in I.
```
Die Menge $G=I\times U$ wird hier auch als **erweiterter Phasenraum** bezeichnet.

````

Speziell in den nächsten Abschnitten behandeln wir DGLs, für welche die Funktion $F$ nicht von der Zeit abhängt.

````{prf:definition} Autonome DGL
Hängt die Funktion $F$ in {prf:ref}`def:DGL` nicht explizit von der Zeit ab, d.h., wir haben $F:U\rightarrow\R^n$ dann heißt die Gleichung

```{math}
:label: eq:DGL
\dot{x(t)} = F(x(t))\quad\forall t\in I
```

**autonome DGL**.

````

## Anfangswertprobleme

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
````
