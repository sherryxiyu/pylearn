import multiprocessing as mp

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
    print(n**100)

def run_pool(nums):
    pool = mp.Pool(4)
    pool.map(worker, nums)
    pool.close()
    pool.join()

if __name__ == "__main__":
    nums = [2, 3, 4]
    # run_func(nums)
    run_pool(nums)