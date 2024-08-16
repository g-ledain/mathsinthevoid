---
layout: post
title:  "Applications of the orbit-stabiliser theorem"
date:   2024-07-17 00:00:00 +0100
categories: 
---

The orbit-stabiliser theorem is a theorem about group actions on sets but it really shines when applied to a group acting on itself.

# The conjugation action

## The action
We have already seen how a group <span>$G$</span> acts on itself and on any collection of cosets <span>$G/H$</span> by left-multiplication - the action is transitive and has stabiliser <span>$H$</span>. There is another action of <span>$G$</span> on itself which always exists - the conjugation action. Specifically, we have an action
<div>$$ G\times G \to G $$</div>
<div>$$ g.h := ghg^{-1}$$</div>
This action has the advantage that conjugation is always an automorphism - so its "curried" form gives a map <span>$G \to \textrm{Hom}_{\textrm{Grp}}(G,G)$</span> rather than simply a map <span>$G \to \textrm{Hom}_{\textrm{Set}}(G,G)$</span> which one would normally have for a group action[^quotients]. 

When we see a new group action we should always compute its orbits, stabilisers and fixed points.

*Definition and notation*[^notation]:\
Let <span>$G$</span> be a group and <span>$g\in G$</span>. We define:
 - The conjugacy class 
<div>$$C(g) = \{hgh^{-1}: h\in G\} $$</div>
 - The centraliser 
<div>$$ C_G(g) = \{h\in G: hgh^{-1}\} = \{h\in G: hg=gh\} $$</div>
 - The centre 
<div>$$Z(G)=\{g\in G: gh=hg \text{ for all } h\in G\} = \{g\in G: ghg^{-1}=h \text{ for all } h\in G\}$$</div>

 *Proposition*: \
 Consider a group <span>$G$</span> acting on itself by conjugation and let <span>$g\in G$</span>. Then:
 - (i) <span>$\textrm{Orb}(g) = C(g)$</span>
 - (ii) <span>$\textrm{Stab}(g) = C_G(g)$</span>
 - (iii) <span>$\textrm{Fix}(g) = C_G(g)$</span>
 - (iv) <span>$g\in \textrm{Stab}(h) \Leftrightarrow h\in \textrm{Stab}(g) \Leftrightarrow g\in \textrm{Fix}(h) \Leftrightarrow h\in \textrm{Stab}(g) \Leftrightarrow g, h \text{ commute }$</span>
 - (v) <span>$ Z(G) = \textrm{Fix}(G) = \bigcap_{g\in G} C_G(g) $</span>[^consequence]

 Proof: Exercise

 The above proposition may seem rather trivial but it is worth stopping to reflect on a few things:
  - There is evidently a very strong link between commutation and conjugation. This link plays an important role in elementary group theory.
  - The centraliser shows up as _both_ the stabiliser and the fixed-points! This turns out to be unreasonably important. Specifically, for a generic group action of <span>$G$</span> on a set <span>$X$</span>, the set of fixed-points is just a plain set, whereas the stabilisers are always subgroups of <span>$G$</span>. However in our case the fixed-points also form a subgroup![^automorphisms]. We will return to this later.

We can extend these notions to subsets of <span>$G$</span>, and doing so leads to another concept which will be important to us - the _normaliser_.

*Definition: Centraliser and normaliser*\
Let <span>$G$</span> be a group and <span>$S\subseteq G$</span>. We define:
 - The centraliser of <span>$S$</span> to be 
<div>$$C_G(S):=\{g\in G: gsg{-1}=s \text{ for all } s\in S\} = \bigcap_{s\in S} C_G(s) $$</div>
 - The normaliser of <span>$S$</span> to be 
<div>$$N_G(S):=\{ g\in G: gSg^{-1}= S\} $$</div>

When <span>$H$</span> is a subgroup of <span>$G$</span>, the normaliser <span>$N_G(H)$</span> is the largest subgroup of <span>$G$</span> in which <span>$H$</span> is normal. However in general the centraliser is _not_ the largest subgroup of <span>$G$</span> in which <span>$S$</span> is central. When <span>$S$</span> is _commutative_, then <span>$C_G(S)$</span> *is* the largest subgroup of <span>$G$</span> such that <span>$C_G(S)$</span> in which <span>$S$</span> is central.

The above definitions are best understood as follows: Since <span>$G$</span> acts on <span>$G$</span> by conjugation, it therefore also acts on <span>$\mathcal{P}(G)$</span>. The normaliser <span>$N_G(S)$</span> is then the stabiliser of <span>$S$</span>. The difference between the centraliser and normaliser of <span>$S$</span> is the difference between a set being fixed _as a set_ and being fixed _pointwise_.

## Orbit decomposition of the conjugation action
Whenever a group <span>$G$</span> acts on a set <span>$X$</span>, we should think about the orbit decomposition of <span>$X$</span>. 

The very smallest orbits contain the most "special" elements of <span>$X$</span> - their stabiliers are largest, so they are the "most symmetrical". I like to think of these elements as lying in the "heart" of the set <span>$X$</span>; the two pictures I keep in mind are the centre of a rotation (say, under the usual action of <span>$S^1$</span> on the plane by rotations) or the axis of a reflection (say, under the action of <span>$\mathbb{Z}/2\mathbb{Z}$</span> by a reflection). The point (resp. the axis) are the only points with nontrivial stabiliser, and all the other points revolve around them.

The largest orbits contain the most "generic" elements of <span>$X$</span> - in most real-life situations, especially geometrical ones, only a finite/discrete set have non-trivial stabilisers[^example]. Actions by finite groups tend to have larger stabilisers but the intuition is good to bear in mind.

When <span>$G$</span> is a <span>$p$</span>-group[^definition], this decomposition is especially simple and powerful: the stabilisers are all powers of <span>$p$</span> and so we can image <span>$X$</span> as having a "filtration" by powers of <span>$p$</span> according to the size of the stabiliser. We can view the lower powers of <span>$p$</span> as being "leading terms" in a kind of power series expansion, and many arguments consist of comparing these leading terms[^adic]. 

In this vein, we now come to possibly the most important application of the orbit-stabiliser theorem to finite group theory.

*Lemma: The <span>$p$</span>-group fixed-point lemma*\
Let <span>$G$</span> be a finite <span>$p$</span>-group acting on a finite set <span>$X$</span>. Then
<div>$$|X| \equiv |\textrm{Fix}(X)| \text{ mod } p$$</div>

Proof:\
We have 
<div>$$X = \coprod_{\mathcal{O} \in \textrm{Orbit}(X)} \mathcal{O} = \textrm{Fix}(X) \coprod \left(\coprod_{\mathcal{O} \in \textrm{Orbit}(X)\text{ nontrivial}} \mathcal{O}\right)$$</div>
so
<div>$$ |X| = \sum\limits_{\mathcal{O} \in \textrm{Orbit}(X)} |\mathcal{O}| = |\textrm{Fix}(X)| + \sum\left(\sum\limits_{\mathcal{O} \in \textrm{Orbit}(X)\text{ nontrivial}} |\mathcal{O}|\right) $$</div>
But by the orbit stabiliser theorem <span>$|\mathcal{O}|$</span> divides <span>$|G|$</span>, so when <span>$|\mathcal{O}|>1$</span>, we have <span>$p$</span> divides <span>$|\mathcal{O}|$</span>.

The same logic of splitting into trivial versus non-trivial orbits underlies a classic result called the "class equation".

*Proposition: The class equation*\
For a finite group <span>$G$</span> we have
<div>$$|G| =  \sum\limits_{\text{conjugacy classes}} [G:C_G(g)] = |Z(G)| + \sum\limits_{\text{non-trivial conjugacy classes}} [G:C_G(g)]$$</div>

Proof: use the orbit-stabiliser theorem and the orbit decomposition.

# Some consequences in finite group theory

## <span>$p$</span>-groups
Applying our fixed-point theorem for <span>$p$</span>-groups acting on themselves by conjugation immediately gives the following:

*Proposition: The centre of a <span>$p$</span>-group*\
<span>$p$</span>-groups have non-trivial centre.

Proof:\
By the <span>$p$</span>-group fixed-point lemma, <span>$p$</span> divides <span>$|Z(G)|$</span>. But <span>$e\in Z(G)$</span> so <span>$|Z(G)|\geq p$</span>.

Corollary: <span>$p$</span>-groups are nilpotent, and in particular are solvable.

*Proposition:*\
Suppose that <span>$G$</span> is a group and <span>$|G|=p^2$</span>. Then <span>$G\cong C_{p^2}$</span> or <span>$G\cong C_p \times C_p$</span>.

Proof:\
By the previous result, we have <span>$Z(G) \neq \{e\}$</span> so fix <span>$x\in Z(G)\setminus\{e\}$</span>. If <span>$G$</span> is cylic we're done, so suppose <span>$y \in G\setminus \langle x \rangle$</span>. Since <span>$G$</span> is not cyclic and <span>$x,y\neq e$</span> we have by Lagrange that <span>$\textrm{ord}(x)=\textrm{ord}(y)=p$</span>. Now <span>$\langle x \rangle \cap \langle y \rangle = 1 \text{ or } p$</span> and <span>$|\langle x,y \rangle| = p \text{ or } p^2$</span>. But <span>$y \not\in \langle x \rangle$</span> so <span>$\langle x \rangle \cap \langle y \rangle = 1$</span> and <span>$|\langle x,y \rangle| = p^2$</span>. Define
<div>$$\phi: C_p\times C_p \to G $$</div>
<div>$$(n,m) \mapsto x^ny^m $$</div>
Then <span>$\phi$</span> is:
 - A homomorphism since <span>$x,y$</span> commute 
 - Injective since <span>$\langle x \rangle \cap \langle y \rangle = 1$</span>
 - Surjective since <span>$|\langle x,y \rangle| = p^2$</span>

Note that the final part of this argument is entirely generic: whenever <span>$H,K$</span> are subgroups of <span>$G$</span> such that elements of <span>$H$</span> commute with elements of <span>$K$</span> and <span>$H\cap K = \{e\}$</span>, we have <span>$G\cong H\times K$</span> via an analogous map.

## Cauchy's theorem
So far we have applied the orbit-stabiliser theorem to groups whose order is divisible by a single prime <span>$p$</span>. However, it can also be applied to get information about the behaviour of a prime <span>$p$</span> dividing the order of an arbitrary group <span>$G$</span>. In particular:
 - (i) Cauchy's theorem states that if <span>$p$</span> divides <span>$|G|$</span>, then <span>$G$</span> has an element of order <span>$p$</span> (and hence a subgroup of order <span>$p$</span>)
  - (ii) At the other extreme, Sylow's (first) theorem states that if <span>$p^n$</span> is the largest power of <span>$p$</span> dividing <span>$|G|$</span>, then <span>$G$</span> has a subgroup of order <span>$p^n$</span>
  - (iii) In fact, for *any* prime power <span>$p^k$</span> dividing <span>$|G|$</span>, <span>$G$</span> has a subgroup of order <span>$p^k$</span>.[^incredible]
In fact, we can already deduce (iii) conditionally on (ii): Suppose <span>$P$</span> has order <span>$p^n$</span>. We saw above that <span>$P$</span> is therefore solvable. Hence, it has a filtration <span>$\{e\}\subseteq P_1 \subseteq P_2 \subseteq \ldots P_{n-1} \subseteq P_n = P$</span> with <span>$P_k/P_{k-1} \cong C_p$</span>. Then <span>$P_k$</span> has order <span>$p^k$</span>. 

*Theorem: Cauchy's theorem*\
Let <span>$G$</span> be a finite group and suppose <span>$p$</span> divides <span>$|G|$</span>. Then <span>$G$</span> has an element of order <span>$p$</span>.

Proof 1:\
Define 
<div>$$X = \{(g_1,\ldots, g_p) \in G^p: g_1g_2\ldots g_p = e\} $$</div>
and let <span>$C_p$</span> act on <span>$X$</span> by cyclic permutation; this action is well-defined since
<div>$$g_2\ldots g_pg_1 = g_1^{-1}g_1\ldots g_pg_1 = g^{-1}g_1 = e $$</div>
But by the <span>$p$</span>-group fixed-point lemma
<div>$$|\textrm{Fix}(X)| \equiv |X| = |G|^{p-1} \equiv 0 \textrm{ mod } p$$</div>
and
<div>$$\textrm{Fix}(X) = \{(g,g,\ldots,g): g\in G \text{ has order } 1 \text{ or } p\} $$</div>
Now <span>$e\in \textrm{Fix}(X)$</span> so <span>$|\textrm{Fix}(X)| \geq p$</span> and any non-identity element of <span>$\textrm{Fix}(X)$</span> then has order <span>$p$</span>.

This argument is almost *too* slick to be easily understood. To get a better grasp on it, consider the case <span>$n=2$</span>; then the fibres of the map <span>$x\mapsto x^2$</span> partition <span>$G$</span> into self-inverse elements and element-inverse pairs. The identity element is always self-inverse, so when <span>$|G|$</span> is even, we then know that there has to be another self-inverse element i.e. an element of order <span>$2$</span>. The above proof should be seen as an adaptation of this strategy to deal with other primes.

We can also give a less slick argument, which I prefer:

Proof 2:\
By induction on <span>$|G|$</span>[^hate]. \
Case <span>$G$</span> is Abelian: Pick <span>$g\in G$</span>. We have three possibilities:
 - (i) <span>$\textrm{ord}(g) = p$</span>, we're done
 - (ii) <span>$p|\textrm{ord}(g)$</span>. Then some power of <span>$g$</span> has order <span>$p$</span>
 - (iii) <span>$p\not |\textrm{ord}(g)$</span>. Then since <span>$G$</span> is Abelian, the subgroup <span>$\langle g\rangle$</span> is normal so we have the quotient group <span>$G/\langle g\rangle$</span>. By induction, <span>$G/\langle g\rangle$</span> has an element of order <span>$p$</span>, whose preimage in <span>$G$</span> has order divisible by <span>$p$</span>, and we're in case (ii).
Case <span>$G$</span> is not Abelian: Note that <span>$|Z(G)| < |G|$</span>. If <span>$p$</span> divides <span>$|Z(G)|$</span>, then by induction <span>$Z(G)$</span> has an element of order <span>$p$</span> and we're done. So suppose that <span>$p$</span> does not divide <span>$|Z(G)|$</span>. By the class equation
<div>$$|G| =  \sum\limits_{\text{conjugacy classes}} [G:C_G(g)] = |Z(G)| + \sum\limits_{\text{non-trivial conjugacy classes}} [G:C_G(g)]$$</div>
and <span>$p$</span> divides <span>$|G|$</span> so there exists <span>$g\in G\setminus Z(G)$</span> such that <span>$p$</span> does not divide <span>$\frac{|G|}{|C_G(g)|}$</span>, hence <span>$p$</span> divides <span>$|C_G(g)|$</span>. By assumption <span>$g\not \in Z(G)$</span> so <span>$|C_G(g)| < |G|$</span> and by induction <span>$C_G(g)$</span> has an element of order <span>$p$</span>.

The main idea (for the non-Abelian case) is to find a proper subgroup of <span>$G$</span> which also has order divisible by <span>$p$</span>. The class equation allows us to play the centre and centralisers against one another in this regard. Notice how it is very important then that the fixed points of the conjugation action form a group! 

In fact, in both the Abelian and non-Abelian case, one is making use of the duality between substructures and quotient structures - in the Abelian case this is subgroups and quotient groups and in the non-Abelian case this is in the category of <span>$G$</span>-sets. Specifically, fixed-points form a sub-<span>$G$</span>-set and the stabiliser <span>$C_G(g)$</span> is like a kind of kernel for the <span>$G$</span>-action on that orbit (that is, conjugacy class) and thus represents how the conjugacy class arises as a quotient <span>$G$</span>-set of <span>$G$</span> (under the conjugation action).

Next time we'll look at some proofs of Sylow's theorems, many of which are souped-up versions of the above proofs.



[^quotients]: Similarly to the left-multiplication action of <span>$G$</span> on the cosets <span>$G/H$</span>, one can have a conjugation action of <span>$G$</span> on <span>$G/H$</span> but it is only well-defined when <span>$H$</span> is a normal subgroup of <span>$G$</span> - thus, it is also an action of <span>$G$</span> on  the group <span>$G/H$</span> by group automorphisms. 

[^notation]: The notation here is awful: <span>$C(G)$</span> and <span>$C_G(g)$</span>? Really? What if I have a subgroup <span>$H \subseteq G$</span> and I want to compare the conjugacy class of <span>$h\in H$</span> with respect to <span>$H$</span> and <span>$G$</span>? I can't use <span>$C_H(g)$</span> and <span>$C_G(g)$</span>. There are probably alternative notations but I am lazy.

[^automorphisms]: This is ultimately a consequence of the action of <span>$G$</span> on itself being by _automorphisms_. More generally you can check that for any group <span>$G$</span> acting on a group <span>$H$</span> by automorphisms, <span>$\textrm{Fix}(g)$</span> is always a subset of <span>$H$</span>.

[^consequence]: This is just a consequence of the general fact that <span>$\textrm{Fix}(G) = \bigcap_{g\in G} \textrm{Fix}(g)$</span>.

[^example]: The two following examples are prime examples of this phenomenon. A slightly more advanced example is the action of <span>$\textrm{SL}_2(\mathbb{Z})$</span> on the upper half-plane by Mobius transformations - the analysis of the stabilisers of this action is an elementary part of the theory of modular forms.

[^definition]: That is, the order of <span>$G$</span> is a power of <span>$p$</span>.

[^adic]: This power series analogy is the concept underlying <span>$p$</span>-adic numbers.

[^incredible]: This is one of those slightly incredible facts which makes me say: *why did no one tell me?*

[^hate]: I actually really hate to put this at the start of the proof - it's much nicer to start the argument and let the idea to use induction fall out of it naturally. But the argument isn't technically correct if you only start inducting halfway through.