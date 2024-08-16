---
layout: post
title:  "Categorical Aspects of Group Actions"
date:   2024-08-15 00:00:00 +0100
categories: 
---

I recently some minor confusion in a conversation with a friend over the words "free group action" and it made me realise a couple of nice things about the category theory of group actions.

# Free group actions are free
Fix a group $G$ and let
$$\text{Forget}: G-\text{Set}\to \text{Set} $$
be the forgetful functor. It is not hard to show that this functor has a left adjoint given by
$$\text{Free}: \text{Set}\to G-\text{Set} $$
$$X\mapsto G\times X $$
where $G$ acts on $G\times X$ by $g.(h,x) = (g.h,x)$. One might then interpret the words "free group action" to mean a group action in the essential image of this functor.

On the other hand, the usual meaning of "free group action" in the theory of group actions is one all of whose stabilisers are trivial. In fact, a group action is free if and only if it is free! In one direction, any group action in the essential image of $\text{Free}$ is free in the usual sense because the action of $G$ on itself by left-multiplication is free (in the usual sense). In the other direction, suppose that the action of $G$ on a set $S$ is free in the usual sense. By the orbit-stabiliser theorem, $S$ is isomorphic (as a $G$-set) to a disjoint union of copies of $G$ with the left-multiplication action. Letting the indexing set of the disjoint union be $X$, we have $S \cong \text{Free}(X)$ as $G$-sets.

# Monad magic
The counit of the above adjunction is a map $G\times X\to X$. How very conspicuous! In fact, this map is *exactly* the map defining the action of $G$ on $X$[^uninteresting]. In particular the action map is a map of $G$-sets when $G\times X$ is equipped with the $G$-action above. This is related to the monadicity of the $G$-set free-forgetful adjunction: recall that an adjunction $F\vdash G$ between categories $\mathcal{C},\mathcal{D}$ is monadic if the category $\mathcal{D}$ is equivalent in a certain natural way to the category of algebras over the monad given by the functor $GF:\mathcal{C}\to\mathcal{C}$ and the functor $\eta$. In particular any $y\in\mathcal{D}$ is equivalent to the algebra given by $G(\epsilon): GFG(y) \to G(y)$. For most algebraic theories over $\text{Set}$, the above algebra is much more complicated to work with concretely than the original presentation of the object $y$. For instance, for $\mathcal{D}=\text{Grp}$ we normally define a group by specifying an identity and a binary operation (subject to some properties). On the other hand, the algebra $\text{Free}(G)\to G$ over the free-forgetful monad sends formal words in $G$ to their "evaluation" in $G$ - which is kind of like a souped-up "unbiased" version of the group multiplication, and on the face of it contains much more information. The point of the monadicity of the adjunction is that this data is in fact equivalent to the description using jus the identity and binary operation.

What's the deal with group actions then? Well here we have a rare instance where the algebra gives *exactly* the same data as was originally specified! This is a pleasant surprise, and almost a bit disconcerting - I would have expected the algebra to be some kind of "unbiased" version of a group action (not that I really know what such a thing would look like). I suspect that the equivalence given by monadicity is in this case actually an isomorphism. There are nice refinesments of Beck's monadicity theorem covering this situation but I don't know them in any great detail so I'll have to leave things there.

# Homework
What does the above story look like for modules? (After all, a module is a "just" linear version of a group action).


[^uninteresting]: The unit $X \to G\times X$ is not nearly as interesting; it's just $x \mapsto (e,x)$.