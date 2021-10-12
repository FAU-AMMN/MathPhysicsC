
# Hamiltonsche Differentialgkeichungen und Phasenportraits

Ein wichtiges Prinzip für viele physikalischen Anwendungen sind Erhaltungssätze und die dazugehörigen Erhaltungsgrößen. Aus der klassichen Mechanik kennen wir z.B.

* Energieerhaltung,

* Impulserhaltung.

In ?? haben wir Bewegungslgleichungen als System von DGLs hergeleitet und gelöst, deshalb wollen wir nun die nötige Theorie entwickeln, die es uns erlaubt Erhaltungsgrößen direkt aus der DGL Formulierung zu erhalten.

````{prf:example} Harmonischer Oszillator
Die Bewgeungsgeleichung für den harmonischen Oszillator is gegeben durch $\dot{x}(t) = \ddot{x}(t) + a x(t)$ wobei $x(t)$ die horizontale 
Auslenkung zum Zeitpunkt $t$ beschreibt. Durch einführung der Variable $v(t)$ als Geschwindigkeit erhalten wir das System von DGLs


```{math}
\dot{x}(t) &= v \\
\dot{v}(t) &= -a x(t)
```

Die Funktion $H(x, v, t) = \frac{1}{2} (v^2 + a x^2)$ beschreibt die totale Energie des Systems und ist eine Erhaltungsgröße.
````
