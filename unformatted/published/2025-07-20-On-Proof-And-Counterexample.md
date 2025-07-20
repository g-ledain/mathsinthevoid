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
The authors introduce the category of continuous $G$-sets.

*Definition: Category of continuous $G$-sets*[^peculiar]

Let $G$ be a topological group. 
The category of continuous $G$-sets, written $BG$ has:
 - Objects: Sets $X$ equipped with a left[^right] $G$ action such that the action function $G\times X \to X$ is continuous when $X$ is given the discrete topology
 - Morphisms: $G$-equivariant maps of $G$-sets

We define the group $G^\delta$ to be $G$ equipped with the discrete topology.
We then evidently have an "inclusion" functor

$$i_G : BG \to BG^\delta$$

For any $X \in BG^\delta$ and $x \in X$ we define the stabiliser (or "isotropy subgroup" in their language)

$$I_x : = \{g \in G: g.x = x\}$$

and thus a functor

$$r_G: BG^\delta \to BG$$
$$r_G(X) := \{ x\in X: I_x \text{ is an open subgroup of } G\}$$

An earlier exercise asks one to prove that for $X \in BG^\delta$, the action of $G$ on $X$ is continuous if and only if for each $x \in X$ (so that $r_G$ is well-defined) and that $r_G$ is a right adjoint to $i_G$. 

We now come to the exercise I want to focus on:

> *Exercise:*
> 
> Prove that the forgetful functor $F: BG \to \textrm{Set}$
> need not preserve infinite limits.

The zeroth thing one ought to do is to realise that the exercise means that this is not true for *arbitrary* $G$ rather than for *all* $G$ (since for $G$ a discrete group the limits *are* preserved).

The first thing one ought to do is to compute the limits in $BG$. 
Since $r_G$ is a right adjoint, we can conclude that it takes limits in $\textrm{Set}$ to limits in $BG$, so that 
$$\lim_{i\in I}^{BG} X_i = \lim_{i\in I}^{BG} r_G(X_i) = r_G\left(\lim_{i \in I}^{BG^\delta} X_i\right)$$

Since the forgetful functor $BG^\delta \to \textrm{Set}$ preserves all limits, we see that we need to find some system of $X_i$ and an element $x \in \lim_{i \in I}^\textrm{Set} X_i$ such that $I_x$ is not an open subgroup of $G$.

## Proving the converse
Now, unless you are more intelligent than me[^likely], your first few attempts at an example of a non-preserved limit here will be unsuccessful. 
A useful trick here is instead of trying to find a counterexample to the preservation of infinite limits, *try to prove that infinite limits are preserved by $F$*. 
Of course, this is not an earnest attempt at a proof. 
What we're really trying to do here is to find relatively general conditions under which the statement is false, so that we can exclude a large section of the search space for a counterexample. 

Instead of considering different kinds of group, we will first consider different kinds of limit. 
Recall that any limit can be considered as an equaliser of a product. 
I claim that $F$ preserves equalisers: for any maps $f,g: X\to Y$ of continuous $G$-sets, the equaliser in $\textrm{Set}$ is a subset of $X$, so it's stabiliser is open because $G$ acts continuously on $X$. 
Therefore, any counterexample must specifically be for infinite products.
Writing the counterexample as $x = (x_i)_{i \in I} \in \Pi X_i $, we see that
$$I_x = \bigcap_{i\in I} I_{x_i}$$

Next, I claim that when $G$ is a Lie group then $F$ preserves infinite products. 
Note that by a topological version of the orbit stabiliser theorem, any continuous $G$ set is isomorphic to a disjoint union of $G$-sets of the form $G/U$ where $U$ is an open subset of $G$ (the openness is needed so that $G$ acts on the coset space continuously).
One can show that subsets of Lie groups are (topologically) closed[^google], and so an open subgroup $U$ must be a (disjoint) union of connected components of $G$. Hence, any intersection of open subgroups must also be a (possibly empty) disjoint union of connected components. Therefore, it will always be open, so will not give a counterexample.

Note that we have now ruled out all of the most familiar/obvious examples of topological groups: discrete groups and Lie groups.
Therefore, we know that we must look for more exotic examples if we are to have any hope of proving the statement.

## A counterexample
Before we go further, note that earlier we showed that for a counterexample to exist it is necessary for $G$ to have an infinite collection $\{U_i\}_{i\in I}$ of open subgroups whose intersection is note open.
Note however that this is in fact sufficient, by setting $X := \Pi_{i\in I} G/U_i$ and taking $x:=(e)_{i \in I}$ so that $I_x$ is not open.

A good general source of more unusual topologies comes from infinite products (recall for example that the Cantor set can be understood as the product of countably-many copies of \{0, 1\}). 
In this vein, let $G = \Pi_{i \in I} \mathbb{Z}$ and then take 
$U_i = \Pi_{j \in \mathbb{N}} a_{ij}\mathbb{Z}$
In fact, for any topological group $G$ and non-trivial open subgroup $F$ we can perform a similar construction to produce a counterexample.

Another good source of (counter)-examples are non-discrete topologies  $\mathbb{Z}$. 
Consider for example the toplogy with basis given by arithmetic sequences (with non-zero common difference)[^Furstenberg]. 
Then the sets $n\mathbb{Z}$ for $n\in\mathbb{N}$ are open subgroups, but their intersection is $\{0\}$, which is not open. Note that this example also ha the slight technical advantage that it does not require us to compute products in the category of topological groups.

## Summary
The kind of reasoning I have used here is not in any way novel or unusual; when constructing a counterexample, it is very natural to ask "what must this counterexample look like?". 
However, I think it is interesting that conceptually we can often conceptualise this search as an attempt to prove that the counterexample *doesn't exist*, and in the process of doing so narrow our search space considerably. 

---

[^peculiar]: Truth be told, I find this to be a slightly peculiar category: the (non-topological) category of $G$-sets is very familiar, and the category of topological spaces equipped with continuous $G$ action (for $G$ a topological group) seems natural (especially seeing as it is an "internalisation" of the usual category of $G$-sets into the category of topoligical spaces). But why would one decide to equip $G$ with a topology and then restrict attention just to the discrete sets for $G$ to act on? I suppose the fact that $BG$ is a topos is quite nice, but it doesn't quite feel enough on it's own. I wonder how t(if at all) this category is related to the classifying space of $G$.

[^right]: Mac Lane and Moerdijk use a right action, but who has time for that?

[^likely]: Indeed, this may well be the case

[^google]: I'm no Lie group guru; I googled this

[^Furstenberg]: The erudite reader will recognise this as the topology from [Furstenberg's proof of the infinitude of the primes](https://en.wikipedia.org/wiki/Furstenberg%27s_proof_of_the_infinitude_of_primes)