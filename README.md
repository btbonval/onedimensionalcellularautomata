See LICENSE for copyright notice.

# Overview

This is a Python implementation of 1D cellular automata using dictionaries and
itertools where possible for speed.

There are three components:
* neighborhoods define the region of interest for rule mapping
* rules map a neighborhood to a single boolean value
* updates run the rules across neighborhoods iteratively

# Neighborhoods

Users may create their own neighborhood functions, but one is provided which
should cover most use cases.

These are simply a list of indices which are supplied to a numpy array. The
neighborhood function must take a target index as input and return the
indices which are in the neighborhood of that target. Generally speaking,
the target will be the center of the neighborhood, but this is not a strict
rule. Neighborhoods might wrap around edges, or they might be truncated by
edges.

# Rules

It is assumed users will create their own rules, but some are provided by way
of example.

Rules are mappings of tuples to boolean values. Each rule's tuple should be the
length of the neighborhood: each rule is mapping a neighborhood onto a cell.

If the neighborhood does not wrap, then variable sized neighborhoods must be
accounted for. A neighborhood of 5 cells centered on an target cell must be
reduced to 3 cells on either edge. Thus mappings must exist for neighborhoods
of size 3, 4, and 5.

Neighborhood of size 2 `==o==` with wrap, assuming target is centered on `o`:

    o==---== (5 cells selected)
    =o==---= (5 cells selected)
    ==o==--- (5 cells selected)
    -==o==-- (5 cells selected)
    
Same neighborhood without wrap, same assumptions as above:

    o==----- (3 cells selected)
    =o==---- (4 cells selected)
    ==o==--- (5 cells selected)
    -==o==-- (5 cells selected)

# States

The user is expected to generate an initial state, normally from numpy.

A state is the automata space defined as a boolean numpy array of some fixed
length `l`. 

# Update 

Users are not expected to modify the update functions.

Functions defined in update.py:
* prepare_update() takes a state, rule, and neighborhood function and prepares
the execution of the next state with itertools
* update() does the same as prepare_update(), but executes the itertools chain
and converts it to a numpy array.
* evolve() calls update() for a given number of steps, or until any state is
encountered for a second time (indicating a loop).

# Example Use

    import numpy
    import neighborhood
    import update
    import rules
    
    # generate initial state of 200 boolean values (0..2 excluding 2, thus 0 or 1)
    state0 = numpy.random.randint(0,2,200).astype(bool)
    # create a neighborhood of 1 (left, center, right) which wraps around edges
    n1_wrap = neighborhood.nx_generator(1, wrap=True)
    # run Wolfram's rule 110 on the initial state.
    # this will also create a matplotlib space-time graph.
    result = update.evolve(100, state0, n1_wrap, rules.wolfram_110)
