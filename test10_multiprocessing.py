import multiprocessing as mp
import time


def cellfunc(q, n):
    q.put(n**100)

def run_func(nums):
    q = mp.Queue()
    for item in nums:
        p = mp.Process(target=cellfunc, args=(q, item))
        p.start()
    res = 0
    for _ in range(len(nums)):
        res += q.get()
    print(res)

def worker(n):
    print(time.time())
    return n**100

def run_pool(nums):
    pool = mp.Pool(4)
    pool.map(worker, nums)
    pool.close()
    pool.join()

def gen_lists(nums):
    with mp.Pool(processes=8) as pool:
        p = pool.starmap(worker, [item for item in nums])
        print(p)
    return p

if __name__ == "__main__":
    # nums = [2, 3, 4]
    # run_func(nums)
    # run_pool(nums)
    nums = [(3,), (4,)]
    gen_lists(nums)