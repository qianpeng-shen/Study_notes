from multiprocessing import Pool
import time
def fun(fn):
    time.sleep(1)
    return fn*fn
test=[1,2,3,4,5,6]
pool=Pool(processes=4)
r=pool.map(fun,test)
pool.close()
pool.join()
print(r)