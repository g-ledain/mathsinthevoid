---
layout: post
title:  "On Proof and counterexample"
date:   2025-07-20 00:00:00 +0100
categories: 
---

A phrase which never fails to frighten me is 

> "Give a proof or a counterexample of the following fact: ..."

Exercises of this sort have a very real qualitative difference to regular exercises in that it is not even clear at the start what the goal of the exercise is.
This makes them a very powerful pedagogical tool; instead of just developing technical skill, they force the student to take ownership of that technique.

A less obvious benefit of being familiar with the proof-or-counterexample style of thinking is that it can be helpful even when a specific goal *is* set in advance. 
I recently experienced this as I worked through the first chapter of Mac Lane and Moerdijk's classic "Sheaves in Geometry and Logic". 

## The Problem
The authors introduce the category of continuous <span>$G$</span>-sets.

*Definition: Category of continuous <span>$G$</span>-sets*[^peculiar]

Let <span>$G$</span> be a topological group. 
The category of continuous <span>$G$</span>-sets, written <span>$BG$</span> has:
 - Objects: Sets <span>$X$</span> equipped with a left[^right] <span>$G$</span> action such that the action function <span>$G\times X \to X$</span> is continuous when <span>$X$</span> is given the discrete topology
 - Morphisms: <span>$G$</span>-equivariant maps of <span>$G$</span>-sets

We define the group <span>$G^\delta$</span> to be <span>$G$</span> equipped with the discrete topology.
We then evidently have an "inclusion" functor

<div>$$i_G : BG \to BG^\delta$$</div>

For any <span>$X \in BG^\delta$</span> and <span>$x \in X$</span> we define the stabiliser (or "isotropy subgroup" in their language)

<div>$$I_x : = \{g \in G: g.x = x\}$$</div>

and thus a functor

<div>$$r_G: BG^\delta \to BG$$</div>
<div>$$r_G(X) := \{ x\in X: I_x \text{ is an open subgroup of } G\}$$</div>

An earlier exercise asks one to prove that for <span>$X \in BG^\delta$</span>, the action of <span>$G$</span> on <span>$X$</span> is continuous if and only if for each <span>$x \in X$</span> (so that <span>$r_G$</span> is well-defined) and that <span>$r_G$</span> is a right adjoint to <span>$i_G$</span>. 

We now come to the exercise I want to focus on:

> *Exercise:*
> 
> Prove that the forgetful functor <span>$F: BG \to \textrm{Set}$</span>
> need not preserve infinite limits.

The zeroth thing one ought to do is to realise that the exercise means that this is not true for *arbitrary* <span>$G$</span> rather than for *all* <span>$G$</span> (since for <span>$G$</span> a discrete group the limits *are* preserved).

The first thing one ought to do is to compute the limits in <span>$BG$</span>. 
Since <span>$r_G$</span> is a right adjoint, we can conclude that it takes limits in <span>$\textrm{Set}$</span> to limits in <span>$BG$</span>, so that 
<div>$$\lim_{i\in I}^{BG} X_i = \lim_{i\in I}^{BG} r_G(X_i) = r_G\left(\lim_{i \in I}^{BG^\delta} X_i\right)$$</div>

Since the forgetful functor <span>$BG^\delta \to \textrm{Set}$</span> preserves all limits, we see that we need to find some system of <span>$X_i$</span> and an element <span>$x \in \lim_{i \in I}^\textrm{Set} X_i$</span> such that <span>$I_x$</span> is not an open subgroup of <span>$G$</span>.

## Proving the converse
Now, unless you are more intelligent than me[^likely], your first few attempts at an example of a non-preserved limit here will be unsuccessful. 
A useful trick here is instead of trying to find a counterexample to the preservation of infinite limits, *try to prove that infinite limits are preserved by <span>$F$</span>*. 
Of course, this is not an earnest attempt at a proof. 
What we're really trying to do here is to find relatively general conditions under which the statement is false, so that we can exclude a large section of the search space for a counterexample. 

Instead of considering different kinds of group, we will first consider different kinds of limit. 
Recall that any limit can be considered as an equaliser of a product. 
I claim that <span>$F$</span> preserves equalisers: for any maps <span>$f,g: X\to Y$</span> of continuous <span>$G$</span>-sets, the equaliser in <span>$\textrm{Set}$</span> is a subset of <span>$X$</span>, so it's stabiliser is open because <span>$G$</span> acts continuously on <span>$X$</span>. 
Therefore, any counterexample must specifically be for infinite products.
Writing the counterexample as <span>$x = (x_i)_{i \in I} \in \Pi X_i $</span>, we see that
<div>$$I_x = \bigcap_{i\in I} I_{x_i}$$</div>

Next, I claim that when <span>$G$</span> is a Lie group then <span>$F$</span> preserves infinite products. 
Note that by a topological version of the orbit stabiliser theorem, any continuous <span>$G$</span> set is isomorphic to a disjoint union of <span>$G$</span>-sets of the form <span>$G/U$</span> where <span>$U$</span> is an open subset of <span>$G$</span> (the openness is needed so that <span>$G$</span> acts on the coset space continuously).
One can show that subsets of Lie groups are (topologically) closed[^google], and so an open subgroup <span>$U$</span> must be a (disjoint) union of connected components of <span>$G$</span>. Hence, any intersection of open subgroups must also be a (possibly empty) disjoint union of connected components. Therefore, it will always be open, so will not give a counterexample.

Note that we have now ruled out all of the most familiar/obvious examples of topological groups: discrete groups and Lie groups.
Therefore, we know that we must look for more exotic examples if we are to have any hope of proving the statement.

## A counterexample
Before we go further, note that earlier we showed that for a counterexample to exist it is necessary for <span>$G$</span> to have an infinite collection <span>$\{U_i\}_{i\in I}$</span> of open subgroups whose intersection is note open.
Note however that this is in fact sufficient, by setting <span>$X := \Pi_{i\in I} G/U_i$</span> and taking <span>$x:=(e)_{i \in I}$</span> so that <span>$I_x$</span> is not open.

A good general source of more unusual topologies comes from infinite products (recall for example that the Cantor set can be understood as the product of countably-many copies of \{0, 1\}). 
In this vein, let <span>$G = \Pi_{i \in I} \mathbb{Z}$</span> and then take 
<span>$U_i = \Pi_{j \in \mathbb{N}} a_{ij}\mathbb{Z}$</span>
In fact, for any topological group <span>$G$</span> and non-trivial open subgroup <span>$F$</span> we can perform a similar construction to produce a counterexample.

Another good source of (counter)-examples are non-discrete topologies  <span>$\mathbb{Z}$</span>. 
Consider for example the toplogy with basis given by arithmetic sequences (with non-zero common difference)[^Furstenberg]. 
Then the sets <span>$n\mathbb{Z}$</span> for <span>$n\in\mathbb{N}$</span> are open subgroups, but their intersection is <span>$\{0\}$</span>, which is not open. Note that this example also ha the slight technical advantage that it does not require us to compute products in the category of topological groups.

## Summary
The kind of reasoning I have used here is not in any way novel or unusual; when constructing a counterexample, it is very natural to ask "what must this counterexample look like?". 
However, I think it is interesting that conceptually we can often conceptualise this search as an attempt to prove that the counterexample *doesn't exist*, and in the process of doing so narrow our search space considerably. 

---

[^peculiar]: Truth be told, I find this to be a slightly peculiar category: the (non-topological) category of <span>$G$</span>-sets is very familiar, and the category of topological spaces equipped with continuous <span>$G$</span> action (for <span>$G$</span> a topological group) seems natural (especially seeing as it is an "internalisation" of the usual category of <span>$G$</span>-sets into the category of topoligical spaces). But why would one decide to equip <span>$G$</span> with a topology and then restrict attention just to the discrete sets for <span>$G$</span> to act on? I suppose the fact that <span>$BG$</span> is a topos is quite nice, but it doesn't quite feel enough on it's own. I wonder how t(if at all) this category is related to the classifying space of <span>$G$</span>.

[^right]: Mac Lane and Moerdijk use a right action, but who has time for that?

[^likely]: Indeed, this may well be the case

[^google]: I'm no Lie group guru; I googled this

[^Furstenberg]: The erudite reader will recognise this as the topology from [Furstenberg's proof of the infinitude of the primes](https://en.wikipedia.org/wiki/Furstenberg%27s_proof_of_the_infinitude_of_primes)