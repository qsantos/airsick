---
title: Basics
date: 2015-07-11
---

> Imagination will often carry us to worlds that never were. But
> without it we go nowhere.
-- [Carl Sagan](https://en.wikipedia.org/wiki/Carl_Sagan),
popular atrophysicist

Units
=====

Dimensions
----------

There exist different units for each kind of measure (e.g. \dist{distance} in
\dist{meters}, \dist{feet}, etc. To avoid confusion, we agreed on which units
should be prefered; they are called SI Units (for *Système International*,
International System).

Dimension         SI unit        Other units
---------         -------        -----------
\angle{angle}     radian (-)     turn (-), degree (°)
\delay{duration}  second (s)     hour (h), day (d), year (y)
\dist {distance}  meter (m)      feet, miles, light-year (ly)
\speed{speed}     m/s            km/h, knot
\mass {mass}      kilogram (kg)  ton, pound
       pressure   pascal (Pa)    atmosphere (atm)

<remark>
A \dist{light} year is the distance that a particle of light can travel in a
\delay{year}. For comparison, it takes light a little more than \delay{eight
minutes} (\delay{8~min}) to get from the Sun to the Earth, meaning that the Sun
is \dist{8~light-minutes} away from the Earth. Kerbin is about
\dist{45~light-seconds} away from Kerbol.
</remark>


Prefixes
--------

We are used to refer to \dist{10,000 meters} (\dist{m}) as \dist{10 kilometers}
(\dist{km}). “kilo-” is a prefix meaning “thoussand”; it is the most used
prefix but others exist:

kilo- (k-)  mega- (M-)  giga- (G-)  tera- (T-)
----------  ----------  ----------  ----------
10³         10⁶         10⁹         10¹²

: Common prefixes

<remark>
There are also prefixes to decrease the value of an unit:

milli- (m-)  micro- (µ-)  nano- (n-)  pico- (p-)
-----------  -----------  ----------  ----------
10⁻³         10⁻⁶         10⁻⁹        10⁻¹²

: Smaller prefixes

</remark>

Conversion
----------

We sometimes need to switch the unit used for a measure. For example, let us
convert $\speed{50~km/h}$ to SI units. We know that $\dist{km} = \dist{1000~m}$
and $\delay{h} = \delay{3600~s}$ so:

$$
\speed{50~km/h}
= 50 (\dist{1000~m})/(\delay{3600~s})
= 50 \times 1000 / 3600 ~\speed{m/s}
= \speed{14~m/s}
$$

This particular example shows how easy it is to include units in computations.
As we will see below, having the units is useful when considering more complex
expressions.


Addition (and substraction)
---------------------------

An addition can only be done with the same kind of measure (e.g. a distance can
only be summed with another distance). This is seems obvious, but simply
checking that the values that are being some are actually of the same kind can
help locate errors early and save tremendous amounts of time. Now, consider the
following operation:

$$
\dist{x} = \dist{2~ly} + \dist{4,730.3~Tm}
$$

We do not know how to sum arbitrary units (for instance \dist{m} with
\mass{kg}). However, we do know that that $\dist{ly} = \dist{9.4607~Tm}$. Thus,
we can replace it in the expression:

\begin{align*}
\dist{x}
&= 2 \times \dist{ly} + \dist{4,730.3~Tm} \\
&= 2 \times \dist{9.4607~Tm} + \dist{4,730.3~Tm} \\
&= (18.92146 + 4,730.3) \dist{Tm} \\
&= \dist{23.6518~Tm}
\end{align*}

Conversely, we could also have said that $\dist{Tm} = \dist{1/9.4607~ly}$ and
then:

\begin{align*}
\dist{x}
&= \dist{2~ly} + \dist{4,730.3~Tm} \\
&= \dist{2~ly} + (4,730.3 / 9.4607) \dist{ly} \\
&= (2 + 0.5) \dist{ly} \\
&= \dist{2.5~ly}
\end{align*}

Of course, the two ways are equivalent and we can check that $\dist{2.5~ly} =
\dist{23.6518~Tm}$.


Multiplication (and division)
-----------------------------

We can create new units pretty easily. For example, if some object travels a
distance $\dist{d} = \dist{15~m}$ in a duration $\delay{t} = \delay{3~s}$, we
can define the velocity $\speed{v} = \dist{d} / \delay{t} = \dist{15~m} /
\delay{3~s} = \speed{5~m/s}$. Conversely, assume the object has traveled at a
velocity $\speed{50~km/h}$ for a duration $\delay{30~s}$; then, the distance it
has gone through is:

$$
\dist{d}
= \speed{v} \times \delay{t}
= (\speed{50~km/h}) \times (\delay{30~s})
= 14~\speed{m/s} \times 30~\delay{s}
= (14 \times 30) (\dist{m}/\strike[red]{\delay{s}} \times \strike[red]{\delay{s}})
= \dist{417~m}
$$

By doing the operations on both the numerical values and the units, we know
what our result is: in this case, it's a distance, and it is expressed in
meters.



Functions
=========

<figure>
\begin{tikzpicture}[->]
\node[point=O] (O) at (0,0) {};
\node          (E) at (5,0) {x};
\node[point=C] (C) at (3,0) {};
\draw (O) -> (E);
\end{tikzpicture}
<figcaption>$\posit{C}$ is moving towards the right at speed $\speed{v}$</figcaption>
</figure>

Let us consider a car $\posit{C}$ moving along a straight road at a speed of
$\speed{v}$ (e.g. $\speed{50~km/h}$). The position of the car, $\posit{C}$, can
be determined by the distance from $\posit{C}$ to an arbitrary fix point
$\posit{O}$ (the **origin**). We will note this distance $\dist{x}$ and we have
thus $\dist{x} = \dist{OC}$.

Say we are interested in the variations of the position of the car as time
changes and say write the current time $\delay{t}$ as the delay since the car
was at the origin ($\posit{C} = \posit{O}$).

In other words, we are interested in $\dist{x}$ as a **function** of
$\delay{t}$. After some time $\delay{t}$ has passed (e.g. $\delay{t} =
delay{10~s}$), we know that $\dist{x} = \speed{v} \times \delay{t}$. We write
it:

$$
\dist{x}(\delay{t}) = \speed{v} \times \delay{t}
$$

This notation gives us a general formula to compute $\dist{x}$ for any given
value of $\delay{t}$. For example:

$$
\dist{x}(\delay{1~h})
= \speed{50~km/h} \times \delay{1~h}
= \dist{50~km}
$$

As another example, it is known that the intensity of the light emitted by a
star decreases proportionnaly to the square of the distance to the star. This
can be written as:

$$
L(\dist{r}) = \frac C {\dist{r}^2}
$$

where $C$ is some **constant** value (i.e. independent from $\dist{r}$) which
is to be determined experimentally.



Derivatives
===========

Definition
----------

Assume we know the position $\dist{x}(\delay{t})$ of the car for any instant
$\delay{t}$ and we want to determine the velocity of the car at a given instant
$\delay{t_0}$.

<figure>
\begin{tikzpicture}
\begin{axis}[
	samples=\samples,
	domain=0:5,
	ticks=none,
	no markers,
	axis lines=left,
	xlabel=$\delay{t}$,
	ylabel=$\dist{x}$,
	clip=false,
]
\addplot+[color=green]{examplepos(x)};
\node[roint=A] (A) at (axis cs:4, {examplepos(4)}) {};
\node[boint={\delay{t_0}}] (t) at (A |- {0,0}) {};
\node[loint={\dist{x}(\delay{t_0})}] (x) at (A -| {0,0}) {};
\draw[dashed] (t) -- (A) -- (x);
\end{axis}
\end{tikzpicture}
<figcaption>
The horizontal axis represents the passage of time, the vertical axis the
position. The blue line shows the current position of the current at every
instant. We are interested in the instant $\delay{t_0}$; this is notated
$\posit{A}$ on the graph.
</figcaption>
</figure>

The velocity is a the **variation** of position through time. Thus, to know how
fast the car is going at time $\delay{t_0}$, we need to look at the position of
the car at two different instants. We already have $\delay{t_0}$; let us also
consider $\delay{t_0+h}$ for some arbitrary value $\delay{h}$.

The difference in position between instants $\delay{t_0}$ and $\delay{t_0+h}$
is thus $\dist{x}(\delay{t_0+h}) - \dist{x}(\delay{t_0})$; a shorter notation
for this is $\dist{\Delta x}(\delay{t_0})$. The value $\delay{h}$ is not shown
because we do not really care about it. The Greek letter $\Delta$, for $d$, is
generally used to denote a **d**ifference (here, the difference in position).

Notice that, the bigger $\delay{h}$, the bigger we expect this difference to
be; to compensate for this, we will divide by how much time has passed, which
is to say $\delay{t_0+h} - \delay{t_0} = \delay{\Delta t_0}$:

$$
\frac {\dist{\Delta x}(\delay{t_0})} {\delay{\Delta t_0}}
$$

This value is the **mean velocity** from instant $\delay{t_0}$ to instant
$\delay{t_0+h}$. However, the mean velocity is a value that only gives a
general idea of the speed on some period of time. In this duration, the
**instant velocity** (actual speed) can very a lot and the mean velocity would
then be far off to these values.

<figure>
\begin{tikzpicture}
\begin{axis}[
	samples=\samples,
	domain=0:5,
	ticks=none,
	no markers,
	axis lines=left,
	xlabel=$\delay{t}$,
	ylabel=$\dist{x}$,
	clip=false,
]
\addplot+[color=green]{examplepos(x)};
\node[roint=A] (A) at (axis cs:4.0, {examplepos(4.0)}) {};
\node[roint=B] (B) at (axis cs:4.9, {examplepos(4.9)}) {};
\node[boint={\delay{t_0}}]   (t0) at (A |- {0,0}) {};
\node[boint={\delay{t_0+h}}] (t1) at (B |- {0,0}) {};
\node[loint={\dist{x}(\delay{t_0})}]   (x0) at (A -| {0,0}) {};
\node[loint={\dist{x}(\delay{t_0+h})}] (x1) at (B -| {0,0}) {};
\draw[dashed] (t0) -- (A) -- (x0);
\draw[dashed] (t1) -- (B) -- (x1);
\draw[color=blue,shorten <=-2cm,shorten >=-1cm] (A) -- (B);
\end{axis}
\end{tikzpicture}
<figcaption>
We add a point $\posit{B}$ to the previous graph at time $\delay{t_0+h}$. The
mean velocity from $\posit{A}$ to $\posit{B}$ can be thought as the slope of
the red line $(AB)$.
</figcaption>
</figure>

Since we expect the speed to not change a lot on short periods of time, a
natural solution is to consider the mean velocity over shorter durations.

<figure>
\begin{tikzpicture}
\foreach \i [
	evaluate=\i as \x using {mod(\i,2)*\linewidth*2},
	evaluate=\i as \y using {-floor(\i/2)*\linewidth*3},
] in {0,...,3}{
	\begin{axis}[
		samples=\samples,
		domain=0:5,
		ticks=none,
		no markers,
		axis lines=left,
		clip=false,
		scale=0.5,
		at={(\x,\y)},
	]
	\addplot+[color=green]{examplepos(x)};
	\node[roint=A] (A) at (axis cs:4.0, {examplepos(4.0)}) {};
	\node[loint=B] (B) at (axis cs:{4.0+0.9/(2^\i)}, {examplepos(4.0+0.9/(2^\i))}) {};
	\draw[color=blue,shorten <=-2cm,shorten >=-1cm] (A) -- (B);
	\end{axis}
}
\end{tikzpicture}
<figcaption>
The closer to $\posit{A}$ we pick $\posit{B}$, the best the red line matches
the curve for velocity at $\posit{A}$.
</figcaption>
</figure>

So, as we pick shorter and shorter durations $\delay{h}$, the value
$\delay{\Delta t_0}$ becomes smaller, but so does $\dist{\Delta x}$. Often, we
will notice that the mean velocity over $\delay{h}$ seems to becomes closer and
closer to a particular value. Instead of continuing to choose smaller and
smaller values of $\delay{h}$, we will pick this values and call it the
**limit** of $\frac {\dist{\Delta x}(\delay{t_0})} {\delay{\Delta t_0}}$ as
$\delay{h}$ tends to $0$ (becomes smaller and smaller):

$$
\lim_{\delay{h} \to \delay{0}} \frac {\dist{\Delta x}(\delay{t_0})} {\delay{\Delta t_0}}
$$

The limit of such an expression is called the **derivative** of $\posit{x}$ at
$\delay{t_0}$. We have a shorter way to note this:

$$
\frac {\dist{\d x}(\delay{t_0})} {\delay{\dt}}
$$

We can then remark that we have actually defined the derivative for any
$\delay{t_0}$. Thus, we have a new function that let us evaluate the velocity
at any $\delay{t_0}$.

$$
\frac {\dist{\d x}} {\delay{\dt}}
$$

<figure>
\begin{tikzpicture}
\begin{axis}[
	samples=\samples,
	domain=0:5,
	ticks=none,
	no markers,
	axis lines=left,
	xlabel=$\delay{t}$,
	ylabel=$\dist{x}$,
	clip=false,
]
\addplot+[color=green]{examplepos(x)};
\end{axis}
\begin{axis}[
	samples=\samples,
	domain=0:5,
	ticks=none,
	no markers,
	axis y line=right,
	axis x line=none,
	ylabel=$\speed{v}$,
	clip=false,
]
\addplot+[color=blue]{examplevel(x)};
\end{axis}
\end{tikzpicture}
<figcaption>
This graph features both \posit{position} and \speed{velocity}. Since they do
not represent the same type of measurement, they each use a different axis and
comparing the relative positions of their curves is meaningless. However, we
can see that, as the position stabilizes in the middle, the velocity decreases;
in the end the object moves again, faster and faster.
</figcaption>
</figure>

<remark>
An even shorter notation is $\speed{\dot x}$. This notation is only used for
derivatives with respect to time.
</remark>


Second derivative
-----------------

The velocity is the derivative of the position. As a function, it can itself
fluctuate and we can be interested in these variations. The derivative of the
velocity is the **acceleration**: $\accel{a} = \accel{\dot v}$.

A shorter way of saying that the acceleration is the derivative of *the
derivative of the position*, is to say that the acceleration is the second
derivative of the position: $\accel{a} = \accel{\ddot x}$.


Formal derivation
-----------------

While we now have a way to compute the derivative of a function at a given
point, it is not accurate: while we do get a better approximation by taking a
smaller value for $h$, the result is still an approximation and can sometimes
stay far off.

Instead, we can look at the expressions to determine the exact value for the
limit. For instance, let us consider the function $f(x) = 12x$ and let us
search for $\frac {\d f(x)} {\d x}$ for any given $x$. First:

$$
\frac {\Delta f(x)} {\Delta x}
= \frac {f(x+h) - f(x)} {(x+h) - x}
= \frac {12(x+h) - 12x} {h}
= \frac {12\strike[red]{h}} {\strike[red]{h}}
= 12
$$

We now look at the value $\frac {\Delta f(x)} {\Delta x}$ as $\Delta x$ gets
small; in this case, it happens to always be $12$, and does not depend on
$\Delta x$. Thus, however small $\Delta x$, the value is $12$, and:

$$
\frac {\d f(x)} {\d x}
= \lim_{h \to 0} \frac {\Delta f(x)} {\Delta x}
= 12
$$

That way, we know the exaxt value of derivative of $f$ in any point. Let us
take a second example with $g(x) = 7x^2$:

$$
\frac {\Delta g(x)} {\Delta x}
= \frac {7(x+h)^2 - 7x^2} {h}
= \frac {7(x^2 + 2xh + h^2) - 7x^2} {h}
= \frac {7x\strike[red]{h} + h^{\strike[red]{2}}} {\strike[red]{h}}
= 7x + h
$$

Here, the expression does depend on $h$. However, the smaller $h$ gets, the
less influence it has on the sum: the value is becoming closer and closer to
$7x$. Thus: $\frac {\d g(x)} {\d x} = 7x$.


Derivation rules
----------------

Now, what if we want to compute the derivative of $h(x) = 12x + 7x^2$? Of
course, we could go through the same step as in the previous part. However, we
can notice that $h = f + g$ (this means that $h(x) = f(x) + g(x)$ for all
$x$'s). It turns out that it can be shown that $\frac {\d} {\d x} (f+g) = \frac
{\d} {\d x} f + \frac {\d} {\d x} g$ for any functions $f$ and $g$. Using this
rule and knowing the derivative of $f$ and $g$, we can derive:

$$
\frac {\d} {\d x} h(x)
= \frac {\d} {\d x} (f+g)(x)
= \frac {\d} {\d x} f(x) + \frac {\d} {\d x} g(x)
= 12 + 7x
$$

There are a few derivation rules that can help us determine the derivative of
complex functions easily.

<figure>
<figure>
\begin{alignat*}{2}
& (\alpha f)'              &&= \alpha f' \\
& (f + g)'                 &&= f' + g' \\
& (f \times g)'            &&= f' \times g' + g' \times f \\
& \left(\frac f g\right)'  &&= \frac {f'g - g'f} {g^2} \\
& (f(g(x))'                &&= g'(x) \times f'(g(x))
\end{alignat*}
<figcaption>derivation rules</figcaption>
</figure><figure>
\begin{alignat*}{2}
& (x^n)'    &&= n x^{n-1}   \\
& (e^x)'    &&= e^x         \\
& (\ln x)'  &&= \frac 1 x \\
& (\cos x)' &&= -\sin x \\
& (\sin x)' &&=  \cos x
\end{alignat*}
<figcaption>common derivatives</figcaption>
</figure>
</figure>



Integrals
=========


Definition
----------

Now, let us consider the reverse situation: we know the velocity of the car
$\speed{v}$ at any given instant and we would like to know where it was at an
arbitrary instant $\delay{t_0}$. In other words, we know the derivative of the
position $\speed{\dot x} = \speed{v}$ and we intend to get the position
$\posit{x}$ back.

The first thing to notice is that the velocity only informs us on *relative*
motion: two cars can have the same velocity through time while being in
different positions. In the example below, the positions of two cars with the
same speed are shown; since the red car starts ahead, it stays ahead.

<figure>
\begin{tikzpicture}
\begin{axis}[
	samples=\samples,
	domain=0:5,
	ticks=none,
	no markers,
	axis lines=left,
	xlabel=$\delay{t}$,
	ylabel=$\dist{x}$,
	clip=false,
]
\addplot{examplepos(x)};
\addplot{5e4+examplepos(x)};
\end{axis}
\end{tikzpicture}
<figcaption>The red car moves like the blue car does, but starts ahead.</figcaption>
</figure>

This means that we need additional information; usually we will assume that the
position of the car at instant $\delay{t} = \delay{0~s}$ is some arbitrary
value $\posit{C}$ or even $\posit{0}$ (when the arbitrary value does not
matter).

???

Given a constant velocity $\speed{v_0}$ and a delay $\delay{t_0}$, we know how
to compute the distance $\posit{x_0}$ as $\posit{x_0} = \speed{v_0} \times
\delay{t_0}$. In this situation however, the velocity changes over the time
interval from $\delay{0~s}$ to $\delay{t_0}$.

As a first approximation, we could pretend the velocity is always equal to
$\speed{v}(\delay{t_0})$, which makes the position trivial to compute:
$\posit{x}(\delay{t_0}) \simeq \speed{v}(\delay{t_0}) \times \delay{t_0}$.

<figure>
\begin{tikzpicture}
\begin{axis}[
	samples=\samples,
	domain=0:5,
	ticks=none,
	no markers,
	axis lines=left,
	xlabel=$\delay{t}$,
	ylabel=$\speed{v}$,
	clip=false,
]
\fill[green,opacity=0.1] (0,0) rectangle (axis cs:3.5, {examplevel2(3.5)});
\addplot+[color=red]{examplevel2(x)};
\node[roint=A] (A) at (axis cs:3.5, {examplevel2(3.5)}) {};
\node[boint={\delay{t_0}}] (t0) at (A |- {0,0}) {};
\node[loint={\speed{v}(\delay{t_0})}] (v0) at (A -| {0,0}) {};
\draw[dashed] (t0) -- (A) -- (v0);
\end{axis}
\end{tikzpicture}
<figcaption>
The graph clearly shows that the velocity may not be close to
$\speed{v}(\delay{t_0})$: this is a very rough first approximation.
</figcaption>
</figure>

Since this value is also the area of a rectangle of sizes
$\speed{v}(\delay{t_0})$ and $\delay{t_0}$, we can visualize it on the graph:

The green area represents the value $\speed{v}(\delay{t_0}) \times
\delay{t_0}$.

Once more, consider the car on the road. We are given its speed $\speed{\dot
x}(\delay{t})$ through the time. Because we know how fast the car was going at
any single instant, we can deduce how much it traveled from time $\delay{t_1}$
to $\delay{t_2}$ for example. The computation of the position depending on the
speed is notated with the integral symbol (which just means sum of small
elements):

$$
\int_{\delay{t_1}}^{\delay{t_2}} \speed{\dot x}(\delay{t}) \delay{\dt}
= \int_{\delay{t_1}}^{\delay{t_2}} \frac {\dist{\d x}} {\strike[red]{\delay{\dt}}} \strike[red]{\delay{\dt}}
= \sum_{\delay{t_1}}^{\delay{t_2}} \dist{\d x}
= \underbrace{
	\dist{x}(\delay{t_2}) - \dist{x}(\delay{t_1})
}_{[\dist{x}]_{\delay{t_1}}^{\delay{t_2}}}
$$


Illustration
------------

For example, if $\speed{\dot x} = \accel{2~m/s^2} \times \delay{t}$, then:

\begin{align*}
\dist{x}(\delay{30~s}) - \dist{x}(\delay{0~s})
&= \int_{\delay{0}}^{\delay{30~s}} \accel{2~m/s^2} \times \delay{t} \delay{\dt} \\
&= \left(\int_{\delay{0})}^{\delay{30~s}} 2 \delay{t} \delay{\dt}\right) \accel{m/s^2} \\
&= [\delay{t}^2]_{\delay{0}}^{\delay{30~s}} \accel{m/s^2} \\
&= (900~s^2 - 0~s^2) \accel{m/s^2} \\
&= \dist{900~m}
\end{align*}

In particular, with we are given the additional information that $\posit{C}$
did start at $\posit{O}$, i.e.  $\dist{x}(\delay{0}) = \dist{0}$, then:

$$
\dist{x}(\delay{30~s}) = \dist{900~m}
$$

Antiderivative
--------------

More generally, in the previous example, we could write:

$$
\dist{x}(\delay{t}) - \dist{x}(\delay{0})
= \int_{\delay{0}}^{\delay{30~s}} \accel{2~m/s^2} \times \delay{t} \delay{\dt}
= \delay{t}^2 \accel{m/s^2}
$$

Another way to write it is:

$$
\dist{x}(\delay{t})
= t^2 \accel{m/s^2} + \dist{C}
$$

where $\dist{C} = \dist{x}(\delay{0})$ is a value independent of $\delay{t}$
which depends on the **initial conditions** (e.g. the position of the car at
the initial instant). Each of the possible expression of $\dist{x}$ (depending
on $\dist{C}$) is a primitive of $\speed{\dot x}$.



Differential equations
======================

Definition
----------

A differential equation is an equation whose unknown is a function in which a
derivative of this function appears. For example:

$$
\frac {\d f} {\d x} = 3x^2
$$

This is a differential equation and we already know how to solve it (find the
expression of $f$). Here, $f(x) = x^3 + C$ (there are several possible
solutions).


Exponential
-----------

The exponential function is defined as $f(x) = e^x$ where $e$ is a mathematical
constant whose value is about $2.718$. It was picked so that:

$$
\frac {\d f} {\d x} = f
$$

In other words:

$$
\frac {\d} {\d x} (e^x) = e^x
$$

<remark>
If we define $f(x) = e^{g(x)}$ instead, derivation rules gives us:

$$
\frac {\d f(x)} {\d x}
= g'(x) e^{g(x)}
$$

so that $\frac {\d f} {\d x} = g' f$.
</remark>


First order
-----------

Now, consider the following equation:

$$
\frac {\d f} {\d x} = f
$$

We already know that $f(x) = e^x$ is a solution; however, so is $f(x) = 2 e^x$.
Actually, the set of solutions to this equation is the functions $f(x) = C e^x$
where $C$ is any constant value.

The remark we made before tell us how to solve a differential equation of the
form:

$$
\frac {\d f} {\d x} = h f
$$

where $h$ is also a function. We just need to find $g$ such that $g' = h$, i.e.
the solutions are:

$$
f(x) = C e^{\int_0^x h(x) \d x}
$$


Geometric integrals
===================

Circle circumference:

\begin{align*}
\dist{d}
&= \oint_C \dist{\d s}
\\
&= \int_{\angle{0}}^{\angle{2\pi}} \dist{R} \angle{\d \theta}
\\
&= \dist{R} \left[ \theta \right]_{\angle{0}}^{\angle{2\pi}}
\\
&= 2\pi \dist{R}
\\
\end{align*}

Disk area:

\begin{align*}
\area{A}
&= \iint_D \area{\d A}
\\
&= \int_{\dist{r}=\dist{0}}^{\dist{R}}
  \int_{\angle{\theta}=\angle{0}}^{\angle{2\pi}}
  \dist{\d r} \times \dist{r} \angle{\d \theta}
\\
&= 2\pi \int_{\dist{0}}^{\dist{R}} \dist{r} \dist{\d r}
\\
&= 2\pi \left[\frac 1 2 \dist{r}^2\right]_{\dist{0}}^{\dist{R}}
\\
&= \pi \dist{R}^2
\end{align*}

Sphere area:

\begin{align*}
\area{A}
&= \oiint_S \area{\d A}
\\
&= \int_{\angle{\theta}=\angle{0}}^{\angle{\pi}}
  \int_{\angle{\phi}=\angle{0}}^{\angle{2\pi}}
  (\dist{R} \sin \angle{\phi} \angle{\d \theta})
  (\dist{R} \angle{\d \phi})
\\
&= 2\pi \dist{R}^2 \int_{\angle{0}}^{\angle{\pi}} \sin \angle{\phi} \angle{\d \phi}
\\
&= 2\pi \dist{R}^2 \left[ - \cos \phi \right]_{\angle{0}}^{\angle{\pi}}
\\
&= 4\pi \dist{R}^2
\end{align*}

Sphere enclosed volume:

\begin{align*}
\vol{V}
&= \iiint_B \vol{\d V}
\\
&= \int_{\dist{r}=\dist{0}}^{\dist{R}}
  \int_{\angle{\theta}=\angle{0}}^{\angle{\pi}}
  \int_{\angle{\phi}=\angle{0}}^{\angle{2\pi}}
  (\dist{r} \sin \angle{\phi} \angle{\d \theta}) (\dist{r} \d \angle{\phi}) \dist{\d r}
\\
&= 2 \pi
  \int_{\dist{r}=\dist{0}}^{\dist{R}}
  \int_{\angle{\theta}=\angle{0}}^{\angle{\pi}} \sin \angle{\phi} \angle{\d \phi} \dist{r}^2 \dist{\d r}
\\
&= 2 \pi
  \left[\frac 1 3 \dist{r}^3\right]_{\dist{0}}^{\dist{R}}
  \left[- \cos \angle{\phi}\right]_{\angle{0}}^{\angle{\pi}}
\\
&= \frac 4 3 \pi \dist{R}^3
\end{align*}