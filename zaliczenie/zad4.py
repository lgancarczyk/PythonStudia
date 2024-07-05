import multiprocessing

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_twin_primes(start, end):
    twin_primes = []
    prev_prime = None

    for num in range(start, end):
        if is_prime(num):
            if prev_prime and num - prev_prime == 2:
                twin_primes.append((prev_prime, num))
            prev_prime = num
    
    return twin_primes

def worker(start, end, queue):
    result = find_twin_primes(start, end)
    queue.put(result)

def main():
    range_start = 1
    range_end = 100000
    num_processes = 4
    chunk_size = (range_end - range_start) // num_processes
    queue = multiprocessing.Queue()
    processes = []

    for i in range(num_processes):
        start = range_start + i * chunk_size
        end = start + chunk_size if i < num_processes - 1 else range_end
        process = multiprocessing.Process(target=worker, args=(start, end, queue))
        processes.append(process)
        process.start()

    twin_primes = []
    for _ in processes:
        twin_primes.extend(queue.get())

    for process in processes:
        process.join()

    print("Twin primes in the range:", twin_primes)

if __name__ == "__main__":
    main()
