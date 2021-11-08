Maß- und Integrationstheorie
===

Die Messung und Berechnung von Längen, Flächen und Volumina 
gehört zu den ersten mathematischen Aktivitäten der Menschheit.
Integration und Volumenberechnung aber sind zwei Seiten einer Medaille:

* In der [**Analysis I**](https://www.math.fau.de/wp-content/uploads/2019/05/knauf_analysis_I_2018-19.pdf) wurde das Riemann-Integral einer (positiven) reellen Funktion als Fläche unter dem Graphen der Funktion eingeführt. Diese Idee wird jetzt auf Funktionen mehrerer Variablen erweitert.

* Ist andererseits $A\subset\R^n$ eine (messbare) Teilmenge, dann ist ihr Maß gleich dem Integral $\int \mathbb{1}_A\,dx$ ihrer charakteristischen Funktion. 

Tatsächlich ist die Integration historisch wesentlich älter als die
Differentiation, die ja (in einer Dimension) ihre Umkehroperation ist.

Andererseits hat sich der Integralbegriff zusammen mit dem Begriff
der Funktion erweitert. 
Bis zum 19. Jahrhundert waren in der Regel die betrachteten Funktionen
stetig (sogar beliebig oft stetig differenzierbar).
In der Zwischenzeit ist uns der Gedanke vertraut geworden, dass 
fraktale Mengen und Funktionen nicht nur als mathematische Konstrukte
sondern auch für die Beschreibung von Naturvorgängen von Bedeutung sind.

Schon beim *Riemann-Integral* muss ja die zu integrierende Funktion
nicht stetig sein, sondern kann Sprungstellen besitzen, wenn diese sich 
nicht häufen.

In den nächsten Wochen werden Sie den Begriff des *Lebesgue-Integrals*
kennen lernen. 
Man kann noch mehr Funktionen Lebesgue-integrieren als
die Riemann\-integrablen, z.B. die charakteristische Funktion
```{math}
\mathbb{1}_\Q:\R\to\{0,1\}
```
der Teilmenge $\Q\subset\R$ der rationalen Zahlen, und es ist $\int_\R \mathbb{1}_\Q\,dx=0$.
Dies bedeutet, dass $\Q$ im Gegensatz zu
den irrationalen Zahlen Maß Null besitzt und korrespondiert mit
der Abzählbarkeit von $\Q$.
Dass man bei der Lebesgue-Integration allgemein sogenannte [**Nullmengen**](https://de.wikipedia.org/wiki/Nullmenge) 
wie z.B. $\Q$ unberücksichtigt lassen kann, ist oft praktisch. 

Der Hauptvorteil des Lebesgue-Integrals gegenüber dem Riemann-Integral
ist aber, dass es sich bei Operationen wie Limesbildung etc. einfacher 
verhält.

Für Funktionen, für die *beide* Integralbegriffe definiert
sind, stimmen aber Riemann-- und Lebesgue-Integral überein.

Die Grundidee aller Integration ist es, das 
$(n+1)$--dimensionale Volumen unter dem Graphen von $f:\R^n\to\R^+$ 
zu betrachten. Integration
lässt sich also auf die Berechnung von Maßen 
zurückführen.
In einem gewissen Sinn sind Maße damit ein fundamentaleres Konzept als
das der Integration. 
