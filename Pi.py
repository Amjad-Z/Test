import random as r
import math as m
from joblib import Parallel, delayed 

def pi_parallel(total):
 # Number of darts that land inside.
 inside = 0
 
 # Iterate for the number of darts.
 for i in range(0, total):
   # Generate random x, y in [0, 1].
   x2 = r.random()**2
   y2 = r.random()**2
    # Increment if inside unit circle.
   if m.sqrt(x2 + y2) < 1.0:
	 inside += 1

 # inside / total = pi / 4
 pi = (float(inside) / total) * 4
 
 # It works!
 #return(pi)
 print(pi)
#print(pi_parallel())


if __name__ == "__main__":
 Parallel(n_jobs=2)(delayed(pi_parallel)(10000) for i in range(2))
 #parallel()(delayed(pi_parallel)() for i in range(5))
