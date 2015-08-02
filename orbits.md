---
title: Orbits
date: 2015-08-01
---

> There is a force in the earth which causes the moon to move.
-- [Johannes Kepler](https://en.wikipedia.org/wiki/Johannes_Kepler), discoverer
of the [laws of orbits
](https://en.wikipedia.org/wiki/Kepler%27s_laws_of_planetary_motion)

Before launching a rocket, we need to know where we are going. Up is only part
of the answer.

Orbital trajectory
==================

Concept
-------

First, the obligatory quote when explaing how orbiting works:

> The knack [of flying] lies in learning how to throw yourself at the ground and miss.
-- [Double Adams](https://en.wikipedia.org/wiki/Douglas_Adams), author of
[*The Hitchhiker's Guide to the Galaxy*](https://en.wikipedia.org/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy)

The part of throwing oneself at the ground is easy:

<figure>
\begin{tikzpicture}
% parameters
\pgfmathsetmacro{\R}{12}
\pgfmathsetmacro{\pe}{1}
\pgfmathsetmacro{\ap}{14}
% drawing
\node (O) at (0, 0) {};  % primary
\node[point=S] (S) at (0, \ap) {};  % projectile
\draw ([shift=(105:\R)]O) arc (105:75:\R);  % ground
\begin{scope}[rotate=90]
\orbit[red]{O}{\ap}{\pe}{0}{-10}; % trajectory
\end{scope}
\end{tikzpicture}
<figcaption>
Most of the time, stuff we throw into the air falls down.
</figcaption>
</figure>

On the figure above, notice that, as we go right, the ground gets lower and
lower due to the **curvature** of the planet. Can we go right fast enough so
that the ground will lower as fast as we fall? Well, yes:

<figure>
\begin{tikzpicture}
% parameters
\pgfmathsetmacro{\R}{2}
\pgfmathsetmacro{\pe}{2.5}
\pgfmathsetmacro{\ap}{2.5}
% drawing
\node[point=P] (O) at (0, 0) {};  % primary
\node[point=S] (S) at (0, \ap) {};  % projectile
\draw (O) circle [radius=\R];
% trajectory
\orbit[red]{O}{\ap}{\pe}{0}{-360};
\end{tikzpicture}
<figcaption>
If we go fast enough, we will keep missing the ground.
</figcaption>
</figure>


Central force
-------------

The point $\posit{S}$ is the **s**atellite whose trajectory we want to
determine. The celestial objects it orbits is called the **primary**. Thanks to
the shell theorem, we can assimilate the **p**rimary with a mass-point
$(\posit{P}, \mass{M})$. Using Newton's Second Law, the acceleration due to the
force of gravitation is:

$$
\accel{\ddot {\vec r}}
= - \frac {\overbrace{\mathcal G \mass{M}}^{\mu}} {\dist{r}^2} \hat r
$$

where $\dist{\vec r} = \dist{\vec{PS}}$ and $\hat r = \frac {\dist{\vec{PS}}}
{\dist{PS}}$ is the direction (**unit vector**) from $P$ to $S$.

<note>
This already tells us that the acceleration, and hence the trajectory, does not
depend on the mass of the satellite.
</note>

\begin{align*}
\accel{\ddot {\vec r}}
&= \frac {\d^2} {\dt^2} \left(\dist{r} \hat r\right) \\
&= \frac {\d} {\dt} \left(\dot r \hat r + r \dot \theta \hat \theta \right) \\
&= \left(\ddot r - r {\dot \theta}^2\right) \hat r + \left(2 \dot r \dot \theta + r \ddot \theta\right) \hat \theta \\
\end{align*}

Hence the equation can be written as::

$$
\left\{
\begin{aligned}
\ddot r - r {\dot \theta}^2
&= - \frac {\mu} {\dist{r}^2} \\
2 \dot r \dot \theta + r \ddot \theta
&= 0 \\
\end{aligned}
\right.
$$

Kepler's second law
-------------------

The second line can be rewritten as:

\begin{align*}
0
&= 2 \dot r \dot \theta + r \ddot \theta \\
&= \frac 1 r \left(2 r \dot r \dot \theta + r^2 \ddot \theta\right) \\
&= \frac 1 r \frac {\d} {\dt} \left( r^2 \dot \theta \right) \\
\end{align*}

This means that $h = r^2 \dot \theta$ is constant.


Variable substitution
---------------------

Now, the trick is to introduce a new variable $u = \frac 1 r$ and to consider
its relation to $\theta$. This means wil will replace $r$, $\dot r$ and $\ddot
r$ with expressions involving $u(\theta)$. For short, we will use the following
notation:

$$
u' = \frac {\d u} {\d \theta}
\text{~and~}
u'' = \frac {\d^2 u} {\d \theta^2}
$$

First, we have:

$$
r = \frac 1 u
$$

Then, we look at the expression of $u'$:

$$
u'
= \frac {\d} {\d \theta} \frac 1 r
= \frac {\dt} {\d \theta} \frac {\d} {\dt} \frac 1 r
= \frac 1 {\dot \theta} \times \left(- \frac {\dot r} {r^2}\right)
= - \frac {\dot r} h
$$

From this, we get that:

$$
\dot r = - h u'
$$

Similarly, we develop the expression of $u''$:

\begin{align*}
u''
&= \frac {\d} {\d \theta} \left(- \frac {\dot r} h\right) \\
&= - \frac 1 h \frac {\dt} {\d \theta} \frac {\d} {\dt} \dot r \\
&= - \frac 1 h \frac 1 {\dot \theta} \ddot r \\
&= - \frac {\ddot r} {h \frac {h} {r^2}}
&&\text{~because~} h = r^2 \dot \theta \\
&= - \frac {\ddot r} {h^2 u^2}
\end{align*}

This let us know that:

$$
\ddot r = - h^2 u^2 u''
$$

Solving the equation
--------------------

We can now rewrite the equation by using $u$, $u'$ and $u''$:

\begin{align*}
\ddot r - r {\dot \theta}^2
&= - \frac {\mu} {r^2}
\\
- h^2 u^2 u'' - \frac 1 u (h u^2)^2
&= - \mu u^2
\\
- h^2 \strike{u^2} u'' - h^2 u^{\strike{3}}
&= - \mu \strike{u^2}
\\
u'' + u
&= \frac {\mu} {h^2}
\end{align*}

It can be shown that the solutions for this equation are of the form:

$$
u = \frac {\mu} {h^2} - A \cos(\theta - \theta_0)
$$

for some values of $A$ and $\theta_0$. Thus:

$$
r = \frac 1 {\frac {\mu} {h^2} - A \cos(\theta - \theta_0)}
$$

Now, if we assume $\theta_0 = 0$ and set $l = \frac {h^2} {\mu}$ and $e = \frac A p$, then:

$$
r = \frac l {1 - e cos(\theta)}
$$

<note>
$e$ is called the **eccentricity** and $l$ the **semi-latus rectum**
</note>


Shape
-----

From this expression of $r$ depending on $\theta$, we can vizualize the
possibles shapes for the trajectories of an objects only subjugated to
gravitation.

First, we notice that the semi-latus rectum, $l$, only affects the scale: the
larger $l$, the larger $r$, in all directions (all values of $\theta$). It
remains to look for the influence of the eccentricity, $e$.

First, notice that $\cos(\theta)$ is an **even** function. It means that
$\cos(- \theta) = \cos(\theta)$, for all values of $\theta$. It implies that
$r(\theta)$ is also even: the trajectory is symmetric along the axis where
$\theta = 0$ (also called the **major axis**).

Second, notice that $- \cos(\theta) = \cos(\theta + \pi)$. This means that
reverting the value of $e$ is the same as doing a $180 \deg$ rotation. For this
reason, we can restrict ourselves to non-negative values of $e$ ($e \geq 0$).

Now, let us look at different cases:

If we set $e = 0$, we get rid of most of the expression and end up with
$r(\theta) = l$. This means that the distance to the origin does not depend on
the direction; in other words, the trajectory is a **circle**.

Because of the fraction, we need to avoid its denominator, $1 - e \cos(\theta)$
to be zero. Since $-1 \leq \cos(\theta) \leq 1$, choosing $0 < e < 1$ will
ensure that $1 - e \cos(\theta) \neq 0$. That way, $r(\theta)$ is well defined
in all directions; it turns out the shape is that of an **ellipse**.

On the other hand, if we choose $e \geq 1$, we will encouter a discontinuity:
since $|\cos(\theta)|$ ranges from $0$ to $1$, there will be a values of
$\theta$ where $1 - e \cos(\theta) \leq 0$, which means an infinite or negative
value for $r(\theta)$. In practice this means that the object will never be in
that direction: this is a **hyperbola** (or **parabola**, in the edge case
where $e = 0$).

<figure>
\begin{tikzpicture}
% parameters
\pgfmathsetmacro{\pe}{2}
% axis
\node[boint=P] (P) at (0, 0) {};
% orbit
\orbit[red]{P}{\pe}{\pe}{0}{360};
\orbit[green]{P}{2*\pe}{\pe}{0}{360};
\horbit[blue]{P}{\pe}{1.5}{1};
\end{tikzpicture}
<figcaption>
orbital trajectories arount primary $\posit{P}$: circular orbit in red,
elliptic orbit in green, and hyperbolic orbit in blue
</figcaption>
</figure>

<note>
An object in free fall is always following an orbital trajectory around its
primary. It is actually said to be **in orbit** when that trajectory does not
intersect the surface (nor goes to deep into the atmosphere).

When the orbit is closed (circular or elliptical), the oject is said to be
**orbiting** its primary. When the orbit is open (hyperbolic or parabolic), the
trajectory is said to be:

* a **capture orbit** (or trajectory) when moving towards the periapsis
* an **escape orbit** (or trajectory) when moving away from it
</note>


Characterisitics
================

Apses
-----

We easily find the extremal value of $r$: the extremal values of $\cos(theta)$
are $-1$ and $1$, which means that $r$ varies between

* $r_{\text{per}} = \frac l {1 + e}$ and $r_{\text{ap}} = \frac l {1 - e}$ when $e < 1$
* $r_{\text{per}} = \frac l {1 + e}$ and $+\infty$ when $e \geq 1$

The point where $r = r_{\text{per}}$ is called the **periapsis** (*peri-* is
Greek for close), while the point where $r = r_{\text{ap}}$ is called the
**apoapsis** (*apo-* is Greek for far).

<note>
While the periapsis is always defined, the apoapsis may not, since an infinite
(or negative) altitude will never be reached.
</note>

When we want to be explicit about the object being orbited, we can use more
specific suffixes that -apsis. For instance, the **perigee** is the periapsis
of an object orbiting the Earth.

Body             Suffix
----             ------
Galactic center  -galacticon
Star             -astron
Sun              -helion
Mercury          -hermion
Venus            -cytherion
Earth            -gee
Moon             -lune, -cynthion, -selene
Mars             -areion
Jupiter          -zene, -jove
Saturn           -krone, -saturnium
Uranus           -uranion
Neptune          -poseidon
Pluto            -hadion

: Suffixes for various bodies

<note>
Various names come from Latin an Greek. For instance, Poseidon is the Greek god
of the ocean, while Neptune is the Roman equivalent. The suffix *-gee* is
related to Gaia, the Greek goddess of the Earth.
</note>


Angles
------

Astronomers use several ways to measure what are essentially angles.

The **true anomaly** is simply the angle $\angle{\theta}$ we have been using in
this chapter; it is also conventionally named $f$.  In the case of an object in
a non-circular orbit, this angle does not change uniformly. There are two
reasons:

1. similar changes in position will result in smaller changes in true anomaly
   the further $\posit{S}$ is from $\posit{P}$
2. the object is moving slower when it is far from $\posit{P}$

The first issue is solved by measuring the angle from the center $\posit{O}$,
and projecting the trajectory on a regular circle. This new angle is named the
**eccentric anomaly**, since it is measured *from* (*ex* in Latin) the
*center*. It is usually notated $\angle{E}$.

<figure>
\begin{tikzpicture}
% parameters
\pgfmathsetmacro{\a}{3}
\pgfmathsetmacro{\e}{0.7}
\pgfmathsetmacro{\pe}{\a*(1-\e)}
\pgfmathsetmacro{\ap}{\a*(1+\e)}
\pgfmathsetmacro{\f}{\e*\a}
\pgfmathsetmacro{\E}{60}  % eccentric anomaly
\pgfmathsetmacro{\true}{2*atan( sqrt((1+\e)/(1-\e)) * tan(\E/2) )}  % true anomaly
% axis
\node[boint=O] (O) at (0, 0) {};
\coordinate    (X) at (\a,0) {};
% orbit
\node[boint=P] (P) at (\f,0) {};
\orbit[red]{P}{\pe}{\ap}{0}{360};
\orbitpoint[roint={S}]{P}{\pe}{\ap}{\true}{S}{}
% true anomaly
\draw (X) -- (P) -- (S);
\markangle{X}{P}{S}{$\theta$}{0.5}
% eccentric anomaly
\draw (O) circle (\a);
\node[point=] (Z) at (S |- {0,0}) {};
\node[point=] (Y) at (\E:\a) {};
\draw[dotted] (Z) -- (Y);
\draw (X) -- (O) -- (Y);
\markangle{X}{O}{Y}{$E$}{0.5}
\end{tikzpicture}
<figcaption>
The orbital trajectory of $\posit{S}$ (in red) is projected to a circle (in
black) and the angle measured from $\posit{O}$ is the eccentric anomaly
$\angle{E}$.
</figcaption>
</figure>

As for the second issue, Kepler's equation defines a new quantity $M$, the
**mean anomaly**:

$$
M
= \angle{E} - e \sin(\angle{E})
$$

It can be shown that $M$ grows linearly with time. It means that we can easily
predict the mean anomaly of an object at time $\delay{t}$ as:

$$
M(\delay{t})
= M(\delay{0}) + n \times \delay{t}
$$

where $n$ is a constant value called the **mean motion**. By knowing the **mean
anomaly at epoch** $M(\delay{0})$ of an object as well as its mean motion, we
can retrieve its mean anomaly; we can then solve Kepler's equation to retrieve
$\angle{E}$, and then $\angle{\theta}$.


Orbital elements
----------------

The state of a mass-point is its position and velocity. In space, we need three
values for each the position and the velocity, for a total of six parameters.
The orbital elements are six such parameters that make it easy to also know the
orbit of an object.

First, we have seen that the eccentricity, $e$, determines the shape of the
orbit. Second, the semi-latus rectum determines the shape, but the periapsis
$\dist{r_{\text{per}}}$ conveys the same information (it is always defined),
and is more intuitive.

To tell where the object is on its orbit, we need an angle. The true anomaly is
intuitive, but does not change regularly through time; for this reason, we will
usually prefer the mean anomaly $M$.

We now need to rotate the orbit in its orbital plane. Since the periapsis is
not necessarily on the $x$ axis, we need an additional angle: the **argument of
periapsis** $\angle{\omega}$.

![
Three angles orient the periapsis in space, and a fourth gives the current
position of the object along its orbit. @orbitangles
](img/Orbit1.svg)

Our orbit is now fully determined in two dimension; we just need to orient the
orbital plane in space. For this, we will need to know the **inclnation**
$\angle{i}$, as well as where the inclination occurs.

The axis around which the orbit is inclined is named the **line of nodes**, and
the two points its intersection with the the orbit are called the **ascending
node** and the **descending node**. Their names corresponds to wether the
object is going up (along the $z$ axis) or down, when going through it. The
line of nodes is simply determined by the **longitude of ascending node**,
$\angle{\Omega}$.

To sum up, the six orbital elements are:

* periapsis, $\dist{r_{\text{per}}}$
* eccentricity $e$
* argument of periapsis $\angle{\omega}$
* inclination $\angle{i}$
* longitude of ascending node $\angle{\Omega}$
* mean anomaly $M$



*Vis viva* equation
===================

The *vis viva* equation is a simple relation between speed and distance, which
uses only one orbital characteristic.

The principle of energy conservation tells us that the total energy (kinetic
and potential energies) of an isolated system is constant:

$$
E
=
\underbrace{\frac 1 2 \mass{m} \speed{v}^2}_{\text{kinetic}}
\underbrace{- \frac {\mathcal G \mass{M} \mass{m}} {\dist{r}}}_{\text{potential}}
\text{~is constant}
\eqtag{eql:orbenergy}
$$

Let us consider this at the two most notable points of a closed orbit:
periapsis and apoapsis. At these points, the distance from center $\dist{r}$ is
extremal (and so is the altitude, or distance from surface); thus, $\speed{\dot
r} = 0$ in both situations. It comes that:

$$
\speed v
= \left| \speed{\dot{\vec r}} \right|
= \left| \speed{\dot r} \hat r + \dist{r} \dot \theta \hat \theta \right|
= \left| \dist{r} \dot \theta \hat \theta \right|
= \dist{r} \dot \theta
$$

Since we already know that $\dist{r}^2 \dot \theta$ is a constant value, it comes that:

$$
\dist{r_a} \speed{v_a} = \dist{r_p} \speed{v_p}
$$

Now, we apply the equation of energy (\ref{eql:orbenergy}) at both apses and
get:

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
and $\dist{a}$. If we use the equation of energy (\ref{eql:orbenergy}) again on
the with an arbitrary point with distance $\dist{r}$ and speed $\speed{v}$:

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
\speed{v}^2
&=
\mathcal G \mass{M} \left(
	\frac 2 {\dist{r}}
	-
	\frac 1 {\dist{a}}
\right)
\eqtag{eql:visviva}
\end{align*}

From this, we can easily determine the speed of an object from its distance to
the primary.


State prediction
================

Finding the position from the orbital parameters if relatively easy. First, we
can find the true anomaly $\angle{\theta}$ from the mean anomaly $M$. Then we
can retrieve the distance from the trajectory equation:

$$
\dist{r}
= \frac {\dist{l}} {1 - e \cos(\angle{\theta})}
$$

For this, we need $\dist{l}$, that we can easily find back using the fact that
$\dist{r_{\text{per}}} = \frac {\dist{l}} {1 + e}$. With this, we have the
polar coordinates $(\dist{r}, \angle{\theta})$ in the oriented orbital plane.

Then, it is only a matter of rotating around the proper axes ($\omega$ around
$(z)$, $i$ around $(x)$ and $\Omega$ around $(z)$) to find the coordinates in
the general frame of reference

Finding the velocity is very similar. We simply use the *vis viva* equation to
determine the speed.



Inferring an orbit
==================

We consider the inverse problem, where we want to determine the orbital
parameters from our current position $\posit{\vec r}$ and velocity $\speed{\vec
v}$.

First, let us define the **specific relative angular momentum** $\vec h =
\posit{\vec r} \times \speed{\vec v}$.  Since both $\posit{\vec r}$ and
$\speed{\vec v}$ are contained in the orbital plane and $\vec h$ is orthogonal
to both these vectors, it means that $\vec h$ is a **normal vector** of the
orbital plane. The angle between $\vec h$ and $(z)$ is the inclination
$\angle{i}$.

If we now compute $\vec n = \vec{u_z} \times \vec h$, we get a vector that is
both in the $(xOy)$ plane and in the orbital plane: this is the line of nodes.
The angle between $\vec n$ and $(x)$ is thus the longitude of ascending node,
$\angle{\Omega}$.

The **eccentricity vector** is defined as:

$$
\vec e
= \frac {\speed{\vec v} \times \vec h} {\mu} - \frac {\dist{\vec r}} {\dist{r}}
$$

It can be shown that its magnitude is the eccentricity and that it points
towards the periapsis. We can thus compute $e = \left|\vec e\right|$, set
$\omega$ as the angle between $\vec n$ and $\vec e$, and $\theta$ as the angle
between $\vec e$ and $\dist{\vec r}$.

It can be shown that $l = \frac {h^2} {\mu}$. Since we know the semi-latus
rectum $l$ and the eccentricity $e$, we know the periapsis
$\posit{r_{\text{per}}} = \frac {\dist{l}} {1 + e}$.
