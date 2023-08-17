import time
import logging
import multiprocessing
from math import factorial

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def find_factorial(arg):
    return factorial(arg)

def async_apply(processes):
    pool = multiprocessing.Pool(processes)
    start = time.time()
    input_val = 100000
    res = pool.apply_async(find_factorial, (input_val,))
    pool.close()
    pool.join()
    end = time.time()
    logger.info(f'Time taken is {end - start}')


if __name__ == "__main__":
    print('2 proc')
    async_apply(processes=2)
    print('3 proc')
    async_apply(processes=3)
    print('4 proc')
    async_apply(processes=4)
    print('5 proc')
    async_apply(processes=5)
    print('6 proc')
    async_apply(processes=6)




