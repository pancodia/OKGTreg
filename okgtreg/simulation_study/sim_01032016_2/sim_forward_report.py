__author__ = 'panc'

import pickle
from okgtreg.simulation.sim_01032016_2.utility import *

pklfile = open('okgtreg/simulation/sim_01032016_2/sim_forward.py.pkl', 'rb')
groups, r2s = pickle.load(pklfile)
pklfile.close()

np.mean(r2s)

printGroupingFrequency(groups)
"""
The following grouping frequencies shows that the forward procedure finds
some univariate transformations are most often. This is against the true
model. However, some true bivariate groups are also recovered among the
top ranked groups. The majority of the groupings are either univariate or
bivariate, which is not too far away from the true model.

However, the true group structures are not detected as most frequent in the
simulation. This makes the methods not very satisfactory.

(5,) : 60
(1,) : 56
(3,) : 53
(9,) : 52
(3, 4) : 46
(1, 2) : 43
(9, 10) : 41
(8,) : 31
(5, 6) : 30
(6, 7) : 17
(7, 8) : 16
(6,) : 16
(7, 10) : 15
(4, 7) : 14
(2, 7) : 11
(6, 8) : 10
(2, 8) : 9
(10,) : 9
(4,) : 9
(4, 8) : 8
(8, 10) : 8
(2, 5) : 6
(4, 6, 8) : 5
(6, 7, 10) : 5
(2,) : 5
(2, 9) : 4
(2, 4, 7) : 4
(2, 7, 10) : 4
(6, 10) : 3
(7,) : 3
(2, 8, 10) : 3
(2, 4, 8) : 3
(6, 9) : 2
(2, 4, 7, 10) : 2
(2, 6) : 2
(6, 8, 10) : 2
(4, 7, 10) : 2
(4, 5) : 2
(4, 6, 7, 10) : 2
(5, 10) : 2
(4, 6, 7) : 2
(2, 6, 8) : 1
(1, 6) : 1
(2, 6, 7) : 1
(8, 9) : 1
(4, 10) : 1
(2, 7, 8) : 1
(6, 7, 8) : 1
(2, 10) : 1
(3, 8) : 1
"""

printGroupFrequency(groups)
"""
([1, 2], [3, 4], [5], [6, 7], [8], [9, 10]) : 6
([1, 2], [3, 4], [5, 6], [7, 8], [9, 10]) : 5
([1], [2, 8], [3, 4], [5], [6, 7], [9, 10]) : 4
([1, 2], [3, 4], [5, 6], [7, 10], [8], [9]) : 3
([1], [2, 5], [3, 4], [6], [7, 8], [9, 10]) : 3
([1], [2, 4, 8], [3], [5], [6, 7, 10], [9]) : 2
([1], [2, 7], [3, 4], [5, 6], [8], [9, 10]) : 2
([1, 2], [3], [4, 7], [5], [6, 8, 10], [9]) : 2
([1], [2, 7], [3, 4], [5, 6], [8, 10], [9]) : 2
([1, 2], [3], [4, 6, 8], [5], [7, 10], [9]) : 2
([1], [2, 7, 10], [3, 4], [5], [6, 8], [9]) : 2
([1], [2, 9], [3, 4], [5, 6], [7, 8], [10]) : 2
([1, 2], [3], [4, 6, 7, 10], [5], [8], [9]) : 2
([1], [2, 8, 10], [3], [4, 7], [5, 6], [9]) : 2
([1], [2, 7, 10], [3], [4, 6, 8], [5], [9]) : 2
([1, 2], [3, 4], [5], [6, 7, 10], [8], [9]) : 2
([1], [2, 5], [3, 4], [6], [7, 10], [8], [9]) : 2
([1, 2], [3], [4, 7], [5, 6], [8], [9, 10]) : 2
([1, 2], [3], [4, 8], [5], [6, 7], [9, 10]) : 2
([1, 2], [3], [4, 7], [5], [6, 8], [9, 10]) : 2
([1, 2], [3], [4, 6, 7], [5], [8], [9, 10]) : 1
([1], [2], [3], [4, 6, 8], [5], [7, 10], [9]) : 1
([1], [2, 4, 7], [3], [5, 6], [8], [9], [10]) : 1
([1, 2], [3, 4], [5, 6], [7], [8, 9], [10]) : 1
([1], [2, 7, 8], [3], [4, 5], [6], [9, 10]) : 1
([1], [2, 8], [3], [4, 7], [5, 10], [6], [9]) : 1
([1, 2], [3, 8], [4], [5, 6], [7], [9, 10]) : 1
([1], [2, 7], [3, 4], [5], [6], [8], [9, 10]) : 1
([1], [2, 4, 7], [3], [5], [6, 8], [9], [10]) : 1
([1, 2], [3], [4, 8], [5, 6], [7, 10], [9]) : 1
([1], [2, 4, 8], [3], [5], [6], [7, 10], [9]) : 1
([1], [2, 4, 7, 10], [3], [5, 6], [8], [9]) : 1
([1, 2], [3], [4, 5], [6], [7, 8], [9, 10]) : 1
([1], [2, 4, 7], [3], [5], [6, 8], [9, 10]) : 1
([1], [2], [3], [4, 8], [5], [6, 7], [9, 10]) : 1
([1], [2, 10], [3], [4], [5], [6, 7], [8], [9]) : 1
([1, 2], [3, 4], [5], [6], [7, 10], [8], [9]) : 1
([1, 2], [3], [4], [5], [6, 8], [7, 10], [9]) : 1
([1], [2, 4, 7], [3], [5, 6], [8, 10], [9]) : 1
([1], [2, 6, 7], [3], [4], [5], [8], [9, 10]) : 1
([1, 6], [2], [3], [4, 7], [5], [8], [9, 10]) : 1
([1], [2, 6, 8], [3, 4], [5], [7, 10], [9]) : 1
([1, 2], [3, 4], [5], [6, 7], [8, 10], [9]) : 1
([1], [2, 4, 7, 10], [3], [5], [6, 8], [9]) : 1
([1], [2, 6], [3, 4], [5], [7, 8], [9, 10]) : 1
([1], [2, 8], [3, 4], [5, 6], [7], [9, 10]) : 1
([1], [2, 8], [3], [4, 7, 10], [5], [6, 9]) : 1
([1, 2], [3], [4], [5], [6, 9], [7, 8], [10]) : 1
([1, 2], [3], [4, 7], [5], [6, 10], [8], [9]) : 1
([1], [2], [3, 4], [5], [6, 7], [8, 10], [9]) : 1
([1], [2, 7], [3], [4], [5, 6], [8], [9, 10]) : 1
([1], [2, 7], [3, 4], [5, 10], [6], [8], [9]) : 1
([1], [2, 8], [3], [4], [5, 6], [7, 10], [9]) : 1
([1], [2, 9], [3], [4, 8], [5], [6, 7], [10]) : 1
([1], [2, 7], [3], [4, 8], [5, 6], [9, 10]) : 1
([1, 2], [3], [4, 6, 7], [5], [8, 10], [9]) : 1
([1, 2], [3], [4, 10], [5], [6, 7, 8], [9]) : 1
([1], [2, 8], [3], [4, 7, 10], [5, 6], [9]) : 1
([1], [2, 6], [3], [4, 8], [5], [7, 10], [9]) : 1
([1, 2], [3, 4], [5], [6], [7, 8], [9, 10]) : 1
([1], [2, 7], [3], [4], [5, 6], [8, 10], [9]) : 1
([1], [2, 5], [3, 4], [6], [7, 8], [9], [10]) : 1
([1], [2], [3], [4, 8], [5], [6, 7, 10], [9]) : 1
([1], [2, 9], [3], [4, 7], [5], [6, 10], [8]) : 1
([1], [2, 7], [3, 4], [5], [6, 8], [9], [10]) : 1
([1], [2, 8, 10], [3], [4, 7], [5], [6], [9]) : 1
([1], [2, 7], [3, 4], [5], [6, 8], [9, 10]) : 1
([1, 2], [3], [4, 7], [5], [6], [8, 10], [9]) : 1
([1, 2], [3], [4], [5], [6, 10], [7, 8], [9]) : 1
"""
