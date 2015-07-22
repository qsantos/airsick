---
title: Launch to orbit
date: 2015-07-11
---

> Can it be that you have come from outer space?
>
> — As a matter of fact, I have!
-- [Yuri Gagarin](https://en.wikipedia.org/wiki/Yuri_Gagarin),
first human being in space, to people near his landing site


Vertical ascent
===============

General expression
------------------

Assume that $\dot m$ is constant. Using (\ref{eql:thrust}), it comes that:

$$
\speed{\Delta v}
= - \speed{v_e} \ln\left(1 - \frac {\dot m} {\mass{m}(\delay{0})} \delay{t}\right)
  + \speed{I}_{\force{F}}(\delay{t})
$$

And integrating once more:

\begin{align*}
\dist{z}
&= - \speed{v_e} \times \frac 1 {- \frac {\dot m} {\mass{m}(\delay{0})}}
\left(
	\left(1 - \frac {\dot m} {\mass{m}(\delay{0})} \delay{t}\right)
	\ln\left(1 - \frac {\dot m} {\mass{m}(\delay{0})} \delay{t}\right)
	+ \frac {\dot m} {\mass{m}(\delay{0})} \delay{t}
\right) + \underbrace{
	\int_{\delay{0}}^{\delay{t}} \speed{I}_{\force{F}}(\delay{t}) \delay{\dt}
}_{\dist{J}_{\force{F}}(\delay{t})} \\
& = \speed{v_e}
	\left(\frac {\mass{m}(\delay{0})} {\dot m} - \delay{t}\right)
	\ln\left(1 - \frac {\dot m} {\mass{m}(\delay{0})} \delay{t}\right)
	+ \speed{v_e} \delay{t}
+ \dist{J}_{\force{F}}(\delay{t})
\end{align*}


Gravity
-------

If we assume $z \ll R$, we can estimate the effect of gravity $\force{F} = -
\frac {\mathcal G \mass{M} \mass{m}} {(R+z)^2} \simeq \mass{m} \accel{g}$ and
$\dist{J}_{\mass{m} \accel{g}} = \frac 1 2 \accel{g} \delay{t}^2$.

The approximation is close enough for large bodies such as Earth or even
Kerbin. On smaller bodies, there is no atmosphere and the ascent is not a
problem. To verify this however, we will use (\ref{eql:thrust}) to get:

$$
\accel{\ddot z}
= - \speed{v_e} \frac {\dot m} {\mass{m}(\delay{0}) - \dot m \delay{t}} - \frac {\mathcal G \mass{M}} {(\dist{R}+\dist{z})^2}
$$

We will then proceed to a numerical approximation:

$$
\left\{
\begin{aligned}
\dist{z}(\delay{0})
&= \dist{0} \\
%
\speed{\dot z}(\delay{0})
&= \speed{0} \\
%
\accel{\ddot z}(\delay{t})
&= - \speed{v_e} \frac {\dot m} {\mass{m}(\delay{0}) - \dot m \delay{t}} - \frac {\mathcal G \mass{M}} {(\dist{R}+\dist{z}(\delay{t}))^2} \\
%
\speed{\dot z}(\delay{t} + \delay{\dt})
&= \speed{\dot z}(\delay{t}) + \delay{\dt} \accel{\ddot z}(\delay{t}) \\
%
\dist{z}(\delay{t} + \delay{\dt})
&= \dist{z}(\delay{t}) + \delay{\dt} \speed{\dot z}(\delay{t})
\end{aligned}
\right.
$$


Graphs
------

We now compare the graphs for the different approaches (ignoring gravity,
constant gravity, or numerical approximation). To get actual values, we
simulate a basic rocket made of the following parts:

* Command Pod Mk1
* FL-T800 Fuel Tank
* LV-T30 Liquid Fuel Engine

<remark>
We could see more clearly the contrast between the different situations by
using a large pod (Mk1-2 Command Pod) instead. However, such a rocket will not
go as high.
</remark>

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
We can see that the assumption that $z \ll R$ is safe enough; moreover, the
effect of gravity on small bodies (c) (d) is negligible on such short periods
of time.
</figcaption>
</figure>



Atmospheric drag
================

Definition
----------

Atmospheric drag exerts a force opposite to the velocity with intensity:

$$
\force{F_D}
= \frac 1 2 \rho \speed{v}^2 C_d \area{A}
$$

where $\rho$ is the density of air and $C_d$ and $A$ are aerodynamics factors.


Terminal velocity
-----------------

When terminal velocity is reached, $\speed{\dot z}$ is constant so
$\accel{\ddot z}$ is null and:

$$
\force{F_D} = \mass{m} \accel{g}
\Leftrightarrow
\speed{v} = \sqrt{2\frac {\mass{m} \accel{g}} {\rho C_d \area{A}}}
$$


Optimal speed
-------------

Equation (\ref{eql:thrust}) shows us that if we want to optimize fuel
consumption, we can simply reason on $\speed{\Delta v}$.

$$
\speed{\Delta v}
= (\force{F_D} + \mass{m} \accel{g}) \delay{\Delta t}
= \left(\frac 1 2 \rho \speed{v}^2 C_d \area{A} + \mass{m} \accel{g}\right) \frac {\dist{\Delta z}} {\speed{v}}
= \left(
	\underbrace{\frac 1 2 \rho C_d \area{A}}_{C_1} \speed{v} +
	\underbrace{\mass{m} \accel{g}}_{\force{C_2}} \frac 1 {\speed{v}}
\right) \dist{\Delta z}
$$

Now we define $f(\speed{v}) = C_1 \speed{v} + \frac {\force{C_2}} {\speed{v}}$
and find its minimum. Its derivative is $f'(v) = C_1 - \frac {\force{C_2}}
{\speed{v}^2}$. It comes that the minimum is $\speed{v} = \sqrt{\frac
{\force{C_2}} {C_1}}$.  It matches the terminal velocity.


Derivation of air pressure
--------------------------

Assume the atmosphere is in a stable state and consider an infenitesimal volume
$\vol{\d V}$. The force exerted on it are the gravity and the pressure
surrounding it. By symmetry, the effects of horizontal pressure cancels out; we
note $\d P$ the difference in pressure below and above $\vol{\d V}$.

<figure>
\begin{tikzpicture}[->]
\node (O) at (0,0) {$\vol{\d V}$};
\draw (O) circle (0.5);
\draw (-2,0) -- node[above]{$P$} (-1,0);
\draw ( 2,0) -- node[above]{$P$} ( 1,0);
\draw (0,-3) -- node[right]{$P$} (0,-1);
\draw (0, 2) -- node[right]{$P$} (0, 1);
\draw (0,-3) -- node[right]{$P - \d P$} (0,-1);
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
\begin{axis}[
	no markers,
	axis lines=left,
	xlabel=$\dist{h}$,
	x unit=m,
	ylabel=$\rho$,
	y unit=kg/m^3,
	legend style={
		cells={anchor=west},
		legend pos=north west,
	}
]
\addlegendentry{$\rho(h)$}
\addplot[blue] table [y=rho] {data/air_density.dat};
\end{axis}
\begin{axis}[
	no markers,
	axis lines=left,
	axis y line=right,
	ylabel=$\speed{v_{\mathrm{term}}}$,
	y unit=m/s,
]
\addlegendentry{$\speed{v_{\mathrm{term}}}(\dist{h})$}
\addplot[red] table [y=v]   {data/air_density.dat};
\end{axis}
\end{tikzpicture}

<figcaption>
The terminal velocity quickly rises after \dist{30~km}
</figcaption>
</figure>



Gravity turn
============

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

<remark>
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
</remark>