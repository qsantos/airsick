---
title: Orbits
date: 2015-07-11
---

> There is a force in the earth which causes the moon to move.
-- [Johannes Kepler](https://en.wikipedia.org/wiki/Johannes_Kepler), discoverer
of the [laws of orbits
](https://en.wikipedia.org/wiki/Kepler%27s_laws_of_planetary_motion)

Orbital mechanics
=================

<remark>
We study orbital mechanics before the ascent since we can always pretend the
space craft is in orbit. When it is resting on the launchpad, it is at its
apoapsis but stays there because of the ground. This apoapsis is raised during
the ascent and the gravity turn is simply raising the periapsis.
</remark>


Set up
------

Consider two mass points $(\posit{P},\mass{M})$ and $(\posit{S},\mass{m})$ with
$\mass{M} \gg \mass{m}$ and $\dist{r} = \dist{PS}$. We consider the
gravitational force exerted by $\posit{P}$ over $\posit{S}$. Using Newton's
Second Law, we have $\accel{\ddot {\vec r}} = - \frac {\mathcal G \mass{M}}
{\dist{r}^2} \hat r$.


Orbital elements
----------------

<figure>
\begin{tikzpicture}
% parameters
\pgfmathsetmacro{\a}{3}
\pgfmathsetmacro{\e}{0.5}
\pgfmathsetmacro{\pe}{\a*(1-\e)}
\pgfmathsetmacro{\ap}{\a*(1+\e)}
\pgfmathsetmacro{\f}{\e*\a}
% axis
\node[boint=O] (O) at (0, 0) {};
\node[roint=X] (X) at (\a,0) {};
% orbit
\node          (F1) at (-\f,0) {};
\node[boint=F] (F2) at ( \f,0) {};
\orbit[red]{F1}{\ap}{\pe}{0}{360};
\orbitpoint[point=P]{F1}{\ap}{\pe}{45}{P}{}
% true anomaly
\draw (X) -- (F2) -- (P);
\markangle{X}{F2}{P}{$\theta$}{0.5}
% eccentric anomaly
\draw (X) -- (O) -- (P);
\markangle{X}{O}{P}{$E$}{0.5}
\end{tikzpicture}
</figure>

* semimajor
* semiminor
* true anomaly
* eccentric anomaly
* inclination
* argument of periapsis
* longitude of ascending node
* eccentricity
* apoapsis
* periapsis


Kepler's second law
-------------------

We use polar coordinates centered in $\posit{P}$. According to Newton's second
law, $\accel{\ddot{\vec r}} = - \frac {\mathcal G \mass{M}} {\dist{r}^2} \hat
r$. Thus $2 \speed{\dot r} \dot \theta + \dist{r} \ddot \theta = \accel{0}$. In
other terms: $\frac 1 {\dist{r}} \frac {\d} {\delay{\dt}} \Big(\dist{r}^2 \dot
\theta\Big) = 0$. This means that the area velocity $\dot {\mathcal A} = \frac
1 2 \dist{r}^2 \dot \theta$ is constant.


*Vis viva* equation
-------------------

The principle of energy conservation tells us that:

$$
E
=
\frac 1 2 \mass{m} \speed{v}^2
- \frac {\mathcal G \mass{M} \mass{m}} {\dist{r}}
\text{~is constant}
\eqtag{eql:orbenergy}
$$

We need two particular points to apply it. Let us consider the two points where
$\dist{r}$ is extremal, namely the apoapsis and periapsis. There, $\speed{\dot
r} = \speed{0}$ meaning that $\speed{\dot{\vec r}} = \dist{r} \dot \theta \hat
\theta$. We can then note that, at these two points:

$$
\dist{\vec r} \times \speed{\dot{\vec r}}
= \dist{r}^2 \dot \theta \underbrace{\hat r \times \hat \theta}_1
= 2 \dot{\mathcal A}
$$

This means that $\dist{r_a} \speed{v_a} = \dist{r_p} \speed{v_p}$. Now, we use
the (\ref{eql:orbenergy}) of energy and get:

\begin{align*}
\frac 1 2 \mass{m} \speed{v_a}^2
- \frac {\mathcal G \mass{M} \mass{m}} {\dist{r_a}}
&=
\frac 1 2 \mass{m} \speed{v_p}^2
- \frac {\mathcal G \mass{M} \mass{m}} {\dist{r_p}}
\\
\speed{v_a}^2 - \speed{v_r}^2
&=
2 {}\mathcal G \mass{M} \left(
	\frac 1 {\dist{r_p}}
	-
	\frac 1 {\dist{r_a}}
\right)
\\
\left(1 - \frac {\dist{r_a}^2} {\dist{r_p}^2}\right) \speed{v_a}^2
&=
2 {}\mathcal G \mass{M} \left(
	\frac 1 {\dist{r_p}}
	-
	\frac 1 {\dist{r_a}}
\right)
\\
\speed{v_a}^2
&=
2 {}\mathcal G \mass{M} \left(
	\frac 1 {\dist{r_p}}
	-
	\frac 1 {\dist{r_a}}
\right)
\frac {\dist{r_p}^2} {\dist{r_p}^2 - \dist{r_a}^2}
\\
&=
2 {}\mathcal G \mass{M}
\frac {\dist{r_a} - \dist{r_p}} {\dist{r_p} \dist{r_a}}
\frac {\dist{r_p}^2} {\dist{r_p}^2 - \dist{r_a}^2}
\\
&=
2 {}\mathcal G \mass{M}
\frac {1} {\dist{r_a}}
\frac {\dist{r_p}} {\dist{r_p} + \dist{r_a}}
\\
&=
\mathcal G \mass{M}
\frac {2 \dist{a} - \dist{r_a}} {\dist{r_a} \dist{a}}
\\
&=
\mathcal G \mass{M}
\left(
\frac 2 {\dist{r_a}}
-
\frac 1 {\dist{a}}
\right)
\end{align*}

We now have an expression of $\speed{v_a}$ that depends only on $\dist{r_a}$
and $\dist{a}$. Let us use (\ref{eql:orbenergy}) of energy again on the
apoapsis and an arbitrary point:

\begin{align*}
\frac 1 2 \mass{m} \speed{v_a}^2
- \frac {\mathcal G \mass{M} \mass{m}} {\dist{r_a}}
&=
\frac 1 2 \mass{m} \speed{v}^2
- \frac {\mathcal G \mass{M} \mass{m}} {\dist{r}}
\\
\speed{v}^2
&=
\mathcal G \mass{M} \left(
	\frac 2 {\dist{r}}
	-
	\frac 2 {\dist{r_a}}
\right)
+ \speed{v_a}^2
\\
&=
\mathcal G \mass{M} \left(
	\frac 2 {\dist{r}}
	-
	\frac 1 {\dist{a}}
\right)
\eqtag{eql:visviva}
\end{align*}



Inclination
===========

TODO



State prediction
================

TODO



Inferring an orbit
==================

TODO
