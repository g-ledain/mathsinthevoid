---
layout: post
title:  "Nilpotent and solvable groups"
date:   2024-08-20 00:00:00 +0100
categories: 
---

Nilpotent and solvable groups are very important concepts but for some reason the basic definitions and results always give me a little more trouble than they should[^lie]. Here I record the fundamentals.

# Series
*Definition: Commutator*
Let <span>$G$</span> be a group and <span>$g,h \in G$</span>. Then the commutator of <span>$g,h$</span> is
<div>$$[g,h] = ghg^{-1}h^{-1} $$</div>
If <span>$A,B\subseteq G$</span>, then we define 
<div>$$[A,B] =\{aba^{-1}b^{-1}: a\in A.b\in B\}$$</div>
Note that if <span>$A,B$</span> are subgroups of <span>$G$</span>, then so is <span>$[A.B]$</span>.

*Definition: Central series*\
Let <span>$G$</span> be a group. A central series for <span>$G$</span> is a sequence of subgroups[^sloppy]
<div>$$\{1\} = A_0 \subseteq A_1 \subseteq A_2 \subseteq \ldots \subseteq A_n = G $$</div> 
such that either of following equivalent conditions hold
 - (i) Each <span>$A_i$</span> is normal[^normal] in <span>$G$</span> and 
 <div>$$A_i/A_{i-1} \subseteq Z(G/A_{i-1}) $$</div>
 - (ii) We have <span>$[G,A_i] \subseteq A_{i-1}$</span>

Cases (i) and (ii) give rise to two different "limiting cases" for central series where we insist that the inclusions are equalities.

*Definition: Upper central series*\
The upper central series (UCS) of a group <span>$G$</span> is the *ascecnding* sequence of subgroups 
<div>$$1= C^0 \subseteq C^1 \subseteq C^2 \subseteq \ldots$$</div>
defined by <span>$C^0=\{1\}$</span> and
<div>$$C^{i+1}/C^i = Z(G/C^i) $$</div>

*Definition: Lower central series*\
The lower central series (LCS) of a group <span>$G$</span> is a *descending* sequence of subgroups 
<div>$$G = C_0 \supseteq C_1 \supseteq C_2 \supseteq \ldots $$</div>
defined by <span>$C_0=G$</span> and
<div>$$C_{i+1} = [G,C_i]$$</div>

Note that in our definition of central series we required that the series start at <span>$\{1\}$</span> and end at <span>$G$</span>, so the upper and lower central series *need not be central series*[^nice]. Nontheless, they are very important.

The upper and lower central series are both extremal among all central series in dual ways. 

*Lemma:*\
The upper central series is the *fastest growing* central series and the lower central series is the *fastest descending* central series.[^technicality]
More precisely, let <span>$G$</span> be a group and suppose that 
<div>$$1= A_0 \subseteq A_1 \subseteq A_2 \subseteq \ldots$$</div>
are normal subgroups of <span>$G$</span> verifying either of conditions (i), (ii) above. Then we have 
<div>$$A_i \subseteq C^i $$</div>
for all integers <span>$i$</span>.\
Dually, suppose that 
<div>$$G = A_0 \supseteq A_1 \supseteq A_2 \supseteq \ldots $$</div>
are normal subgroups of <span>$G$</span> verifying either of conditions (i), (ii) above. Then we have 
<div>$$C_i\subseteq A_i $$</div>
for all integers <span>$i$</span>.\
In particular, we have <span>$C_i \subseteq C^i$</span>.

There is another important series which is called the "derived series".

*Definition: Derived series*\
Let <span>$G$</span> be a group. Its derived series is the descending sequence of subgroups
<div>$$G=D_0\subseteq D_1\subseteq D_2\subseteq \ldots $$</div>
Defined by <span>$D_0=G$</span> and 
<div>$$D_{i+1} = [D_i,D_i] $$</div>

# Exact sequences

The language of extensions of groups always escapes me so I'm going to write down the definitions here more for my own benefit than anyone else's.

*Definition: Extension of a group by a group*\
We say that a group <span>$G$</span> is an extension *of* a group <span>$H$</span> *by* a normal subgroup <span>$N$</span> of <span>$G$</span> if there is a short exact sequence
<div>$$1 \to N \to G \to H \to 1 $$</div>

If <span>$N$</span> is central in <span>$G$</span>, we say that <span>$G$</span> is a "central extension" of <span>$H$</span>. 

# Nilpotence and solvability[^soluble]
Most of the definitions and proofs from now on will come in two different flavours: one in the language of central/derived series and one in the language of exact sequences/composition series. It's good to be conversant in both flavours.

*Definition: Nilpotent group*\
A group <span>$G$</span> is said to be nilpotent if any of the following equivalent conditions hold:
 - (i) <span>$G$</span> has a central series
 - (ii) The upper central series of <span>$G$</span> ends in <span>$G$</span>
 - (iii) The lower central series of <span>$G$</span> ends in <span>$\{1\}$</span> 
 - (iv) <span>$G$</span> has a sequence of normal subgroups
 <div>$$\{1\} = A_0 \subseteq A_1 \subseteq \ldots \subseteq A_n = G $$</div> 
such that <span>$A_i/A_{i-1} \subseteq Z(G/A_{i-1}) $</span>
 - (v) <span>$G$</span> is an iterated central extension of <span>$\{1\}$</span>. Tht is, there is a sequence of short exact sequences
  <div>$$1 \to \zeta_i \to G_{i+1} \to G_i \to 1 $$</div>
  with <span>$\zeta_i \subseteq Z(G_{i+1})$</span>, <span>$\zeta_0 = \{1\}$</span> and <span>$G_n = G$</span>

*Definition: Solvable group*\
A group <span>$G$</span> is said to be solvable if any of the following equivalent conditions hold:
 - (i) The derived series of <span>$G$</span> terminates in <span>$\{1\}$</span>
 - (ii) <span>$G$</span> has a sequence of subgroups 
 <div>$$\{1\} = A_0 \subseteq A_1 \subseteq \ldots\subseteq A_n = G  $$</div>
 such that <span>$A_{i+1}/A_i$</span> is Abelian for all <span>$i$</span>.
 - (iii) The composition factors of <span>$G$</span> are all Abelian
 - (iv) <span>$G$</span> is an iterated extension of <span>$\{1\}$</span> by Abelian groups. More precisely, there exists a sequence of short exact sequences
 <div>$$1 \to G_{i-1} \to G_{i} \to H_i \to 1 $$</div>
 where <span>$G_0 =\{1\}$</span>, <span>$G_n=G$</span> and the <span>$H_i$</span> are all Abelian 

*Proof of equivalence (nilpotent):*\
<span>$(ii) \Rightarrow (i)$</span>, <span>$(iii)\Rightarrow(i)$</span> are immediate and <span>$(i) \Leftrightarrow (iv)$</span> is just by definition of central series. <span>$(i)\Rightarrow (ii)$</span> and <span>$(i)\Rightarrow (iii)$</span> follow from the extremality of the upper and lower central series. So we just need to show <span>$(iv) \Leftrightarrow (v)$</span>. But denoting the quotient maps in (v) by
<div>$$\pi_{i}: G_i \to G_{i-1} $$</div>
we have an equivalence given by
<div>$$G_i = G/A_{n-i} $$</div>
<div>$$\zeta_i = A_{n-i+1}/A_{n-i} $$</div>
and
<div>$$A_i = \pi_{n} \circ \ldots \circ \pi_{n-i+1}(\zeta_i) $$</div>

*Proof of equivalence (solvable):*\
<span>$(ii)\Leftrightarrow (iii)$</span> is an easy exercise in composition series and <span>$(ii)\Leftrightarrow (iv)$</span> is immediate. To see <span>$(i) \Rightarrow (ii)$</span>, note that the derived series has Abelian quotients[^abelianisation]. To see <span>$(ii) \Rightarrow (i)$</span>, suppose <span>$\{1\} = A_0 \subseteq A_1 \subseteq \ldots\subseteq A_n = G$</span> is a sequence as in <span>$(ii)$</span> and note that <span>$A_i \subseteq D_i$</span>. Since <span>$\{D_i\}_{1 \leq i \leq n}$</span> terminates in <span>$\{1\}$</span>, so does <span>$\{A_i\}_{1 \leq i \leq n}$</span>.

Both solvable and nilpotent groups come with a notion of how complicatedly nilpotent or solvable they are. 

*Definition: Derived length*\
Let <span>$G$</span> be a solvable group. Its derived length is the length of its derived series. 

Alternatively, we can give an inductive definition: The group <span>$\{1\}$</span> has derived length zero and a group <span>$G$</span> has derived length <span>$n\geq 1$</span> if it is a extension of an Abelian group by a group of derived length <span>$n-1$</span> and it is not itself a group of derived length <span>$n-1$</span>.

*Definition: Nilpotency class*\
The nilpotency class of a nilpotent group <span>$G$</span> is the length of its shortest central series. 

Again, we can give an inductive definition: The group <span>$\{1\}$</span> has nilpotency class zero and a group <span>$G$</span> has nilpotency class <span>$n\geq 1$</span> if it is a central extension of a group of nilpotency class <span>$n-1$</span> and is not itself a group of milpotency class <span>$n-1$</span>.

*Lemma:*\
Let <span>$G$</span> be a nilpotent group. Then its nilpotency class is the length of both its upper central series and its lower central series.

*Proof:*\
With a bit of careful thought about indexing, this results from the respective extremality properties of the upper and lower central series.

The relationship between nilpotent and solvable groups is a subtle affair which took me a while to become comfortable with[^quote]. In some ways they are dual to one another: solvable groups are iterated extensions of <span>$\{1\}$</span> *by* Abelian groups, whereas nilpotent groups are iterated *central* extensions of <span>$\{1\}$</span>, meaning that the "commutativity" is the in the group you're extending *by*. On the other hand, they both have characterisations by series and in terms of short exact sequences. Strangely, nilpotent groups have both ascending and descending versions of their defining series, but solvable groups only seem to have an ascending version. Despite their apparent duality, nilpotence is actually a special case of solvability.

*Lemma: Nilpotent implies solvable*\
Suppose that <span>$G$</span> is a nilpotent group. Then <span>$G$</span> is solvable.

*Proof:*\
(By series): Note that the derived series is contained at each stage in the lower central series. But the lower central series terminates in <span>$\{1\}$</span>, hence so does the derived series.\
(By quotients): By definition of the composition factors of <span>$G$</span> are Abelian.

*Lemma: Subgroups and quotients of nilpotent and solvable groups*\
Let <span>$H \subseteq G$</span>.
 - (i) If <span>$G$</span> is solvable, then so is <span>$H$</span>
 - (ii) If <span>$G$</span> is nilpotent, then so is <span>$H$</span>
 - (iii) If <span>$H$</span> is normal and <span>$G$</span> is solvable, then so is <span>$G/H$</span>
 - (iv) If <span>$H$</span> is normal and <span>$G$</span> is nilpotent, then so is <span>$G/H$</span>
 - (v) If <span>$H$</span> is normal and <span>$H$</span>, <span>$G/H$</span> are both solvable, then so is <span>$G$</span> 

*Proof:*\
All of the above can be proven using series or composition factors. (i), (ii), (iii), (iv) are more or less immediate using the characterisation using series, whereas (v) can be deduced from the lovely fact that given a composition series of <span>$H$</span> and <span>$G/H$</span>, we can construct a composition series of <span>$G$</span> whose composition factors are exactly those of <span>$H$</span> followed by those of <span>$G/H$</span>.

Note that it can be the case that <span>$H$</span> is normal and <span>$H$</span>, <span>$G/H$</span> are both nilpotent, but <span>$G$</span> is *not* nilpotent! Exercise: find an example. (Hint: use the fun fact below to help you find it).

# Fun fact
I recently discovered the following wonderful fact, and I think that no discussion of nilpotence would be complete without it.

*Theorem: Classification of finite nilpotent groups*\
A finite group is nilpotent exactly if it is a direct product of <span>$p$</span>-groups (in particular, a direct product of its Sylow subgroups).

*Proof*: I haven't studied a proof of this in any detail, but [this](https://dept.math.lsa.umich.edu/~speyer/594/B_594_W_22_worksheets.pdf) [^archived] seems like a fun guided exercise.

[^lie]: Actually, I was exposed to the definition of nilpotence and most of these propositions in the context of Lie algebras first, but I think it's nicer to learn about them in the context of groups. 

[^normal]: For practical purposes, if we are using definition (i) we need only verify that each <span>$A_i$</span> is normal in <span>$A_{i+1}$</span> since the centrality condition then *implies* that <span>$A_i$</span> is normal in <span>$G$</span>. However, for the purposes of stating the definition this would simply be an inductive headache.

[^sloppy]: We're going to be sloppy with the numbering: sometimes our central series will have <span>$A_i \subseteq A_{i+1}$</span> and sometimes they will have <span>$A_i \supseteq A_{i+1}$</span>

[^nice]: Maybe it would be nice to define "ascending", "descending" and "bounded" central series, but it doesn't seem that this is standard and I'm not feeling adventurous today

[^soluble]: Or should that be solubility? I'm never sure...

[^technicality]: Again note that the theorem statement actually applies to sequences of subgroups which don't start at <span>$\{1\}$</span> and end at <span>$G$</span>, so may not technically be central series as we have defined them.

[^archived]: [Archived](https://web.archive.org/web/20240105011905/https://dept.math.lsa.umich.edu/~speyer/594/B_594_W_22_worksheets.pdf)

[^quote]: I am reminded of the von Neumann quote: "In mathematics you don't understand things. You just get used to them."

[^abelianisation]: Because the Abelianisation <span>$G/[G,G]$</span> is Abelian!