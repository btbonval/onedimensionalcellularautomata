'''
Example rules are defined herein. Rules are generally meant to be defined by
the user.
'''

from itertools import starmap, repeat, izip
from utils import i2bt, bt2i

# Generate Wolfram's rules for neighborhood 1 automata
def wolfram(rulenum):
    '''
    Wolfram's numbering system refers to the ordered arrangement of all
    possible neighborhoods. Neighborhood 1 has 3 elements (left, center, right),
    which could present as 8 possible values: 000, 001, 010, ... 111.
    Each of the 8 neighborhoods is mapped to a 1 or 0. These mappings are put
    together, in order, as a binary like 01101110 for 000 => 0, 001 => 1, ..
    111 => 0, which would be passed in as decimal 110 (Wolfram's rule 110).
    Supply an integer which represents the mapping string.
    '''

    # for a verbose version of rules 110 and 8, see versions of this file
    # starting at commit 0f423902b5600c311f417316bee595e2bc3a85cf or earlier

    width = 3
    image = i2bt(rulenum, 2**width)[::-1]
    # for 0 to 8, run i2bt(0, width) to i2bt(8, width)
    preimage = starmap(i2bt, izip(range(0,2**width), repeat(width)))
    # line up the preimages with the images and make it a dict/hashmap
    return dict(izip(preimage, image))
