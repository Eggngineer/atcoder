from time import time

def solve():
    A = list(map(int, input().rstrip('\n').split()))

if __name__ == '__main__':
    start = time()
    solve()
    process_time = time() - start

    print(process_time)