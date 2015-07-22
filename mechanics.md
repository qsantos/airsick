---
title: Mechanics
date: 2015-07-11
---

> Every body continues in its state of rest, or of uniform motion in a right
> line, unless it is compelled to change that state by forces impressed upon
> it.
-- [Isaac Newton](https://en.wikipedia.org/wiki/Isaac_Newton), discoverer of
the laws of [motion](https://en.wikipedia.org/wiki/Newton's_laws_of_motion)
and [gravitation](https://en.wikipedia.org/wiki/Newton's_law_of_universal_gravitation)

Referential
===========

A referential is the object you use as a landmark (origin) to keep track of
interesting points. A system of coordinates if the kind of data you use to
store the position of these points relatively to the origin.

Cartesian coordinates
---------------------

Cartesian coordinates are the most common. You basically choose two directions
on give the how much you have to go on each coordinate to get from the origin
to the point.

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
$\posit{P}$ is at coordinates $\posit{(1,2)}$ in this referential
</figcaption>
</figure>

Cartesian coordinates can be used in three dimensions by adding one axis
(usually notated $z$).


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


Polar coordinates
-----------------

We define the polar base as $(\hat r, \hat \theta) = ((\cos \angle{\theta},
\sin \angle{\theta}), (-\sin \angle{\theta}, \cos \angle{\theta}))$. It means
that the point $(\angle{\theta}:\dist{r})$ has Cartesian coordinates $r(\cos
\angle{\theta}, \sin \angle{\theta})$. First, we remark that:

$$
\left\{
\begin{aligned}
\frac {\d} {\dt} \hat r      &= \dot \theta (- \sin \angle{\theta},   \cos \angle{\theta}) = \dot \theta \hat \theta \\
\frac {\d} {\dt} \hat \theta &= \dot \theta (- \cos \angle{\theta}, - \sin \angle{\theta}) = - \dot \theta \hat r \\
\end{aligned}
\right.
$$

Then, when we derive a vector in polar base, we get:

$$
\speed{\dot {\vec r}}
= \frac {\d} {\delay{\dt}} \Big(\dist{r} \hat r\Big)
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

If we consider a point-mass $(\posit{P}, \mass{m})$ which is subjected to
forces $\force{\vec F}$. Note that $\force{\vec F}$ represent the sum of all
the forces exerted on $\posit{P}$.

$$
\accel{\vec a} = \frac 1 {\mass{m}} \force{\vec F}
$$

<remark>
When $\force{\vec F} = 0$, the acceleration is null as well and the speed is
constant (in practise, there are forces of friction, which slows objects down).
This is Newton's first law (chapter quote).
</remark>



Shell theorem
=============

We consider a sphere of center $\posit{C}$, radius $\dist{R}$ and uniform
density $\mu$ whose center is at distance $\dist{r}$ of mass point
$(\mass{m},\posit{P})$. We wish to infer the force $\vec g$ exerted by
$\posit{C}$ on $\posit{P}$. We will use spherical coordinates and center the
referential on $\posit{P}$ since it is the one point not moving when
integrating.

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

Because of the symmetry around the axis $(PC)$, we already know that $\vec g$
will be in the same direction as $\dist{\overrightarrow{PC}}$.

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
&= \mathcal G \underbrace{\frac 4 3 \pi \dist{R}^3}_{= \mass{M}} \times \frac 1 {\dist{r}^2}
\end{align*}

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



Sphere of incluence
===================

Consider spherical bodies $(\posit{P_1}, \mass{M_1})$ and $(\posit{P_2},
\mass{M_2})$ and a point-mass $(\posit{P}, \mass{m})$ between those two
($\posit{P} \in [\posit{P_1}, \posit{P_2}]$). We want to estimate how much
$\posit{P_1}$ amounts in the gravitation forces exerted on $\posit{P}$.
According to the previous section we don't need to know the radius of the
bodies and can just pretend they are point-masses as well. The intensity of
forces $\force{F_1}$ and $\force{F_2}$ respectively exerted by $\posit{P_1}$
and $\posit{P_2}$ are:

$$
\force{F_1} = \mathcal G \frac {\mass{M_1} \mass{m}} {\dist{P_1 P}^2}
\text{~and~}
\force{F_2} = \mathcal G \frac {\mass{M_2} \mass{m}} {\dist{P_2 P}^2}
$$

Thus, with $\dist{r} = \dist{P_1 P}$ and $\dist{P_2 P} = \dist{P_1 P_2}
- \dist{r}$:

$$
\frac {\force{F_1}} {\force{F_2}}
= \frac {\mass{M_1} (\dist{P_1 P_2} - \dist{r})^2} {\mass{M_2} \dist{r}^2}
= \frac {\mass{M_1}} {\mass{M_2}} \left(\frac {\dist{P_1 P_2}} {\dist{r}} - 1\right)^2
$$

So, if we want $F_1$ to be at least $p$ of the exerted force, we want:

\begin{align*}
\frac {\force{F_1}} {\force{F_1} + \force{F_2}} \ge p
& \Leftrightarrow 1 + \frac {\force{F_2}} {\force{F_1}} \le p^{-1} \\
& \Leftrightarrow \frac {\force{F_1}} {\force{F_2}} \ge \frac 1 {p^{-1} - 1} \\
& \Leftrightarrow \frac {\mass{M_1}} {\mass{M_2}} \left(\frac {\dist{P_1 P_2}} {\dist{r}} - 1\right)^2 \ge \frac 1 {p^{-1} - 1} \\
& \Leftrightarrow \frac {\dist{P_1 P_2}} {\dist{r}} - 1 \ge \sqrt{\frac 1 {p^{-1} - 1} \frac {\mass{M_2}} {\mass{M_1}}} \\
& \Leftrightarrow \frac {\dist{r}} {\dist{P_1 P_2}} \le \frac 1 {1 + \sqrt{\frac 1 {p^{-1} - 1} \frac {\mass{M_2}} {\mass{M_1}}}} \\
\end{align*}

$\force{F_1} = \mathcal G \frac {\mass{M_1} \mass{m}} {\dist{a}^2}$

$\force{F_2} = \mathcal G \frac {\mass{M_2} \mass{m}} {\dist{r}^2}$

\begin{align*}
\force{F_1} = \force{F_2}
& \Leftrightarrow \frac {\mass{M_1}} {\dist{a}^2} = \frac {\mass{M_2}} {\dist{r}^2} \\
& \Leftrightarrow \dist{r} = \dist{a} \sqrt{\frac {\mass{M_2}} {\mass{M_1}}} \\
\end{align*}



Thrust
======

Set up
------

We consider a rocket with center of mass $\posit{R}$. From $\delay{t}$ to
$\delay{t}+\delay{dt}$, it ejects $\mass{\dm}$ of its fuel with relative
velocity $\speed{v_e}$; its center of mass is notated $\posit{F}$. We will use
$\posit{G}$ to refer to the center of mass of the system containing both the
rocket and the ejected fuel.


Derivation of exerted force
---------------------------

At time $\delay{t}$, we have $\speed{v_G}(\delay{t}) = \speed{v_R}(\delay{t}) =
\speed{v_F}(\delay{t})$ so, at time $\delay{t}+\delay{dt}$:

\begin{align*}
\speed{v_R}(\delay{t}+\delay{\dt}) \times \mass{m}
+
\speed{v_F}(\delay{t}+\delay{\dt}) \times \mass{\dm}
&=
\speed{v_G}(\delay{t}+\delay{\dt}) \times (\mass{m}+\mass{\dm})
\\
%
%
\speed{v_R}(\delay{t}+\delay{\dt}) \times (\mass{m}+\mass{\dm})
+
\speed{v_e} \times \mass{\dm}
&=
\speed{v_G}(\delay{t}+\delay{\dt}) \times (\mass{m}+\mass{\dm})
& \text{~with~} \speed{v_F} = \speed{v_R} - \speed{v_e}
\\
%
%
\speed{v_R}(\delay{t}+\delay{\dt}) \times \mass{m}
+
\speed{v_e} \times \mass{\dm}
&=
\speed{v_G}(\delay{t}+\delay{\dt}) \times \mass{m}
& \text{~because~} \mass{m}+\mass{\dm} \simeq \mass{m}
\\
%
%
\speed{v_R}(\delay{t}+\delay{\dt}) \times \mass{m}
+
\speed{v_e} \times \mass{\dm}
&=
\speed{v_R}(\delay{t}) \times \mass{m}
+
\force{F} \delay{\dt}
& \text{~with~} \speed{v_G}(\delay{t}+\delay{\dt}) = \speed{v_G}(\delay{t}) + \accel{\dot {v_G}} \delay{\dt}
\\
%
%
\frac {\speed{v_R}(\delay{t}+\delay{\dt}) - \speed{v_R}(\delay{t})} {\delay{\dt}}
&=
- \speed{v_e} \times \frac {\mass{\dm}} {\delay{\dt}} \times \frac 1 {\mass{m}} + \frac {\force{F}} {\mass{m}}
& \text{~by dividing by~} \delay{\dt}
\\
%
%
\mass{m} \accel{\dot {v_R}}
&=
\underbrace{- \speed{v_e} \dot m}_{\force{F_t}}
+ \force{F}
\eqtag{eql:accel}
\end{align*}


Specific impulse
----------------

In KSP, the engines are defined by their maximum thrust $\force{F_t}$ and their
$\delay{I_{\mathrm{sp}}}$ (“atmosphereCurve” in config files). The SPecific
Impulse is just the force exerted per unit (in weight) of fuel used, i.e.
$\delay{I_{\mathrm{sp}}} = \frac {\force{F_t}} {\dot m \accel{g}}$. Thus:

$$
\begin{array}{lr}
\dot m
= \frac {\force{F_t}} {\delay{I_{\mathrm{sp}}} \times \accel{g}}
,
&
\speed{v_e}
= - \delay{I_{\mathrm{sp}}} \times \accel{g}
\end{array}
$$


Tsiolkovsky rocket equation
---------------------------

We can now integrate (\ref{eql:accel}) to get the velocity change of a rocket:

\begin{align*}
\speed{\Delta v}
&= \int_{\delay{0}}^{\delay{t}} \accel{\dot{v_R}} \delay{\dt} \\
&= \int_{\delay{0}}^{\delay{t}} \left(
	- \speed{v_e} \frac {\dot m} {\mass{m}}
	+ \frac {\force{F}} {\mass{m}}
\right) \delay{\dt} \\
&= \left[- \speed{v_e} \ln(\mass{m})\right]_{\delay{0}}^{\delay{t}}
+ \underbrace{
	\int_{\delay{0}}^{\delay{t}} \frac {\force{F}} {\mass{m}} \delay{\dt}
}_{\speed{I}_{\force{F}}(\delay{t})} \\
&= \speed{v_e} \ln \frac {\mass{m}(\delay{0})} {\mass{m}(\delay{t})} + \speed{I}_{\force{F}}(\delay{t})
\eqtag{eql:thrust}
\end{align*}

This formula is usually applied when $\force{F}$ can be ignored (e.g. in
orbit). Note that, during ascent, $\frac {\force{F}} {\mass{m}} = - \frac
{\mathcal G \mass{M}} {(R + z)^2}$ leads to a quadratic differential equation
of second order which is difficult to solve.

Conversely, we can compute the amount of fuel to eject to reach a given speed:

$$
\mass{\Delta m} = \mass{m} \left(1 - e^{-\frac {\speed{\Delta v}} {\speed{v_e}}}\right)
$$