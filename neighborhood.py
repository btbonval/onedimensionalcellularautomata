'''
Neighborhood functions are defined herein.

Each neighborhood function will accept a total array length and an index for
the neighborhood's center.

Each neighborhood function will return a list of indices.
'''

import numpy

class nx_generator(object):
    '''
    Generates a function which takes in index i and returns the neighborhood
    specified by x neighbors on either side with wrapping around edges as
    True or False. The generator needs to know the size of the automata (l) for
    wrapping purposes.

    The bound selector() function for some instantiated nx_generator object may
    be passed into the automata update as a neighborhood function.

    If the constructor is called without l, it must be specified by set_length()
    prior to calling selector().

    To create an object which has a neighborhood of 1 (center, left and
    right) that does not wrap around edges:
    n1_nowrap = nx_generator(1, False)
    '''
    def __init__(self, x, wrap, l = None):
        '''
        Creates an object which calculates the simple neighborhood of x (on
        either side of some center), and specifies whether the left and right
        bounds wrap around the array or terminate.
        Optionally specify automata size / array length l. This must be
        specified prior to calling selector().
        '''
        self.x = x
        self.wrap = wrap
        if l is not None:
            self.set_length(l)

    def __call__(self, *args, **kwargs):
        '''
        Alias for self.selector()
        '''
        return self.selector(*args, **kwargs)

    def set_length(self, l):
        '''
        Change the internal automata size / array length registered for
        calculating the neighborhood function.
        '''
        self.l = l

    def selector(self, i):
        '''
        Returns a selection array for the neighborhood around index i.
        '''
        if self.l is None:
            raise TypeError('Automata size / array length l must be set with set_length().')
        return nx(self.x, self.l, i, self.wrap)

def nx(x, l, i, wrap):
    '''
    Given a neighborhood of x and total length l,
    return a list of indices that will select the neighborhood.
    Wrap is logically true if neighorhoods may wrap around the edges of
    the array bounds.
    '''
    if (x > (l-1)/2):
        # neighborhood is larger than the state space
        raise TypeError('neighborhood exceeds state space')

    # determine the index bounds which should be selected
    a = i - x
    b = i + x + 1 # + 1 because slices are semi-closed

    # ensure indices do not wrap around bounds
    if not wrap and a < 0:
        a = 0
    if not wrap and b > l:
        b = l

    # create a range of indices that go negative to end.
    # negative indices automatically wrap to the right boundary.
    # the modulus maps indices that are too large wrap around the left boundary.
    return numpy.arange(a,b) % l
