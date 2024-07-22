---
layout: post
title:  "The orbit-stabiliser theorem"
date:   2024-07-13 00:00:00 +0100
categories: 
---

I never fully appreciated the orbit-stabiliser theorem at university. Since then I've better understood its relationship with Lagrange's theorem and come to appreciate it as a consequence of one of my favourite theorems: the first isomorphism theorem, in all its guises.

# Basic definitions and facts

## Definitions: Orbit, stabiliser, fixed-point
Let <span>$G$</span> be a group acting on a set <span>$X$</span>. We define
 - The orbit of <span>$x \in X$</span>, written <span>$G.x$</span> or <span>$\textrm{Orb}(x)$</span>, as <span>$\{g.x: g\in G\}$</span>
 - The stabiliser of <span>$x \in X$</span>, written <span>$G_x$</span> or <span>$\textrm{Stab}(x)$</span>, as <span>$\{g \in G: g.x=x\}$</span>
 - The fixed-points of <span>$g$</span>, written <span>$X^g$</span> or <span>$\textrm{Fix}(g)$</span>, as <span>$\{x\in X: g.x=x\}$</span>

All three notions extend in the obvious way to subsets of <span>$X$</span>, <span>$G$</span>. We then have a Galois connection between fixed-points and stabilisers. 

Let <span>$\rho: G\times X \to X$</span> denote the action. Letting <span>$G$</span> act on <span>$G\times X$</span> by <span>$h.(g,x) = (hg,x)$</span>, we see that <span>$\rho$</span> is a map of <span>$G$</span>-sets! Fixing some <span>$x\in X$</span> gives a map of <span>$G$</span>-sets

<div>$$ \rho_x: G \to X $$</div>
<div>$$g \mapsto g.x $$</div>

with image <span>$G.x$</span>, hence a map <span>$\rho_x: G \twoheadrightarrow G.x$</span>.

We have 
<div>$$\rho_x^{-1}(\{y\}) = \{g\in G: g.x=y\}$$</div>
and hence in particular:
<div>$$\rho_x^{-1}(\{x\}) = \textrm{Stab}(x)$$</div>

## Proposition:
For <span>$x,y \in X, S \subseteq X$</span> and <span>$g \in G$</span>, we have 
- If <span>$x,y$</span> are in different <span>$G$</span>-orbits, then <span>$\rho_x^{-1}(\{y\}) = \emptyset$</span>
- We have 
 <div>$$\rho_x^{-1}(g.S)=g\rho_x^{-1}(S) $$</div> 
 In particular, 
 <div>$$\rho_x^{-1}(\{g.y\})=g\rho_x^{-1}(\{y\})$$</div>
- We have 
 <div>$$\rho_{g.x}^{-1}(S)=\rho_x^{-1}(S)g^{-1} $$</div> 
 In particular, 
 <div>$$\rho_{g.x}^{-1}(\{y\})=g\rho_x^{-1}(\{y\})g^{-1}$$</div>
- If <span>$y = g.x$</span>, then 
 <div>$$\rho_y^{-1}(\{y\}) = \textrm{Stab}(y) = g\textrm{Stab}(x)g^{-1} = \rho_x^{-1}(\{x\}) $$</div>

Proof: exercise

## Theorem: Orbit-Stabiliser theorem (first formulation)
Let <span>$G$</span> be a group acting on a set <span>$X$</span> via an action <span>$\rho: G\times X \to X$</span> and fix <span>$x\in X$</span>. Then the sets 
<div>$$\{\rho_x^{-1}(\{y\}): y\in G.x\} $$</div> 
are equinumerous and partition <span>$G$</span>.
In particular, when <span>$G$</span> and <span>$X$</span> are finite, we have for any <span>$x\in X$</span> that 
<div>$$|\textrm{Orb}(x)| |\textrm{Stab}(x)| =|G| $$</div>

Proof: 
Since <span>$G.x = \textrm{Im}(\rho_x)$</span>, the sets evidently partition <span>$G$</span>. But for <span>$y\in G.x$</span> we have
<div>$$\rho_x^{-1}(\{g.x\})=g\textrm{Stab}(x) = g\rho_x^{-1}(\{x\}) $$</div> 
so they are equinumerous.

Note the similarity to Lagrange's theorem, which says that for a subgroup <span>$H$</span> of a group <span>$G$</span>, the cosets of <span>$H$</span> partition <span>$G$</span> and are equinumerous. The similarity can be made more explicit by the following formulation of the theorem:

## Theorem: Orbit-Stabiliser theorem (second formulation)
Let <span>$\rho :G\times X\to X$</span> be an action of a group <span>$G$</span> on a set <span>$X$</span> and fix <span>$x\in X$</span>. Define an equivalence relation <span>$\sim$</span> on <span>$G$</span> by 
<div>$$g\sim h \Leftrightarrow g.x = h.x $$</div>
Then 
<div>$$G/\sim \cong G/\textrm{Stab(x)} $$</div>
 and by the "first isomorphism theorem for <span>$G$</span>-sets". we get an isomorphism of <span>$G$</span>-sets
<div>$$\tilde{\rho_x}: G/\textrm{Stab}(x) \tilde{\to} G.x $$</div> 
<div>$$g\mapsto g.x $$</div>

Proof: Recall 
<div>$$G.x = \textrm{Im}(\rho_x) $$</div>
Now note that <span>$g.x = h.x$</span> iff <span>$gh^{-1}\in \textrm{Stab}(x)$</span>. (In fact, *every* quotient of the left-multiplication action of <span>$G$</span> on itself is given by <span>$G/H$</span> for some <span>$H\leq G$</span>).

Thus, the orbit-stabiliser theorem is exactly Lagrange's theorem "pushed through" the map <span>$\rho_x$</span>.

This formulation of the theorem has a very nice eye-catching moral: Note that a <span>$G$</span>-set <span>$X$</span> is always the disjoint union of its orbits, so we can understand the action of <span>$G$</span> on <span>$X$</span> by understanding the action of <span>$G$</span> on each of the orbits separately. But by orbit-stabiliser, each orbit is isomorphic as a <span>$G$</span>-set to the left-multiplication action of <span>$G$</span> on <span>$G/H$</span> for some <span>$H\leq G$</span>. So the category of <span>$G$</span>-sets can be understood completely by understanding how <span>$G$</span> acts on itself![^overstatement].

Note that a similar moral holds for linear <span>$G$</span>-representations, especially in the semisimple case (e.g. when <span>$G$</span> is finite and the ground field <span>$k$</span> is algebraically closed of characteristic zero); in this case, every representation is a direct sum (not disjoint union) of simples (not orbits) and every simple <span>$G$</span>-representation appears as a quotient (and summand, by semisimplicity) of <span>$kG$</span>. In fact, a nice perspective on semisimplicity might be that it allows us to emulate as closely as possible the case of <span>$G$</span> acting on a mere set, rather than a vector space.

[^overstatement]: This is really an overstatement - in practice, it may not be so easy to apply this knowledge to specific <span>$G$</span>-sets <span>$X$</span>. But at least for theoretical and spiritual purposes, this is a good idea to take to heart.