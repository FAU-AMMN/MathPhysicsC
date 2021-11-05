# Differentialformen

In diesem Kapitel werden wir nun [Differentialformen](https://de.wikipedia.org/wiki/Differentialform) einführen. Die entscheidende Neuerung im Vergleich zum vorhergehenden Kapitel, ist 
dass wir zusätzlich zur Vektorraumstruktur nun ein Konzept von Räumlichkeit einführen, speziell betrachten wir eine offene Menge $U\subset\R^n$. Ein weiterer wichtiger Aspekt, ist dass wir im Folgenden mit glatten Funktion arbeiten wollen, d.h., mit dem Raum $C^\infty(U,\R^n)$.


Eine\href{}
{\em Differentialform}
:label: Differentialform $\omega$ auf$U\subseteq\bR^n$ ist eine von Ortzu Ort variierende "au"sere Form, deren Variation wir als glattvoraussetzen.

Wir schreiben eine allgemeine {\em $k$--Form} $\omega$ in der {\em Grundform}
\beq
\omega = \sum_{1\leq i_1<\ldots<i_k\leq n}\omega_{i_1\ldots i_k}
dx_{i_1}\wedge\ldots\wedge dx_{i_k}\in\Omega^k(U),
\Leq{om:k}
wobei\begin{enumerate}[$\bullet$]
*
die $\omega_{i_1\ldots i_k}\in \Omega^0(U):=C^\infty(U,\bR)$, also
glatte reelle Funktionen auf $U$ sind,*
und die $dx_i$ den Koordinatenfunktionen $x_i:\bR^n\to\bR$ zugeordnete
$1$--Differentialformen sind ($dx_i\in\Omega^1(\bR^n)$).
*
Den Raum der $k$--Differentialformen schreiben wir ab jetzt zur
Unterscheidung vom Raum der "au"seren $k$--Formen
mit dem Symbol $\Omega$ statt $\Lambda$.
\end{enumerate}
%
Die $dx_i$ sind durch ihre Wirkung auf ein Vektorfeld $v:U\to
\bR^n$ definiert, und $dx_i(v)( y) := v_i( y)$.
$1$--Differentialformen machen also aus Vektorfeldern Funktionen, undf"ur $k$ Vektorfelder $v^{(l)}:U\to\bR^n$ ist f"ur das $\omega$ aus ({prf:ref}`om:k`)
\[\omega\l(v^{(1)},\ldots,v^{(k)}\ri) := \sum_{1\leq i_1<\ldots<i_k\leq n}
\omega_{i_1\ldots i_k}\cdot\det\bsm dx_{i_1}(v^{(1)})&\ldots& dx_{i_k}(v^{(1)})\\
\vdots&&\vdots\\
dx_{i_1}(v^{(k)})&\ldots& dx_{i_k}(v^{(k)}) \esm\]
definiert. Das Ergebnis ist also eine reelle Funktion auf $U$.\\
Die Rechenregeln "ubertragen sich von den "au"seren Formen auf dieDifferentialformen.

Auf dem $\bR$--Vektorraum\beq
\Omega^*(U) := \bigoplus_{k=0}^n\Omega^k(U)
\Leq{om:stern}der Differentialformen betrachten wir jetzt
den {\em Differentialoperator} $d$, der durch
\begin{enumerate}[$\bullet$]
*
$df := \sum_{i=1}^n\frac{\pa f}{\pa x_i}dx_i$ f"ur Funktionen
$f\in C^\infty(U,\bR) = \Omega^0(U)$
*
und $d\omega := \sum_{1\leq i_1<\ldots<i_k\leq n}d\omega_{i_1\ldots i_k}
\wedge dx_{i_1}\wedge\ldots\wedge dx_{i_k}$ f"ur $k$--Formen\linebreak
$\omega = \sum_{1\leq i_1<\ldots<i_k\leq n}\omega_{i_1\ldots i_k}
dx_1\wedge\ldots\wedge dx_{i_k}$
\end{enumerate}
definiert ist. $d$ verwandelt eine $k$--Form also in eine $(k+1)$--Form.
%
\begin{defi}\quad\\
Die lineare Abbildung$d:\Omega^*(U)\to\Omega^*(U)$ hei"st\href{https://de.wikipedia.org/wiki/%C3%84u%C3%9Fere_Ableitung}
**äu\ss ere Ableitung**
:label: aeussere Ableitung.
\end{defi}
%

````{prf:example} \"Au\ss ere Ableitung
:label: ex:10.14\quad\\[-6mm]
\begin{enumerate}[1.]
*
F"ur $\omega\in\Omega^0(\bR^3)$ ist $d\omega = \frac{\pa\omega}{\pa x_1}dx_1+
\frac{\pa\omega}{\pa x_2}dx_2+\frac{\pa\omega}{\pa x_3}dx_3$.
*
F"ur $\omega = \omega_1dx_1+\omega_2dx_2+\omega_3dx_3\in\Omega^1(\bR^3)$
ist
\beqno
d\omega &=& (d\omega_1)\wedge dx_1+(d\omega_2)\wedge dx_2+(d\omega_3)\wedge
dx_3\\
&=& \l(\frac{\pa\omega_2}{\pa x_1}-\frac{\pa\omega_1}{\pa x_2}\ri)
dx_1\wedge dx_2+ \l(\frac{\pa\omega_3}{\pa x_2}-\frac{\pa\omega_2}{\pa x_3}\ri)
dx_2\wedge dx_3\\
&& + \l(\frac{\pa\omega_1}{\pa x_3}-\frac{\pa\omega_3}{\pa x_1}\ri)
dx_3\wedge dx_1
\eeqno
*
F"ur $\omega = \omega_{12}dx_1\wedge dx_2+\omega_{23}dx_2\wedge dx_3
+\omega_{31}dx_3\wedge dx_1 \in\Omega^2(\bR^3)$ ist
\[d\omega = \l(\frac{\pa\omega_{12}}{\pa x_3} + \frac{\pa\omega_{23}}{\pa x_1}
+ \frac{\pa\omega_{31}}{\pa x_2}\ri)dx_1\wedge dx_2\wedge dx_3.\]
*
F"ur $\omega\in\Omega^3(\bR^3)$ ist $d\omega=0$.
\hfill $\Diamond$
\end{enumerate}
````

%
\begin{theorem}
$d$ ist eine\href{https://de.wikipedia.org/wiki/Derivation_(Mathematik)#Antiderivationen}
**Antiderivation**
:label: Antiderivation, d.h.\ f"ur$\alpha\in\Omega^k(U)$
und $\beta\in\Omega^l(U)$ ist
\[d(\alpha\wedge\beta) = (d\alpha)\wedge\beta+(-1)^k\alpha\wedge d\beta.\]
\end{theorem}
%
{\footnotesize**Beweis:**
Wegen der Linearit"at von $d$ gen"ugt es, diese Gleichung f"ur Monome
\[\alpha := f\underbrace{dx_{i_1}\wedge\ldots\wedge dx_{i_k}}_{\tilde
{\alpha}}\qmbox{,}\beta := g\underbrace{dx_{j_1}\wedge\ldots\wedge dx_{j_l}}_
{\tilde{\beta}},\ f,g\in C^\infty(U,\bR)\]zu beweisen.
Es gilt\beqno
d(\alpha\wedge\beta) &=& d(f\cdot g)\tilde{\alpha}\wedge
\tilde{\beta} = \big((df)g+f(dg)\big)\,\tilde{\alpha}\wedge\tilde{\beta}\\
&=& (df)\tilde{\alpha}\wedge g\tilde{\beta}+ (-1)^kf\tilde{\alpha}
\wedge(dg)\tilde{\beta} = d\alpha\wedge\beta+(-1)^k\alpha\wedge d\beta.
\eeqno
\hfill $\Box$}
%
\begin{theorem}
:label: thm:dd
Auf $\Omega^*(U)$ gilt\hspace*{3mm}
\framebox{$dd=0$}.
\end{theorem}
%
{\footnotesize**Beweis:**
\begin{enumerate}[1.]
*
F"ur $f\in\Omega^0(U)$ ist
\beqno
ddf &=& d\l(\sum_{i=1}^n\frac{\pa f}
{\pa x_i}dx_i\ri) = \sum_{i=1}^n\sum_{l=1}^n\frac{\pa^2f}{\pa x_l\pa x_i}
dx_l\wedge dx_i\\
& =& \sum_{1\leq r< s\leq n}\l(\frac{\pa^2 f}{\pa x_r
\pa x_s} - \frac{\pa^2f}{\pa x_s\pa x_r}\ri)dx_r\wedge dx_s = 0,
\eeqno
da wir wegen der Glattheit von $f$ die partiellen Ableitungen vertauschen
k"onnen.
*
F"ur $\omega = \sum\omega_{i_1\ldots i_k}dx_{i_1}\wedge\ldots\wedge dx_{i_k}
\in\Omega^k(U)$ ist\
\[dd\omega = \sum(\underbrace{dd\omega_{i_1\ldots i_k}}_0)
\wedge dx_{i_1}\wedge\ldots\wedge dx_{i_k} = 0, \]
denn gem"a"s Satz {prf:ref}`Antiderivation` wird die "au"sere Ableitung auf die
1-Formen $d\omega_{i_1\ldots i_k}$ und $dx_{i_l}$ angewandt, und nach Teil 1.\
ist das Ergebnis Null.
\hfill $\Box$
\end{enumerate}}
%
\begin{defi}:label: geschlossen:exakt
Eine Differentialform $\vv\in\Omega^*(U)$ hei"st
\begin{enumerate}[$\bullet$]
* **geschlossen**, wenn $d\vv=0$,***exakt**, wenn $\vv=d\psi$ f"ur ein $\psi\in\Omega^*(U)$ gilt.
\end{enumerate}
\end{defi}
%
Nach Satz {prf:ref}`thm:dd` sind exakte Differentialformen geschlossen.\\F"ur $k$--Formen auf konvexen offenen Teimengen $U\subseteq \bR^n$gilt f"ur $k\ge 1$auch die Umkehrung (sog.\\href{https://de.wikipedia.org/wiki/Poincar%c3%a9-Lemma}
{\em Poincar\'{e}-Lemma},  siehe Kapitel {prf:ref}`sect:Poinca`).
%