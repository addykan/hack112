#################################################
# hw10.py
#
# Your name: Michael Crotty
# Your andrew id: mcrotty
#################################################
import math
import cs112_f20_week10_linter
#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Functions for you to write
#################################################

def hasAdjacentValues(L): # Total runtime: 2n + 2 = O(n)
    setL = set(L)                           # O(n)
    for v in setL:                          # O(n)
        if (v + 1) in setL: return True     # O(1)
        if (v - 1) in setL: return True     # O(1)
    return False

def hasTriplicate(L): # Total runtime: 2n + 3 = O(n)
    d = dict()                              # O(1)
    for i in L:                             # O(n)
        d[i] = d.get(i, 0) + 1              # O(1)
    for key in d:                           # O(n)
        if d[key] >= 3: return True         # O(1)
    return False

def boxesAnInteger(L): # Total runtime: nlogn + n + 2 = O(nlogn)
    L.sort()                                                          # O(nlogn)
    for i in range(1, len(L)):                                        # O(n)
        if (L[i] % 1 == 0.0) or (L[i - 1] % 1 == 0.0): pass           # O(1)
        elif (math.ceil(L[i - 1]) == math.floor(L[i])): return True   # O(1)
    return False

def test(x):
    return x/0

#################################################
# Test Functions
#################################################

def testHasAdjacentValues():
    print('Testing hasAdjancentValues()...', end='')
    assert(hasAdjacentValues([1,5,8,2]) == True)
    assert(hasAdjacentValues([1,5,8,0]) == True)
    assert(hasAdjacentValues([1,5,8,4]) == True)
    assert(hasAdjacentValues([1,5,8,6]) == True)
    assert(hasAdjacentValues([1,5,8,3]) == False)
    assert(hasAdjacentValues([1,5,8,-5]) == False)
    assert(hasAdjacentValues([ ]) == False)
    assert(hasAdjacentValues([2,0,-2]) == False)
    assert(hasAdjacentValues([1,-1,2,0]) == True)
    assert(hasAdjacentValues([-15,16,19,-21,0]) == False)
    assert(hasAdjacentValues([-15,16,-16,-21,0]) == True)
    print('Passed! (pending O() check)')

def testHasTriplicate():
    print('Testing hasTriplicate()...', end='')
    assert(hasTriplicate([ 1, 1, 1 ]) == True)
    assert(hasTriplicate(list(range(10))*3 ) == True)
    assert(hasTriplicate([ ]) == False)
    assert(hasTriplicate(list(range(100))*2) == False)
    assert(hasTriplicate([ 1, 2, 3 ]) == False)
    assert(hasTriplicate([ 1, 2, 3, 1 ]) == False)
    assert(hasTriplicate([1, 5, 1, 1, 2]) == True)
    assert(hasTriplicate([-3, -2, 1, -2, -2, 3]) == True)
    assert(hasTriplicate([-3, -2, 1, -2, 2, -3]) == False)
    assert(hasTriplicate(list(range(-1000, 1000))) == False)
    assert(hasTriplicate(list(set([1, 5, 1, 1, 2]))) == False)
    assert(hasTriplicate(list("Axolotls")) == False)
    assert(hasTriplicate(list("mushroom soup")) == True)
    assert(hasTriplicate(list("Bumfuzzle Cattywampus Gardyloo")) == True)
    print('Passed! (pending O() check)')

def testBoxesAnInteger():
    print('Testing boxesAnInteger()...', end='')
    assert(boxesAnInteger([ 2.3, 9.4, 1.7 ]) == True)
    assert(boxesAnInteger([ 2.3, 9.4, 0.7 ]) == False)
    assert(boxesAnInteger([ 2.0, 9.4, 1.7 ]) == False)
    assert(boxesAnInteger([ ]) == False)
    assert(boxesAnInteger([ 15.0, 15.0 ]) == False)
    assert(boxesAnInteger([ 0.0, 2.1, 3.5, 14.8 ]) == True)
    assert(boxesAnInteger([ 2.1, 0.0, 0.9, 15.2, 13.66 ]) == False)
    print('Passed! (pending O() check)')

#################################################
# testAll and main
#################################################

def testAll():
    testHasAdjacentValues()
    testHasTriplicate()
    testBoxesAnInteger()
    test(5)
    #assert(1 == 2)

def main():
    cs112_f20_week10_linter.lint()
    testAll()

if __name__ == '__main__':
    main()