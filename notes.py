###################### CRETING LOG FILE ##################
# creating log files for the code
import logging
from os import times
logging.basicConfig(filename='example.log',level=logging.INFO)

def fnCall():
    # do something in the fn
    logging.info(
        # do what we want to print in the file
        'function ran {}'.format(__name__))

################### GENERATORS ##########################
# 1.. throws a single value at a times, memory and space optimized
# 2.. in list comprehension use a = () instead of a = []
import time
import random
import memory_profiler

names = ['Naruto', 'Jiraya', 'Sasuke', 'Tsunade','Hinata']
discipline = ['clone jutsu', 'sage jutsu', 'byakugan','regeneration jutsu', 'sharingan']
print("memory before {}".format(memory_profiler.memory_usage()))
def listGenerator(size ):
    ninjas = []
    for i in range(size):
        ninja = {
            'id': i,
            'name': random.choice(names),
            'discipline': random.choice(discipline)
        }
        ninjas.append(ninja)
    return ninjas

def genGenerator(size ):
    ninjas = []
    for i in range(size):
        ninja = {
            'id': i,
            'name': random.choice(names),
            'discipline': random.choice(discipline)
        }
        ninjas.append(ninja)
    yield ninjas
    
t1 = time.perf_counter()
newNinjas = genGenerator(100000)
t2 = time.perf_counter()
t = t2-t1
print("time taken {}".format(t))
print("memory after {}".format(memory_profiler.memory_usage()))

################################ THREADING ###########################
# 1.. various modules available in python for theading, threadin,concurrent.futures,asyncio

########################### LAMBDA FUNCTIONS ############################

# al = lambda x, y: x if x>y else y
# print(al(2,3))

########################## is keyword ###################################
# l1 = [1,2,3]
# l2 = [1,2,3]

# l1 == l2 // True
# l1 is l2 // False