---
title: Launch to orbit
date: 2016-07-24
---

> Can it be that you have come from outer space?
>
> — As a matter of fact, I have!
-- [Yuri Gagarin](https://en.wikipedia.org/wiki/Yuri_Gagarin),
first human being in space, to people near his landing site


Vertical ascent
===============

Thrust
------

From the Tsiolkovsky equation (\ref{eql:thrust}), we know that:

$$
\speed{\Delta v_t}
= - \speed{v_e} \ln\left(1 - \frac {\dot m} {\mass{m}(\delay{0})} \delay{t}\right)
$$

If we now assume that $\dot m$ (and thus the thrust) is constant:

\begin{align*}
\dist{\Delta x_t}
&= - \speed{v_e} \times \frac 1 {- \frac {\dot m} {\mass{m}(\delay{0})}}
\left(
	\left(1 - \frac {\dot m} {\mass{m}(\delay{0})} \delay{t}\right)
	\ln\left(1 - \frac {\dot m} {\mass{m}(\delay{0})} \delay{t}\right)
	+ \frac {\dot m} {\mass{m}(\delay{0})} \delay{t}
\right) \\
& = \speed{v_e}
	\left(\frac {\mass{m}(\delay{0})} {\dot m} - \delay{t}\right)
	\ln\left(1 - \frac {\dot m} {\mass{m}(\delay{0})} \delay{t}\right)
	+ \speed{v_e} \delay{t}
\end{align*}

This gives us the displacement done by the thrust of the engines.

Gravity
-------

Let us notate $\mu = \mathcal G \mass{M}$ the gravitational parameter of the
body our rocket is landed at, $\dist{R}$ the radius of that body, and
$\dist{z}$ the current altitude of the rocket. As long as $\dist{z} \ll
\dist{R}$, the acceleration due to gravity will be:

$$
\accel{a_g}
= \frac {\mu} {(\dist{R} + \dist{z})^2}
\simeq \frac {\mu} {\dist{R}^2}
$$

<note>
The approximation $\dist{z} \ll \dist{R}$ is verified on large bodies since we
will usually aim for a low orbit topping the atmosphere. On small bodies, the
gravity as well as the atmosphere will usually be negligible.
</note>

Then, integrating twice:

$$
\dist{\Delta x_g}
= \frac 1 2 \delay{t}^2 \times \accel{a_g}
$$

This is the displacement due to gravity.

General expression
------------------

We now compare the graphs for the different approaches (ignoring gravity,
constant gravity, or numerical approximation). To get actual values, we
simulate a basic rocket made of the following parts:

* Command Pod Mk1
* FL-T800 Fuel Tank
* LV-T30 Liquid Fuel Engine

<note>
We could see more clearly the contrast between the different situations by
using a large pod (Mk1-2 Command Pod) instead. However, such a rocket will not
go as high.
</note>

<figure>
\begin{tikzpicture}[scale=0.69]
\foreach \b [
	count=\i,
	evaluate=\i as \x using {mod(\i-1,2)*\linewidth*2},
	evaluate=\i as \y using {-floor((\i-1)/2)*\linewidth*3},
] in {Earth, Kerbin, Moon, Mun} {
	\begin{axis}[
		no markers,
		axis lines=left,
		xlabel=$\text{\Large\b~}\delay{t}$,
		x unit=s,
		ylabel=$\dist{z}$,
		y unit=m,
		legend style={
			cells={anchor=west},
			legend pos=north west,
		},
		at={(\x,\y)},
	]
	\addlegendentry{$\force{F}=\force{0}$}
	\addlegendentry{$\force{F}=\frac {\mathcal G \mass{M} \mass{m}} {\dist{R}^2}$}
	\addlegendentry{$\force{F}=\frac {\mathcal G \mass{M} \mass{m}} {(\dist{R}+\dist{z})^2}$}
	\foreach \y in {zn,zg,zG}
	{
		\addplot table [y=\y] {data/ascent_\b.dat};
	}
	\end{axis}
}
\end{tikzpicture}
<figcaption>
Here, $\force{F}$ is the model used for gravity: we either ignore it
($\force{0}$), assume it is a constant ($\frac {\mathcal G \mass{M} \mass{m}}
{\dist{R}^2}$), or use the exact formula ($\frac {\mathcal G \mass{M} \mass{m}}
{(\dist{R}+\dist{z})^2}$). From the graphs, we see that assuming that the
gravity is constant ($z \ll R$) makes for a good approximation. Moreover, on
small bodies (c) (d), gravity has a very limited impact on such short periods.
</figcaption>
</figure>



Atmospheric drag
================

Definition
----------

An object moving through a fluid (gaz or liquid) pushes matter around; by the
principle of action-reaction, the object will be subjected to an opposing
force. We are only interested in two effects of this: **drag**, which is the
**prograde** component (along the velocity vector), and **lift**, a **normal**
component.

For now, we will assume an axial symmetry around the velocity vector. In other
words, we make it so as not to generate lift. It has been measured that the
force of drag was of the form:

$$
\force{F_d}
= \frac 1 2 \rho \times C_d \area{A} \times \speed{v}^2
$$

where $\rho$ is the density of air and $C_d$ and $\area{A}$ are aerodynamics
factors dependent on the shape of the ship.


Terminal velocity
-----------------

Let us consider a falling object subjected only to gravitation and atmospheric
drag. Gravitation is a constant force oriented downwards; here, drag is a force
oriented upwards and growing with speed. There will hthus be a point where
gravitation and drag balances and speed becomes constant. This speed is named
**terminal velocity**.

When terminal velocity is reached, $\speed{\dot z}$ is constant so
$\accel{\ddot z}$ is null and:

\begin{align*}
\accel{\ddot z} = 0
&\Leftrightarrow \accel{a_g} = \accel{a_d} \\
&\Leftrightarrow \force{F_g} = \force{F_d} \\
&\Leftrightarrow \frac 1 2 \rho \times C_d \area{A} \times \speed{v_{\text{term}}}^2 = \mass{m} \accel{g} \\
&\Leftrightarrow \speed{v_{\text{term}}} = \sqrt{\frac {2 \mass{m} \accel{g}} {\rho C_d \area{A}}}
\end{align*}

<note>
In Kerbal Space Program pre-1.0, \area{A} used to be computed as
$\frac 1 {125} ~\area{m^2}/\mass{kg} \times \mass{m}$. This means that the terminal
velocity only depended on the air density $\rho$ and the coefficient of drag
$C_d$ (usually about 0.2).

$\frac {\mass{m}} {125 \mass{kg} / \area{m^2}}$. This means that the terminal

This is not realistic since, according to the square-cube law, mass tends to
grow cubically while area tends to grow quadratically: larger ships should
experience *proportionally* less drag.

The new aerodynamic model ("drag cubes") avoids this issue.
</note>

Ascent optimal speed
--------------------

Since drag grows with speed, we face the problem of aiming for an ascent speed
that minimizes the time of ascent (implying a higher speed) as well as the drag
(implying a lower speed).

Ultimately, we are trying to minimize the cost in propellant, measured in
$\speed{\Delta v}$ to reach an altitude $\posit{\Delta z}$. If we assume
$\speed{v}$ is constant, then so is $\force{F_d}$ (as well as $\force{F_g}$
from above), and:

\begin{align*}
\speed{\Delta v}
&= (\accel{a_g} + \accel{a_d}) \delay{\Delta t} \\
&= \left(\frac {\force{F_d}} {\mass{m}} + \accel{g}\right) \delay{\Delta t} \\
&= \left(\frac 1 2 \rho C_d \times \area{A} \times \speed{v}^2 + \mass{m} \accel{g} \right) \frac 1 {\mass{m}} \frac {\dist{\Delta z}} {\speed{v}} \\
&= \underbrace{\left(
	\frac 1 2 \rho C_d \area{A} \speed{v} + \mass{m} \accel{g} \frac 1 {\speed{v}}
\right) }_{f(\speed{v})} \dist{\Delta z}
\end{align*}

To find the minimum of $\speed{\Delta v}$, we try to minimize $f(\speed{v})$:

\begin{align*}
f(\speed{v}) \text{~min}
&\Rightarrow f'(\speed{v}) = 0 \\
&\Rightarrow \frac 1 2 \rho C_d \area{A} - \mass{m} \accel{g} \frac 1 {\speed{v}^2} = 0 \\
&\Rightarrow \frac 1 2 \rho C_d \area{A} - \mass{m} \accel{g} \frac 1 {\speed{v}^2} = 0 \\
&\Leftrightarrow \speed{v} = \sqrt{\frac {2 \mass{m} \accel{g}} {\rho C_d \area{A}}} \\
&\Leftrightarrow \speed{v} = \speed{v_{\text{term}}}
\end{align*}

From this, we see that the optimal vertical ascent speed is the terminal
velocity.


Air pressure
------------

Assume the atmosphere is in a stable state and consider an infenitesimal volume
$\vol{\d V}$. The force exerted on it are the gravity and the pressure
surrounding it. By symmetry, the effects of horizontal pressure cancels out; we
note $\d P$ the difference in pressure below and above $\vol{\d V}$.

<figure>
\begin{tikzpicture}[->]
\node (O) at (0,0) {$\vol{\d V}$};
\draw[dist,->] (-2.5,-1) node[right]{$z$} -- (-2.5,1) node[right]{$z + \d z$};
\draw (O) circle (0.5);
\draw (-2,0) -- node[above]{$P$} (-1,0);
\draw ( 2,0) -- node[above]{$P$} ( 1,0);
\draw (0, 2) -- node[right]{$P + \d P$} (0, 1);
\draw (0,-3) -- node[right]{$P$} (0,-1);
\end{tikzpicture}
<figcaption>
The pressure below $\vol{\d V}$ must be stronger to fight gravity. $\d P$ will
be a negative value, so that we can keep the vertical axis orientation up
</figcaption>
</figure>

The resultant force of pressure on $\vol{\d V}$ is $\area{\d A} \d P$ where
$\area{\d A}$ is the bottom area of $\vol{\d V}$. We have $\vol{\d V} =
\area{\d A} \dist{\d z}$. To fight gravity, we must have $\area{\d A} \d P = -
\accel{g} \mass{\dm} = - \accel{g} \rho \vol{\d V}$. We can divide by $\vol{\d
V}$ on both hands of the equations to get:

$$
\frac {\d P} {\dist{\d z}} = - \rho \accel{g}
$$

The value $\accel{g}$ can assumed to be a constant but $\rho$ depends on
$\posit{P}$. According to the ideal gas law:

$$
P\vol{V} = n RT
\Rightarrow
\rho
= \frac {n {\mass{M}}} {\vol{V}}
= \frac {P {\mass{M}}} {RT}
$$

where $\vol{V}$ is the considered volume, $n$ the number of molecules of gas in
it, $R$ a convenient constant, $T$ the temperature and $\mass{M}$ the mean mass
of a molecule of the gas. From this, we can deduce the following differential
equation:

$$
\frac {\d P} {\dist{\d z}} = - \frac {\accel{g} \mass{M}} {RT} P
$$

To solve it, we need to find a primitive. We will assume that the gravitation
is constant and that the temprature decrease linearly with altitude (rate $L$).

$$
\int_{\dist{0}}^{\dist{z}} \frac {\accel{g} \mass{M}} {RT} \dist{\d z}
= \frac {\accel{g} \mass{M}} R
  \int_{\dist{0}}^{\dist{z}} \frac 1 {T - L\dist{z}} \dist{\d z}
= - \frac {\accel{g} \mass{M}} {LR}
  \left[ \ln (T-L\dist{z}) \right]_{\dist{0}}^{\dist{z}}
= - \frac {\accel{g} \mass{M}} {LR}
  \ln \left(1 - \frac {L\dist{z}} {T}\right)
$$

Thus:

$$
P(\dist{z})
= P_0 e^{\frac {\accel{g} \mass{M}} {LR} \ln \left(1 - \frac {L\dist{z}} {T}\right)}
= P_0 \left(1 - \frac {L\dist{z}} {T}\right)^{- \frac {\accel{g} \mass{M}} {LR}}
$$


Evolution of terminal velocity
------------------------------

Using the closed expression for the pressure, we can now derive the density and
then the terminal velocity depending on the altitude:

<figure>
\begin{tikzpicture}
\pgfmathsetmacro{\Pz}{101325}
\pgfmathsetmacro{\L}{0.0065}
\pgfmathsetmacro{\Tz}{288.15}
\pgfmathsetmacro{\g}{9.80665}
\pgfmathsetmacro{\M}{0.0289644}
\pgfmathsetmacro{\R}{8.31447}
\pgfmathsetmacro{\Rsp}{287.058}
\pgfmathsetmacro{\H}{\R*\Tz/\g/\M}
\pgfmathsetmacro{\m}{1000}
\pgfmathsetmacro{\A}{0.008*\m}
\pgfmathsetmacro{\Cd}{0.2}
\pgfmathdeclarefunction{p}{1}{\pgfmathparse{\Pz*(1 - \L*#1/\Tz)^(\g*\M/\R/\L)}}
%\pgfmathdeclarefunction{p}{1}{\pgfmathparse{\Pz*exp(-#1/\H)}}
\pgfmathdeclarefunction{T}{1}{\pgfmathparse{\Tz - \L * #1}}
\pgfmathdeclarefunction{rho}{1}{\pgfmathparse{p(#1)/\Rsp/T(#1)}}
\pgfmathdeclarefunction{vterm}{1}{\pgfmathparse{sqrt(2*\g*\m/rho(#1)/\A/\Cd)}}
\begin{axis}[
	domain=0:30000,
	samples=\samples,
	no markers,
	axis lines=left,
	xlabel=$\dist{h}$,
	x unit=m,
	ylabel=$\rho$,
	y unit=kg/m\^3,
	legend style={
		cells={anchor=west},
		legend pos=north west,
	},
	scaled ticks=false,
	yticklabel style={/pgf/number format/fixed},
]
\addplot[black] {p(x)};
\end{axis}
\begin{axis}[
	domain=0:30000,
	samples=\samples,
	no markers,
	axis lines=left,
	axis y line=right,
	ylabel=$\speed{v_{\mathrm{term}}}$,
	y unit=m/s,
	scaled ticks=false,
	yticklabel style={/pgf/number format/fixed},
]
\addplot[speed] {vterm(x)};
\end{axis}
\end{tikzpicture}
<figcaption>
Terminal velocity increases as air density decreases; notice that the terminal
velocity at the surface is about \speed{100~m/s} in this example
</figcaption>
</figure>



Insertion burn
==============

Principle
---------

Once the spacecraft has left the atmosphere, it is not subject to air drag
anymore and can set its orbit. For this, it simply need to raise its orbit from
the center of the body to above the atmosphere. It is more convenient for
further maneuvers to have a circular orbit.

<figure>
\begin{tikzpicture}
\def\R{2}
\def\h{0.5}
\def\ap{3}
\def\pea{0.1}
\def\peb{3}
\def\an{-7}
\node[loint=O] (O) at (0,0) {};
\path[
	right color=blue!5,
	left color=blue!5!black!10,
]
(O) circle (\R+\h);
\orbit[red]{O}{\ap}{\pea}{-180}{\an};
\path[
	right color=blue!20,
	left color=blue!20!black,
]
(O) circle (\R);
\orbitpoint[boint=P]{O}{\ap}{\pea}{\an}{}{};
\orbit[red,dotted]{O}{\ap}{\pea}{\an}{360+\an};
\orbit[blue]{O}{\ap}{\peb}{-180}{180};
\orbitpoint[roint=B]{O}{\ap}{\peb}{0}{}{};
\end{tikzpicture}
<figcaption>
When $\posit{P}$ leaves the atmosphere and burns in $\posit{B}$, it can change
from the \textcolor{red}{red} “orbit” to the \textcolor{blue}{blue} orbit.
</figcaption>
</figure>


Classical burn
--------------

Using the *vis-viva* equation (\ref{eql:visviva}), we can compute the requisite
speed for orbiting:

$$
\speed{v}^2
=
\mathcal G \mass{M} \left(\frac 2 {\dist{r_a}} - \frac 2 {\dist{r_a}+\dist{r_a}}\right)
=
\frac {\mathcal G \mass{M}} {\dist{r_a}}
$$

For example, on Kerbin, you need to reach an horizontal velocity of:

$$
\speed{v_{\text{orbit}}}
=
\sqrt{\frac {6.67 \times 10^{11}~m^3/kg/s^2 \times \mass{5.29 \times 10^{22}~kg}} {\dist{600~km} + \dist{80~km}}}
=
\speed{2279~m/s}
$$

<note>
To save $\speed{\Delta v}$, launches are done close to the equator to go with
the movement of the surface due to the body's rotation. On Kerbin, we save
($\delay{T}$ is the orbital period):

$$
\speed{v_{\text{surf}}}
=
\frac {2\pi \dist{R}} {\delay{T}}
=
\speed{174.5~m/s}
$$
</note>


Gravity turn
------------
