---
layout: post
title:  "Nilpotent and solvable groups"
date:   2024-08-20 00:00:00 +0100
categories: 
---

Nilpotent and solvable groups are very important concepts but for some reason the basic definitions and results always give me a little more trouble than they should[^lie]. Here I record the fundamentals.

# Series
*Definition: Commutator*
Let $G$ be a group and $g,h \in G$. Then the commutator of $g,h$ is
$$[g,h] = ghg^{-1}h^{-1} $$
If $A,B\subseteq G$, then we define 
$$[A,B] =\{aba^{-1}b^{-1}: a\in A.b\in B\}$$
Note that if $A,B$ are subgroups of $G$, then so is $[A.B]$.

*Definition: Central series*\
Let $G$ be a group. A central series for $G$ is a sequence of subgroups[^sloppy]
$$\{1\} = A_0 \subseteq A_1 \subseteq A_2 \subseteq \ldots \subseteq A_n = G $$ 
such that either of following equivalent conditions hold
 - (i) Each $A_i$ is normal[^normal] in $G$ and 
 $$A_i/A_{i-1} \subseteq Z(G/A_{i-1}) $$
 - (ii) We have $[G,A_i] \subseteq A_{i-1}$

Cases (i) and (ii) give rise to two different "limiting cases" for central series where we insist that the inclusions are equalities.

*Definition: Upper central series*\
The upper central series (UCS) of a group $G$ is the *ascecnding* sequence of subgroups 
$$1= C^0 \subseteq C^1 \subseteq C^2 \subseteq \ldots$$
defined by $C^0=\{1\}$ and
$$C^{i+1}/C^i = Z(G/C^i) $$

*Definition: Lower central series*\
The lower central series (LCS) of a group $G$ is a *descending* sequence of subgroups 
$$G = C_0 \supseteq C_1 \supseteq C_2 \supseteq \ldots $$
defined by $C_0=G$ and
$$C_{i+1} = [G,C_i]$$

Note that in our definition of central series we required that the series start at $\{1\}$ and end at $G$, so the upper and lower central series *need not be central series*[^nice]. Nontheless, they are very important.

The upper and lower central series are both extremal among all central series in dual ways. 

*Lemma:*\
The upper central series is the *fastest growing* central series and the lower central series is the *fastest descending* central series.[^technicality]
More precisely, let $G$ be a group and suppose that 
$$1= A_0 \subseteq A_1 \subseteq A_2 \subseteq \ldots$$
are normal subgroups of $G$ verifying either of conditions (i), (ii) above. Then we have 
$$A_i \subseteq C^i $$
for all integers $i$.\
Dually, suppose that 
$$G = A_0 \supseteq A_1 \supseteq A_2 \supseteq \ldots $$
are normal subgroups of $G$ verifying either of conditions (i), (ii) above. Then we have 
$$C_i\subseteq A_i $$
for all integers $i$.\
In particular, we have $C_i \subseteq C^i$.

There is another important series which is called the "derived series".

*Definition: Derived series*\
Let $G$ be a group. Its derived series is the descending sequence of subgroups
$$G=D_0\subseteq D_1\subseteq D_2\subseteq \ldots $$
Defined by $D_0=G$ and 
$$D_{i+1} = [D_i,D_i] $$

# Exact sequences

The language of extensions of groups always escapes me so I'm going to write down the definitions here more for my own benefit than anyone else's.

*Definition: Extension of a group by a group*\
We say that a group $G$ is an extension *of* a group $H$ *by* a normal subgroup $N$ of $G$ if there is a short exact sequence
$$1 \to N \to G \to H \to 1 $$

If $N$ is central in $G$, we say that $G$ is a "central extension" of $H$. 

# Nilpotence and solvability[^soluble]
Most of the definitions and proofs from now on will come in two different flavours: one in the language of central/derived series and one in the language of exact sequences/composition series. It's good to be conversant in both flavours.

*Definition: Nilpotent group*\
A group $G$ is said to be nilpotent if any of the following equivalent conditions hold:
 - (i) $G$ has a central series
 - (ii) The upper central series of $G$ ends in $G$
 - (iii) The lower central series of $G$ ends in $\{1\}$ 
 - (iv) $G$ has a sequence of normal subgroups
 $$\{1\} = A_0 \subseteq A_1 \subseteq \ldots \subseteq A_n = G $$ 
such that $A_i/A_{i-1} \subseteq Z(G/A_{i-1}) $
 - (v) $G$ is an iterated central extension of $\{1\}$. Tht is, there is a sequence of short exact sequences
  $$1 \to \zeta_i \to G_{i+1} \to G_i \to 1 $$
  with $\zeta_i \subseteq Z(G_{i+1})$, $\zeta_0 = \{1\}$ and $G_n = G$

*Definition: Solvable group*\
A group $G$ is said to be solvable if any of the following equivalent conditions hold:
 - (i) The derived series of $G$ terminates in $\{1\}$
 - (ii) $G$ has a sequence of subgroups 
 $$\{1\} = A_0 \subseteq A_1 \subseteq \ldots\subseteq A_n = G  $$
 such that $A_{i+1}/A_i$ is Abelian for all $i$.
 - (iii) The composition factors of $G$ are all Abelian
 - (iv) $G$ is an iterated extension of $\{1\}$ by Abelian groups. More precisely, there exists a sequence of short exact sequences
 $$1 \to G_{i-1} \to G_{i} \to H_i \to 1 $$
 where $G_0 =\{1\}$, $G_n=G$ and the $H_i$ are all Abelian 

*Proof of equivalence (nilpotent):*\
$(ii) \Rightarrow (i)$, $(iii)\Rightarrow(i)$ are immediate and $(i) \Leftrightarrow (iv)$ is just by definition of central series. $(i)\Rightarrow (ii)$ and $(i)\Rightarrow (iii)$ follow from the extremality of the upper and lower central series. So we just need to show $(iv) \Leftrightarrow (v)$. But denoting the quotient maps in (v) by
$$\pi_{i}: G_i \to G_{i-1} $$
we have an equivalence given by
$$G_i = G/A_{n-i} $$
$$\zeta_i = A_{n-i+1}/A_{n-i} $$
and
$$A_i = \pi_{n} \circ \ldots \circ \pi_{n-i+1}(\zeta_i) $$

*Proof of equivalence (solvable):*\
$(ii)\Leftrightarrow (iii)$ is an easy exercise in composition series and $(ii)\Leftrightarrow (iv)$ is immediate. To see $(i) \Rightarrow (ii)$, note that the derived series has Abelian quotients[^abelianisation]. To see $(ii) \Rightarrow (i)$, suppose $\{1\} = A_0 \subseteq A_1 \subseteq \ldots\subseteq A_n = G$ is a sequence as in $(ii)$ and note that $A_i \subseteq D_i$. Since $\{D_i\}_{1 \leq i \leq n}$ terminates in $\{1\}$, so does $\{A_i\}_{1 \leq i \leq n}$.

Both solvable and nilpotent groups come with a notion of how complicatedly nilpotent or solvable they are. 

*Definition: Derived length*\
Let $G$ be a solvable group. Its derived length is the length of its derived series. 

Alternatively, we can give an inductive definition: The group $\{1\}$ has derived length zero and a group $G$ has derived length $n\geq 1$ if it is a extension of an Abelian group by a group of derived length $n-1$ and it is not itself a group of derived length $n-1$.

*Definition: Nilpotency class*\
The nilpotency class of a nilpotent group $G$ is the length of its shortest central series. 

Again, we can give an inductive definition: The group $\{1\}$ has nilpotency class zero and a group $G$ has nilpotency class $n\geq 1$ if it is a central extension of a group of nilpotency class $n-1$ and is not itself a group of milpotency class $n-1$.

*Lemma:*\
Let $G$ be a nilpotent group. Then its nilpotency class is the length of both its upper central series and its lower central series.

*Proof:*\
With a bit of careful thought about indexing, this results from the respective extremality properties of the upper and lower central series.

The relationship between nilpotent and solvable groups is a subtle affair which took me a while to become comfortable with[^quote]. In some ways they are dual to one another: solvable groups are iterated extensions of $\{1\}$ *by* Abelian groups, whereas nilpotent groups are iterated *central* extensions of $\{1\}$, meaning that the "commutativity" is the in the group you're extending *by*. On the other hand, they both have characterisations by series and in terms of short exact sequences. Strangely, nilpotent groups have both ascending and descending versions of their defining series, but solvable groups only seem to have an ascending version. Despite their apparent duality, nilpotence is actually a special case of solvability.

*Lemma: Nilpotent implies solvable*\
Suppose that $G$ is a nilpotent group. Then $G$ is solvable.

*Proof:*\
(By series): Note that the derived series is contained at each stage in the lower central series. But the lower central series terminates in $\{1\}$, hence so does the derived series.\
(By quotients): By definition of the composition factors of $G$ are Abelian.

*Lemma: Subgroups and quotients of nilpotent and solvable groups*\
Let $H \subseteq G$.
 - (i) If $G$ is solvable, then so is $H$
 - (ii) If $G$ is nilpotent, then so is $H$
 - (iii) If $H$ is normal and $G$ is solvable, then so is $G/H$
 - (iv) If $H$ is normal and $G$ is nilpotent, then so is $G/H$
 - (v) If $H$ is normal and $H$, $G/H$ are both solvable, then so is $G$ 

*Proof:*\
All of the above can be proven using series or composition factors. (i), (ii), (iii), (iv) are more or less immediate using the characterisation using series, whereas (v) can be deduced from the lovely fact that given a composition series of $H$ and $G/H$, we can construct a composition series of $G$ whose composition factors are exactly those of $H$ followed by those of $G/H$.

Note that it can be the case that $H$ is normal and $H$, $G/H$ are both nilpotent, but $G$ is *not* nilpotent! Exercise: find an example. (Hint: use the fun fact below to help you find it).

# Fun fact
I recently discovered the following wonderful fact, and I think that no discussion of nilpotence would be complete without it.

*Theorem: Classification of finite nilpotent groups*\
A finite group is nilpotent exactly if it is a direct product of $p$-groups (in particular, a direct product of its Sylow subgroups).

*Proof*: I haven't studied a proof of this in any detail, but [this](https://dept.math.lsa.umich.edu/~speyer/594/B_594_W_22_worksheets.pdf) [^archived] seems like a fun guided exercise.

[^lie]: Actually, I was exposed to the definition of nilpotence and most of these propositions in the context of Lie algebras first, but I think it's nicer to learn about them in the context of groups. 

[^normal]: For practical purposes, if we are using definition (i) we need only verify that each $A_i$ is normal in $A_{i+1}$ since the centrality condition then *implies* that $A_i$ is normal in $G$. However, for the purposes of stating the definition this would simply be an inductive headache.

[^sloppy]: We're going to be sloppy with the numbering: sometimes our central series will have $A_i \subseteq A_{i+1}$ and sometimes they will have $A_i \supseteq A_{i+1}$

[^nice]: Maybe it would be nice to define "ascending", "descending" and "bounded" central series, but it doesn't seem that this is standard and I'm not feeling adventurous today

[^soluble]: Or should that be solubility? I'm never sure...

[^technicality]: Again note that the theorem statement actually applies to sequences of subgroups which don't start at $\{1\}$ and end at $G$, so may not technically be central series as we have defined them.

[^archived]: [Archived](https://web.archive.org/web/20240105011905/https://dept.math.lsa.umich.edu/~speyer/594/B_594_W_22_worksheets.pdf)

[^quote]: I am reminded of the von Neumann quote: "In mathematics you don't understand things. You just get used to them."

[^abelianisation]: Because the Abelianisation $G/[G,G]$ is Abelian!