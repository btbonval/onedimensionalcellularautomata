'''
Update rule.

given some automata state, neighborhood, and update rule, perform the update
function.
'''

import numpy
from matplotlib import pyplot
from matplotlib import cm

from itertools import imap
from itertools import starmap
from itertools import repeat 
from itertools import izip

def prepare_update(state, neighborhood, rule):
    '''
    state should be a 1D numpy array.
    neighborhood should be a function that takes the automata length and an
    index and returns a list of indices.
    rule should be a hashmap which maps each initial condition, as a 1D numpy
    array, to the correct final condition, which is a single boolean value.
    returns an iterable.
    '''

    # needed for iterating through the state array.
    l = len(state)
    # convenience function for nx_generator objects
    if hasattr(neighborhood, 'set_length'):
        neighborhood.set_length(l)

    # generate neighborhood selections for each index of state
    #n = imap(neighborhood, range(0,l)) # e.g. neighborhood(0)
    # apply each slice to state
    #o = imap(state.__getitem__, n) # e.g. state[neighborhood(0)]
    # convert each numpy array into an immutable tuple
    #p = imap(tuple, o) # e.g. tuple(state[neighborhood(0)])
    # determine the new state for each of the state slices
    #q = imap(rule.__getitem__, p) # e.g. rule[tuple(state[neighborhood(0)])]

    #return q

    # comments above left for readability, all of it strung together for speed:
    return imap(rule.__getitem__, imap(tuple, imap(state.__getitem__, imap(neighborhood, range(0,l)))))

def update(*args, **kwargs):
    '''
    See prepare_update().
    Calls prepare_update() and converts the iterable into a 1D numpy array
    of booleans.
    '''

    return numpy.array(tuple(prepare_update(*args, **kwargs)), dtype=bool)

def evolve(steps, state, *args, **kwargs):
    '''
    Calls update() with steps iterations or until the state loops.
    Returns a 2D array with increasing rows over time.
    '''

    l = len(state)
    state_history = numpy.zeros( (steps, l), dtype=bool )
 
    # track all previous states
    previous_states = set()

    for s in range(0,steps):
        state_history[s,:] = state
        previous_states.add(tuple(state_history[s,:]))
        state = update(state, *args, **kwargs)
        # once stationary, always stationary. cut the execution
        if (tuple(state) in previous_states): break
    state_history[s,:] = state
    s = s + 1

    # plot the result
    pyplot.imshow(state_history[0:s,:], interpolation='none', cmap=cm.gray, aspect=l/float(s))
    pyplot.tick_params(axis='both', which='both', length=0, width=0, labelbottom='off', labeltop='off', labelleft='off', labelright='off')
    if s == steps:
        pyplot.title('Truncated at ' + str(s) + ' steps.')
    else:
        pyplot.title('Completed after ' + str(s) + ' steps.')
    pyplot.ylabel('< iterations')
    pyplot.xlabel('state')
    pyplot.show()

    # return only the calculated rows
    return state_history[0:s, :]
