import numpy as np

array = np.arange(100)

def testfunc_duplicate(vals):
  for i in vals:
    vals[i] = vals[i]*2
    
  return vals

testfunc_duplicate(array)
