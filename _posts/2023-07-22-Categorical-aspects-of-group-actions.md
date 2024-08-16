---
layout: post
title:  "Categorical Aspects of Group Actions"
date:   2023-07-22 00:00:00 +0100
categories: 
---

I recently some minor confusion in a conversation with a friend over the words "free group action" and it made me realise a couple of nice things about the category theory of group actions.

# Free group actions are free
Fix a group <span>$G$</span> and let
<div>$$\text{Forget}: G-\text{Set}\to \text{Set} $$</div>
be the forgetful functor. It is not hard to show that this functor has a left adjoint given by
<div>$$\text{Free}: \text{Set}\to G-\text{Set} $$</div>
<div>$$X\mapsto G\times X $$</div>
where <span>$G$</span> acts on <span>$G\times X$</span> by <span>$g.(h,x) = (g.h,x)$</span>. One might then interpret the words "free group action" to mean a group action in the essential image of this functor.

On the other hand, the usual meaning of "free group action" in the theory of group actions is one all of whose stabilisers are trivial. In fact, a group action is free if and only if it is free! In one direction, any group action in the essential image of <span>$\text{Free}$</span> is free in the usual sense because the action of <span>$G$</span> on itself by left-multiplication is free (in the usual sense). In the other direction, suppose that the action of <span>$G$</span> on a set <span>$S$</span> is free in the usual sense. By the orbit-stabiliser theorem, <span>$S$</span> is isomorphic (as a <span>$G$</span>-set) to a disjoint union of copies of <span>$G$</span> with the left-multiplication action. Letting the indexing set of the disjoint union be <span>$X$</span>, we have <span>$S \cong \text{Free}(X)$</span> as <span>$G$</span>-sets.

# Monad magic
The counit of the above adjunction is a map <span>$G\times X\to X$</span>. How very conspicuous! In fact, this map is *exactly* the map defining the action of <span>$G$</span> on <span>$X$</span>[^uninteresting]. In particular the action map is a map of <span>$G$</span>-sets when <span>$G\times X$</span> is equipped with the <span>$G$</span>-action above. This is related to the monadicity of the <span>$G$</span>-set free-forgetful adjunction: recall that an adjunction <span>$F\vdash G$</span> between categories <span>$\mathcal{C},\mathcal{D}$</span> is monadic if the category <span>$\mathcal{D}$</span> is equivalent in a certain natural way to the category of algebras over the monad given by the functor <span>$GF:\mathcal{C}\to\mathcal{C}$</span> and the functor <span>$\eta$</span>. In particular any <span>$y\in\mathcal{D}$</span> is equivalent to the algebra given by <span>$G(\epsilon): GFG(y) \to G(y)$</span>. For most algebraic theories over <span>$\text{Set}$</span>, the above algebra is much more complicated to work with concretely than the original presentation of the object <span>$y$</span>. For instance, for <span>$\mathcal{D}=\text{Grp}$</span> we normally define a group by specifying an identity and a binary operation (subject to some properties). On the other hand, the algebra <span>$\text{Free}(G)\to G$</span> over the free-forgetful monad sends formal words in <span>$G$</span> to their "evaluation" in <span>$G$</span> - which is kind of like a souped-up "unbiased" version of the group multiplication, and on the face of it contains much more information. The point of the monadicity of the adjunction is that this data is in fact equivalent to the description using jus the identity and binary operation.

What's the deal with group actions then? Well here we have a rare instance where the algebra gives *exactly* the same data as was originally specified! This is a pleasant surprise, and almost a bit disconcerting - I would have expected the algebra to be some kind of "unbiased" version of a group action (not that I really know what such a thing would look like). I suspect that the equivalence given by monadicity is in this case actually an isomorphism. There are nice refinesments of Beck's monadicity theorem covering this situation but I don't know them in any great detail so I'll have to leave things there.

# Homework
What does the above story look like for modules? (After all, a module is a "just" linear version of a group action). Hint: enrich!


[^uninteresting]: The unit <span>$X \to G\times X$</span> is not nearly as interesting; it's just <span>$x \mapsto (e,x)$</span>.