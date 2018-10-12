#!/usr/bin/env python

import multiprocessing
from multiprocessing import Manager

manager = Manager()

### when creating objects to be used in function, must use manager.type()
globalList = manager.list([])

### define function
def multifunc(str):
    globalList.append(str)
    return

pool = multiprocessing.Pool(processes=9)     ### define number of processes to run in pool object
pool.map(multifunc, list_of_values_to_iterate_through)     ### run function on each list item
pool.close()     ### close pool
pool.join()     ### join all pool processes

### print new list
print(globalList)
