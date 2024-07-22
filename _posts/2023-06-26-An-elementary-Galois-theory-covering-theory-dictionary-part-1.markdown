---
layout: post
title:  "An elementary Galois theory-covering theory dictionary (part 1)"
date:   2023-06-26 00:00:00 +0100
categories: 
---
There is a deep analogy between Galois theory and the theory of covering spaces. Understanding and making formal the details of this analogy requires the sophisticated language and machinery of scheme theory. However, it is possible to state the basic ideas of the analogy in an entirely elementary fashion, needing no knowledge beyond a first course in Galois theory and a first course on the fundamental group. This is what I want to do here.

(Note: throughout we will be assuming that our topological spaces are nice enough that we can apply the Galois correspondence for covering spaces. Specifically, they need to be path-connected, locally path-connected and semi-locally simply connected. You can consider topological manifolds or CW-complexes instead if you wish.)

# A table of correspondences

| Field extension                             | Local homeomorphism                      |
|---------------------------------------------|------------------------------------------|
| Separable field extension                   | Covering space                           |
| Degree of an extension                      | Degree of a cover                        |
| Galois field extension                      | Regular cover                            |
| Map of field extensions                     | Covering transformation                  |
| Galois group                                | Group of deck transformations            |
| Separable closure                           | Universal cover                          |
| Absolute Galois group                       | Fundamental group                        |
| Choice of embedding into a Galois extension | Choice of inverse image of the basepoint |

The analogy results from two basic ideas: covering spaces are analogous to separable field extensions. Now chant the mantra "reverse all the morphisms": take all the maps involved in the field theoretic results and reverse them to get the topological results (and vice versa).

The reversing of the arrows makes this correspondence 'contravariant'. For instance, in Galois theory we fix a field <span>$K$</span> and consider maps out of it, while in covering theory we fix a space <span>$X$</span> and consider (covering) maps into it. This is a very deep theme in mathematics: geometry and algebra are dual to each other.

# Deck transformations and the automorphism group

The key to understanding the analogy between Galois theory and covering theory is to understand the group of deck transformations of a cover, and how it relates to the fundamental group. From here, the rest of the correspondence largely follows by 'reversing the arrows'.

*Definition: Deck transformation*

Let <span>$p: \tilde{X} \to X$</span> be a covering map. A (continuous) map <span>$f: X \to X$</span> is called a deck transformation of <span>$p$</span> if <span>$p=p \circ f$</span> i.e. if the figure 1a below commutes:

![]({{ site.baseurl }}/assets/img/deck_transformation.png)

*Fig 1a: A deck transformation*

![]({{ site.baseurl }}/assets/img/field_automorphism.png)

*Fig 1b: An automorphism of field extensions*


Note that <span>$f$</span> is in fact a homeomorphism, and its inverse is also a deck transformation. Hence, the set of deck transformations forms a group, which we denote <span>$\text{Deck}(\tilde{X}|X)$</span>.

Compare this to a homomorphism of field extensions: for a homomorphism of field extensions we fix some field extension <span>$\phi: K \hookrightarrow L$</span> and then a homomorphism of <span>$K$</span>-extensions from <span>$L$</span> to itself is a field homomorphism <span>$f: L \to L$</span> such that <span>$\phi = \phi \circ f$</span>.  The analogy between this group and the deck group of a cover should be clear.

Slightly more general is the notion of a morphism of covering spaces, which corresponds to the idea of a homomorphism of field extensions.

*Definition: Morphism of covers*

Let <span>$p: Y \to X$</span> and <span>$q: Z \to X$</span> be covering maps. Then a morphism of covers from <span>$Y$</span> to <span>$Z$</span> is a covering map <span>$f: Y \to Z$</span> such that the diagram figure 2b below commutes.

![]({{ site.baseurl }}/assets/img/morphism_of_covering_spaces.png)

*Fig 2a: A morphism of covering spaces*

![]({{ site.baseurl }}/assets/img/field_extension_hom.png)

*Fig 2b: A homomorphism of K-extensions*

# Galois extensions and regular covers

The first thing we need to do to understand an analogy with Galois theory is to understand what the analogous concept to a Galois extension is. Recall the definition:

*Definition: Galois extension*

We say that a homormophism <span>$\phi: K \to L$</span> of fields is a Galois extension if <span>$L^{\text{Aut}_K(L)}=K$</span>, where <span>$L^{\text{Aut}_K(L)}$</span> denotes the fixed points of <span>$L$</span> under the action of <span>$\text{Aut}_K(L)$</span>. 

Another way to formulate this is as follows:

<span>$\phi: K \to L$</span> is a Galois extension if <span>$K$</span> is the equaliser of <span>$\text{Aut}(L\vert K)$</span>

The equaliser of a set of maps is just the subset on which all of these maps take the same values. This is equivalent to the usual definition via fixed points because the identity map is of course contained in <span>$\text{Aut}(L\vert K)$</span>. We can further refine our understanding of Galois extensions by phrasing it in more category-theoretic terms. 

*Definition: Equaliser*

(All the maps in the following are maps of <span>$K$</span>-extensions).
Let <span>$\phi: K\to L$</span> be a field extension and let <span>$S \subseteq \text{Aut}(L\vert K)$</span>. Then we say that <span>$E \subseteq L$</span> is the equaliser of <span>$S$</span> if <span>$f_1 \circ i = f_2 \circ i$</span> for all <span>$f_1,f_2 \in S$</span> and for any <span>$K$</span>-extension <span>$M$</span> and any map <span>$g\in \text{Hom}_K(M,L)$</span> such that <span>$f_1 \circ g = f_2 \circ g$</span> for all <span>$f_1,f_2 \in S$</span>, then there exists a unique map <span>$h: M \to E$</span> such that <span>$i \circ h =g$</span> (where <span>$i: K \hookrightarrow M$</span> is the inclusion map)

![]({{ site.baseurl }}/assets/img/equaliser.png)

*Fig 3a: The equaliser*

It is easy to check that the equaliser is indeed unique. In our case, <span>$S$</span> will be a subset and so the conditions <span>$f_1 \circ i = f_2 \circ i$</span>, <span>$g \circ f = g \circ f_2$</span> are equivalently <span>$f \circ i = i$</span>, <span>$g \circ f = g$</span> since <span>$\text{id} \in S$</span>.
The analogy with covering spaces will always be made by reversing all the maps. Thus we get the following definition:

*Definition: Coequaliser*

(All the maps in the following are covering maps).
Let <span>$p: Y\to X$</span> be a covering map and let <span>$S \subseteq \text{Deck}(Y\vert X)$</span>. Then we say that a pair <span>$(Z,q_Z)$</span> where <span>$q_Z: Y \to Z$</span> is the coequaliser of <span>$S$</span> if <span>$q_Z \circ f_1 = q_Z \circ f_2$</span> for all <span>$f_1,f_2 \in S$</span> and for any cover <span>$q_W: W \to X$</span> and any map of <span>$X$</span>-covers <span>$g \in \text{Hom}_X(Y,W)$</span> such that <span>$g \circ f_1 = g \circ f_2$</span> for all <span>$f_1,f_2 \in S$</span>, then there exists a unique map <span>$h: Z \to W$</span> such that <span>$h \circ q_Z =g$</span>

![]({{ site.baseurl }}/assets/img/co-equaliser.png)

*Fig 3b: The co-equaliser*

It is easy to check that <span>$q_Z$</span> is in fact a quotient map, so <span>$Z$</span> may be thought of as a quotient space of <span>$Y$</span>.

*Proposition:*

Let <span>$p:Y \to X$</span> be a covering space and <span>$S$</span> be a set of covering maps <span>$Y \to Y$</span>. Let <span>$\sim$</span> be the smallest equivalence relation on <span>$X$</span> such that <span>$f_1(x) \sim f_2(x)$</span> for all <span>$ f_1,f_2 \in S$</span>. Then <span>$Y/\sim$</span> is a coequaliser of <span>$S$</span>.
Moreover, for any coequaliser <span>$(C,q_c)$</span> of <span>$S$</span>, the map <span>$q_c$</span> is a quotient map, and the quotient <span>$C$</span> by the relation <span>$x \sim y \Leftrightarrow q_c(x)=q_c(y)$</span> equals <span>$Y/\sim$</span>
Proof: This is an essentially categorical argument.
Consider <span>$W,g$</span> as in the definition of coequaliser. Since <span>$g\circ f_1 = g\circ f_2$</span> for all <span>$f_1,f_2 \in S$</span>, we have <span>$g(x)=g(y)$</span> if <span>$x\sim y$</span> and so by a well-known fact about quotient spaces there is a unique continuous map <span>$h: Y/\sim \to W$</span> such that <span>$g = h\circ \pi$</span>, where <span>$\pi$</span> is the quotient map.

For the second part, note that the above argument gives us a map <span>$h_1: Y/\sim \to C$</span>. But the definition of the coequaliser gives us a map <span>$h_2: C \to Y\sim$</span>. But note that the maps <span>$\text{id}_{Y/\sim}, \text{id}_C$</span> also satisfy the properties listed in the definition of the coequaliser so by uniqueness we have <span>$h_1\circ h_2 = \text{id}_C$</span> and <span>$h_2\circ h_1 = \text{id}_{Y/\sim}$</span>, so <span>$Y/\sim \cong C$</span>. One can check that this isomorphism turns <span>$\pi$</span> into <span>$q_C$</span> by a similar argument.

It is now clear that the fixed points of an automorphism group are analogous to the coequaliser of the set of Deck transformations. We will denote this coequaliser by <span>$Y/\text{Deck}(Y\vert X)$</span>. This lets us formulate the analogous concept to a Galois extension:

*Definition: Regular cover*

Let <span>$p: Y \to X$</span> be a covering map. We say that it is a regular cover if the coequaliser <span>$Y/\text{Deck}(Y\vert X)$</span> is just <span>$X$</span> itself (when <span>$X$</span> is considered as a quotient space of <span>$Y$</span> with quotient map <span>$p$</span>).
Spelled out, this means the following: notice that if two points of <span>$Y$</span> differ by a covering transformation of <span>$p$</span>, then <span>$p$</span> takes the same value on them. So <span>$p$</span> descends to a map <span>$\overline{p}: Y/\text{Deck}(Y\vert X) \to X$</span>. We say that <span>$p$</span> is a regular cover if the map <span>$\overline{p}$</span> is a homeomorphism.

![]({{ site.baseurl }}/assets/img/regular_cover.png)

*Fig 4: A regular cover*

The idea here is that we want <span>$X$</span> to be the largest quotient space of <span>$Y$</span> on which <span>$\text{Deck}(Y\vert X)$</span> acts trivially. This quotient space is easy to find; we just take the quotient of <span>$Y$</span> by the action of <span>$\text{Deck}(Y\vert X)$</span>, which we denote <span>$Y/\text{Deck}(Y\vert X)$</span>.

This is a rather unusual definition of regular cover. The typical definition is as follows:

*Definition: Regular cover*

A covering map <span>$p: Y \to X$</span> is regular if for any <span>$x \in X$</span>, and <span>$y_1,y_2 \in p$</span>, there exists a covering transformation <span>$f:Y \to Y$</span> of <span>$p$</span> such that <span>$f(y_1)=y_2$</span>.

One the face of it, it's plausible that these two definitions should be equivalent: two pre-images under <span>$p$</span> are related by a covering transfomation exactly when they are equal in the quotient, in which case the quotient should look like the image <span>$X$</span> of <span>$p$</span>. This is the idea behind the following sketch proof.

*Proposition: The two definitions of regular cover are equivalent*

Sketch proof: Two points <span>$y_1,u_2 \in Y$</span> satisfy <span>$y_1=f(y_2)$</span> for some <span>$f\in S$</span> if and only if <span>$y_1 = y_2$</span> in <span>$Y/\text{Deck}(Y|X)$</span>. This shows that <span>$\overline{p}$</span> is a bijection. It is not hard to show that it is a bijection.

The fundamental group and the absolute Galois group

We now have an understanding of how Galois extensions of fields relate to covering maps. However, the Galois correspondence for covering spaces is usually expressed in terms of the fundamental group. So we need to understand how the fundamental group relates to deck transformations.

*Theorem:*

Let <span>$(X,b)$</span> be a (pointed) topological space and let <span>$p: (\tilde{X},\tilde{b}) \to (X,b)$</span> be the universal cover. Then <span>$\pi_1(X,b)$</span> is isomorphic to the group <span>$\text{Deck}(\tilde{X}|X)$</span>.
Sketch proof:
Let <span>$\ell$</span> be a path in <span>$X$</span> based at <span>$b$</span>. This lifts to a path <span>$\tilde{\ell}$</span> in <span>$\tilde{X}$</span> starting at <span>$\tilde{b}$</span>. Recall that the universal cover of a space is in fact a regular cover, so there exists a covering transformation <span>$f_\ell$</span>. Note that by definition, this transformation <span>$f_ell$</span> is a lift of the map <span>$p$</span> and recall that if two lifts of the same map agree at a point, they agree everywhere. Thus the map <span>$f$</span> is unique. So we may define an isomorphism 
<span>$\pi_1(X,b) \to \text{Deck}(\tilde{X}|X)$</span>
<span>$[\ell] \mapsto f_\ell$</span>
It is now easy to check that this map is injective, surjective and indeed a homomorphism.

What is the fundamental group analogous to in Galois theory? To answer that, we need to find an analogous object to the universal cover, and then take the Galois group of that object. The universal cover of a space <span>$X$</span> can be thought of as the 'largest' connected space which covers <span>$X$</span>. So the analogous concept is the largest separable extension into which a field <span>$K$</span> embeds. The following definitions make this idea more precise.

*Definition: Universal cover*

The universal cover <span>$\tilde{X}$</span> of a space <span>$X$</span> is a space is a covering space <span>$q_1: \tilde{X} \to X$</span> such that for every covering space <span>$q_2: Y \to X$</span> there exists a covering map <span>$q_3: \tilde{X} \to Y$</span> such that <span>$q_2 \circ q_3 = q_1$</span>. 

The space <span>$\tilde{X}$</span> is indeed unique up to isomorphism - but the isomorphism itself is not unique unless <span>$\pi_1(X,b)$</span> is trivial!

![]({{ site.baseurl }}/assets/img/field_extension_hom.png)

*Fig 5a: The universal cover*

What about the field-theoretic analogue? A good guess would be the algebraic closure. This is almost right, but not quite.

*Definition: Separable closure*

Let <span>$K$</span> be a field. The separable closure <span>$K^\text{sep}$</span> is a <span>$K$</span>-extension such that for any separable <span>$K$</span>-extension <span>$L$</span>, there exists a map of <span>$K$</span>-extensions <span>$L \hookrightarrow K^\text{sep}$</span>. One can show that <span>$K^\text{sep}$</span> exists and is unique up to isomorphisms of <span>$K$</span>-extensions.

![]({{ site.baseurl }}/assets/img/separable_closure.png)

*Fig 5b: The separable closure*

The separable closure is somewhat similar to the algebraic closure, and in fact always embeds into it as a <span>$K$</span>-extension (since separable extensions are by definition algebraic). For fields of characteristic 0 and finite fields, we have <span>$K^\text{sep} \cong K^\text{alg}$</span> (indeed, this is the case over any so-called 'perfect field').

One can also define a simply-connected space as a space whose universal cover is itself (or equivalently such that it has no non-trivial covers), and analogous a separably-closed field is a field which is its own separable closure (or equivalently one which admits no non-trivial separable extensions). For example, the algebraic integers <span>$\mathbb{A}$</span> and complex numbers <span>$\mathbb{C}$</span> are separably closed (because they are algebraically closed fields of characteristic 0).

This highlights an important different in the classical presentations of Galois theory and of covering space. In covering space theory, we fix a topological space <span>$X$</span> and classify its covers via subgroups of the fundamental group, i.e. the deck transformations <span>$\text{Deck}(\tilde{X}\vert X)$</span>. This is all intrinsic to the space <span>$X$</span>. For Galois theory, instead of taking just a field <span>$K$</span>, we specify a Galois extension <span>$K \hookrightarrow L$</span>, and then classify intermediate extensions between <span>$K$</span> and <span>$L$</span> by subgroups of <span>$\text{Gal}(L\vert K)$</span>. 

One could do Galois theory in a similar way to covering space theory, by embedding all of our <span>$K$</span>-extensions into the separable closure <span>$K^\text{sep}$</span>, and thinking of all of our Galois groups as subgroups of the absolute Galois group <span>$\text{Gal}(K^\text{sep}\vert K)$</span>. This is in some ways a cleaner perspective, and in more advanced treatments it is sometimes taken. Why isn't Galois theory traditionally done in this way? Arguably, sometimes it is: many first courses only consider finite extensions of <span>$\mathbb{Q}$</span>, and embed them all into the complex numbers <span>$\mathbb{C}$</span> (in fact, they actually embed into the algebraic numbers <span>$\mathbb{A}$</span>). However, we do not take this perspective for computing Galois groups because the absolute Galois group <span>$\text{Gal}(K^\text{sep}\vert K)$</span> is in general very hard to compute, and is not well understood even in the case <span>$\text{Gal}(\mathbb{A}\vert \mathbb{Q})$</span>. 

# The Galois correspondence

At long last, we come to the Galois correspondence. First, we state the field-theoretic Galois correspondence.

*Theorem: The fundamental theorem of Galois theory*

Let <span>$K \hookrightarrow L$</span> be a finite separable field extension. Let <span>$G=\text{Gal}(L\vert K)$</span> and <span>$H=\text{Gal}(L\vert M)$</span> Then:
 - (i) There is an inclusion-reversing bijection: 
 <div>$$ \{\text{intermediate fields } K \subseteq M \subseteq L\} \leftrightarrow \{\text{subgroups } H \subseteq \text{Gal}(L\vert K)\} $$</div> 
 <div>$$M \mapsto \text{Gal}(L\vert M)$$</div> 
 with inverse 
 <div>$$H \mapsto L^H$$</div>

 - (ii) For such <span>$M, H$</span>, we have <span>$[M:K]=\vert G:H \vert$</span>

 - (iii) An intermediate extension <span>$K \subseteq M \subseteq L$</span> is Galois over <span>$K$</span> if and only if <span>$H$</span> is normal in <span>$G$</span>, and in this case we have

<div>$$\text{Gal}(M\vert K) \cong G/H = \text{Gal}(L|K)/\text{Gal}(L\vert M)$$</div>

It is worth taking some time to try to write down for yourself what the corresponding theorem for covering spaces is. We will state it now:

*Theorem: The Galois correspondence (covering spaces)*

Let <span>$p: \tilde{X} \to X$</span> be a finite regular cover and <span>$b \in X$</span>. Let <span>$G=\text{Deck}(\tilde{X},X)$</span> and <span>$H=\text{Gal}(L\vert M)$</span> Then:
 - (i) There is a bijection:
<div>$$\{\text{intermediate covers } \tilde{X} \to Y \to X\} \leftrightarrow \{\text{subgroups } H \subseteq \text{Gal}(\tilde{X}|X)\}$$</div>
<div>$$Y \mapsto \text{Deck}(Y\vert X)$$</div>
with inverse
<div>$$H \mapsto X/H$$</div>

 - (ii) For such <span>$Y, H$</span>, we have that the sheetedness of the cover <span>$Y \to X$</span> is <span>$\vert G:H \vert$</span>

 - (iii) An intermediate cover <span>$\tilde{X} \to Y \to X$</span> is a regular cover of <span>$X$</span> if and only if <span>$H$</span> is normal in <span>$G$</span>, and in this case we have

<div>$$\text{Deck}(Y\vert X) \cong G/H = \text{Deck}(\tilde{X}\vert X)/\text{Deck}(\tilde{X}\vert Y)$$</div>

This statement of the Galois correspondence might not be very familiar, but it is entirely equivalent to the usual one. In particular, setting <span>$\tilde{X}$</span> to be the universal cover of <span>$X$</span> gives the usual correspondence, after identifying <span>$\text{Deck}(\tilde{X}\vert X)$</span> with <span>$\pi_1(X)$</span>. Conversely, applying part (iii) to the usual correspondence yields the one given here.

Note that not only are the statements here analogous, but so are the proofs too: The fact that <span>$L^{\text{Gal}(L\vert M)}=M$</span> follows by definition of a Galois extension, but showing that <span>$\text{Gal}(L\vert L^H)=H$</span> is significantly harder, and is usually done via Artin's lemma. Similarly, showing that <span>$\tilde{X}/\text{Deck}(\tilde{X}\vert Y) \cong Y$</span> follows directly from the definition of a regular cover and holds even when <span>$X$</span> isn't semi-locally simply connected, but showing that there exists a cover corresponding to each subgroup is significantly harder, and needs the semi-locally simply connected assumption.

One might wonder if there is a version of the Galois correspondence for field extensions which classifies all separable extensions via subgroups of <span>$\text{Gal}(\overline{K}\vert K)$</span>. Indeed there is, but it is more technical to state: one has to put a topology on the group <span>$\text{Gal}(\overline{K}\vert K)$</span> and consider closed subgroups rather than arbitrary subgroups. In fact, when <span>$X$</span> is a more pathological topological space then one must topologise <span>$\pi_1(X)$</span> in much the same way in order to classify covering spaces of <span>$X$</span> properly.

# Summary

Lets sum up:
 - Separable field extensions are analogous to covering maps of topological spaces.
 - The degree of a field extension corresponds to the sheetedness of a cover.
 - Automorphisms of such extensions are field automorphisms which leave the base field fixed. These are analogous to homeomorphisms of the covering space which leave the covered space fixed (ie covering transformations).
 - Galois field extensions are those such that the subset of fixed points equals the base field. Regular covering maps are those such that the quotient by the group action gives the covered space.
 - The Galois group of a field extension is analogous to the group of deck transformations of a cover.
 - The universal cover of a space is a covering space which covers all others i.e. the largest connected covering space.The separable closure of a field is a separable extension which contains all other separable extensions i.e. the largest separable extension of the field.
 - The deck transformations of the universal cover can be (non-canonically) identified with the fundamental group of a space. The Galois group of the separable closure of <span>$K$</span> over <span>$K$</span> is called the 'absolute Galois group'.
 - Under these correspondences, the two 'Galois correspondences' are identified with each other.

## But what about

There are a couple of points we haven't covered here.

The biggest, and most pressing, is why this analogy exists in the first place. To each field <span>$K$</span>, one can associate a geometric object called a scheme, which we denote <span>$\text{Spec}(K)$</span>. A field extension <span>$K \to L$</span> gives a morphism of schemes <span>$\text{Spec}(L) \to \text{Spec}(K)$</span>. Since schemes are geometric objects, they have an analogous covering theory to topological spaces and this theory becomes Galois theory once it is transposed back into the language of field extensions. A more complete account of these ideas would take us too far afield though.

Another mysterious aspect is that the analogy is seen most cleanly by removing the basepoint from the picture. What, if anything, is the role of the basepoint in field theory? We will answer this question in another post - in fact, trying to understand the role of the basepoint will lead us to the concept of a 'Galois category', which is a formal account of the properties which lie behind the Galois correspondence.

Finally, there are various aspects of each topic which don't find an obvious analogue in the other. On the side of covering spaces, there's the role of the unit interval <span>$[0,1]$</span>, paths in the space <span>$X$</span>, semi-locally simply connectedness and path-connectedness. On the side of field theory, there's the role of polynomials and algebraically closed fields. I don't know whether these concepts find analogues or if they are superfluous to the analogy.

# Further reading
## The fundamental group 
 - Allen Hatcher, 'Algebraic topology'.
 - John F. Kennison, 'What is the Fundamental Group?': this paper considers several different definitions of the fundamental group, including as a topological group.

## Galois theory
  - J.S. Milne, 'Fields and Galois Theory': includes both the Galois theory of finite extensions and infinite extensions.

## The analogy
 - Tamas Szamuely, 'Galois Groups and Fundamental Groups': This book starts with a brief recap of Galois theory (including the Galois correspondence for infinite field extensions!) and the theory of the fundamental group, and goes on to discuss the Galois theory of schemes.
 - Alexander Grothendieck, 'Revêtements étales et groupe fondamental (SGA 1)': This is where the covering theory of schemes was first developed.
 - Ned Summers, 'Galois and Tannakian Categories': Gives an overview of category-theoretic ideas followed by a definition of a 'Galois category', which is the basic theoretical concept unifying Galois theory and covering space theory.