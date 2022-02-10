# Die Komplexen Zahlen

Wir werden hier zunächst die wichtigen Grundlagen der komplexen Zahlen wiederholen.
Die komplexen Zahlen werden eingeführt als das Tupel

```{math}
\C := (\R^2,+,\cdot)
```

zusammen mit den Operationen

```{math}
(x_1,y_1) + (x_2,y_2) &:= (x_1 + x_2, y_1+y_2),\\
(x_1,y_1) \cdot (x_2,y_2) &:= (x_1\cdot x_2 - y_1\cdot y_2, y_1\cdot x_2 + x_1\cdot y_2).
```

Diese Struktur bildet einen **Körper** mit dem Einselement $1:=(1,0)$. Das Element $i:=(0,1)$ heißt **imaginäre Einheit** und erfüllt die Gleichung

```{math}
i^2 = (0,1)\cdot(0,1) = -(1,0) = -1.
```

Als reeller Vektorraum hat $\C$ die kanonische Basis $\{(1,0),(0,1)\}=\{1,i\}$ weshalb wir jedes Element darstellen können über

```{math}
(x,y) = x + iy.
```

Für eine komplexe Zahl $z=x+ iy\in\C$ definieren wir

1. $\Re(z):= x$ den **Realteil**,

2. $\Im(z):=y$ den **Imaginärteil**,

3. $\overline{z}:= x-iy$ die **komplexe Konjugation**,

4. $\abs{z} = \sqrt{z\overline{z}} = \sqrt{x^2+y^2}$ den **Betrag**.

Für den Betrag komplexer Zahlen gelten die bekannten Rechenregeln

```{math}
\abs{0}&=0,\\
\abs{z\cdot w} &= \abs{z}\cdot \abs{w},\\
\abs{z+w}&\leq\abs{z}+\abs{w},
```

für zwei komplexe Zahlen $z,w\in\C$

Insbesondere induziert der Betrag die Metrik

```{math}
d(z,w):= \abs{z-w}
```

und damit auch eine Topologie sowie die Begriffe Konvergenz und Stetigkeit einer Funktion $f:\C\to\C$.
