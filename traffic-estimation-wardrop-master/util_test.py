'''
Created on Jul 16, 2014

@author: jeromethai
'''

import util
from cvxopt import matrix, spmatrix, solvers
import draw_graph as d
import numpy as np
from multiprocessing import Pool
import time


def test1(x):
    """Test bisection"""
    def F(x):
        return 1 + 0.15*(x**4)
    return util.bisection(F, x, 0.0, 5.0)


def test2():
    """Test save_mat"""
    Ms = [matrix(1.0, (3,2)), spmatrix(1.0, range(3), range(3))]
    names = ['M1', 'M2']
    util.save_mat(Ms, names, 'test')


def test3():
    """Test multiprocessing"""
    start = time.clock()
    pool = Pool(processes=4)
    list = np.linspace(1.0,4.0,2001)
    print pool.map(test1, list)
    t1 = time.clock() - start
    start = time.clock()
    print [test1(x) for x in list]
    t2 = time.clock() - start
    print t1, t2
    
    
def test4(b):
    """Test cvxopt and provide a function using cvxopt package for test6"""
    A = matrix([ [-1.0, -1.0, 0.0, 1.0], [1.0, -1.0, -1.0, -2.0] ])
    c = matrix([ 2.0, 1.0 ])
    sol=solvers.lp(c,A,b)
    return sol['x']
    

def test5():
    """Test cvxopt together with multiprocessing on Python, this works!"""
    b = matrix([ 1.0, -2.0, 0.0, 4.0 ])
    pool = Pool(processes=4)
    print pool.map(test4, [0.5*b, 1.0*b, 1.5*b, 2.0*b])


def test6():
    """Test distance_on_unit_sphere()"""
    arc = util.distance_on_unit_sphere(34.049240, -118.238456, 34.073238, -118.284118)
    print 'distance in miles', 3960.0*arc
    print 'distance in km', 6373.0*arc


def main():
    #print test1(4.0)
    #test2()
    #test3()
    #test3()
    #return test4(matrix([ 1.0, -2.0, 0.0, 4.0 ]))
   # test5()
   test6()


if __name__ == '__main__':
    main()