---
layout: post
title:  "The Group Ring As Hopf Algebra"
date:   2024-08-23 00:00:00 +0100
categories: 
---

The study of finite-dimensional representations of a finite group[^finite] MORE WORDS HERE. In particular, group representations can be understood in terms of their characters, which are elements of the dual of the group ring. This dual has its own algebra structure, which is also of central importance. This structure on the group ring can be formalised in the notion of a *Hopf algebra*, and it has been enlightening for me to revisit group representation theory in the spirit of this duality and its presentation via Hopf algebras.

# Hopf algebras
*Definition: Hopf algebra (joke)*\
A Hopf algebra is a Hopf algebra object in the category of vector spaces.

The above is genuinely a very nice and compact definition of a Hopf algebra, but it doesn't mean very much unless one is acquainted with rather more monoidal category theory than it is respectable to assume. I'll write this post without assuming that you know *any* monoidal category theory, but it is nice to know that most everything here can be generalised in that context (and to stop to consider it!).

A nice point of view on the group ring is that it is a kind of "linearised" version of a the group, where we have replaced the underlying set of the group <span>$G$</span> with an underlying vector space (specifically, the *free* vector space on <span>$G$</span>). To see how we might go about this, let's revisit the definition of a group. 

*Definition: Group*\



[^finite]: Actually, the finiteness assumptions are not necessary for the most formal aspects of the relationship between the group ring and group representations to go through. But infinite-dimensional spaces are best studied when they are equipped with extra (e.g. geometric, topological, measure-theoretic) structure.  