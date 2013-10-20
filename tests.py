'''
Some integration tests. Unit tests span multiple infinites, so it is more
practical in this instance to simply build out a few expected cases and ensure
they continue to work as expected.

Written with nose tests in mind.
'''

import numpy
import rules
import utils
import update
import neighborhood

n1_wrap = neighborhood.nx_generator(1, True)

def i2a(integer, width):
    return numpy.array(utils.i2bt(integer, width), dtype=bool)

class testWolfram30(object):
    '''
    Test that wolfram rule 30 resolves correctly for some arbitrarily chosen
    cases.
    '''

    update_cases = {
        (14, 4): (8, 4),
        (617, 10): (463, 10),
        (945531, 20): (117058, 20),
    }

    evolve_cases = {
        (3, 4, 0): (14, 4),
        (3, 4, 10): (14, 4),
        (3, 4, 9): (4, 4),
    }

    def testUpdate(self):
        for inp, outp in self.update_cases.iteritems():
            # convert integers into boolean arrays
            inp_arr = i2a(*inp)
            outp_arr = i2a(*outp)
            # run the input array
            test_out = update.update(inp_arr, n1_wrap, rules.wolfram(30))
            # compare to the output array
            assert(numpy.all(test_out == outp_arr))

    def testEvolve(self):
        for inp, outp in self.evolve_cases.iteritems():
            # convert integers into boolean arrays
            inp_arr = i2a(*inp[:2])
            outp_arr = i2a(*outp)
            # run the input array
            test_out = update.evolve(inp[2], inp_arr, n1_wrap, rules.wolfram(30), plot=False)
            # compare to the output array
            assert(numpy.all(test_out[-1,:] == outp_arr))
