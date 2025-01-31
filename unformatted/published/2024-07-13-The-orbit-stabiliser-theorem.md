---
layout: post
title:  "The orbit-stabiliser theorem"
date:   2024-07-13 00:00:00 +0100
categories: 
---

I never fully appreciated the orbit-stabiliser theorem at university. Since then I've better understood its relationship with Lagrange's theorem and come to appreciate it as a consequence of one of my favourite theorems: the first isomorphism theorem, in all its guises.

# Basic definitions and facts

## Definitions: Orbit, stabiliser, fixed-point
Let $G$ be a group acting on a set $X$. We define
 - The orbit of $x \in X$, written $G.x$ or $\textrm{Orb}(x)$, as $\{g.x: g\in G\}$
 - The stabiliser of $x \in X$, written $G_x$ or $\textrm{Stab}(x)$, as $\{g \in G: g.x=x\}$
 - The fixed-points of $g$, written $X^g$ or $\textrm{Fix}(g)$, as $\{x\in X: g.x=x\}$

All three notions extend in the obvious way to subsets of $X$, $G$. We then have a Galois connection between fixed-points and stabilisers. 

Let $\rho: G\times X \to X$ denote the action. Letting $G$ act on $G\times X$ by $h.(g,x) = (hg,x)$, we see that $\rho$ is a map of $G$-sets! Fixing some $x\in X$ gives a map of $G$-sets

$$ \rho_x: G \to X $$
$$g \mapsto g.x $$

with image $G.x$, hence a map $\rho_x: G \twoheadrightarrow G.x$.

We have 
$$\rho_x^{-1}(\{y\}) = \{g\in G: g.x=y\}$$
and hence in particular:
$$\rho_x^{-1}(\{x\}) = \textrm{Stab}(x)$$

## Proposition:
For $x,y \in X, S \subseteq X$ and $g \in G$, we have 
- If $x,y$ are in different $G$-orbits, then $\rho_x^{-1}(\{y\}) = \emptyset$
- We have 
 $$\rho_x^{-1}(g.S)=g\rho_x^{-1}(S) $$ 
 In particular, 
 $$\rho_x^{-1}(\{g.y\})=g\rho_x^{-1}(\{y\})$$
- We have 
 $$\rho_{g.x}^{-1}(S)=\rho_x^{-1}(S)g^{-1} $$ 
 In particular, 
 $$\rho_{g.x}^{-1}(\{y\})=g\rho_x^{-1}(\{y\})g^{-1}$$
- If $y = g.x$, then 
 $$\rho_y^{-1}(\{y\}) = \textrm{Stab}(y) = g\textrm{Stab}(x)g^{-1} = \rho_x^{-1}(\{x\}) $$

Proof: exercise

## Theorem: Orbit-Stabiliser theorem (first formulation)
Let $G$ be a group acting on a set $X$ via an action $\rho: G\times X \to X$ and fix $x\in X$. Then the sets 
$$\{\rho_x^{-1}(\{y\}): y\in G.x\} $$ 
are equinumerous and partition $G$.
In particular, when $G$ and $X$ are finite, we have for any $x\in X$ that 
$$|\textrm{Orb}(x)| |\textrm{Stab}(x)| =|G| $$

Proof: 
Since $G.x = \textrm{Im}(\rho_x)$, the sets evidently partition $G$. But for $y\in G.x$ we have
$$\rho_x^{-1}(\{g.x\})=g\textrm{Stab}(x) = g\rho_x^{-1}(\{x\}) $$ 
so they are equinumerous.

Note the similarity to Lagrange's theorem, which says that for a subgroup $H$ of a group $G$, the cosets of $H$ partition $G$ and are equinumerous. The similarity can be made more explicit by the following formulation of the theorem:

## Theorem: Orbit-Stabiliser theorem (second formulation)
Let $\rho :G\times X\to X$ be an action of a group $G$ on a set $X$ and fix $x\in X$. Define an equivalence relation $\sim$ on $G$ by 
$$g\sim h \Leftrightarrow g.x = h.x $$
Then 
$$G/\sim \cong G/\textrm{Stab(x)} $$
 and by the "first isomorphism theorem for $G$-sets". we get an isomorphism of $G$-sets
$$\tilde{\rho_x}: G/\textrm{Stab}(x) \tilde{\to} G.x $$ 
$$g\mapsto g.x $$

Proof: Recall 
$$G.x = \textrm{Im}(\rho_x) $$
Now note that $g.x = h.x$ iff $gh^{-1}\in \textrm{Stab}(x)$. (In fact, *every* quotient of the left-multiplication action of $G$ on itself is given by $G/H$ for some $H\leq G$).

Thus, the orbit-stabiliser theorem is exactly Lagrange's theorem "pushed through" the map $\rho_x$.

This formulation of the theorem has a very nice eye-catching moral: Note that a $G$-set $X$ is always the disjoint union of its orbits, so we can understand the action of $G$ on $X$ by understanding the action of $G$ on each of the orbits separately. But by orbit-stabiliser, each orbit is isomorphic as a $G$-set to the left-multiplication action of $G$ on $G/H$ for some $H\leq G$. So the category of $G$-sets can be understood completely by understanding how $G$ acts on itself![^overstatement].

Note that a similar moral holds for linear $G$-representations, especially in the semisimple case (e.g. when $G$ is finite and the ground field $k$ is algebraically closed of characteristic zero); in this case, every representation is a direct sum (not disjoint union) of simples (not orbits) and every simple $G$-representation appears as a quotient (and summand, by semisimplicity) of $kG$. In fact, a nice perspective on semisimplicity might be that it allows us to emulate as closely as possible the case of $G$ acting on a mere set, rather than a vector space.

[^overstatement]: This is really an overstatement - in practice, it may not be so easy to apply this knowledge to specific $G$-sets $X$. But at least for theoretical and spiritual purposes, this is a good idea to take to heart.