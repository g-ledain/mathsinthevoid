---
layout: post
title:  "Sylow's theorems"
date:   2024-08-04 00:00:00 +0100
categories: 
---

I never remembered, let alone understood, the proofs of Sylow's theorems (even consistently stating the third one correctly gave me trouble). On the one hand, looking up several different proofs has let me pick and choose which ones I like the best. On the other hand, finding their commonalities has helped me identify the crucial parts of the arguments.

# Sylow I
*Theorem: Sylow I*\
Let <span>$G$</span> be a finite group and <span>$n$</span> be the largest integer such that <span>$p^n$</span> divides <span>$|G|$</span>.
Then for any <span>$0 \leq k \leq n$</span>, there exists a subgroup <span>$P$</span> of <span>$G$</span> with order <span>$p^k$</span>.

Most of the proofs of Sylow I we present here will be souped-up versions of the arguments we used to prove Cauchy's theorem, with the exception of the final proof which iteratively uses Cauchy's theorem to construct subgroups of order <span>$p,p^2,\ldots,p^n$</span>.

We call a subgroup <span>$P$</span> of <span>$G$</span> of order <span>$p^n$</span> a <span>$p$</span>-Sylow subgroup, or just a Sylow subgroup for short. Throughout, we will use <span>$n_p$</span> to refer to the number of <span>$p$</span>-Sylow subgroups of <span>$G$</span>.

Throughout, we will be referring to the largest power of a prime <span>$p$</span> which divides an integer <span>$m$</span>, and it will be helpful to fix some notation for this.

*Definition: <span>$p$</span>-adic valuation:*\
Fix a prime <span>$p$</span>. We write 
<div>$$v_p: \mathbb{Z} \to \mathbb{Z}\cup \{\infty\} $$</div>
<div>$$v_p(x) = \begin{cases} \text{The largest power of } p \text{ which divides } x & \text{ if } x\neq 0 \\ \infty & \text{ if } x=0 \end{cases} $$</div>
We call <span>$v_p(x)$</span> the <span>$p$</span>-adic valuation of <span>$x$</span>.

Our first argument will be a counting argument using group actions. To glue things together, we will need a lemma to relate <span>$p$</span>-divisibility to counting.

*Lemma: Kummer's lemma*\
Let <span>$0\leq k\leq n$</span> and <span>$k \not | u$</span>. Then <span>$p^{n-k}$</span> is the largest power of <span>$p$</span> dividing <span>$\binom{p^nu}{p^k}$</span>

*Proof:* Not now.

*Proof of Sylow I:*
Let 
<div>$$X = \{S\subseteq G: |S|=p^k\} $$</div>
where <span>$G$</span> acts by left-multiplication. We have 
<div>$$v_p(|X|)=\binom{p^nu}{p^k} $$</div>
so 
<div>$$v_p(|X|)= n-k=: r $$</div>
For any <span>$S\in X$</span> and <span>$a\in S$</span>, we have <span>$G_S.a\subseteq S$</span>, so
<div>$$|G_S|=|G_S.a| \leq |S| = p^k $$</div>
so <span>$v_p(|G_S|)\leq k$</span> hence by orbit-stabiliser <span>$v_p(|G.S|) \geq r$</span>. We have 
<div>$$|G| = \sum_{G-\text{ orbits } \mathcal{O} \text{ of } X} |\mathcal{O}|$$</div>
If all the <span>$G.S$</span> have <span>$v_p(|G.S|)>r$</span>, then we would have <span>$v_p(|G|) > r$</span> which is a contradiction. So there exists <span>$S \in X$</span> with <span>$v_p(|G.S|)=r$</span>, hence <span>$v_p(G_S)=k$</span>. But <span>$|G_S|\leq p^k$</span>, so <span>$|G_S|=p^k$</span>, whence <span>$G_S$</span> is the desired subgroup.

As in most proofs using group actions, the most important part is the careful choice of a set and an action of <span>$G$</span> on that set. Why did we choose this particular set and this particular action? We needed to magic up a subgroup of the right order out of thin air, so we may as well start with something we always have in abundance: subsets. As for the action, note that it is easiest to characterise subgroups via the left-multiplication action (rather than, say, the conjugation action): a subset <span>$S\subseteq G$</span> is a subgroup exactly when <span>$S=G_S$</span>. In fact, in the proof we used that for any <span>$S\subseteq G$</span> and <span>$a\in S$</span> we have <span>$G_S.a\in S$</span>, which is lkind of like a half-measure which applies to mere subsets.

After an appropriate set and action were chosen, the key ideas of the proof was the calculation of the <span>$p$</span>-adic valuation of <span>$|X|$</span> via Kummer's lemma, getting a lower bound[^trivial] on the <span>$p$</span>-adic valuation of the orbits, and then comparing 'leading terms'. 

*Another proof of Sylow I:*\
By induction on <span>$|G|$</span>.

**Case <span>$G$</span> is Abelian:**
By the classification of finite Abelian groups[^nice], <span>$G$</span> is a product of prime-power-order cyclic groups. Let the '<span>$p$</span>-part' of the decomposition be isomorphic to 
<div>$$\prod_{i=1}^N \mathbb{Z}/p^{t_i}\mathbb{Z} $$</div>
for some <span>$t_i\in \mathbb{N}$</span>, so <span>$\sum_{i=1}^N t_i = n $</span> and let <span>$g_i$</span> generate the copy of <span>$\mathbb{Z}/p^{t_i}\mathbb{Z}$</span>. For any <span>$0\leq k\leq n$</span>, we can write 
<div>$$k=\sum_{i=1}^N t_i' $$</div>
for some <span>$0\leq t_i'\leq t_i$</span> and then 
<div>$$\langle g_i^{t_1-t_1'},\ldots, g_i^{t_N-t_N'} \rangle \subseteq G$$</div>
has order <span>$p^k$</span>.

**Case <span>$G$</span> is non-Abelian:**
If <span>$p$</span> divides <span>$|Z(G)|$</span>, then write <span>$|Z(G)|=p^ru'$</span> where <span>$p\not | u'$</span>. Since <span>$G$</span> is non-Abelian we have <span>$|Z(G)|<|G|$</span> and since <span>$p$</span> divides <span>$|Z(G)$</span> we have <span>$|G/Z(G)|<|G|$</span>. By the inductive hypothesis[^abelian] there exists a subgroup <span>$A\subseteq Z(G)|$</span> of order <span>$p^r$</span> and since 
<div>$$k-r\leq n-r = v_p(|G/A|) $$</div>
there exists by the inductive hypothesis a subgroup <span>$\tilde{P} = P/A \subseteq G/A$</span> of order <span>$p^{k-r}$</span>.
Now 
<div>$$|P| = |\tilde{P}||A| = p^{k-r}p^r = p^k $$</div>
so <span>$P$</span> is our desired subgroup. 

If <span>$p$</span> does not divide <span>$|Z(G)|$</span>, then by the class equation there exists <span>$g\in G\setminus Z(G)$</span> such that <span>$p$</span> does not divide <span>$|G|/|C_G(g)|$</span>, so <span>$v_p(|C_G(g)) = v_p(|G|)$</span>. Since <span>$g\not\in Z(G)$</span> we have <span>$C_G(g) \neq G$</span> and by the inductive hypothesis <span>$C_G(g)$</span> contains subgroups of the desired order.

We are again using the duality between substructures and quotient structures throughout this argument: both in the guise of the subgroup <span>$A$</span> versus the quotient <span>$G/A$</span>, but also at the level of <span>$G$</span>-sets in the form of the orbit-union <span>$Z(G)$</span> (which is a <span>$G$</span>-subset) versus the stabiliser <span>$C_G(g)$</span> (insofar as a stabiliser is a sort of <span>$G$</span>-set kernel and hence controls a quotient). Once again, the minor miracle that the union of *orbits* <span>$Z(G)$</span> forms a subgroup (rather than just a subset) is of central[^haha] importance in the argument.

*Another another proof of Sylow I:*\
By induction on <span>$k$</span>.\
The case <span>$k=1$</span> is Cauchy's theorem. Suppose there exists a subgroup <span>$P$</span> of order <span>$p^{k-1}$</span>. Note that 
<div>$$N_G(P)/P \subseteq G/P $$</div>
is the fixed points of the left-multiplication action of <span>$P$</span> on <span>$G/P$</span>, that is:
<div>$$N_G(P)/P = (G/P)^P $$</div>
Since <span>$p^n$</span> divides <span>$|G|$</span> and <span>$n>k-1$</span>, we have
<div>$$|G/P| \cong 0 \text{ mod } p $$</div>
and by the <span>$p$</span>-group fixed-point lemma we have 
<div>$$ |N_G(P)/P| = |G/P| \cong 0 \text{ mod } p$$</div>
By Cauchy's theorem[^funny], there exists <span>$g\in N_G(P)$</span> such that <span>$[g]\in N_G(P)/P$</span> has order <span>$p$</span>. Let
<div>$$\pi: N_G(P) \twoheadrightarrow P $$</div> 
be the quotient map and let
<div>$$P'= \pi^{-1}(\langle [g]\rangle) = \langle g,P\rangle $$</div>
Then
<div>$$|P'|=|P||\langle[g]\rangle|=p^{k-1}p = p^k $$</div>
which completes the induction.

A crude attempt at this argument would be to use Cauchy to get a subgroup <span>$P_1$</span> of order <span>$p$</span>, then apply Cauchy to <span>$G/P$</span> and take the pre-image to get a subgroup <span>$P_2$</span> of order <span>$p^2$</span> and so on. The issue is that <span>$P_1,P_2,\ldots$</span> may not be normal. The normaliser provides the technical fix which makes the argument work; <span>$N_G(P)$</span> is by definition the largest subgroup of <span>$G$</span> in which <span>$P$</span> is normal.

The above proof actually shows something stronger than the above theorem statement - namely that every subgroup of <span>$G$</span> of order <span>$p^k$</span> (with <span>$k<n$</span>) is contained in a subgroup of order <span>$p^{k+1}$</span>. Consequently, the subgroups of order <span>$p^n$</span> are exactly those <span>$p$</span>-subgroups which are maximal with respect to inclusion.

# Sylow II and III
The second and third Sylow theorems are closely related to one another, closer than either is to the first. They both pertain to how <span>$G$</span> and its subgroups act on Sylow subgroups by conjugation. Usually, one uses one to help prove the other, and we will see both directions.

# Sylow II
*Theorem: Sylow II:*\
Let <span>$G$</span> be a finite group and <span>$P$</span> a <span>$p$</span>-Sylow subgroup. For any <span>$p$</span>-subgroup <span>$Q\subseteq G$</span>, there exists <span>$g\in G$</span> with
<div>$$gQg^{-1} \subseteq P $$</div>
In particular, Sylow subgroups are unique up to conjugation - equivalently, <span>$G$</span> acts transitively on the <span>$p$</span>-Sylows by conjugation.

*Corollary:* By orbit-stabiliser,  <span>$n_p$</span> divides <span>$|G|$</span>[^different].

It's worth thinking philosophically about Sylow II a little bit: Sylow I is a very straightforward existence theorem about <span>$p$</span>-subgroups of <span>$G$</span>, and in particular <span>$p$</span>-Sylow subgroups. We therefore might want a uniqueness theorem for <span>$p$</span>-Sylow subgroups. The most naive uniqueness theorem - that Sylow subgroups are unique 'up to equality' is as false as you can get - basically any group you care to think of provides a counterexample. Slightly better might be that Sylow subgroups are unique up to isomorphism. Even better would be that they are unique up to isomorphism *as subgroups*[^isomorphism]. Even better than this would be for this to isomorphism to come from within <span>$G$</span> itself - for it to be a conjugation. This is exactly what the above theorem says. So Sylow II affirms the most optimistic uniqueness statement for Sylow subgroups we could realistically hope for. There is mercy in the world after all!

*Proof of Sylow II:*
Consider the left-multiplication action of <span>$Q$</span> on <span>$G/P$</span>. By the <span>$p$</span>-group fixed point lemma, we have 
<div>$$|(G/P)^Q|\cong |G/P| \not\cong 0 \text{ mod }p $$</div>
so there exists <span>$g\in (G/P)^Q$</span>. Then <span>$g^{-1}Qg\subseteq P$</span>.

Note that this proof *doesn't* use the conjugation action, despite its statement being about conjugation. Huh. I have nothing insightful to say about this. This proof also yields another proof that the <span>$p$</span>-Sylow subgroups are exactly maximal <span>$p$</span>-subgroups.

*Corollary of Sylow II:*\
Since <span>$G$</span> acts transitively on the Sylow subgroups, and the stabiliser of a Sylow subgroup <span>$P$</span> under this action is <span>$N_G(P)$</span>, we have 
<div>$$n_p =  |G/N_G(P)|$$</div>


# Sylow III

*Theorem: Sylow III*\
We have <span>$n_p \cong 1 \text{ mod } p$</span>[^fanciful]. Consequently <span>$p | u$</span>, where <span>$|G|=p^nu$</span> and <span>$p\not |u$</span>. 

Unlike the first two Sylow theorems, I only know essentially one way to prove the third Sylow theorem, which is to consider the conjugation action of a fixed Sylow subgroup on the set of Sylow subgroups. One then shows the following fact:

*Important lemma:*\
Let <span>$G$</span> be a finite group and <span>$\textrm{Syl}_p = \{ P_1,\ldots,P_m \}$</span> be the set of its Sylow subgroups. Then the orbits of <span>$\textrm{Syl}_p$</span> under the conjugation action by <span>$P_i$</span> are exactly <span>$\{P_i\}$</span> and a collection of orbits each of which has order divisible by <span>$p$</span>. Hence <span>$\textrm{Orb}_G(P_i)  \equiv  1 \text{ mod } p$</span>.

Notice for example that once one has the transitivity of the action of <span>$G$</span> on <span>$\textrm{Syl}_p$</span> (i.e. Sylow II), then Sylow III immediately follows. In essence, this is a 'decategorification' to the level of sets of the congrucence <span>$n_p \equiv 1 \text{ mod } p$</span>.

*First proof of important lemma*\
Evidently <span>$P \in \textrm{Syl}_p^P$</span>. On the other hand, suppose for a contradiction that <span>$P' \in \textrm{Syl}_p^P\setminus P$</span>. Pick <span>$g\in P\setminus P'$</span>. Then  <span>$g\in N_G(P') \setminus P'$</span>, so <span>$[g] \in N_G(P')/P'$</span> is non-trivial. But <span>$g$</span> has <span>$p$</span>-power order so <span>$p$</span> divides <span>$|N_G(P')/P'|$</span> which contradicts <span>$|P'|=p^n$</span>. Hence <span>$\textrm{Syl}_p^P=\{P\}$</span>.
Every other <span>$P$</span>-orbit of <span>$\textrm{Syl}_p$</span> is then non-trivial so must have order divisible by <span>$p$</span> by orbit-stabiliser[^same].

*Proof of Sylow III:* This immediately follows from Sylow II and the above lemma.

I lied; the following proof does not use the important lemma. However it is not particularly enlightening.

*Proof of Sylow III*:\
By the <span>$p$</span>-group fixed point lemma and the maximality of the <span>$p$</span>-power order of <span>$P$</span>, we have 
<div>$$ |N_G(P)/P| = |(G/P)^P| \cong |G/P| \not\cong 0\text{ mod } p$$</div>
Dividing (modulo <span>$p$</span>) by <span>$|N_G(P)/P|$</span> gives 
<div>$$|G/N_G(P)|\cong 1 \text{ mod } p$$</div>
and now we use our corollary (of Sylow II) <span>$n_p =  |G/N_G(P)|$</span>.

At the cost of a slightly irksome lemma, we can also prove our important lemma directly (without the help of Sylow II), from which we can extract another proof of Sylow II.

*Irksome lemma:*[^irksome]\
Let 
<div>$$K_{ij} = \textrm{Stab}_{P_i}(P_j) $$</div>
be the stabiliser of <span>$P_j$</span> under the <span>$P_i$</span>-conjugation action on <span>$\textrm{Syl}_p$</span>. Then 
<div>$$K_{ij} = P_i\cap P_j $$</div>

*Proof of irksome lemma:*\
Evidently <span>$K_{ij}\in P_i$</span> and <span>$P_i\cap P_j \subseteq K_{ij}$</span>, so we just need to show that <span>$K_{ij}\subseteq P_j$</span>. Recall that for two subgroups <span>$A$</span>,<span>$B$</span> the subset <span>$AB$</span> is a subgroup iff <span>$AB=BA$</span>. But by construction <span>$P_jK_{ij} = K_{ij}P_j$</span> so <span>$P_j K_{ij}$</span> is a subgroup. Evidently <span>$P_j$</span> is normal in <span>$K_{ij}$</span>.
Now by the second isomorphism theorem[^second]
<div>$$ \frac{K_{ij}P_j}{P_j}\cong \frac{K_{ij}}{K_{ij}\cap P_j}$$</div>
so <span>$|K_{ij}P_j| = |P_j||K_{ij}||K_{ij}\cap P_j|$</span>. But every groups on the right hand side is a subgroup of a Sylow subgroup, so <span>$K_{ij}P_j$</span> has <span>$p$</span>-power order. But <span>$P_j \subseteq K_{ij}P_j$</span> and <span>$P_j$</span> has maximal <span>$p$</span>-power order so <span>$P_{ij} = K_{ij}P_j$</span> so <span>$K_{ij} \subseteq P_j$</span>.

*Alternative proof of important lemma:*\
By the irksome lemma, we have <span>$\textrm{Stab}_{P_i}(P_j) = P_i\cap P_j$</span>. Then by orbit-stabiliser, <span>$|\textrm{Orb}_{P_i}(P_i)| = 1$</span> and <span>$p$</span> divides <span>$|\textrm{Orb}_{P_i}(P_j)|$</span> for <span>$j\neq i$</span>.

*Proof of Sylow III:*\
It remains to show that the <span>$G$</span> acts transitively by conjugation on <span>$\textrm{Syl}_p$</span> (i.e. a weak version of our Sylow II). Suppose for a contradiction that <span>$P_i,P_j$</span> are not in the same orbit. We have 
<div>$$ \textrm{Orb}_G(P_i) \equiv 1 \text{ mod } p$$</div>
but considering <span>$ \textrm{Orb}_G(P_i) $</span> as a disjoint union of <span>$P_j$</span>-orbits we have 
<div>$$|\textrm{Orb}_G(P_i)| \equiv 0 \text{ mod }p $$</div>
since <span>$\{P_j\}$</span> is *not* one of these orbits (by assumption). This is a contradiction.

# Parting thoughts
It would be interesting to try to extend the orbit-decomposition argument that we used to prove Sylow III to cover other <span>$p$</span>-subgroups, in the same way that Sylow I and Sylow II have statements which cover <span>$p$</span>-subgroups of arbitrary order.


# Sources/further reading
 - The final proofs of Sylow II and III are taken from M.A Armstrong's textbook "Groups and Symmetry"
 - The last proof of Sylow I and the first proofs of Sylow II and III are taken from the blog [Annoying Precision](https://qchu.wordpress.com/2020/11/01/meditation-on-the-sylow-theorems-i/), which contains several more proofs of the Sylow theorems and some interesting historical comments
 - The first proof of Sylow I is from the Wikipedia article on the Sylow theorems.

--- 

[^trivial]: In fact, in the paradigm case of Sylow I, namely subgroups of order <span>$p^n$</span>, this bound is trivial, so the proof simplifies significantly. 

[^abelian]: Or just by the Abelian case

[^nice]: It would be really nice to know a version of this proof which does not rely on the classification.

[^haha]: haha!

[^funny]: This is one of those funny arguments where you actually use the base case as part of the inductive step.

[^different]: People usually state this part of the Sylow theorems a bit differently: that <span>$n_p$</span> divides <span>$u$</span>, where <span>$|G|=p^nu$</span> and <span>$p\not |u$</span>. This stronger fact is really a consequence of Sylow III, and I find that tying the theorem statement and proof together as closely as possible helps me to remember both.

[^isomorphism]: That is, for <span>$p$</span>-Sylow subgroups <span>$P,Q$</span> there is an automorphism of <span>$G$</span> which takes <span>$P$</span> to <span>$Q$</span>.

[^irksome]: Perhaps I am too unkind to the lemma; its statement is perfectly pleasant and it is a good fact to know. However, the proof leaves something to be desired.

[^same]: You will sometimes see versions of this argument which invoke the <span>$p$</span>-group fixed-point lemma, but they're really the same argument.

[^second]: On the face of it, we are not invoking the second isomorphism as it is usually stated here: usually we have a group <span>$G$</span>, a subgroup <span>$H$</span> and a subgroup <span>$N$</span> which we *know* is normal. Then the theorem *concludes* that <span>$NH$</span> is a subgroup and that <span>$N$</span> is normal in <span>$NH$</span>. Here we instead strengthen the assumptions to include that <span>$NH$</span> is a group and <span>$N$</span> is normal in <span>$NH$</span> and get the same result (by the same argument). Alternatively, we can in fact get our result by an application of the second isomorphism theorem as typically stated so long as we choose <span>$N_G(P)$</span> as our "ambient" group. 

[^fanciful]: Fancifully, we might say that Sylow subgroups are "unique mod <span>$p$</span>", or that the prime <span>$p$</span> "thinks there is a unique Sylow subgroup".