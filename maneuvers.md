---
title: Maneuvers
date: 2015-07-11
---

> The six words you *never* say at NASA: “And besides — it works in Kerbal
> Space Program.”
-- [xkcd](https://xkcd.com/1244/), cartoonist and NASA roboticist

In this chapter, we will see how to change from a circular orbit to another.

Pro-/retro- grade burn
======================

The vis-viva equation (\ref{eql:visviva}) tells us:

$$
\speed{v}^2
=
\mathcal G \mass{M} \left(
	\frac 2 {\dist{r}}
	-
	\frac 2 {\dist{r_a} + \dist{r_p}}
\right)
$$

For example, if we are at an apsis (apo- or peri-) and want to rise the
opposite point, we need to speed up (burn prograde), and slow down to decrease
it; the formula above tells us how much so.

<figure>
\begin{tikzpicture}
\def\peri{1}
\def\apoa{1}
\def\apob{4}
\node[point=O] (O) at (0,0) {};
\node (A0) at (0,\apoa) {};
\node (A1) at (0,\apob) {};
\orbit[color=blue]{O}{\apoa}{\peri}{0}{360}
\orbit[color=red] {O}{\apob}{\peri}{0}{360}
\node[loint=B] (B) at (-\peri,0) {};
\end{tikzpicture}
<figcaption>
A satellite on the \textcolor{blue}{blue} orbit can switch to the
\textcolor{red}{red} one by burning prograde (speeding up) at $\posit{B}$;
conversely it can switch from the \textcolor{red}{red} orbit to the
\textcolor{blue}{blue} one by burning retro grade at this same point.
</figcaption>
</figure>

When searching for good trajectories, we are interested in saving propellant.
According to (\ref{eql:thrust}), this is the same as saving for $\speed{\Delta
v}$ (althgouh proportionally). If $\dist{r}$ is the apsis where the burn is
performed, $\dist{r_0}$ the opposite apsis before the burn and $\dist{r_1}$
after:

\begin{align*}
\speed{\Delta v}
&=
|\speed{v_1} - \speed{v_0}|
\\
\frac 1 {\sqrt{\mathcal G \mass{M}}} \speed{\Delta v}
&=
\left|
\sqrt{
	\frac 2 {\dist{r}}
	-
	\frac 2 {\dist{r} + \dist{r_1}}
}
-
\sqrt{
	\frac 2 {\dist{r}}
	-
	\frac 2 {\dist{r} + \dist{r_0}}
}
\right|
\eqtag{eql:burn}
\end{align*}



Hohmann transfer
================

Now, assume we are in a circular orbit of radius $\dist{r_0}$ and want to do a
simple transfer to a circular orbit of radius $\dist{r_1}$. During a Hohmann
transfer, we first raise our apoapsis to $\dist{r_1}$ and then the periapsis
(from the new apopsis).

<figure>
\begin{tikzpicture}
\def\rada{1}
\def\radb{3}
\node[point=O] (O) at (0,0) {};
\orbit[color=blue] {O}{\rada}{\rada}{  0}{360}
\orbit[color=green]{O}{\radb}{\rada}{180}{360}
\orbit[color=red]  {O}{\radb}{\radb}{  0}{360}
\node[loint=B1] (B1) at (-\rada,0) {};
\node[roint=B2] (B2) at ( \radb,0) {};
\end{tikzpicture}
<figcaption>
We first switch from the \textcolor{blue}{blue} orbit to the
\textcolor{green}{green} one by burning at $\posit{B1}$ and then from the
\textcolor{green}{green} one to the \textcolor{red}{red} one by burning at
$\posit{B2}$.
</figcaption>
</figure>

$$
\frac 1 {\sqrt{\mathcal G \mass{M}}} \speed{\Delta v}
=
\left|
\sqrt{
	\frac 2 {\dist{r_0}}
	-
	\frac 2 {\dist{r_0} + \dist{r_1}}
}
-
\frac 1 {\sqrt{\dist{r_0}}}
\right|
+
\left|
\frac 1 {\sqrt{\dist{r_1}}}
-
\sqrt{
	\frac 2 {\dist{r_1}}
	-
	\frac 2 {\dist{r_0} + \dist{r_1}}
}
\right|
$$

We can multiply both hands by $\sqrt{\dist{r_0}}$ and set $x = \frac
{\dist{r_1}} {\dist{r_0}}$ to get a simpler expression:

$$
\underbrace{
	\sqrt{\frac {\dist{r_0}} {\mathcal G \mass{M}}}
}_{\alpha}
\speed{\Delta v}
=
\left|
\sqrt{2 - \frac 2 {1 + x}}
-
1
\right|
+
\left|
\frac 1 {\sqrt{x}}
-
\sqrt{\frac 2 x - \frac 2 {1 + x}}
\right|
$$

<figure>
\begin{tikzpicture}
\begin{axis}[
	samples=\samples,
	domain=0.25:4,
	xtick={0.25,1,2,3,4},
	ytick={0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9},
	no markers,
	axis lines=left,
	xlabel=$\frac {\dist{r_1}} {\dist{r_0}}$,
	ylabel=$\alpha \speed{\Delta v}$
]
\addplot{abs(sqrt(2-2/(1+x)) - 1) + abs(1/sqrt(x) - sqrt(2/x - 2/(1+x)))};
\end{axis}
\end{tikzpicture}
<figcaption>
Note that decreasing an orbit by half costs about as much as the converse
(doubling it), but dividing it by four costs twice as much as the converse.
</figcaption>
</figure>



Bi-elliptical transfer
======================

The idea is to use three burns instead of two.

<figure>
\begin{tikzpicture}
\def\rada{1}
\def\radb{3}
\def\radi{5}
\node[point=O] (O) at (0,0) {};
\orbit[color=blue]  {O}{\rada}{\rada}{  0}{360}
\orbit[color=green] {O}{\radi}{\rada}{180}{360}
\orbit[color=violet]{O}{\radi}{\radb}{  0}{180}
\orbit[color=red]   {O}{\radb}{\radb}{  0}{360}
\node[loint=B1] (B1) at (-\rada,0) {};
\node[roint=B2] (B2) at ( \radi,0) {};
\node[roint=B3] (B3) at (-\radb,0) {};
\end{tikzpicture}
<figcaption>
During a bi-elliptical transfer, we use two intermediate orbits
(\textcolor{green}{green}, then \textcolor{violet}{violet}); the idea is that
it will be easier to raise the \textcolor{green}{green} periapsis from a higher
apoapsis
</figcaption>
</figure>

\begin{align*}
\frac 1 {\sqrt{\mathcal G \mass{M}}} \speed{\Delta v}
=&
\left|
\sqrt{
	\frac 2 {\dist{r_0}}
	-
	\frac 2 {\dist{r_0} + \dist{r_1}}
}
-
\frac 1 {\sqrt{\dist{r_0}}}
\right|
\\
&+
\left|
\sqrt{
	\frac 2 {\dist{r_1}}
	-
	\frac 2 {\dist{r_2} + \dist{r_1}}
}
-
\sqrt{
	\frac 2 {\dist{r_1}}
	-
	\frac 2 {\dist{r_0} + \dist{r_1}}
}
\right|
\\
&+
\left|
\frac 1 {\sqrt{\dist{r_2}}}
-
\sqrt{
	\frac 2 {\dist{r_2}}
	-
	\frac 2 {\dist{r_2} + \dist{r_1}}
}
\right|
\end{align*}

Again, we set $x = \frac {\dist{r_2}} {\dist{r_0}}$ and $y = \frac {\dist{r_1}}
{\dist{r_0}}$ and:

\begin{align*}
\underbrace{
	\sqrt{\frac {\dist{r_0}} {\mathcal G \mass{M}}}
}_{\alpha}
\speed{\Delta v}
=&
\left|
\sqrt{2 - \frac 2 {1 + y}}
-
1
\right|
\\
&+
\left|
\sqrt{\frac 2 y - \frac 2 {x + y}}
-
\sqrt{\frac 2 y - \frac 2 {1 + y}}
\right|
\\
&+
\left|
\frac 1 {\sqrt{x}}
-
\sqrt{\frac 2 x - \frac 2 {x + y}}
\right|
\end{align*}

<figure>
\begin{tikzpicture}
\begin{axis}[
	samples=\samples,
	domain=5:20,
	no markers,
	axis lines=left,
	xlabel=$\frac {\dist{r_1}} {\dist{r_0}}$,
	ylabel=$\alpha \speed{\Delta v}$,
	legend pos=north west,
]
\addplot{abs(sqrt(2-2/(1+x)) - 1) + abs(1/sqrt(x) - sqrt(2/x - 2/(1+x)))};
\addlegendentry{Hohmann}
\foreach \myy in {10,50}{
	\addplot{abs(sqrt(2-2/(1+\myy)) - 1) + abs(sqrt(2/\myy - 2/(x+\myy)) - sqrt(2/\myy - 2/(1+\myy))) + abs(1/sqrt(x) - sqrt(2/x - 2/(x+\myy)))};
	\edef\temp{\noexpand
	\addlegendentry{Bi ($y = \myy$)}
	}\temp
}
\end{axis}
\end{tikzpicture}
</figure>



Inclination change
==================

<important>
Remember, we are only considering **circular** orbits. The formulas and
derivations below only make sense for circular orbits. We advise you to set
your inclination in a circular orbit before any subsequent maneuver.
</important>

(Anti-)normal burn
------------------

Consider the orbital plane in which a satellite is moving. We are interested in
the effect of an acceleration orthogonal to the plane (normal or antinormal).
For this, we study the evolution of the velocity.

<figure>
\begin{tikzpicture}[->,thick]
\node[boint=P] (P)   at (0,0) {};
\node (V)   at ( 50:3)    {$\speed{\overrightarrow v}$};
\node (dV)  at (140:1)    {$\speed{\overrightarrow {\d v}}$};
\node (VdV) at ($(V)+(dV)$) {$\speed{\overrightarrow {v + \d v}}$};
\draw[->,thick] (P) -- (V);
\draw[->,thick] (P) -- (dV);
\draw[->,thick] (P) -- (VdV);
\markangle{V}{P}{VdV}{$\d \theta$}{1.5}
\end{tikzpicture}
<figcaption>
The satellite is heading towards $\speed{\vec v}$ and an acceleration is
applied to it so that during a time $\delay{\dt}$, its velocity is changed by
$\speed{\vec{\d v}}$.
</figcaption>
\label{fig:normalburn}
</figure>

As seen in figure (\ref{fig:normalburn}), we can easily find the change in
inclination:

\begin{align*}
\angle{\d \theta}
\simeq
\tan \angle{\d \theta}
&=
\frac {\speed{\d v}} {\speed{v}}
\\
\int \frac {\angle{\d \theta}} {\delay{\dt}} \delay{\dt}
&=
\int \frac {\accel{a} \delay{\dt}} {\speed{v}}
\\
\angle{\theta}
&=
\frac {\accel{a} \delay{t}} {\speed{v}}
=
\frac {\speed{\Delta v}} {\speed{v}}
\end{align*}


Straight burn
-------------

Doing a $180^{\circ}$ inclination chage using a constant radial burn like
exposed above yields a $\speed{\Delta v}$ proportional to the current orbital
velocity $\speed{v}$: $\speed{\Delta v} = \angle{\pi} \speed{v} \simeq 3
\speed{v}$. However, simply going retrograde until the speed is reverse only
yields $\speed{\Delta v} = 2 \speed{v}$ for the same result.

You can find another derivation of the cost in @incproof @incproof2.

<figure>
\begin{tikzpicture}[->,thick]
\node[boint=P] (P)   at (0,0) {};
\coordinate (V0) at (40:3);
\coordinate (V1) at (80:3);
\coordinate (VV) at ($(V1)-(V0)$);
\draw (P) -- +(V0) node[above]{$\speed{\overrightarrow {v_0}}$};
\draw (P) -- +(V1) node[above]{$\speed{\overrightarrow {v_1}}$};
\draw[red] (P) -- +(VV) node[above]{$\speed{\overrightarrow {\Delta v}}$};
\draw[red] (V0) -- +(VV);
\markangle{V0}{P}{V1}{$\theta$}{1}
\end{tikzpicture}
<figcaption>
A rotation of angle $\angle{\theta}$ from velocity vector $\speed{\vec{v_0}}$
to $\speed{\vec{v_1}}$ is done in a straight change in speed $\speed{\Delta
v}$.
</figcaption>
</figure>

We need to compute $\speed{\Delta v}$ for given $\speed{v} =
\speed{|\vec{v_0}|} = \speed{|\vec{v_1}|}$ and $\angle{\theta}$. Because the
triangle is isosceles, the altitude and the median from $P$ are one so:

$$
\speed{\Delta v}
=
\left|2 \speed{v} \sin \frac {\angle{\theta}} 2\right|
$$

For $\angle{\theta} = \angle{\pi}$, we get $\speed{\Delta v} = 2 \speed{v}$
which is the expected result.

<figure>
\begin{tikzpicture}
\begin{axis}[
	samples=\samples,
	domain=-180:180,
	xtick={-180,-135,...,180},
	no markers,
	axis lines=left,
	xlabel=$\theta$ ($^{\circ}$),
	ylabel=$\frac {\speed{\Delta v}} {\speed{v}}$,
]
\addplot{abs(2*sin(x/2))};
\end{axis}
\end{tikzpicture}
<figcaption>
An inclination change of about $\angle{30^{\circ}}$ already costs half the
orbital speed; $\angle{60^{\circ}}$ costs as much as the orbital speed.
</figcaption>
</figure>


Bi-elliptical inclination change
--------------------------------

Whatever the method used for the inclination change, the cost is proportional
to the current orbital speed. Thus, it is more efficient to do such a maneuver
at low speed (e.g. at apoapsis). /u/ObsessedWithKSP demonstrated a maneuver
similar to the bi-elliptical transfer for a more efficient plane change
@biincchange @biincchange2.

A formal derivation of the optimal inclination change has been published by
/u/listens\_to\_galaxies @incproof @incproof2.

<figure>
\begin{tikzpicture}
\def\rada{2}
\def\radi{5}
\def\width{\rada^0.5 * \radi^0.5}
\node[point=O] (O) at (0,0) {};
\node[loint=B1] (B1) at (-\rada,0) {};
\node[roint=B2] (B2) at ( \radi,0) {};
\begin{scope}[canvas is xy plane at z=0,color=blue]
\orbit{O}{\rada}{\rada}{0}{360}
\orbit{O}{\radi}{\rada}{180}{360}
\draw (-\rada,-\width) rectangle (\radi,\width);
\end{scope}
\begin{scope}[canvas is zx plane at y=0,rotate=90,color=red]
\draw (-\rada,-\width) rectangle (\radi,\width);
\orbit{O}{\radi}{\rada}{0}{180}
\orbit{O}{\rada}{\rada}{0}{360}
\end{scope}
\end{tikzpicture}
<figcaption>
Starting in the \textcolor{blue}{blue} plane on the circular orbit, the
spacecraft first burns prograde in $\posit{B1}$ to raise its apoapsis to
$\posit{B2}$; once there, its speed is lower and it can proceed to the
inclination change to the \textcolor{red}{red} plane effectively; finaly, it
burns retrograde back in $\posit{B1}$ to return to a circular orbit.
</figcaption>
</figure>


Radial in/out burn
==================

TODO



Arbitrary burn
==============

TODO
