---
layout: post
title:  "A User's Guide To Monoidal Category Coherence Theorems"
date:   2024-08-30 00:00:00 +0100
categories: 
---

# Introduction
One of the perennial questions I find myself asking when learning category theory is "why those commutative diagrams? Why not more? Why not less?". When choosing which commutative diagrams to include in a definition, there are essentially two possible approaches: 
 - A "biased" definition using a logically minimal number of diagrams (hence which is "biased" in the sense that it gives a special role to these diagrams)
 - An "unbiased" versiom using a logically maximal number of diagrams - in particular which includes all diagrams which commute as a *formal* consequence of the diagrams in the biased definition

Coherence theorems are (from one point of view) theorems which state an equivalence between a biased and an unbiased definition. Such theorems play more than one role:
 - Conceptual: Often, the biased form of the definition, while easy to establish, is not very conceptually motivating or enlightening. By providing an equivalent unbiased form, we gain a better understanding of what it is that the definition expresses
 - Practical: We may frequently want to establish whether a diagram commutes, and in particular if it commutes for purely formal reasons. Coherence theorems allow us to recognise a large class of commutative diagrams with minimal effort
 
It is the second reason which primarily concerns us here, and as such we will focus mostly on the practical use of the coherence theorems rather than their precise statement, and proofs will be absent.

In a concrete sense, coherence theorems (especially for monoidal categories) take the form[^alternative] of a concrete description of the *free (braided/symmetric) monoidal category* on a set[^morphisms] of objects[^usual]. If we understand which diagrams commute in these free monoidal category, then their image in an arbitrary monoidal category <span>$\mathcal{C}$</span> gives a large class of commuting diagrams in <span>$\mathcal{C}$</span> for free.

# Monoidal categories

*Theorem: Coherence theorem for monoidal categories*\
Let <span>$S$</span> be a set. The free monoidal category <span>$\text{Free}(S)$</span> on <span>$S$</span> can be described recursively as:
 - Objects: 
    - An object <span>$1$</span> not in <span>$S$</span> 
    - An object <span>$s$</span> for each <span>$s\in S$</span> 
    - For each <span>$s\in S$</span> and each <span>$x \in \mathcal{C}$</span>, an object <span>$s\otimes x$</span> and an object <span>$x\otimes s$</span> 
 - Morphisms:
   - For each <span>$x \in \mathcal{C}$</span>, a map <span>$id_x: x\to x$</span>
   - For each <span>$x\in\mathcal{C}$</span>, maps <span>$\rho_x: x\otimes 1 \to x$</span> and <span>$\tilde{\rho_x}: x\to x\otimes 1$</span>
   - For each <span>$x\in\mathcal{C}$</span>, maps <span>$\lambda_x: 1\otimes x \to x$</span> and <span>$\tilde{\lambda_x}: 1\otimes x \to x$</span>
   - For each <span>$x,y,z\in \mathcal{C}$</span>, maps <span>$\alpha_{x,y,z}: x\otimes (y\otimes z) \to (x\otimes y)\otimes z$</span> and <span>$\tilde{\alpha_{x,y,z}}: (x\otimes y) \otimes z$</span>

Let's see how we can use the above theorem to conclude that a certain diagram commutes: Consider <span>$\rho_x \circ \tilde{\rho_x}: x\to x$</span>. By the description above, there is a unique map <span>$x\to x$</span>, which is <span>$id_x: x\to x$</span>. Hence, <span>$\rho_x \circ \tilde{\rho_x} = id_x$</span>. \
More generally, note that there is at most one morphism between two objects in <span>$\text{Free}(S)$</span>, so every diagra, in <span>$\text{Free}(S)$</span> commutes.

*Corollary: "Every diagram commutes"*\
Let <span>$\mathcal{C}$</span> be a monoidal category. Then any diagram in <span>$\mathcal{C}$</span> composed entirely of unitors and associators commutes which exists entirely for formal reasons commutes.

This corollary is a bit mealy-mouthed in that it has that irritating caveat "which exists entirely for formal reasons". The point here is that a monoidal category <span>$\mathcal{C}$</span> can contain objects <span>$x,y,z$</span> such that <span>$x\otimes(y\otimes z) = (x\otimes y)\otimes z$</span>. A more careful statement of the corollary actually amounts to a proof: specifically, let <span>$S$</span> be some collection of objects in a monoidal category <span>$\mathcal{C}$</span>. Then by the universal property, there exists a unique (up to isomorphism) strong monoidal functor <span>$F: \text{Free}(S) \to \mathcal{C}$</span>. Any diagram in the image of <span>$F$</span> commutes.

Trying to state the corollary precisely is a red herring: it is best thought of as a vague principle which one should internalise in order to recognise commutative diagrams at a glance.

This coherence theorem is probably the most famous of all coherence theorems, and can give one the false expectation that every coherence theorem is of the form "every diagram commutes". In fact, most coherence theorems are of the form "lots of diagrams commute" and give a tractcable description of the "lots".

# Braided monoidal categories
The coherence theorem for braided monoidal categories no longer takes the form "every diagram commutes". Rather, it associates to every morphism in the free braided monoidal category a "braid", and states that two morphisms are equal if they have the same source and target and the same associated braid. 

# Symmetric monoidal categories
The coherence theorem for symmetric monoidal categories is closely analogous to the case of braided monoidal categories, but replaces braids with permutations.

This is nice to visualise pictorially: in the case of braids, the strands could pass over or under one another, and thus exchanging two objects twice may give the identity. In the case of symmetric monoidal categories, exchanging two objects twice *does* give the identity, and thus the "over" and "under" information is lost. Visually, this corresponds to "flattening" the braid and flattened braids are clearly just permutations.
