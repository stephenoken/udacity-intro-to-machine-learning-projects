""" quiz materials for feature scaling clustering """

# FYI, the most straightforward implementation might
# throw a divide-by-zero error, if the min and max
# values are the same
# but think about this for a second--that means that every
# data point has the same value for that feature!
# why would you rescale it?  Or even use it at all?

from __future__ import division


data = [115, 140, 175]


def featureScaling(arr):
    x_max = max(*arr)
    x_min = min(*arr)
    if (x_max == x_min):
        return None
    return map(lambda x: (x - x_min)/(x_max - x_min), arr)

# tests of your feature scaler--line below is input data


print featureScaling(data)
