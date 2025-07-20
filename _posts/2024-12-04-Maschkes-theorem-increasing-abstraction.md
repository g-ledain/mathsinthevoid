---
layout: post
title:  "Maschke's theorem at increasing levels of abstraction"
date:   2024-12-04 00:00:00 +0000
categories: 
---

I've recently been ruminating on Maschke's theorem, and have been pleasantly surprised by how much of the proof comes down to a few simple ideas, namely using a natural projection onto invariant subspaces and the monoidal closed structure of the category of representations.

Throughout, fix a finite group <span>$G$</span> and a field <span>$k$</span> whose characteristic does not divide the order of <span>$G$</span>, over which we consider vector spaces.

# A down-to-earth proof

*Theorem: Maschke's theorem*  
Let <span>$\rho: G \to \textrm{GL}(V)$</span> be a <span>$G$</span>-representation and <span>$U \subseteq V$</span> a subrepresentation. Then there exists a subrepresentation <span>$W \subseteq V$</span> such that 
<div>$$ V = U \oplus W $$</div>

*Proof:*  
Let <span>$i: U \to V$</span> be the inclusion map. By linear algebra, there exists a map <span>$r: V \to U$</span> such that <span>$r\circ i = \textrm{id}_U$</span>. Now define 
<div>$$r': V \to U $$</div>
<div>$$r'(v) = \frac{1}{|G|} \sum_{g\in G} g.r(g^{-1}.v) $$</div>
and
<div>$$ W: = \textrm{ker}(r') $$</div>
I claim that <span>$W$</span> is the desired direct complement to <span>$U$</span>. An easy symmetry argument shows that <span>$W$</span> is <span>$G$</span>-invariant. By another symmetry argument, we see that <span>$r'\circ r' = r'$</span> i.e. that <span>$r'$</span> is a projection, which gives 
<div>$$V = \textrm{im}(r') \oplus \textrm{ker}(r') = U \oplus W$$</div>
where <span>$r'$</span> is surjective because <span>$r'\circ i = \textrm{id}_U$</span>

This is a nice proof, and has the virtue of being very hands-on. It is even more hands-on if you spell out the symmetry arguments and show that <span>$W$</span> is a direct complement by a direct argument rather than by appealing to general facts about projection maps.

# Monoidal closure

As nice as it is, our proof doesn't feel especially revealing. In particular, the map <span>$r'$</span> is key to the whole thing but is rather pulled out of a hat. 

The proof ultimately rests on three key facts:
 - If <span>$V$</span> and <span>$W$</span> are <span>$G$</span>-representations, then so is[^ambient] <span>$\textrm{Hom}_(V,W)$</span>, where <span>$G$</span> acts by 
<div>$$(g.f)(v) = g.f(g^{-1}v) $$</div>
 - For any <span>$G$</span>-representation <span>$V$</span>, we have a projection <span>$\pi^V: V \to V^G$</span> onto the <span>$G$</span>-invariants given by 
 <div>$$\pi^V(v) = \frac{1}{|G|}\sum_{g\in G} g.v$$</div>
 - The invariants <span>$\textrm{Hom}_{V,W}^G$</span> are exactly the maps of <span>$G$</span>-representations from <span>$V$</span> to <span>$W$</span>


The first fact essentially tells us that the category <span>$G-\textrm{rep}$</span> of <span>$G$</span>-representations is a monoidal closed category, with the tensor product as monoidal product. The second one has an important naturality property: any map of <span>$G$</span>-reps <span>$f: V\to W$</span> restricts to a map <span>$f: V^G \to W^G$</span> and we have
<div>$$f\circ \pi^V = \pi^V \circ f $$</div>

The other piece of the puzzle lies in viewing Maschke's theorem as a story about short exact sequences, and in particular about "promoting" structures on short exact sequences of vector spaces to structures on short exact sequences of <span>$G$</span>-representations.

Recall the following fact from homological algebra:

*Proposition:*  
Let 
<div>$$0 \to U \xrightarrow{i} V \xrightarrow{q} W \to 0$$</div>
be a short exact sequence in some Abelian category. Then the following are equivalent:
 1. <span>$i$</span> splits. That is, there is a map <span>$r: V \to U$</span> such that <span>$r\circ i = \textrm{Id}_U$</span>
 2. <span>$q$</span> splits. That is, there is a map <span>$s: W \to V$</span> such that <span>$q\circ s = \textrm{Id}_W$</span>
 3. We have a direct sum <span>$V \cong U \oplus W$</span>

More specifically, <span>$r,s$</span> can be obtained from the direct sum as the projection and inclusion (respectively) along the summands, and 
<div>$$V = \textrm{im}(i\circ r) \oplus \textrm{ker}(i\circ r) = i(U)\oplus \textrm{ker}(i\circ r) \cong U \oplus W$$</div>
and
<div>$$V = \textrm{im}(s\circ q) \oplus \textrm{ker}(s\circ q) = s(W)\oplus \textrm{ker}(s\circ q) \cong U \oplus W$$</div>

*Proof:* A mildly tedious, but nontheless important exercise.

There are two contexts in which it will be natural for us to consider this lemma: in the category of vector spaces[^trivial], and the category of <span>$G$</span>-representations.

Our proof of Maschke's theorem can now be summarised as follows: The short exact sequence of <span>$G$</span>-reps admits a splitting as vector spaces. Applying the projection map to the splitting makes it into a map of <span>$G$</span>-reps, and the naturality of the projection means that this map of <span>$G$</span>-reps still splits the original short exact sequence. Thus, we have the direct complement as required.

The proof in more detail is as follows:

*Theorem: Maschke's theorem*  
Any short exact sequence 
<div>$$ 0 \xrightarrow{i} U \to V \xrightarrow{q} W \to 0 $$</div>
of <span>$G$</span>-representations on <span>$k$</span>-vector spaces splits in the category of <span>$G$</span>-reps.

*Proof:*[^lie-algebras]
In our "down-to-earth" proof, we showed that <span>$i$</span> split. For variety, we will now show thar <span>$q$</span> splits (but either argument can trivially be adapted to cover the other situation). Again, there exists a map of vector spaces <span>$s: W\to V$</span> such that <span>$s\circ q = \textrm{Id}_W$</span>. I claim that <span>$\pi^{\textrm{Hom(W,V)}}(s)$</span> is a map of <span>$G$</span>-representations which splits <span>$q$</span>. To see this, define a map <span>$q_*$</span> by
<div>$$q_*: \textrm{Hom}(V,V) \to \textrm{Hom}(V,W) $$</div>
<div>$$f \mapsto q\circ f $$</div>
and note that by naturality of <span>$\pi$</span> we have 
<div>$$q_* \circ \pi^{\textrm{Hom}(W,V)} = \pi^{\textrm{Hom}(W,W)} \circ q_*$$</div>
Applying this map to <span>$s$</span> gives
<div>$$q \circ \left(\pi^{\textrm{Hom}(W,V)}(s)\right) = \pi^{\textrm{Hom}(W,W)}( q_*(s)) =  \pi^{\textrm{Hom}(W,W)}( q\circ s) = \pi^{\textrm{Hom}(W,W)}( \textrm{Id}_{W}) = \textrm{Id}_{W}$$</div>

# Natural transformations
We're now ready for the final level of abstract nonsense. We have seen above that Maschke's theorem comes down to applying a projection map <span>$\pi$</span> to several vector spaces in such a way that it respects the maps between them, and shrewdly applying this to the monoidal closed structure on the category of <span>$G$</span>-reps. We can collect all these maps <span>$\pi$</span> together into a natural transformation.

*Definitions:*  
We define the invariants functor by
<div>$$\textrm{inv}: G\textrm{-rep} \to G\textrm{-rep} $$</div>
<div>$$\textrm{inv}(V) = V^G $$</div>
<div>$$\textrm{inv}(f) = f^G: V^G \to W^G \text{ is the restriction of } f$$</div> 

We define the inclusion natural transformation
<div>$$i: \textrm{inv} \Rightarrow \textrm{Id}_{G\textrm{-rep}} $$</div>
<div>$$i^V: V^G \to V \textrm{ is the inclusion}$$</div>
and the projection natural transformation
<div>$$\pi: \textrm{Id}_{G\textrm{-rep}} \Rightarrow \textrm{inv} $$</div>
<div>$$\pi^V: V \to V^G \textrm{ is the projection defined earlier}$$</div>

Note that the action of <span>$\textrm{inv}$</span> on morphisms is actually determined by the fact that <span>$i$</span> is a natural transformations and its components are monomorphisms - this corresponds to the map <span>$f^G$</span> being a restriction of <span>$f$</span> and hence "not providing any more information" than <span>$f$</span> does.

This new language and notation largely leaves the previous proof unchanged, but necessitates inserting a few more instances of <span>$i$</span> (which previously were elided because we equivocated on whether <span>$q_\ast$</span> was a map <span>$\textrm{Hom}(V,V) \to \textrm{Hom}(V,W)$</span> or <span>$\textrm{Hom}(V,V)^G \to \textrm{Hom}(V,W)^G$</span>), so I won't rehash it. What is interesting here is not a new presentation of the proof, but rather that several of the key ideas of the proof can be categorified. Ultimately, the naturality of <span>$\pi^V$</span> is really what makes the whole thing tick: otherwise, we couldn't be sure that the map of <span>$G$</span>-representations that we soup up would still split our original short exact sequence.

# Further
One can surely take all of this much further - I imagine there are rather general settings in which this argument can be made to work (that <span>$\textrm{Hom}(V,W)^G$</span> comprises the maps of <span>$G$</span>-reps feels the most "non-categorical" part of the argument as presented here), and there are (co)homological techniques and interpretations of the semisimplicity of various categories of representations. However, I do not know them nearly well enough to blog about them.

# A small aside
Note that the functors <span>$i$</span> and <span>$\pi$</span> of course have the very nice property that <span>$\pi \circ i = \textrm{Id}_{\textrm{inv}}$</span>. Consequently, <span>$\pi^v$</span> always splits <span>$i^V$</span> so the invariants <span>$V^G$</span> always have direct complement in <span>$V$</span>, namely <span>$V = V^G\oplus \textrm{ker}(\pi^V) $</span>. You will notice, however, that this fact is not in any way necessary for all of the above arguments - you will only see <span>$i$</span> and <span>$\pi$</span> composed in the order <span>$i^V \circ \pi^V$</span>. This tickles me.

---

[^ambient]: All the hom-sets here are to be understood as hom-sets in the category of vector spaces
[^lie-algebras]: I first saw this proof during a course on the Lie algebras. The lecturer reassured us that the proof should be familiar because it was essentially the "same proof" as the one we knew from the representation theory of finite groups. This was quite confusing, as the proofs superficially look pretty different. This post is in essense me working my way backwards to understand how the proof looks for finite groups [^difference]
[^difference]: There's quite an interesting difference between the case of finite groups and of semisimple Lie algebras. Specifically, in the finite group case, one shows that there is a natural projection onto the invariant subspace. This yields as a corollary both the semisimplicity of the category of representations, and the fact that the invariants always have a direct complement. In the case of semisimple Lie algebras, one instead *first* shows that the invariants always have a direct complement. This then yields a natural projection, and hence the semisimplicity of the representations. To my knowledge, there is no nice formula for the projection like there is in the case of finite groups, but the Casmimir element comes close: its kernel is exactly, but it acts non-trivially on the complement of the kernel.
[^trivial]: where, incidentally, the hypotheses of the lemma always hold, so the lemma is rather trivial