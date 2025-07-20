---
layout: post
title:  "Maschke's theorem at increasing levels of abstraction"
date:   2024-12-04 00:00:00 +0000
categories: 
---

I've recently been ruminating on Maschke's theorem, and have been pleasantly surprised by how much of the proof comes down to a few simple ideas, namely using a natural projection onto invariant subspaces and the monoidal closed structure of the category of representations.

Throughout, fix a finite group $G$ and a field $k$ whose characteristic does not divide the order of $G$, over which we consider vector spaces.

# A down-to-earth proof

*Theorem: Maschke's theorem*  
Let $\rho: G \to \textrm{GL}(V)$ be a $G$-representation and $U \subseteq V$ a subrepresentation. Then there exists a subrepresentation $W \subseteq V$ such that 
$$ V = U \oplus W $$

*Proof:*  
Let $i: U \to V$ be the inclusion map. By linear algebra, there exists a map $r: V \to U$ such that $r\circ i = \textrm{id}_U$. Now define 
$$r': V \to U $$
$$r'(v) = \frac{1}{|G|} \sum_{g\in G} g.r(g^{-1}.v) $$
and
$$ W: = \textrm{ker}(r') $$
I claim that $W$ is the desired direct complement to $U$. An easy symmetry argument shows that $W$ is $G$-invariant. By another symmetry argument, we see that $r'\circ r' = r'$ i.e. that $r'$ is a projection, which gives 
$$V = \textrm{im}(r') \oplus \textrm{ker}(r') = U \oplus W$$
where $r'$ is surjective because $r'\circ i = \textrm{id}_U$

This is a nice proof, and has the virtue of being very hands-on. It is even more hands-on if you spell out the symmetry arguments and show that $W$ is a direct complement by a direct argument rather than by appealing to general facts about projection maps.

# Monoidal closure

As nice as it is, our proof doesn't feel especially revealing. In particular, the map $r'$ is key to the whole thing but is rather pulled out of a hat. 

The proof ultimately rests on three key facts:
 - If $V$ and $W$ are $G$-representations, then so is[^ambient] $\textrm{Hom}_(V,W)$, where $G$ acts by 
$$(g.f)(v) = g.f(g^{-1}v) $$
 - For any $G$-representation $V$, we have a projection $\pi^V: V \to V^G$ onto the $G$-invariants given by 
 $$\pi^V(v) = \frac{1}{|G|}\sum_{g\in G} g.v$$
 - The invariants $\textrm{Hom}_{V,W}^G$ are exactly the maps of $G$-representations from $V$ to $W$


The first fact essentially tells us that the category $G-\textrm{rep}$ of $G$-representations is a monoidal closed category, with the tensor product as monoidal product. The second one has an important naturality property: any map of $G$-reps $f: V\to W$ restricts to a map $f: V^G \to W^G$ and we have
$$f\circ \pi^V = \pi^V \circ f $$

The other piece of the puzzle lies in viewing Maschke's theorem as a story about short exact sequences, and in particular about "promoting" structures on short exact sequences of vector spaces to structures on short exact sequences of $G$-representations.

Recall the following fact from homological algebra:

*Proposition:*  
Let 
$$0 \to U \xrightarrow{i} V \xrightarrow{q} W \to 0$$
be a short exact sequence in some Abelian category. Then the following are equivalent:
 1. $i$ splits. That is, there is a map $r: V \to U$ such that $r\circ i = \textrm{Id}_U$
 2. $q$ splits. That is, there is a map $s: W \to V$ such that $q\circ s = \textrm{Id}_W$
 3. We have a direct sum $V \cong U \oplus W$

More specifically, $r,s$ can be obtained from the direct sum as the projection and inclusion (respectively) along the summands, and 
$$V = \textrm{im}(i\circ r) \oplus \textrm{ker}(i\circ r) = i(U)\oplus \textrm{ker}(i\circ r) \cong U \oplus W$$
and
$$V = \textrm{im}(s\circ q) \oplus \textrm{ker}(s\circ q) = s(W)\oplus \textrm{ker}(s\circ q) \cong U \oplus W$$

*Proof:* A mildly tedious, but nontheless important exercise.

There are two contexts in which it will be natural for us to consider this lemma: in the category of vector spaces[^trivial], and the category of $G$-representations.

Our proof of Maschke's theorem can now be summarised as follows: The short exact sequence of $G$-reps admits a splitting as vector spaces. Applying the projection map to the splitting makes it into a map of $G$-reps, and the naturality of the projection means that this map of $G$-reps still splits the original short exact sequence. Thus, we have the direct complement as required.

The proof in more detail is as follows:

*Theorem: Maschke's theorem*  
Any short exact sequence 
$$ 0 \xrightarrow{i} U \to V \xrightarrow{q} W \to 0 $$
of $G$-representations on $k$-vector spaces splits in the category of $G$-reps.

*Proof:*[^lie-algebras]
In our "down-to-earth" proof, we showed that $i$ split. For variety, we will now show thar $q$ splits (but either argument can trivially be adapted to cover the other situation). Again, there exists a map of vector spaces $s: W\to V$ such that $s\circ q = \textrm{Id}_W$. I claim that $\pi^{\textrm{Hom(W,V)}}(s)$ is a map of $G$-representations which splits $q$. To see this, define a map $q_*$ by
$$q_*: \textrm{Hom}(V,V) \to \textrm{Hom}(V,W) $$
$$f \mapsto q\circ f $$
and note that by naturality of $\pi$ we have 
$$q_* \circ \pi^{\textrm{Hom}(W,V)} = \pi^{\textrm{Hom}(W,W)} \circ q_*$$
Applying this map to $s$ gives
$$q \circ \left(\pi^{\textrm{Hom}(W,V)}(s)\right) = \pi^{\textrm{Hom}(W,W)}( q_*(s)) =  \pi^{\textrm{Hom}(W,W)}( q\circ s) = \pi^{\textrm{Hom}(W,W)}( \textrm{Id}_{W}) = \textrm{Id}_{W}$$

# Natural transformations
We're now ready for the final level of abstract nonsense. We have seen above that Maschke's theorem comes down to applying a projection map $\pi$ to several vector spaces in such a way that it respects the maps between them, and shrewdly applying this to the monoidal closed structure on the category of $G$-reps. We can collect all these maps $\pi$ together into a natural transformation.

*Definitions:*  
We define the invariants functor by
$$\textrm{inv}: G\textrm{-rep} \to G\textrm{-rep} $$
$$\textrm{inv}(V) = V^G $$
$$\textrm{inv}(f) = f^G: V^G \to W^G \text{ is the restriction of } f$$ 

We define the inclusion natural transformation
$$i: \textrm{inv} \Rightarrow \textrm{Id}_{G\textrm{-rep}} $$
$$i^V: V^G \to V \textrm{ is the inclusion}$$
and the projection natural transformation
$$\pi: \textrm{Id}_{G\textrm{-rep}} \Rightarrow \textrm{inv} $$
$$\pi^V: V \to V^G \textrm{ is the projection defined earlier}$$

Note that the action of $\textrm{inv}$ on morphisms is actually determined by the fact that $i$ is a natural transformations and its components are monomorphisms - this corresponds to the map $f^G$ being a restriction of $f$ and hence "not providing any more information" than $f$ does.

This new language and notation largely leaves the previous proof unchanged, but necessitates inserting a few more instances of $i$ (which previously were elided because we equivocated on whether $q_\ast$ was a map $\textrm{Hom}(V,V) \to \textrm{Hom}(V,W)$ or $\textrm{Hom}(V,V)^G \to \textrm{Hom}(V,W)^G$), so I won't rehash it. What is interesting here is not a new presentation of the proof, but rather that several of the key ideas of the proof can be categorified. Ultimately, the naturality of $\pi^V$ is really what makes the whole thing tick: otherwise, we couldn't be sure that the map of $G$-representations that we soup up would still split our original short exact sequence.

# Further
One can surely take all of this much further - I imagine there are rather general settings in which this argument can be made to work (that $\textrm{Hom}(V,W)^G$ comprises the maps of $G$-reps feels the most "non-categorical" part of the argument as presented here), and there are (co)homological techniques and interpretations of the semisimplicity of various categories of representations. However, I do not know them nearly well enough to blog about them.

# A small aside
Note that the functors $i$ and $\pi$ of course have the very nice property that $\pi \circ i = \textrm{Id}_{\textrm{inv}}$. Consequently, $\pi^v$ always splits $i^V$ so the invariants $V^G$ always have direct complement in $V$, namely $V = V^G\oplus \textrm{ker}(\pi^V) $. You will notice, however, that this fact is not in any way necessary for all of the above arguments - you will only see $i$ and $\pi$ composed in the order $i^V \circ \pi^V$. This tickles me.

---

[^ambient]: All the hom-sets here are to be understood as hom-sets in the category of vector spaces
[^lie-algebras]: I first saw this proof during a course on the Lie algebras. The lecturer reassured us that the proof should be familiar because it was essentially the "same proof" as the one we knew from the representation theory of finite groups. This was quite confusing, as the proofs superficially look pretty different. This post is in essense me working my way backwards to understand how the proof looks for finite groups [^difference]
[^difference]: There's quite an interesting difference between the case of finite groups and of semisimple Lie algebras. Specifically, in the finite group case, one shows that there is a natural projection onto the invariant subspace. This yields as a corollary both the semisimplicity of the category of representations, and the fact that the invariants always have a direct complement. In the case of semisimple Lie algebras, one instead *first* shows that the invariants always have a direct complement. This then yields a natural projection, and hence the semisimplicity of the representations. To my knowledge, there is no nice formula for the projection like there is in the case of finite groups, but the Casmimir element comes close: its kernel is exactly, but it acts non-trivially on the complement of the kernel.
[^trivial]: where, incidentally, the hypotheses of the lemma always hold, so the lemma is rather trivial