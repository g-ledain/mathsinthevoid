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

The reversing of the arrows makes this correspondence 'contravariant'. For instance, in Galois theory we fix a field $K$ and consider maps out of it, while in covering theory we fix a space $X$ and consider (covering) maps into it. This is a very deep theme in mathematics: geometry and algebra are dual to each other.

# Deck transformations and the automorphism group

The key to understanding the analogy between Galois theory and covering theory is to understand the group of deck transformations of a cover, and how it relates to the fundamental group. From here, the rest of the correspondence largely follows by 'reversing the arrows'.

*Definition: Deck transformation*

Let $p: \tilde{X} \to X$ be a covering map. A (continuous) map $f: X \to X$ is called a deck transformation of $p$ if $p=p \circ f$ i.e. if the figure 1a below commutes:

![]({{ site.baseurl }}/assets/img/deck_transformation.png)

*Fig 1a: A deck transformation*

![]({{ site.baseurl }}/assets/img/field_automorphism.png)

*Fig 1b: An automorphism of field extensions*


Note that $f$ is in fact a homeomorphism, and its inverse is also a deck transformation. Hence, the set of deck transformations forms a group, which we denote $\text{Deck}(\tilde{X}|X)$.

Compare this to a homomorphism of field extensions: for a homomorphism of field extensions we fix some field extension $\phi: K \hookrightarrow L$ and then a homomorphism of $K$-extensions from $L$ to itself is a field homomorphism $f: L \to L$ such that $\phi = \phi \circ f$.  The analogy between this group and the deck group of a cover should be clear.

Slightly more general is the notion of a morphism of covering spaces, which corresponds to the idea of a homomorphism of field extensions.

*Definition: Morphism of covers*

Let $p: Y \to X$ and $q: Z \to X$ be covering maps. Then a morphism of covers from $Y$ to $Z$ is a covering map $f: Y \to Z$ such that the diagram figure 2b below commutes.

![]({{ site.baseurl }}/assets/img/morphism_of_covering_spaces.png)

*Fig 2a: A morphism of covering spaces*

![]({{ site.baseurl }}/assets/img/field_extension_hom.png)

*Fig 2b: A homomorphism of K-extensions*

# Galois extensions and regular covers

The first thing we need to do to understand an analogy with Galois theory is to understand what the analogous concept to a Galois extension is. Recall the definition:

*Definition: Galois extension*

We say that a homormophism $\phi: K \to L$ of fields is a Galois extension if $L^{\text{Aut}_K(L)}=K$, where $L^{\text{Aut}_K(L)}$ denotes the fixed points of $L$ under the action of $\text{Aut}_K(L)$. 

Another way to formulate this is as follows:

$\phi: K \to L$ is a Galois extension if $K$ is the equaliser of $\text{Aut}(L\vert K)$

The equaliser of a set of maps is just the subset on which all of these maps take the same values. This is equivalent to the usual definition via fixed points because the identity map is of course contained in $\text{Aut}(L\vert K)$. We can further refine our understanding of Galois extensions by phrasing it in more category-theoretic terms. 

*Definition: Equaliser*

(All the maps in the following are maps of $K$-extensions).
Let $\phi: K\to L$ be a field extension and let $S \subseteq \text{Aut}(L\vert K)$. Then we say that $E \subseteq L$ is the equaliser of $S$ if $f_1 \circ i = f_2 \circ i$ for all $f_1,f_2 \in S$ and for any $K$-extension $M$ and any map $g\in \text{Hom}_K(M,L)$ such that $f_1 \circ g = f_2 \circ g$ for all $f_1,f_2 \in S$, then there exists a unique map $h: M \to E$ such that $i \circ h =g$ (where $i: K \hookrightarrow M$ is the inclusion map)

![]({{ site.baseurl }}/assets/img/equaliser.png)

*Fig 3a: The equaliser*

It is easy to check that the equaliser is indeed unique. In our case, $S$ will be a subset and so the conditions $f_1 \circ i = f_2 \circ i$, $g \circ f = g \circ f_2$ are equivalently $f \circ i = i$, $g \circ f = g$ since $\text{id} \in S$.
The analogy with covering spaces will always be made by reversing all the maps. Thus we get the following definition:

*Definition: Coequaliser*

(All the maps in the following are covering maps).
Let $p: Y\to X$ be a covering map and let $S \subseteq \text{Deck}(Y\vert X)$. Then we say that a pair $(Z,q_Z)$ where $q_Z: Y \to Z$ is the coequaliser of $S$ if $q_Z \circ f_1 = q_Z \circ f_2$ for all $f_1,f_2 \in S$ and for any cover $q_W: W \to X$ and any map of $X$-covers $g \in \text{Hom}_X(Y,W)$ such that $g \circ f_1 = g \circ f_2$ for all $f_1,f_2 \in S$, then there exists a unique map $h: Z \to W$ such that $h \circ q_Z =g$

![]({{ site.baseurl }}/assets/img/co-equaliser.png)

*Fig 3b: The co-equaliser*

It is easy to check that $q_Z$ is in fact a quotient map, so $Z$ may be thought of as a quotient space of $Y$.

*Proposition:*

Let $p:Y \to X$ be a covering space and $S$ be a set of covering maps $Y \to Y$. Let $\sim$ be the smallest equivalence relation on $X$ such that $f_1(x) \sim f_2(x)$ for all $ f_1,f_2 \in S$. Then $Y/\sim$ is a coequaliser of $S$.
Moreover, for any coequaliser $(C,q_c)$ of $S$, the map $q_c$ is a quotient map, and the quotient $C$ by the relation $x \sim y \Leftrightarrow q_c(x)=q_c(y)$ equals $Y/\sim$
Proof: This is an essentially categorical argument.
Consider $W,g$ as in the definition of coequaliser. Since $g\circ f_1 = g\circ f_2$ for all $f_1,f_2 \in S$, we have $g(x)=g(y)$ if $x\sim y$ and so by a well-known fact about quotient spaces there is a unique continuous map $h: Y/\sim \to W$ such that $g = h\circ \pi$, where $\pi$ is the quotient map.

For the second part, note that the above argument gives us a map $h_1: Y/\sim \to C$. But the definition of the coequaliser gives us a map $h_2: C \to Y\sim$. But note that the maps $\text{id}_{Y/\sim}, \text{id}_C$ also satisfy the properties listed in the definition of the coequaliser so by uniqueness we have $h_1\circ h_2 = \text{id}_C$ and $h_2\circ h_1 = \text{id}_{Y/\sim}$, so $Y/\sim \cong C$. One can check that this isomorphism turns $\pi$ into $q_C$ by a similar argument.

It is now clear that the fixed points of an automorphism group are analogous to the coequaliser of the set of Deck transformations. We will denote this coequaliser by $Y/\text{Deck}(Y\vert X)$. This lets us formulate the analogous concept to a Galois extension:

*Definition: Regular cover*

Let $p: Y \to X$ be a covering map. We say that it is a regular cover if the coequaliser $Y/\text{Deck}(Y\vert X)$ is just $X$ itself (when $X$ is considered as a quotient space of $Y$ with quotient map $p$).
Spelled out, this means the following: notice that if two points of $Y$ differ by a covering transformation of $p$, then $p$ takes the same value on them. So $p$ descends to a map $\overline{p}: Y/\text{Deck}(Y\vert X) \to X$. We say that $p$ is a regular cover if the map $\overline{p}$ is a homeomorphism.

![]({{ site.baseurl }}/assets/img/regular_cover.png)

*Fig 4: A regular cover*

The idea here is that we want $X$ to be the largest quotient space of $Y$ on which $\text{Deck}(Y\vert X)$ acts trivially. This quotient space is easy to find; we just take the quotient of $Y$ by the action of $\text{Deck}(Y\vert X)$, which we denote $Y/\text{Deck}(Y\vert X)$.

This is a rather unusual definition of regular cover. The typical definition is as follows:

*Definition: Regular cover*

A covering map $p: Y \to X$ is regular if for any $x \in X$, and $y_1,y_2 \in p$, there exists a covering transformation $f:Y \to Y$ of $p$ such that $f(y_1)=y_2$.

One the face of it, it's plausible that these two definitions should be equivalent: two pre-images under $p$ are related by a covering transfomation exactly when they are equal in the quotient, in which case the quotient should look like the image $X$ of $p$. This is the idea behind the following sketch proof.

*Proposition: The two definitions of regular cover are equivalent*

Sketch proof: Two points $y_1,u_2 \in Y$ satisfy $y_1=f(y_2)$ for some $f\in S$ if and only if $y_1 = y_2$ in $Y/\text{Deck}(Y|X)$. This shows that $\overline{p}$ is a bijection. It is not hard to show that it is a bijection.

The fundamental group and the absolute Galois group

We now have an understanding of how Galois extensions of fields relate to covering maps. However, the Galois correspondence for covering spaces is usually expressed in terms of the fundamental group. So we need to understand how the fundamental group relates to deck transformations.

*Theorem:*

Let $(X,b)$ be a (pointed) topological space and let $p: (\tilde{X},\tilde{b}) \to (X,b)$ be the universal cover. Then $\pi_1(X,b)$ is isomorphic to the group $\text{Deck}(\tilde{X}|X)$.
Sketch proof:
Let $\ell$ be a path in $X$ based at $b$. This lifts to a path $\tilde{\ell}$ in $\tilde{X}$ starting at $\tilde{b}$. Recall that the universal cover of a space is in fact a regular cover, so there exists a covering transformation $f_\ell$. Note that by definition, this transformation $f_ell$ is a lift of the map $p$ and recall that if two lifts of the same map agree at a point, they agree everywhere. Thus the map $f$ is unique. So we may define an isomorphism 
$\pi_1(X,b) \to \text{Deck}(\tilde{X}|X)$
$[\ell] \mapsto f_\ell$
It is now easy to check that this map is injective, surjective and indeed a homomorphism.

What is the fundamental group analogous to in Galois theory? To answer that, we need to find an analogous object to the universal cover, and then take the Galois group of that object. The universal cover of a space $X$ can be thought of as the 'largest' connected space which covers $X$. So the analogous concept is the largest separable extension into which a field $K$ embeds. The following definitions make this idea more precise.

*Definition: Universal cover*

The universal cover $\tilde{X}$ of a space $X$ is a space is a covering space $q_1: \tilde{X} \to X$ such that for every covering space $q_2: Y \to X$ there exists a covering map $q_3: \tilde{X} \to Y$ such that $q_2 \circ q_3 = q_1$. 

The space $\tilde{X}$ is indeed unique up to isomorphism - but the isomorphism itself is not unique unless $\pi_1(X,b)$ is trivial!

![]({{ site.baseurl }}/assets/img/field_extension_hom.png)

*Fig 5a: The universal cover*

What about the field-theoretic analogue? A good guess would be the algebraic closure. This is almost right, but not quite.

*Definition: Separable closure*

Let $K$ be a field. The separable closure $K^\text{sep}$ is a $K$-extension such that for any separable $K$-extension $L$, there exists a map of $K$-extensions $L \hookrightarrow K^\text{sep}$. One can show that $K^\text{sep}$ exists and is unique up to isomorphisms of $K$-extensions.

![]({{ site.baseurl }}/assets/img/separable_closure.png)

*Fig 5b: The separable closure*

The separable closure is somewhat similar to the algebraic closure, and in fact always embeds into it as a $K$-extension (since separable extensions are by definition algebraic). For fields of characteristic 0 and finite fields, we have $K^\text{sep} \cong K^\text{alg}$ (indeed, this is the case over any so-called 'perfect field').

One can also define a simply-connected space as a space whose universal cover is itself (or equivalently such that it has no non-trivial covers), and analogous a separably-closed field is a field which is its own separable closure (or equivalently one which admits no non-trivial separable extensions). For example, the algebraic integers $\mathbb{A}$ and complex numbers $\mathbb{C}$ are separably closed (because they are algebraically closed fields of characteristic 0).

This highlights an important different in the classical presentations of Galois theory and of covering space. In covering space theory, we fix a topological space $X$ and classify its covers via subgroups of the fundamental group, i.e. the deck transformations $\text{Deck}(\tilde{X}\vert X)$. This is all intrinsic to the space $X$. For Galois theory, instead of taking just a field $K$, we specify a Galois extension $K \hookrightarrow L$, and then classify intermediate extensions between $K$ and $L$ by subgroups of $\text{Gal}(L\vert K)$. 

One could do Galois theory in a similar way to covering space theory, by embedding all of our $K$-extensions into the separable closure $K^\text{sep}$, and thinking of all of our Galois groups as subgroups of the absolute Galois group $\text{Gal}(K^\text{sep}\vert K)$. This is in some ways a cleaner perspective, and in more advanced treatments it is sometimes taken. Why isn't Galois theory traditionally done in this way? Arguably, sometimes it is: many first courses only consider finite extensions of $\mathbb{Q}$, and embed them all into the complex numbers $\mathbb{C}$ (in fact, they actually embed into the algebraic numbers $\mathbb{A}$). However, we do not take this perspective for computing Galois groups because the absolute Galois group $\text{Gal}(K^\text{sep}\vert K)$ is in general very hard to compute, and is not well understood even in the case $\text{Gal}(\mathbb{A}\vert \mathbb{Q})$. 

# The Galois correspondence

At long last, we come to the Galois correspondence. First, we state the field-theoretic Galois correspondence.

*Theorem: The fundamental theorem of Galois theory*

Let $K \hookrightarrow L$ be a finite separable field extension. Let $G=\text{Gal}(L\vert K)$ and $H=\text{Gal}(L\vert M)$ Then:
 - (i) There is an inclusion-reversing bijection: 
 $$ \{\text{intermediate fields } K \subseteq M \subseteq L\} \leftrightarrow \{\text{subgroups } H \subseteq \text{Gal}(L\vert K)\} $$ 
 $$M \mapsto \text{Gal}(L\vert M)$$ 
 with inverse 
 $$H \mapsto L^H$$

 - (ii) For such $M, H$, we have $[M:K]=\vert G:H \vert$

 - (iii) An intermediate extension $K \subseteq M \subseteq L$ is Galois over $K$ if and only if $H$ is normal in $G$, and in this case we have

$$\text{Gal}(M\vert K) \cong G/H = \text{Gal}(L|K)/\text{Gal}(L\vert M)$$

It is worth taking some time to try to write down for yourself what the corresponding theorem for covering spaces is. We will state it now:

*Theorem: The Galois correspondence (covering spaces)*

Let $p: \tilde{X} \to X$ be a finite regular cover and $b \in X$. Let $G=\text{Deck}(\tilde{X},X)$ and $H=\text{Gal}(L\vert M)$ Then:
 - (i) There is a bijection:
$$\{\text{intermediate covers } \tilde{X} \to Y \to X\} \leftrightarrow \{\text{subgroups } H \subseteq \text{Gal}(\tilde{X}|X)\}$$
$$Y \mapsto \text{Deck}(Y\vert X)$$
with inverse
$$H \mapsto X/H$$

 - (ii) For such $Y, H$, we have that the sheetedness of the cover $Y \to X$ is $\vert G:H \vert$

 - (iii) An intermediate cover $\tilde{X} \to Y \to X$ is a regular cover of $X$ if and only if $H$ is normal in $G$, and in this case we have

$$\text{Deck}(Y\vert X) \cong G/H = \text{Deck}(\tilde{X}\vert X)/\text{Deck}(\tilde{X}\vert Y)$$

This statement of the Galois correspondence might not be very familiar, but it is entirely equivalent to the usual one. In particular, setting $\tilde{X}$ to be the universal cover of $X$ gives the usual correspondence, after identifying $\text{Deck}(\tilde{X}\vert X)$ with $\pi_1(X)$. Conversely, applying part (iii) to the usual correspondence yields the one given here.

Note that not only are the statements here analogous, but so are the proofs too: The fact that $L^{\text{Gal}(L\vert M)}=M$ follows by definition of a Galois extension, but showing that $\text{Gal}(L\vert L^H)=H$ is significantly harder, and is usually done via Artin's lemma. Similarly, showing that $\tilde{X}/\text{Deck}(\tilde{X}\vert Y) \cong Y$ follows directly from the definition of a regular cover and holds even when $X$ isn't semi-locally simply connected, but showing that there exists a cover corresponding to each subgroup is significantly harder, and needs the semi-locally simply connected assumption.

One might wonder if there is a version of the Galois correspondence for field extensions which classifies all separable extensions via subgroups of $\text{Gal}(\overline{K}\vert K)$. Indeed there is, but it is more technical to state: one has to put a topology on the group $\text{Gal}(\overline{K}\vert K)$ and consider closed subgroups rather than arbitrary subgroups. In fact, when $X$ is a more pathological topological space then one must topologise $\pi_1(X)$ in much the same way in order to classify covering spaces of $X$ properly.

# Summary

Lets sum up:
 - Separable field extensions are analogous to covering maps of topological spaces.
 - The degree of a field extension corresponds to the sheetedness of a cover.
 - Automorphisms of such extensions are field automorphisms which leave the base field fixed. These are analogous to homeomorphisms of the covering space which leave the covered space fixed (ie covering transformations).
 - Galois field extensions are those such that the subset of fixed points equals the base field. Regular covering maps are those such that the quotient by the group action gives the covered space.
 - The Galois group of a field extension is analogous to the group of deck transformations of a cover.
 - The universal cover of a space is a covering space which covers all others i.e. the largest connected covering space.The separable closure of a field is a separable extension which contains all other separable extensions i.e. the largest separable extension of the field.
 - The deck transformations of the universal cover can be (non-canonically) identified with the fundamental group of a space. The Galois group of the separable closure of $K$ over $K$ is called the 'absolute Galois group'.
 - Under these correspondences, the two 'Galois correspondences' are identified with each other.

## But what about

There are a couple of points we haven't covered here.

The biggest, and most pressing, is why this analogy exists in the first place. To each field $K$, one can associate a geometric object called a scheme, which we denote $\text{Spec}(K)$. A field extension $K \to L$ gives a morphism of schemes $\text{Spec}(L) \to \text{Spec}(K)$. Since schemes are geometric objects, they have an analogous covering theory to topological spaces and this theory becomes Galois theory once it is transposed back into the language of field extensions. A more complete account of these ideas would take us too far afield though.

Another mysterious aspect is that the analogy is seen most cleanly by removing the basepoint from the picture. What, if anything, is the role of the basepoint in field theory? We will answer this question in another post - in fact, trying to understand the role of the basepoint will lead us to the concept of a 'Galois category', which is a formal account of the properties which lie behind the Galois correspondence.

Finally, there are various aspects of each topic which don't find an obvious analogue in the other. On the side of covering spaces, there's the role of the unit interval $[0,1]$, paths in the space $X$, semi-locally simply connectedness and path-connectedness. On the side of field theory, there's the role of polynomials and algebraically closed fields. I don't know whether these concepts find analogues or if they are superfluous to the analogy.

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