---
title: Mechanics
date: 2015-07-28
---

> Every body continues in its state of rest, or of uniform motion in a right
> line, unless it is compelled to change that state by forces impressed upon
> it.
-- [Isaac Newton](https://en.wikipedia.org/wiki/Isaac_Newton), discoverer of
the laws of [motion](https://en.wikipedia.org/wiki/Newton's_laws_of_motion)
and [gravitation](https://en.wikipedia.org/wiki/Newton's_law_of_universal_gravitation)

Mechanics is the study of movement. In this chapter, we will describe how
physicists study the movement of physical objects using mathematical laws. With
this knowledge, we will then see how this is relevant to rocket science.

Referential
===========

Origin
------

The first thing we want to do is to find a way to describe **where** objects
are. For this, we will elect an object (an actual physical object or just an
arbitrary virtual point in space) to be fixed, and consider all movements
relative to this **origin**.


Dimensions
----------

If all the objects are on a same line (for instance a race track), then we can
describe the position of each object with a single measure: the distance from
the origin. Since a single measure is sufficient, a line is said to have one
dimension.

If all the objects are on a same surface (for instance, on a checkboard), then
we need two numbers to fully describe the position of any of these objects. For
example, we may arrange items on a grid a tell their positions as the row and
column numbers; we can locate a location on the surface of the Earth using
longitude and latitude. Since two measures are needed, a surface is said to
have two dimensions.

<important>
There are many ways to choose how to describe the position of an object. For
instance, rather than using the row and column number, we could use the
distance from the center and the angle formed with a fixed line. When we say
"there are two dimensions", the "two dimensions" do not refer to any particular
measures, but to the necessity of two different ones. There are many choices of
two measures to describe two dimensions.
</important>

Finally, we can consider an arbitrary location in space, which needs three
dimensions. For example, if we add altitude to longitude and latitude, we can
easily locate any object.

A referential is the object we use as a landmark (origin) to keep track of
interesting points. A system of coordinates if the kind of data you use to
store the position of these points relatively to the origin.

The most common set of measures used in two dimensions are the **Cartesian
coordinate** and the **polar coordinate** systems. The Cartesian coordinate
system extend to three dimensions naturally; there are two ways to extend the
polar coordinates system to a third dimension: the **cylindrical coordinate**
and the **spherical coordinate** systems.


Cartesian coordinates
---------------------

Cartesian coordinates are the most common. We basically choose two (or three,
in space) directions, and the measures describes how much you have to go each
way to get from the origin to the point.

<figure>
\begin{tikzpicture}
\def \axlen {3}
\def \x {1}
\def \y {2}
\node[boint=O]  (O) at (0,0) {};
\node[point=P]  (P)  at (\x,\y) {};
\node[boint=\x] (Px) at (\x,0) {};
\node[loint=\y] (Py) at (0,\y) {};
\draw[thick,->] (O) -- (\axlen,0) node[anchor=west] {$x$};
\draw[thick,->] (O) -- (0,\axlen) node[anchor=south]{$y$};
\draw (P) edge[dashed] (Px);
\draw (P) edge[dashed] (Py);
\end{tikzpicture}
<figcaption>
$\posit{P}$ is at coordinates $\posit{(1,2)}$ in this referential: to go from
origin $\posit{O}$ to $\posit{O}$, we have to go along direction $\vec x$ for
$1$ unit, and along direction $\vec y$ for $2$ units
</figcaption>
</figure>

The directions used in Cartesian coordinates (the axes) are usually
perpendicular and conventionally named $x$ and $y$, (and $z$)).

### Derivatives

A nice property of the Cartesian coordinate system is that, if we are
interested in the variation of some point $\posit{P}$ with Cartesian
coordinates $(x, y)$, we can simply consider the **vector** (x, y).

<note>
While a point denotes an offset from the origin, a vector denotes an offset
from an unspecified point.
</note>


Polar coordinates
-----------------

Polar coordinates work in two dimensions. One value is simply the distance to
the origin while a second is the angle of $\posit{P}$ with a fixed
porientation.

<figure>
\begin{tikzpicture}
\def \R  {3}
\def \th {40}
\node[point=O] (O) at (0,0) {};
\node          (X) at (0:\R) {};
\node[point=P] (P) at (\th:\R) {};
\draw (O) -- (X);
\draw (O) -- node[above left]{$\dist{r}$} (P);
\markangle{X}{O}{P}{$\theta$}{\R/3};
\end{tikzpicture}
<figcaption>
The polar coordinates of $\posit{P}$ are $\posit{(r,\theta)}$
</figcaption>
</figure>

### Derivative

Consider a point $\posit{P}$ given in polar coordinates $(\angle{\theta},
\dist{r})$. We can use the corresponding Cartesian coordinates: $\posit{P} =
(\dist{r} \cos(\angle{\theta}), \dist{r} \sin(\angle{\theta}))$. Then we can
derive on each Cartesian coordinate using the derivation rules for function
composition.

If we define $\hat r =  = (\cos \angle{\theta}, \sin \angle{\theta})$ and $\hat
\theta = (-\sin \angle{\theta}, \cos \angle{\theta}))$, then:

$$
\left\{
\begin{aligned}
\frac {\d} {\dt} \hat r
&= (- \dot \theta \sin \angle{\theta}, \dot \theta \cos \angle{\theta})
= \dot \theta \hat \theta \\
\frac {\d} {\dt} \hat \theta
&= (- \dot \theta \cos \angle{\theta}, - \dot \theta \sin \angle{\theta}) = - \dot \theta \hat r \\
\end{aligned}
\right.
$$

Now, $\posit{P}$ is at an offset $\posit{\vec r}$ to the origin, where:

$$
\posit{\vec r}
= (\dist{r} \cos(\angle{\theta}), \dist{r} \sin(\angle{\theta}))
= \dist{r} \hat r
$$

thus:

$$
\speed{\dot {\vec r}}
= \frac {\d} {\delay{\dt}} \Big(\dist{r} \hat r\Big)
= \hat r \frac {\d} {\delay{\dt}} \dist{r}
+ \dist{r} \frac {\d} {\delay{\dt}} \hat r
= \speed{\dot r} \hat r + \dist{r} \dot \theta \hat \theta
$$

By deriving again, we get the acceleration:

$$
\accel{\ddot {\vec r}}
= \frac {\d} {\delay{\dt}} \Big(\speed{\dot r} \hat r + \dist{r} \dot \theta \hat \theta\Big)
= (\accel{\ddot r} - \dist{r} {\dot \theta}^2) \hat r
  + (2 \speed{\dot r} \dot \theta + \dist{r} \ddot \theta) \hat \theta
$$


Spherical coordinates
---------------------

Spherical coordinates are simply the generalization of polar coordinates to
three dimensions. To the usual coordinates $\posit{r}$ and $\angle{\theta}$, we
add a third one, $\angle{\phi}$, which is the angle with the polar plane:

<figure>
\begin{tikzpicture}[tdplot_main_coords]
\def \r  {4}
\def \th {30}
\def \ph {60}
\node[loint=O]  (O) at (0,0,0) {};
\draw[thick,->] (O) -- (4,0,0) node[anchor=north east]{$x$};
\draw[thick,->] (O) -- (0,4,0) node[anchor=north west]{$y$};
\draw[thick,->] (O) -- (0,0,4) node[anchor=south]{$z$};
\tdplotsetcoord{P}{\r}{\th}{\ph}
\draw[red,-stealth] (O) -- (P) node[above right] {$P$};
\draw[red,dashed]   (O) -- (Pxy);
\draw[red,dashed]   (P) -- (Pxy);
\tdplotsetthetaplanecoords{\ph}
\tdplotdrawarc                       {(O)}{1}{0}{\ph}{anchor=north}     {$\phi$}
\tdplotdrawarc[tdplot_rotated_coords]{(O)}{2.5}{0}{\th}{anchor=south west}{$\theta$}
\end{tikzpicture}
<figcaption>
The spherical coordinates of $\posit{P}$ are $\posit{(r,\theta,\phi)}$
</figcaption>
</figure>



Newtonian mechanics
===================

Center of mass
--------------

For the sake of simplicity, we will pretend that objects are simple points
(e.g. $\posit{P}$) associated to their mass (e.g. $\mass{m}$); such points
(e.g. $(\posit{P},\mass{m})$) are called mass-points. For a given object, the
point we will use is called the center of mass (CoM). It is easy to find for
regular and uniform objects (e.g. a sphere).

We will usually refer to the position $\posit{P}$ by using the vector
$\dist{\vec r} = \dist{\overrightarrow{OP}}$. The velocity is simply the
derivative of the position: $\speed{\vec v} = \speed{\dot{\vec r}}$; the
acceleration is the derivative of the velocity: $\accel{a} = \accel{\dot{\vec
v}} = \accel{\ddot{\vec r}}$.


Newton's second law
-------------------

Consider a mass-point $(\posit{P}, \mass{m})$ subjected to forces $\force{\vec
F_1}, \force{\vec F_2}, \dots$. We need not consider every force independentely
and can sum them as the **resultant force** $\force{\vec F} = \sum \force{\vec
F_i}$.

Then, according to Newton's second law:

$$
\accel{\vec a} = \frac 1 {\mass{m}} \force{\vec F}
$$

This equation means several things. First, it means that an object on which is
exerted a non-zero resultant force will be accelerated (acceleration
encompasses the slowing down of an object). Second, the more mass it has, the
less it will accelerate; since this is perceived as a resistance to movement,
we call this inertia.

<note>
When $\force{\vec F} = 0$, the acceleration is null as well. Thus, the speed is
constant; this is Newton's first law (chapter quote).
</note>


Gravitation
-----------

The gravitational force is one of the four fundamental forces that physicist
have identified, along with the electromagnetic, weak and strong forces.

Gravitation says that any two objects with a mass attract each other, at any
distance.  Since it is extremely feeble, we do not observe it within common
objects. It becomes perceptible when huge masses are grouped together; for
instance, we observe an apple falling because of the vast mass of the Earth
effecting the apple.

The amount of force exerted by an object of mass $\mass{M}$ over an object of
mass $\mass{m}$ is:

$$
\force{F}
= \mathcal G \frac {\mass{M} \mass{m}} {\dist{r}^2}
$$

where $\dist{r}$ is the distance between the two objects.

<note>
The object of mass $\mass{m}$ attracts the object of $\mass{M}$ with the exact
same mount of force. The reason the Earth does not seem to move towards a falling
apple is because of inertia (see Newton's second law).
</note>



Shell theorem
=============

Problem
-------

We are interested in knowing the gravitation exerted by a celestial body
$\posit{C}$ (i.e. the gravity). We will assume the celestial body is a ball of radius
$\dist{R}$ and uniform density $\mu$  and consider a mass-point $(\mass{m},
\posit{P})$ at distance $\dist{r}$ from $\posit{C}$:

<figure>
\begin{tikzpicture}
\def \r  {5}
\def \R  {2}
\def \th {40}
\draw (0,0) circle (\R);
\node[point={C,\mu}]         (C) at (0, 0)   {};
\node[point={P,\mass{m}}]    (P) at (\r,0)   {};
\node[point={Q,\mass{\d m}}] (Q) at (\th:\R) {};
\draw (C) -- node[below]{$\dist{r}$} (P);
\draw (P) -- node[above]{$\dist{s}$} (Q);
\draw (Q) -- node[above]{}  (C);
\markangle{C}{P}{Q}{$\psi$}{1}
\markangle{Q}{C}{P}{$\theta$}{1}
\end{tikzpicture}
</figure>


Elementary force
----------------

The usual way to solve a large problem is to split it in smaller problems and
solve those instead. Here, to find the total force exerted, we will split the
spherical body in many mass points $(\posit{Q}, \mass{\d m})$.

The force exerted by $\posit{Q}$ over $\posit{P}$ is oriented along $\dist{\vec
{QP}}$ and has magnitude:

$$
\force{F}
= \accel{\vec{\d g}} \mass{m}
= \mathcal G \frac {\mass{m} \mass{\d m}} {\dist{PQ}^2}
$$

Another way to write this is:

$$
\accel{\vec{\d g}}
= \mathcal G \frac {\mu \vol{\d V}} {\dist{s}^2}
$$

where $\dist{s}$ is just $\dist{PQ}$


Symmetry
--------

Now, to simplify things, we can notice the axial symmetry of the whole
situation around $(CP)$. This means that the resultant force $\accel{\vec g}$
can only be along the axis $(CP)$: no other could be justified without breaking
the symmetry.

Thus, we can only choose to only consider the effect of $\posit{Q}$ along
$(CP)$; the others effect will cancel out. The effect of gravitation from
$\posit{Q}$ exerted on $\posit{P}$ along $(CP)$ is:

$$
\accel{\vec{\d g}} \cdot \frac {\dist{\vec{PC}}} {\dist{PC}}
= \mathcal G \frac {\mu \vol{\d V}} {\dist{s}^2} \times \cos{\angle{\psi}}
$$

where $\angle{\psi}$ is the angle $\hat{CPQ}$.


Integrating
-----------

Now, it is only a matter of integrating. We first extend the elementary volume
$\vol{\d V}$ in spherical coordinates as $(\dist{\rho} \sin \angle{\psi}
\angle{\d \theta}) (\dist{\rho} \angle{\d \psi})$. Then we just need to do a
substitution and to cancel out terms.

\begin{align*}
\accel{g}
&= \iiint_S \d \accel{\vec g} \cdot \frac {\dist{\overrightarrow{PC}}} {\dist{PC}} \\
%
&= \iiint \frac {\mathcal G \mu \vol{\d V}} {\dist{s}^2} \cos \angle{\psi} \\
%
&= \mathcal G \mu
   \int_{\dist{\rho}=\dist{\rho_-}}^{\dist{\rho^+}}
   \int_{\angle{\psi}=\angle{0}}^{\angle{\alpha}}
   \int_{\angle{\theta}=\angle{0}}^{\angle{2\pi}}
   \frac {\cos \angle{\phi}} {\dist{\rho}^2}
   \times (\dist{\d \rho})
   (\dist{\rho} \sin \angle{\psi} \angle{\d \theta}) (\dist{\rho} \angle{\d \psi}) \\
%
&= 2\pi \mathcal G \mu
   \int_{\dist{\rho}=\dist{\rho_-}}^{\dist{\rho^+}}
   \int_{\angle{\psi}=\angle{0}}^{\angle{\alpha}}
   \cos \angle{\psi} \sin \angle{\psi} \angle{\d \psi} \dist{\d \rho} \\
%
&= 2\pi \mathcal G \mu
   \int_{\angle{\psi}=\angle{0}}^{\angle{\alpha}}
   2 \sqrt{\dist{R}^2 - \dist{r}^2 \sin^2 \angle{\psi}}
   \cos \angle{\psi} \sin \angle{\psi} \angle{\d \psi} \dist{\d \rho}
\eqtag{eql:before}
\\
%
&= 4\pi \mathcal G \mu
   \int_{\dist{u}=\strike[green]{\dist{R}}}^{\strike[green]{\dist{0}}}
   \dist{u}
   \sqrt{\strike[blue]{1} - \frac {\strike[blue]{\dist{R}^2-\dist{u}^2}} {\dist{r}^2}}
   \frac {\strike[red]{\sqrt{\dist{R}^2-\dist{u}^2}}} {\dist{r}}
   \frac {\strike[green]{-}\dist{u}} {
	 \strike[blue]{\sqrt{\dist{r}^2 - \dist{R}^2 + \dist{u}^2}}
	\strike[red]{\sqrt{\dist{R}^2 - \dist{u}^2}}
   } \dist{\d u}
\eqtag{eql:after}
\\
%
&= 4\pi \mathcal G \mu
   \frac 1 {\dist{r}^2}
   \int_{\dist{0}}^{\dist{R}}
   \dist{u}^2 \dist{\d u} \\
%
&= \mathcal G \mu \underbrace{\frac 4 3 \pi \dist{R}^3}_{= \vol{V}} \times \frac 1 {\dist{r}^2}
\end{align*}


Result
------

In the end, $\accel{g} = \mathcal G \frac {\mass{M}} {\dist{s}^2}$. It means
that, the resultant gravitation force exerted by a planet is the same as the
mass-point in the center with the same mass, even when close to it.

This will make all considerations involving the gravitation of a planet
relatively easy, as long as we assume it is spherical and uniform.


Details on the substitution
---------------------------

To get from (\ref{eql:before}) to (\ref{eql:after}), we substitute $\dist{u} =
\sqrt{\dist{R}^2 - \dist{r}^2\sin^2\angle{\psi}}$ for $\angle{\psi}$. This
means that $\angle{\psi} = \arcsin \frac {\sqrt{\dist{r}^2 - \dist{u}^2}}
{\dist{r}}$ and subsequently:

$$
\angle{\d \psi}
= \frac 1 {\sqrt{1 - \frac {\dist{R}^2-\dist{u}^2} {\dist{r}^2}}}
  \times \frac {-2 \dist{u} \dist{\d u}} {2 \dist{r} \sqrt{\dist{R}^2 - \dist{u}^2}}
= - \frac {\dist{u}} {
	\sqrt{\dist{r}^2
	- \dist{R}^2
	+ \dist{u}^2} \sqrt{\dist{R}^2
	- \dist{u}^2}
} \dist{\d u}
$$

We then use the relations $\sin(\arcsin x) = x$ and $\cos(\arcsin x) = \sqrt{1
- x^2}$ for $0 \leq x \leq \frac {\pi} 2$.


Sphere of influence
===================

Patched conics
--------------

In reality, an object travelling through space is influenced by all moons,
planets and stars of the universe. Even when restricting to the closest moon,
closest planet and closest star, the combined influence of several bodies is
hard to take into account simultaneously.

A simple approximation is to only consider the body with the most influence.
The region where a celestial body has the most influence is called the **sphere
of influence**. When leaving the sphere of influence of one body, we transition
to that of another. The trajectory is then made of two parts (two conics),
hence the name **patched conics** approximation.


Influences
----------

We will consider two mass-points $(\posit{P_1}, \mass{M_1})$ and $(\posit{P_2},
\mass{M_2})$ and look at their influences on a mass-point $(\posit{P},
\mass{m})$ between them.

The intensity of forces $\force{F_1}$ and $\force{F_2}$ respectively exerted by
$\posit{P_1}$ and $\posit{P_2}$ are:

$$
\force{F_1} = \mathcal G \frac {\mass{M_1} \mass{m}} {\dist{P_1 P}^2}
\text{~and~}
\force{F_2} = \mathcal G \frac {\mass{M_2} \mass{m}} {\dist{P_2 P}^2}
$$

For short, we define $\dist{r} = \dist{P_1 P}$ and $\dist{R} = \dist{P_1 P_2}$.
Thus, $\dist{P_2 P} = \dist{P_1 P_2} - \dist{P_1 P} = \dist{R} - \dist{r}$. We
also define $\mu_1 = \mathcal G \mass{M_1}$ and $\mu_2 = \mathcal G \mass{M_2}$
(the **gravitational parameters**). The accelerations due to each are:

$$
\accel{g_1} = \frac {\mu_1} {\dist{r}^2}
\text{~and~}
\accel{g_2} = \frac {\mu_2} {(\dist{R} - \dist{r})^2}
$$

The acceleration exerted by $\posit{P_1}$ over $\posit{P_2}$, and by
$\posit{P_2}$ over $\posit{P_1}$ are respectively:

$$
\accel{g_{1,2}} = \frac {\mu_1} {\dist{R}^2}
\text{~and~}
\accel{g_{2,1}} = \frac {\mu_2} {\dist{R}^2}
$$

Perturbations
-------------

Now, if we look at the acceleration of $\posit{P}$ **relatively**  to
$\posit{P_1}$, it is **perturbed** by the fact that $\posit{P_2}$ does not
exert the same acceleration over $\posit{P}$ and over $\posit{P_1}$. The
absolute perturbation is $\accel{g_2} - \accel{g_{2,1}}$ (the difference in
acceleration from $\posit{P_2}$).

In practice, this value only makes sense when compared to the **main**
acceleration $\accel{g_1}$. Here, we will assume that $\dist{r} \ll \dist{R}$;
it makes sense when $\posit{P_1}$ is an object significantly smaller than
$\posit{P_2}$. We define the relative perturbation $Q_1$ as:

$$
Q_1
= \frac {\accel{g_2} - \accel{g_{2,1}}} {\accel{g_1}}
= \frac {\frac {\mu_2} {(\dist{R} - \dist{r})^2} - \frac {\mu_2} {\dist{R}^2}} {\frac {\mu_1} {\dist{r}^2}}
= \frac {\dist{r}^2} {\dist{R}^2} \frac {\mu_2} {\mu_1} \left(\frac 1 {\left(1 - \frac {\dist{r}} {\dist{R}}\right)^2} - 1\right)
$$

Now, it can be shown that, when $x$ is small, $\frac 1 {(1 - x)^2} = 1 + 2 x +
3 x^2 + \dots \simeq 1 + 2 x$. With $x = \frac {\dist{r}} {\dist{R}}$ we get
that:

$$
Q_1
= \frac {\dist{r}^2} {\dist{R}^2} \frac {\mu_2} {\mu_1} \times 2 \frac {\dist{r}} {\dist{R}}
= 2 \frac {\dist{r}^3} {\dist{R}^3} \frac {\mu_2} {\mu_1}
$$

Similarly, the relative perturbation due to $\posit{P_1}$ when looking at the
acceleration of $\posit{P}$ relatively to $\posit{P_2}$ is:

$$
Q_2
= \frac {\accel{g_1} - \accel{g_{1,2}}} {\accel{g_2}}
= \frac {\frac {\mu_1} {\dist{r}^2} \strike{- \frac {\mu_1} {\dist{R}^2}}} {\frac {\mu_2} {(\dist{R} \strike{- \dist{r}})^2}}
= \frac {\mu_1} {\mu_2} \frac {\dist{R}^2} {\dist{r}^2}
$$

Again, we use the fact that $x \ll X$ to simplify the expression.


Radius of influence
-------------------

Now, we are interested in the point $\posit{P}$ between $\posit{P_1}$ and
$\posit{P_2}$ where both relative perturbations are of the same magnitude. We
thus solve:

\begin{align*}
Q_1 = Q_2
&\Leftrightarrow
2 \frac {\dist{r}^3} {\dist{R}^3} \frac {\mu_2} {\mu_1}
= \frac {\mu_1} {\mu_2} \frac {\dist{R}^2} {\dist{r}^2}
\\
&\Leftrightarrow
\dist{r}
= \frac 1 {2^{\frac 1 5}} \dist{R} \left(\frac {\mu_1} {\mu_2}\right)^{\frac 2 5}
= 2^{- \frac 1 5} \dist{R} \left(\frac {\mass{M_1}} {\mass{M_2}}\right)^{\frac 2 5}
\end{align*}

<note>
The $2^{- \frac 1 5}$ factor seems to be forgotten often. Since its value is
about 0.87, it is still the right order of magnitude.
</note>



Thrust
======

Propulsion
----------

A car can push along the road thanks to friction; a plane can generate lift
from air and speed; a balloon can use buoyancy in the atmosphere.  However, a
rocket needs to be able to operate in the vacuum of outer space, which implies
no physical object to push against.

Articulating an object into space will not move its center of mass. It means
that a rocket can only gain speed by interacting with the exterior. Thus, the
only way a rocket can accelerate is by throwing parts of its mass out. This is
exactly what their exhaust do: it ejects lots of mass (propellant) down, so
that the rocket will lift up.

<note>
Technically, outer space is not empty: light from the Sun is theoretically
enough for the low-thrust propulsion of **solar sails**.
</note>


Conserved momentum
------------------

We consider a **r**ocket with center $\posit{R}$ of mass $\mass{m}$. From
$\delay{t}$ to $\delay{t}+\delay{\dt}$, it ejects $\mass{\dm}$ of its
**p**ropellant ($\posit{P}$) with relative (**exhaust**) velocity
$\speed{v_e}$.

Let us notate $\posit{G}$ the center of mass of the system $\{\posit{R},
\posit{P}\}$. Since the system did not interact with its environment, the speed
of $\posit{G}$ remains unchanged by the ejection. However, since $\posit{P}$ is
moving downwards, it means the rocket have gained speed.

![
Before time $\delay{t}$, $\posit{R}$ and $\posit{P}$ are moving together. Then,
$\posit{P}$ is ejected downwards at speed $\speed{v_e}$. Since the **momentum**
of the pair $\{\posit{R}, \posit{P}\}$ has not changed, it means that the
rocket has gained some speed upwards.
](img/rocket_exhaust.svg)


Exerted force
-------------

We are interested in the changes of speed $\speed{\d v_R}$ and $\speed{\d v_P}$
from $\delay{t}$ to $\delay{t+dt}$. If we do not take into account external
forces, then $\speed{\d v_g} = 0$. Thus:

\begin{align*}
0
&= \speed{\d v_G} \\
&= \speed{\d v_R} \mass{m} + \speed{\d v_P} \mass{\d m} \\
&= \speed{\d v_R} (\mass{m} + \mass{\d m}) + \speed{v_e} \mass{\d m}
&& \text{~because~} \speed{v_P} = \speed{v_R} - \speed{v_e} \\
\end{align*}

Dividing by $\delay{dt}$ and with $\mass{m+\d m} \simeq \mass{m}$, it follows
that:

$$
\mass{m} \frac {\d \speed{v_r}} {\delay{\dt}} = - \speed{v_e} \frac {\mass{\d m}} {\delay{\dt}}
$$

We finally get the expression of the thrusting force:

$$
\force{F_t} = \mass{m} \accel{a_R} = - \speed{v_e} \dot m
\eqtag{eql:accel}
$$

Specific impulse
----------------

In KSP, the engines are defined by their maximum thrust $\force{F_t}$ and their
$\delay{I_{\mathrm{sp}}}$ (“atmosphereCurve” in configuration files). The
**sp**ecific **i**mpulse is just the force exerted per unit (in weight) of fuel
used, i.e.  $\delay{I_{\mathrm{sp}}} = \frac {\force{F_t}} {\dot m \accel{g}}$.
Thus:

$$
\begin{array}{lr}
\dot m
= \frac {\force{F_t}} {\delay{I_{\mathrm{sp}}} \times \accel{g}}
\text{~and~}
&
\speed{v_e}
= - \delay{I_{\mathrm{sp}}} \times \accel{g}
\end{array}
$$


Tsiolkovsky rocket equation
---------------------------

We can now integrate equation (\ref{eql:accel}) to get the velocity change of a
rocket over a long period of time:

\begin{align*}
\speed{\Delta v}
&= \int_{\delay{0}}^{\delay{t}} \accel{\dot{v_R}} \delay{\dt} \\
&= \int_{\delay{0}}^{\delay{t}} - \speed{v_e} \frac {\dot m} {\mass{m}} \delay{\dt} \\
&= \left[- \speed{v_e} \ln(\mass{m})\right]_{\delay{0}}^{\delay{t}} \\
&= \speed{v_e} \ln \frac {\mass{m}(\delay{0})} {\mass{m}(\delay{t})}
\eqtag{eql:thrust}
\end{align*}

Conversely, we can compute the amount of propellant $\mass{\Delta m}$ to eject
to bring a mass $\mass{m}$ to a given speed:

$$
\mass{\Delta m} = \mass{m} \left(1 - e^{-\frac {\speed{\Delta v}} {\speed{v_e}}}\right)
$$
