import scipy.interpolate
import numpy


def createLookupArray(func, length=256):
    """Return a lookup for whole-number inputs to a function.

    The lookup values are clamped to [0, length - 1].

    """
    if func is None:
        return None
    lookupArray = numpy.empty(length)
    i = 0
    while i < length:
        func_i = func(i)
        lookupArray[i] = min(max(0, func_i), length - 1)
        i += 1
    return lookupArray


def createCompositeFunc(outer, inner):
    """Return a composite of two functions."""
    if outer is None:
        return inner
    if inner is None:
        return outer
    return lambda x: outer(inner(x))


def applyLookupArray(lookupArray, src, dst):
    """Map a source to a destination using a lookup."""
    if lookupArray is None:
        return
    dst[:] = lookupArray[src]


def createCurveFunc(points):
    """Return a function derived from control points."""
    if points is None:
        return None
    numPoints = len(points)
    if numPoints < 2:
        return None
    xs, ys = zip(*points)
    if numPoints < 3:
        kind = 'linear'
    elif numPoints < 4:
        kind = 'quadratic'
    else:
        kind = 'cubic'
    # 好像是插值哦。
    # 从两个（或几个）值能创建一个插值吗？
    return scipy.interpolate.interp1d(xs, ys, kind,
                                      bounds_error=False)