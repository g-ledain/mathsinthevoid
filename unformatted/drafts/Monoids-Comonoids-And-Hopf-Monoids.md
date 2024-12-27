---
layout: post
title:  "Monoids, Comonoids and Hopf Monoids"
date:   2024-08-27 00:00:00 +0100
categories: 
---

Monoidal categories are categories equipped with a categorified version of the familiar structure of a monoid. By the [microcosm principle]{}[^archive], this means they provide a natural context in which we can formulate a generalisation of the usual set-based definition of monoids. They also provide a natural context in which to define comonoids[^comonoidal-cat], and in the presence of a braiding on the underlying category one can write down a compatibility relation between a monoid and comonoid structure on an object, giving the notion of bimonoid.

Throughout, let $\mathcal{C}$ be a monoidal category.

*Definition: Monoid*
TO DO: DEF

*Definition: Comonoid*
TO DO: DEF

*Definition: Bimonoid*
A bimonoid object in $\mathcal{C}$ is an object $x \in \mathcal{C}$ equipped with any one of the three following equivalent structures:
 - TO DO: BAREBONES DEFINITION
 - A comonoid structure in the category of monoids in $\mathcal{C}$
 - A monoid object structure in the category of comonoids in $\mathcal{C}$

The last two definitions perhaps give some motivation for the specific choice of commutative diagrams in the first definition, though they are both irksomely non-symmetrical. Note that this is *not* one of those definitions where you form every possible diagram from the structure morphisms and demand that they commute! For instance, GIVE EXAMPLE OF DIAGRAM WHICH DOESN'T COMMUTE.

*Definition: Hopf monoid*
TO DO: DEFINITION

The notion of a Hopf monoid is rather alien at first, and a little offputting. The notion of Hopf monoid is best thought of as a generalisation of the notion of a group to arbitrary monoidal categories. However at first glance, there is a *lot more* to a Hopf monoid than to a group - specifically, a Hopf monoid has a comonoid structure and a compatibility between the monoid and the comonoid structures which is unfamiliar from the world of groups. However, these structures are actually already latent in the definition of a group, once one has presented it in sufficiently categorical language.

*Definition: Group object*\
Let $\mathcal{C}$ be a category with all small limits. A group object in $\mathcal{C}$ is an object $x\in\mathcal{C}$ along with maps 
$$m: x \times x \to x $$
$$e: 1\to x $$
$$i: x\to x$$
such that the following diagrams commute
TO DO: DIAGRAMS

Note in particular that in order to even formulate the condition that $i$ is the "inverse" map, we have made essential use of the diagonal map $\Delta: x \to x\times x $ and of the terminal map $x\to 1$. Recall that the most natural and general context for defining a monoid is in a *monoidal* category (rather than just a complete category). But monoidal categories do not in general come equipped with such maps![^quantum] Therefore, in order to generalise the definition of a group to a monoidal category, we have to *supply* such maps $x\to x\times x$, $x\to 1$ as part of the data, and it is a short step to then demand that these maps satisfy the comonoid condition[^comfortable].

The utter invisibility of the comonoid structure in group theory is explained not just by the naturalness of this choice of comonoid structure, but by the fact that it is *unique*!

*Proposition: Uniqueness of comonoids in Cartesian monoidal categories*\
Let $\mathcal{C}$ be a Cartesian monoidal category and $x\in \mathcal{C}$. Then there is a unique comonoid structure on $x$, specifically given by 
$$\Delta: x\to x\times x \text{ is the diagonal map }$$
$$x \to 1 \text{ is the unique terminal map} $$

In particular, the category of comonoids in $\mathcal{C}$ is equivalent to $\mathcal{C}$ in the obvious way.

*Proof*: There is a unique map $x\to 1$. Then the comonoid conditions force the choice of $\Delta$.

*Corollary: Hopf monoids in Cartesian monoidal categories*\
A Hopf monoid in a Cartesian category is exactly a group object in that category. In particular, a Hopf monoid in $\textrm{Set}$ is just a group.


[^archive]: [archived]{}

[^comonoidal-cat]: One might expect that a *comonoidal category* would be the natural context in which to define comonoids, and one could wonder whether there is a notion of monoid internal to a comonoidal category. We will soon discover that any set has a unique comonoid structure and a categorified version of this result holds, so that a category has only one cmonoidal structure up to equivalence. Thus, comonoidal categories are unfortunately dull.

[^quantum]: This is of importance in linear logic and it's application to quantum computing; in that context, the diagonal map represents a kind of "duplication" of resources, and the absence of a diagonal map is a manifestation of the no-cloning theorem. At least, so I am told.

[^comfortable]: This "short step" is actually the part of the reasoning with which I am least comfortable.