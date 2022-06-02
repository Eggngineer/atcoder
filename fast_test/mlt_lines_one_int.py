from time import time

def solve():
    A = [int(input().rstrip('\n')) for _ in range()]

if __name__ == '__main__':
    start = time()
    solve()
    process_time = time() - start

    print(process_time)