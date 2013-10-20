import numpy

def binary_tuple_to_integer(bintuple):
    '''
    Convert a tuple of all T/F values or all 1/0 values into a decimal number.
    index 0 is the MSB, index N is the LSB for a tuple of length N.
    returns an integer.
    '''
    # inner product of 1/0 array against decreasing powers of two
    return numpy.sum((1 << numpy.arange(len(bintuple)-1,-1,-1)) * bintuple)
# shorter name
bt2i = binary_tuple_to_integer

def integer_to_binary_tuple(integer, width=0):
    '''
    Convert an integer into a tuple of all T/F values.
    index 0 is the LSB, index N is the MSB for a tuple of length N.
    width specifies a padding width; if the tuple has fewer values than this,
    it will be zero padded on the left side (MSB).
    returns a tuple of boolean values.
    '''
    # convert int to binary string: 2 => '0b10'
    # convert list of strings to list of integers: '10' => ['1','0'] => [1,0]
    # tuplize: [1,0] => (1,0)
    r = tuple(map(int, bin(integer)[2:]))
    l = len(r)
    if l < width:
        # slooow padding. 
        for i in range(0, width-l):
            r = (0,) + r
        # numpy might be faster, but requires tuple => array => tuple conv.
        # r = tuple(numpy.concatenate((numpy.zeros(width-l), r)))
    return r
# shorter name
i2bt = integer_to_binary_tuple
