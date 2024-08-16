---
layout: post
title:  "Sylow's theorems"
date:   2024-08-04 00:00:00 +0100
categories: 
---

I never remembered, let alone understood, the proofs of Sylow's theorems (even consistently stating the third one correctly gave me trouble). On the one hand, looking up several different proofs has let me pick and choose which ones I like the best. On the other hand, finding their commonalities has helped me identify the crucial parts of the arguments.

# Sylow I
Most of the proofs of Sylow I we present here will be souped-up versions of the arguments we used to prove Cauchy's theorem, with the exception of the final proof which iteratively uses Cauchy's theorem to construct subgroups of order $p,p^2,\ldots,p^n$.

We call a subgroup $P$ of $G$ of order $p$ a $p$-Sylow subgroup, or just a Sylow subgroup for short. Throughout, we will use $n_p$ to refer to the number of $p$-Sylow subgroups of $G$.

Throughout, we will be referring to the largest power of a prime $p$ which divides an integer $n$, and it will be helpful to fix some notation for this.

*Definition: $p$-adic valuation:*\
Fix a prime $p$. We write 
$$v_p: \mathbb{Z} \to \mathbb{Z}\cup \{\infty\} $$
$$v_p(x) = \begin{cases} \text{The largest power of } p \text{ which divides } n & \text{ if } n\neq 0 \\ \infty & \text{ if } n=0 \end{cases} $$
We call $v_p(n)$ the $p$-adic valuation of $n$.

Our first argument will be a counting argument using group actions. To glue things together, we will need a lemma to relate $p$-divisibility to counting.

*Lemma: Kummer's lemma*\
Let $0\leq k\leq n$ and $k \not | u$. Then $p^{n-k}$ is the largest power of $p$ dividing $\binom{p^nu}{p^k}$

*Proof:* Not now.

*Proof of Sylow I:*
Let 
$$X = \{S\subseteq G: |S|=p^k\} $$
where $G$ acts by left-multiplication. We have 
$$v_p(|X|)=\binom{p^nu}{p^k} $$
so 
$$v_p(|X|)= n-k=: r $$
For any $S\in X$ and $a\in S$, we ahve $G_S.a\subseteq S$, so
$$|G_S|=|G_S.a| \leq |S| = p^k $$
so $v_p(|G_S|)\leq k$ hence by orbit-stabiliser $v_p(|G.S|) \geq r$. We have 
$$|G| = \sum_{G-\text{ orbits } \mathcal{O} \text{ of } X} |\mathcal{O}|$$
If all the $G.S$ have $v_p(|G.S|)>r$, then we would have $v_p(|G|) > r$ which is a contradiction. So there exists $S \in X$ with $v_p(|G.S|)=r$, hence $v_p(G_S)=k$. But $|G_S|\leq p^k$, so $|G_S|=p^k$, whence $G_S$ is the desired subgroup.

As in most proofs using group actions, the most important part is the careful choice of a set and an action of $G$ on that set. Why did we choose this particular set and this particular action? We needed to magic up a subgroup of the right order out of thin air, so we may as well start with something we always have in abundance: subsets. As for the action, note that it is easiest to characterise subgroups via the left-multiplication action (rather than, say, the conjugation action): a subset $S\subseteq G$ is a subgroup exactly when $S=G_S$. In fact, in the proof we used that for any $S\subseteq G$ and $a\in S$ we have $G_S.a\in S$, which is lkind of like a half-measure which applies to mere subsets.

After an appropriate set and action were chosen, the key ideas of the proof was the calculation of the $p$-adic valuation of $|X|$ via Kummer's lemma, getting a lower bound[^trivial] on the $p$-adic valuation of the orbits, and then comparing 'leading terms'. 

*Another proof of Sylow I:*\
By induction on $|G|$.

**Case $G$ is Abelian:**
By the classification of finite Abelian groups[^nice], $G$ is a product of prime-power-order cyclic groups. Let the '$p$-part' of the decomposition be isomorphic to 
$$\prod_{i=1}^N \mathbb{Z}/p^{t_i}\mathbb{Z} $$
for some $t_i\in \mathbb{N}$, so $\sum_{i=1}^N t_i = n $ and let $g_i$ generate the copy of $\mathbb{Z}/p^{t_i}\mathbb{Z}$. For any $0\leq k\leq n$, we can write 
$$k=\sum_{i=1}^N t_i' $$
for some $0\leq t_i'\leq t_i$ and then 
$$\langle g_i^{t_1-t_1'},\ldots, g_i^{t_N-t_N'} \rangle \subseteq G$$
has order $p^k$.

**Case $G$ is non-Abelian:**
If $p$ divides $|Z(G)|$, then write $|Z(G)|=p^ru'$ where $p\not | u'$. Since $G$ is non-Abelian we have $|Z(G)|<|G|$ and since $p$ divides $|Z(G)$ we have $|G/Z(G)|<|G|$. By the inductive hypothesis^[^abelian] there exists a subgroup $A\subseteq Z(G)$ of order $p^r$ and since 
$$k-r\leq n-r = v_p(|G/A?) $$
there exists by the inductive hypothesis a subgroup $\tilde{P} = P/A \subseteq G/A$ of order $p^{k-r}$.
Now 
$$|P| = |\tilde{P}||A| = p^{k-r}p^r = p^k $$
so $P$ is our desired subgroup. 

If $p$ does not divide $|Z(G)|$, then by the class equation there exists $g\in G\setminus Z(G)$ such that $p$ does not divide $|G|/|C_G(g)|$, so $v_p(|C_G(g)) = v_p(|G|)$. Since $g\not\in Z(G)$ we have $C_G(g) \neq G$ and by the inductive hypothesis $C_G(g)$ contains subgroups of the desired order.

We are again using the duality between substructures and quotient structures throughout this argument: both in the guise of the subgroup $A$ versus the quotient $G/A$, but also at the level of $G$-sets in the form of the orbit-union $Z(G)$ (which is a $G$-subset) versus the stabiliser $C_G(g)$ (insofar as a stabiliser is a sort of $G$-set kernel and hence controls a quotient). Once again, the minor miracle that the union of *orbits* $Z(G)$ forms a subgroup (rather than just a subset) is of central[^haha] importance in the argument.

*Another another proof of Sylow I:*\
By induction on $k$.\
The case $k=1$ is Cauchy's theorem. Suppose there exists a subgroup $P$ of order $p^{k-1}$. Note that 
$$N_G(P)/P \subseteq G/P $$
is the fixed points of the left-multiplication action of $P$ on $G/P$, that is:
$$N_G(P)/P = (G/P)^P $$
Since $p^n$ divides $|G|$ and $n>k-1$, we have
$$|G/P| \cong 0 \text{ mod } p $$
and by the $p$-group fixed-point lemma we have 
$$ |N_G(P)/P| = |G/P| \cong 0 \text{ mod } p$$
By Cauchy's theorem[^funny], there exists $g\in N_G(P)$ such that $[g]\in N_G(P)/P$ has order $p$. Let
$$\pi: N_G(P) \twoheadrightarrow P $$ 
be the quotient map and let
$$P'= \pi^{-1}(\langle [g]\rangle) = \langle g,P\rangle $$
Then
$$|P'|=|P||\langle[g]\rangle|=p^{k-1}p = p^k $$
which completes the induction.

A crude attempt at this argument would be to use Cauchy to get a subgroup $P_1$ of order $p$, then apply Cauchy to $G/P$ and take the pre-image to get a subgroup $P_2$ of order $p^2$ and so on. The issue is that $P_1,P_2,\ldots$ may not be normal. The normaliser provides the technical fix which makes the argument work; $N_G(P)$ is by definition the largest subgroup of $G$ in which $P$ is normal.

The above proof actually shows something stronger than the above theorem statement - namely that every subgroup of $G$ of order $p^k$ (with $k<n$) is contained in a subgroup of order $p^{k+1}$. Consequently, the subgroups of order $p^n$ are exactly those $p$-subgroups which are maximal with respect to inclusion.

# Sylow II and III
The second and third Sylow theorems are closely related to one another, closer than either is to the first. They both pertain to how $G$ and its subgroups act on Sylow subgroups by conjugation. Usually, one uses one to help prove the other, and we will see both directions.

# Sylow II
*Theorem: Sylow II:*\
Let $G$ be a finite group and $P$ a $p$-Sylow subgroup. For any $p$-subgroup $Q\subseteq G$, there exists $g\in G$ with
$$gQg^{-1} \subseteq P $$
In particular, Sylow subgroups are unique up to conjugation - equivalently, $G$ acts transitively on the $p$-Sylows by conjugation.

*Corollary:* By orbit-stabiliser,  $n_p$ divides $|G|$[^different].

It's worth thinking philosophically about Sylow II a little bit: Sylow I is a very straightforward existence theorem about $p$-subgroups of $G$, and in particular $p$-Sylow subgroups. We therefore might want a uniqueness theorem for $p$-Sylow subgroups. The most naive uniqueness theorem - that Sylow subgroups are unique 'up to equality' is as false as you can get - basically any group you care to think of provides a counterexample. Slightly better might be that Sylow subgroups are unique up to isomorphism. Even better would be that they are unique up to isomorphism *as subgroups*[^isomorphism]. Even better than this would be for this to isomorphism to come from within $G$ itself - for it to be a conjugation. This is exactly what the above theorem says. So Sylow II affirms the most optimistic uniqueness statement for Sylow subgroups we could realistically hope for. There is mercy in the world after all!

*Proof of Sylow II:*
Consider the left-multiplication action of $Q$ on $G/P$. By the $p$-group fixed point lemma, we have 
$$|(G/P)^Q|\cong |G/P| \not\cong 0 \text{ mod }p $$
so there exists $g\in (G/P)^Q$. Then $g^{-1}Qg\subseteq P$.

Note that this proof *doesn't* use the conjugation action, despite its statement being about conjugation. Huh. I have nothing insightful to say about this. This proof also yields another proof that the $p$-Sylow subgroups are exactly maximal $p$-subgroups.

*Corollary of Sylow II:*\
Since $G$ acts transitively on the Sylow subgroups, and the stabiliser of a Sylow subgroup $P$ under this action is $N_G(P)$, we have 
$$n_p =  |G/N_G(P)|$$


# Sylow III

*Theorem: Sylow III*\
We have $n_p \cong 1 \text{ mod } p$[^fanciful]. Consequently $p | u$, where $|G|=p^nu$ and $p\not |u$. 

Unlike the first two Sylow theorems, I only know essentially one way to prove the third Sylow theorem, which is to consider the conjugation action of a fixed Sylow subgroup on the set of Sylow subgroups. One then shows the following fact:

*Important lemma:*\
Let $G$ be a finite group and $\textrm{Syl}_p = \{ P_1,\ldots,P_m \}$ be the set of its Sylow subgroups. Then the orbits of $\textrm{Syl}_p$ under the conjugation action by $P_i$ are exactly $\{P_i\}$ and a collection of orbits each of which has order divisible by $p$. Hence $\textrm{Orb}_G(P_i)  \equiv  1 \text{ mod } p$.

Notice for example that once one has the transitivity of the action of $G$ on $\textrm{Syl}_p$ (i.e. Sylow II), then Sylow III immediately follows. In essence, this is a 'decategorification' to the level of sets of the congrucence $n_p \equiv 1 \text{ mod } p$.

*First proof of important lemma*\
Evidently $P \in \textrm{Syl}_p^P$. On the other hand, suppose for a contradiction that $P' \in \textrm{Syl}_p^P\setminus P$. Pick $g\in P\setminus P'$. Then  $g\in N_G(P') \setminus P'$, so $[g] \in N_G(P')/P'$ is non-trivial. But $g$ has $p$-power order so $p$ divides $|N_G(P')/P'|$ which contradicts $|P'|=p^n$. Hence $\textrm{Syl}_p^P=\{P\}$.
Every other $P$-orbit of $\textrm{Syl}_p$ is then non-trivial so must have order divisible by $p$ by orbit-stabiliser[^same].

*Proof of Sylow III:* This immediately follows from Sylow II and the above lemma.

I lied; the following proof does not use the important lemma. However it is not particularly enlightening.

*Proof of Sylow III*:\
By the $p$-group fixed point lemma and the maximality of the $p$-power order of $P$, we have 
$$ |N_G(P)/P| = |(G/P)^P| \cong |G/P| \not\cong 0\text{ mod } p$$
Dividing (modulo $p$) by $|N_G(P)/P|$ gives 
$$|G/N_G(P)|\cong 1 \text{ mod } p$$
and now we use our corollary (of Sylow II) $n_p =  |G/N_G(P)|$.

At the cost of a slightly irksome lemma, we can also prove our important lemma directly (without the help of Sylow II), from which we can extract another proof of Sylow II.

*Irksome lemma:*[^irksome]\
Let 
$$K_{ij} = \textrm{Stab}_{P_i}(P_j) $$
be the stabiliser of $P_j$ under the $P_i$-conjugation action on $\textrm{Syl}_p$. Then 
$$K_{ij} = P_i\cap P_j $$

*Proof of irksome lemma:*\
Evidently $K_{ij}\in P_i$ and $P_i\cap P_j \subseteq K_{ij}$, so we just need to show that $K_{ij}\subseteq P_j$. Recall that for two subgroups $A$,$B$ the subset $AB$ is a subgroup iff $AB=BA$. But by construction $P_jK_{ij} = K_{ij}P_j$ so $P_j K_{ij}$ is a subgroup. Evidently $P_j$ is normal in $K_{ij}$.
Now by the second isomorphism theorem[^second]
$$ \frac{K_{ij}P_j}{P_j}\cong \frac{K_{ij}}{K_{ij}\cap P_j}$$
so $|K_{ij}P_j| = |P_j||K_{ij}||K_{ij}\cap P_j|$. But every groups on the right hand side is a subgroup of a Sylow subgroup, so $K_{ij}P_j$ has $p$-power order. But $P_j \subseteq K_{ij}P_j$ and $P_j$ has maximal $p$-power order so $P_{ij} = K_{ij}P_j$ so $K_{ij} \subseteq P_j$.

*Alternative proof of important lemma:*\
By the irksome lemma, we have $\textrm{Stab}_{P_i}(P_j) = P_i\cap P_j$. Then by orbit-stabiliser, $|\textrm{Orb}_{P_i}(P_i)| = 1$ and $p$ divides $|\textrm{Orb}_{P_i}(P_j)|$ for $j\neq i$.

*Proof of Sylow III:*\
It remains to show that the $G$ acts transitively by conjugation on $\textrm{Syl}_p$ (i.e. a weak version of our Sylow II). Suppose for a contradiction that $P_i,P_j$ are not in the same orbit. We have 
$$ \textrm{Orb}_G(P_i) \equiv 1 \text{ mod } p$$
but considering $ \textrm{Orb}_G(P_i) $ as a disjoint union of $P_j$-orbits we have 
$$|\textrm{Orb}_G(P_i)| \equiv 0 \text{ mod }p $$
since $\{P_j\}$ is *not* one of these orbits (by assumption). This is a contradiction.

# Parting thoughts
It would be interesting to try to extend the orbit-decomposition argument that we used to prove Sylow III to cover other $p$-subgroups, in the same way that Sylow I and Sylow II have statements which cover $p$-subgroups of arbitrary order.


# Sources/further reading
 - The final proofs of Sylow II and III are taken from <ARMSTRONG>
 - The last proof of Sylow I and the first proofs of Sylow II and III are taken from <Qchu>, which contains several more proofs of the Sylow theorems and some interesting historical comments
 - The first proof of Sylow I is from the Wikipedia article on the Sylow theorems.

[^trivial]: In fact, in the paradigm case of Sylow I, namely subgroups of order $p^n$, this bound is trivial, so the proof simplifies significantly. 

[^abelian]: Or just by the Abelian case

[^nice]: It would be really nice to know a version of this proof which does not rely on the classification.

[^haha]: haha!

[^funny]: This is one of those funny arguments where you actually use the base case as part of the inductive step.

[^different]: People usually state this part of the Sylow theorems a bit differently: that $n_p$ divides $u$, where $|G|=p^nu$ and $p\not |u$. This stronger fact is really a consequence of Sylow III, and I find that tying the theorem statement and proof together as closely as possible helps me to remember both.

[^isomorphism]: That is, for $p$-Sylow subgroups $P,Q$ there is an automorphism of $G$ which takes $P$ to $Q$.

[^irksome]: Perhaps I am too unkind to the lemma; its statement is perfectly pleasant and it is a good fact to know. However, the proof leaves something to be desired.

[^same]: You will sometimes see versions of this argument which invoke the $p$-group fixed-point lemma, but they're really the same argument.

[^second]: On the face of it, we are not invoking the second isomorphism as it is usually stated here: usually we have a group $G$, a subgroup $H$ and a subgroup $N$ which we *know* is normal. Then the theorem *concludes* that $NH$ is a subgroup and that $N$ is normal in $NH$. Here we instead strengthen the assumptions to include that $NH$ is a group and $N$ is normal in $NH$ and get the same result (by the same argument). Alternatively, we can in fact get our result by an application of the second isomorphism theorem as typically stated so long as we choose $N_G(P)$ as our "ambient" group. 

[^fanciful]: Fancifully, we might say that Sylow subgroups are "unique mod $p$", or that the prime $p$ "thinks there is a unique Sylow subgroup".