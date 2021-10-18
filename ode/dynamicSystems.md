# Einführung in dynamische Systeme

Dynamische Systeme spielen eine zentrale Rolle bei der Beschreibung zeitabhängiger Prozesse in vielen verschiedenen Anwendungsgebieten, wie zum Beispiel der Biologie oder der Physik.
Durch diese Art von mathematischen Modellen ist es beispielsweise möglich das Ausschwingen eines Pendels zu beschreiben oder den Bestand zweier unterschiedlicher Populationen über die Zeit in einer Räuber-Beute Beziehung zu untersuchen.

Maßgeblich für dynamische Systeme ist die Beobachtung, dass die beschriebenen Prozesse nicht von der Wahl des Anfangszeitpunktes abhängig sind, sondern lediglich von dem gewählten Anfangszustand.
Wir werden diese Eigenschaft später in Kapitel \xxx noch genauer mathematisch charakterisieren.

Je nach Anwendungsgebiet können dynamische Systeme entweder **diskret** oder **kontinuierlich** in der Zeitentwicklung sein.
Wir wollen im Folgenden zwei Beispiele zur Illustration des Unterschieds in der Zeitmodellierung diskutieren.

## Diskrete dynamische Systeme
Zur Veranschaulichung von diskreten dynamischen System wollen wir uns im Folgenden mit einem Beispiel aus der Biologie beschäftigen.
````{prf:example} Wachstum von Bakterien

In diesem Beispiel wollen wir annehmen, dass wir das **exponentielle Wachstum** von Bakterien durch Zellteilung als diskretes dynamisches System zu festen, äquidistanten Zeitpunkten $t_0, t_1, \ldots \in I$ in einem offenen Zeitintervall $I\subset\R^+_0$ untersuchen wollen.
Wir modellieren die (ungefähre) Anzahl der Bakterien zu einem Zeitpunkt $t \in I$ als Funktion $F \colon I \rightarrow \R_0^+$.
Da die Zeitpunkte äquidistant gewählt sind können wir eine einheitliche Wachstumsrate $\alpha \in \R^+$ mit $\alpha > 1$ annehmen, so dass für alle $n \in \N$ gilt:

```{math}
F(t_{n+1}) = \alpha \cdot F(t_n).
```

Wir erkennen, dass der Prozess des Bakterienwachstums nicht von der konkreten Wahl des Startzeitpunkts $t_0 \in I$ abhängt, sondern nur von anfänglichen Anzahl der Bakterien $F_0 \coloneqq F(t_0)$. Abbildung \xxx zeigt, dass eine unterschiedliche Wahl des Anfangszeitpunkt bei gleicher Wahl der Anfangspopulation keinen Effekt auf die zeitliche Dynamik hat.

Dies können wir wie folgt mathematisch verifizieren. Seien $t_m, t_n \in I$ mit $n,m \in \N$ zwei unterschiedliche Anfangszeitpunkte für die die gleiche Anfangspopulation $F_0 \in \N$ von Bakterien angenommen wird, d.h.,
```{math}
F(t_m) = F_0 = F(t_n).
```
Betrachten wir nun für die beiden unterschiedlichen Anfangszeitpunkte das Bakterienwachstum nach $k \in \N$ äquidistanten Zeitschritten, so ergibt sich:
```{math}
F(t_{m+k}) = \alpha \cdot F(t_{m+k-1}) = \ldots = \alpha^k \cdot F(t_{m}) = \alpha^k \cdot F_0 = \alpha^k \cdot F(t_n) = F(t_{n+k}).
```
Wir erkennen also, dass unabhängig vom gewählten Anfangszeitpunkt die Bakterienpopulation nach $k \in \N$ Zeitschritten gleich ist.
````

Diskrete dynamische Systeme tauchen auch in anderen spannenden Anwendungen auf, wie beispielsweise in der [Chaostheorie](https://de.wikipedia.org/wiki/Bifurkation_(Mathematik)#Bifurkationsdiagramm) und in der [Stochastik](https://de.wikipedia.org/wiki/Markow-Kette).

## Kontinuierliche dynamische Systeme
Im Unterschied zu diskreten dynamischen Systemen wird die Zeit bei kontinuerlichen dynamischen Systemen nicht an abzählbar vielen Punkten modelliert, sondern als Kontinuum.
Im Folgenden beschreiben wir das physikalische Experiment des freien Falls als Spezialfall eines kontinuierlichen dynamischen Systems.
````{prf:example} Freier Fall
In diesem Beispiel betrachten wir ein physikalisches Modell für den freien Fall eines Steins mit Masse $m \in \R^+$, den wir in einer Hand halten, bis wir ihn zu einem definierten Anfangszeitpunkt $t_0 \in I$ mit $I \subset \R^+_0$ fallen lassen.

Die aktuelle Entfernung des Steins zum Boden zu einem Zeitpunkt $t \in I$, d.h. seine gegenwärtige Höhe, ist gegeben durch eine monoton-fallende Funktion $F \colon I \rightarrow \R^+_0$.
Unsere Hand befindet sich zum Anfangszeitpunkt $t_0$ in einer Höhe von $F_0 > 0$.
Für jeden beliebigen Zeitpunkt $t > t_0$ lässt sich die aktuelle Höhe des fallenden Steins mit Hilfe des Newtonschen Gravitationsgesetzes wie folgt angeben:
```{math}
F(t) = \max(0, F_0 - \frac{1}{2}gt^2),
```
wobei $g = 9,81 \frac{m}{s^2}$ die Erdbeschleunigungskonstante bezeichnet.

Es wird klar, dass auch hier die Dynamik des freien Falls nicht von der Wahl des Anfangszeitpunkts $t_0 \in I$ abhängt.
Anschaulich gesprochen, würde der Stein genauso fallen, wenn wir ihn noch einige Sekunden länger festhalten würden.
````
Häufig kommen zur Beschreibung von kontinuierlichen dynamischen Systemen sogenannte **autonome gewöhnliche Differentialgleichungen** zum Einsatz, wie die in Beispiel \xxx implizit genutzten Bewegungsgleichungen. 
Wir werden diese Art von Differentialgleichungen in Kapitel \xxx mathematisch genauer betrachten.