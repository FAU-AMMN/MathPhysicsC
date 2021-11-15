# Stabilitätsbegriffe

Im Folgenden wollen wir grundlegende Begriffe der Stabilitätsanalyse von Ruhelagen einführen und diskutieren.
Wie in {ref}`s:fluesse` definiert, nennen wir einen Punkt $x\in U$ im Phasenraum $U$ **Ruhelage**, falls für den zugehörigen Phasenfluss $\Phi \colon I \times U \rightarrow U$ des dynamischen Systems gilt: $\Phi(t,x) = x, \forall t \in I$, d.h., wenn für alle $t \in I$ der Zustand $x \in U$ ein **Fixpunkt des Flusses** ist.

Für autonome Differentialgleichungssysteme mit

```{math}
\dot{x}(t) = F(x)
```

ist $x \in U$ auch eine Ruhelage, falls $F(x) = 0$ gilt, d.h., falls $x$ eine Nullstelle von $F$ ist.
Das ist einfach zu verstehen, da die Zeitableitung auf der linken Seite für eine Ruhelage Null ist und somit die Funktion $F$, die nur vom Ort abhängt, sich nicht ändern kann.

Anschaulich versteht man unter der Stabilitätsanalyse von Ruhelagen die mathematische Untersuchung, ob benachbarte Lösungen von einer Ruhelage wegstreben oder nicht.
Dies ist insbesondere in technischen Anwendungen wichtig, da man dort häufig danach strebt ein dynamisches System in eine Gleichgewichtslage zu bringen.
Da dies nur bis zu einer gewissen Genauigkeit möglich ist, muss man also mit kleinen Störungen rechnen.

Ist eine Ruhelage stabil, dann bleiben benachbarte Lösungen auch für zukünftige Zeitpunkte $t \in I$ nahe der Ruhelage.
Ist sie jedoch nicht stabil, so muss das im Allgemeinen nicht gelten und die Lösungen können dann mit der Zeit von der Ruhelage divergieren.
Diese Anschauung wollen wir in der folgenden Definition mathematisch formalisieren.
Hierbei werden wir den Stabilitätsbegriff für allgemeine Lösungen einführen und später Ruhelagen als ein Spezialfall dieser Lösungen interpretieren.

````{prf:definition} Stabilität von Lösungen
:label: def:Stabilitaet

Sei $\Phi \colon I \times U \rightarrow U$ der Phasenfluss zu dem Vektorfeld $F\in C^1(U;\R^n)$ auf $U$, dass durch die rechte Seite des zugehörigen Differentialgleichungssystems gegeben ist.

1\. Eine Lösung $t \in [0,\infty) \mapsto \Phi_t(x)$ heißt **(Lyapunov-)stabil**, wenn zu jedem $\epsilon > 0$ ein $\delta>0$ existiert mit:

```{math}
\|x-y\|<\delta \ \Rightarrow \ \sup_{t\geq0}\|\Phi_t(x)-\Phi_t(y)\|<\epsilon.
```

2\. Eine Lösung $ t \in [0,\infty) \mapsto \Phi_t(x)$ heißt **asymptotisch stabil**, wenn ein $\delta > 0$ existiert mit:

```{math}
\|x-y\|<\delta \ \Rightarrow \ \lim_{t\to\infty}\|\Phi_t(x)-\Phi_t(y)\|=0.
```

3\. Eine Lösung heißt **instabil**, wenn sie nicht (Lyapunov-)stabil ist.
````

```{margin} Aleksandr Lyapunov
[Alexander Michailowitsch Ljapunow](https://de.wikipedia.org/wiki/Alexander_Michailowitsch_Ljapunow) (Geboren 6. Juni 1857 in Jaroslawl; Gestorben 3. November 1918 in Odessa) war ein russischer Mathematiker und Physiker.
```

Es ist klar, dass der Begriff der asymptotischen Stabilität *stärker* als der Begriff der Lyapunov-Stabilität von Lösungen ist, da jede asymptotisch stabile Lösung auch schon Lyapunov-stabil ist.
Die Umkehrung gilt jedoch im Allgemeinen nicht.
Dies wird durch das folgende Beispiel nochmal illustriert.

````{prf:example} Stabilitätsanalyse für den harmonischer Oszillator

Der Phasenfluss für den harmonischen Oszillator ist, wie wir in {prf:ref}`ex:oscillations` gesehen haben, gegeben durch 

```{math}
\Phi(t, (p,x)) = \begin{pmatrix}
p \cos(\omega t) - m x \sin(\omega t)\\
\frac{p}{\omega m}\sin(\omega t) + x\cos(\omega t)
\end{pmatrix}
```
 
Wir suchen nun einen Fixpunkt $(p_r,x_r) \in U$ des Flusses der unabhängig ist vom Zeitpunkt $t$. 
Man sieht leicht ein, dass eine **Ruhelage** sich bei $(p_r,x_r) = (0,0)^T \in U$ befindet, da $\Phi(t,(0,0)) = (0,0)^T$ ist für alle $t \in I$.
Die gefundene Ruhelage ist **Lyapunov-stabil**, denn wie wir im Phasenporträt in []() gesehen haben, ist jeder Orbit um die Ruhelage $(0,0)$ periodisch. Damit kann das dynamische System insgesamt nicht wegstreben von der Ruhelage.

Mathematisch lässt sich diese Eigenschaft wie folgt zeigen.
Für ein beliebiges $\epsilon > 0$ sei $(p,y) \in U$ ein Punkt im Phasenraum mit periodischen Orbit $O(p,y)$ um die Ruhelage $(p_r,x_r) = (0,0)^T \in U$, so dass dessen maximaler Abstand zur Ruhelage kleiner als $\epsilon$ ist, d.h.

```{math}
\sup_{t \geq 0} ||\Phi_t(p_r,x_r) - \Phi_t(p,y)|| < \epsilon
```

Auf Grund der ersten Eigenschaft des Phasenflusses $\Phi_0(p,y) = (p,y)$ gilt dann aber schon

```{math}
||(p_r, x_r) - (p,y)|| = ||\Phi_0(p_r, x_r) - \Phi_0(p,y)|| < \epsilon.
```

Wählen wir nun $\delta \coloneqq \epsilon$, so haben wir gezeigt, dass die Ruhelage $(p_r, x_r) = (0,0)^T$ Lyapunov-stabil ist.
Sie ist jedoch auf Grund der Periodizität der Orbits um die Ruhelage **nicht asymptotisch stabil**, da für beliebige Punkte $(p,y) \in U$ mit $||(p_r,x_r) - (p,y)|| < \delta$ für ein $\delta > 0$ gilt

```{math}
\lim_{t\to\infty}\|\Phi_t(p_r, x_r)-\Phi_t(p,y)\| \neq 0.
```
````

Im allgemeinen Fall der gedämpften Schwingungsgleichung in {prf:ref}`ex:oscillations` hängt die Stabilität der Ruhelage im Ursprung intuitiverweise von der Reibungskonstanten ab, wie folgende Bemerkung festhält.

````{prf:remark} Stabilität bei der gedämpften Schwingungsgleichung
Für den Fall der gedämpften Schwingungsgleichung in [](eq:schwingungsgleichung) lässt sich folgendes Stabilitätsverhalten der Ruhelage im Ursprung in Abhängigkeit der Reibungskonstanten $r \in \R$ beobachten:
1. Die Ruhelage ist **asymptotisch stabil** für den Fall mit positiver Reibung $r>0$.
2. Die Ruhelage ist **Lyapunov-stabil** für den reibungsfreien Fall $r=0$.
3. Die Ruhelage ist **instabil** für den Fall einer negativen Reibung $r < 0$, d.h. für einen externen Antrieb.
````
