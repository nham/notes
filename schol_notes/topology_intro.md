---
title: "Introduction to topology"
---

<hr>
pt2

## Coarseness/fineness of topologies

If ``X`` is a set and ``\mathcal{S}`` and ``\mathcal{T}`` are topologies on ``X`` such that every open set in ``\mathcal{S}`` is an open set in ``\mathcal{T}``, then ``\mathcal{S}`` is said to be **coarser** than ``\mathcal{T}`` (and ``\mathcal{T}`` is **finer** than ``\mathcal{S}``).

The coarsest topology on any set ``X`` is the **trivial topology** ``\{ \emptyset, X\}``, while the finest topology, the power set of ``X``, is called the **discrete topology**.


<hr>

## Dense/nowhere dense subsets

A subset ``S`` of a topological space ``X`` is **dense** in ``X`` if its closure is ``X``, and **nowhere dense** in ``X`` if the interior of its closure is empty.

Equivalently, ``S`` is dense iff every non-empty open subset of ``X`` contains an element of ``S``: ``S`` being dense is the same as every point of ``X`` being a closure point of ``S``, which is the same as every neighborhood of any point intersecting ``S``.

Also equivalently, ``S`` is nowhere dense in ``X`` iff ``X - clo(S)`` is dense in ``X``: ``S`` is nowhere dense iff ``clo(S)`` has no interior iff ``clo(S)`` is all boundary points of ``clo(S)``. Clearly

```math
    X = clo S \sqcup X - clo S
```

and also

```math
    clo(X - clo S) = \partial(X - clo S) \sqcup int(X - clo S) = \partial clo S \sqcup X - clo S
```

since the boundary of a set and its complement are equal and since ``X - clo S`` is open. So ``clo(X - clo S) = X`` iff ``clo S = \partial clo S``.
