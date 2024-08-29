---
layout: post
title:  "A Thousand And One Monoidal Category Definitions"
date:   2024-08-24 00:00:00 +0100
categories: 
---

# Flavours of monoidal category, functor, natural transformation

*Definition: Monoidal category*\
A monoidal category is a category <span>$\mathcal{C}$</span> with the following extra structure:
STRUCTURE
subject to the following axioms:
AXIOMS

Since we are considering categories equipped with some extra structure, we should ask for our morphisms (i.e. categories) between these structures to preserve this extra structure. Unlike in the case of sets with (algebraic) structure, there is more than one sensible way to do this. Essentially, this is because in the case of sets-with-structure the compatibility relations are expressed by equalities, which are symmetric, but for categories-with-structure[^2-theory] the compatibilities are given by certain morphisms, which are not. One then two choices about which way to make the morphisms "point"[^higher]. All of the classes of functor between monoidal categories that we are about to discuss are closed under both horizontal and vertical composition.

From now on, let <span>$\mathcal{C},\mathcal{D}$</span> be monoidal categories.
*Definition: (Strong) Lax monoidal functor*\
A lax monoidal functor from <span>$\mathcal{C}$</span> to <span>$\mathcal{D}$</span> is a functor 
<div>$$F:\mathcal{C}\to \mathcal{D} $$</div>
together with natural transformations
<div>$$\phi_{x,y}: F(x)\otimes_mathcal{D} F(y) \to F(x\otimes_\mathcal{C} y)$$</div>
<div>$$i: 1_\mathcal{D} \to F(1_\mathcal{C}) $$</div>
such that the following diagrams commute:
DIAGRAMS
We say that the functor <span>$F$</span> is "strong lax" or just "strong" if <span>$\phi_{x,y}, i$</span> are isomorphisms.

The definition of lax monoidal functor has always seemed the "wrong way round" to me - it has this weird contravariance in the directions of <span>$\phi, i$</span> relative to <span>$F$</span>. The name is perhaps better justified by the relationship between lax functors and algebras (and dually, between colax functors and coalgebras), which we will see later.

*Definition: (Strong) Colax monoidal functor*\
A colax (or oplax) monoidal functor from <span>$\mathcal{C}$</span> to <span>$\mathcal{D}$</span> is a functor 
<div>$$F:\mathcal{C}\to \mathcal{D} $$</div>
together with natural transformations
<div>$$\phi_{x,y}: F(x\otimes_\mathcal{C} y) \to F(x)\otimes_\mathcal{D} F(y)$$</div>
<div>$$i: F(1_\mathcal{C}) \to 1_\mathcal{D} $$</div>
such that the following diagrams commute:
DIAGRAMS
We say that the functor <span>$F$</span> is "strong colax" or just "costrong" if <span>$\phi_{x,y}, i$</span> are isomorphisms.

Note that <span>$(F,\phi,i)$</span> is strong exactly when <span>$(F, \phi^{-1},i^{-1})$</span> is costrong.

The definition of monoidal category we have been considering so far imposes no relationship between <span>$x\otimes y$</span> and <span>$y\otimes x$</span>. Unlike in the case of "monoidal sets" (i.e. monoids), commutativity of monoidal categories comes in two different strengths[^higher-monoidal]: "braided" and "symmetric".

*Definition: Braided monoidal category, Symmetric monoidal category*\

Since symmetry is a *property* of a braided monoidal category, rather than being an extra structure on it, there are no new classes of functor or natural transformations between symmetric monoidal categories beyond those between braided monoidal categories. In other words, the functors and natural transformations between symmetric monoidal categories are just the functors and natural transformations between their underlying braided monoidal categories.

From now on suppose that <span>$\mathcal{C}$</span> is a braided lax monoidal category with braiding <span>$\gamma$</span>.

*Definition: Braided lax monoidal functor, Braided colax monoidal functor*\

The relationship between <span>$x\otimes y$</span> and <span>$y\otimes x$</span> in braided monoidal categories allows us to express a compatibility condition between a lax and a colax structure on a functor, giving rise to the notion of a "bilax" monoidal functor. Note that this functor *need not neccesarily be braided lax/braided colax*. If it is both braided lax and braided colax, then it is said to be *braided bilax*. This is an unusual case where extra structure on objects (here categories) can induce classes of morphism between those objects which don't "respect" the object structure in the conventional sense.

*Definition: (Strong, Braided) Bilax monoidal functor*\
A bilax monoidal functor is a functor <span>$F$</span> with both a lax monoidal structure <span>$(\phi,i)$</span> and a colax monoidal structure <span>$(\psi,j)$</span> such that the following diagram commutes:\
DIAGRAM HERE\
We say a functor is strong bilax if the lax and colax structures are both strong. Note that in this case we actually have <span>$\phi = \psi^{-1}$</span> and <span>$i=j^{-1}$</span>.\
We say a functor is braided bilax if the lax and colax structures are both braided.

*Definition: Braided lax monoidal natural transformation, Braided colax monoidal natural transformation*\

*Definition: Bilax monoidal natural transformation*\




# Monoidal categories and adjunctions

[^2-theory]: There is an entire theory of 2-monads, largely due to Kelley, which formalises the resulting structure. Much of what we will discuss above is subsumed by this theory. See, for instance [here]{https://ncatlab.org/nlab/show/doctrine} and [here]{https://ncatlab.org/nlab/show/doctrinal+adjunction} as starting points

[^higher]: I am personally very interested in developing a systematic theory for describing and working with the myriad ways of directing coherence morphisms which occur in higher categories. 

[^higher-monoidal]: Why exactly two strengths? Why not just one as in the case of monoids, or why not many more? The case of monoidal structures on sets and on categories fits into a general story (conjectural, in some formulations) about monoidal structures on higher categories. Specifically, there is an equivalence between: <span>$(n+k)$</span>-categories which are trivial at level <span>$k$</span> and below, <span>$n$</span>-categories with <span>$k$</span> compatible monoidal structures, and <span>$n$</span>-categories with a monoidal structure which is suitably commutative. The aforementioned objects are called "<span>$k$</span>-tuply monoidal <span>$n$</span>-categories". A nice introduction to this phenomenon (among other things) is given in John Baez's ["What n-categories should be like"]{https://math.ucr.edu/home/baez/n_categories/what.pdf}.

[^usual]: In fact, it seems that these theorems are usually stated for the free monoidal category on a *single* object. However, I confess that I do not understand how one would obtain a 

[^morphisms]: As such, the coherence theorems we will present here only concerns commuting diagrams whose arrows are composed of the structural morphisms of the monoidal category (e.g. unitor, associator, braiding). In order to obtain a simi;ar description of commuting diagrams with non-structural morphisms, one would have to give a description of the free (braided/symmetric) monoidal category on a *categoy*. In full generality this is surely a hopeless task. Perhaps it would be more tractable if we were given some presentation of the category (over the category of graphs, say) by generators and relations, but even this sounds difficult.

[^alternative]: In fact, there are several traditional ways to formulate coherence theorems, one of which is a description of a class of diagrams which commute in any monoidal category. This can be obtained from our theorem by using a suitable universal property of free monoidal categories. It would be nice to examine the relationship between different statements of coherence theorems more closely in a future post, when I understand them better.