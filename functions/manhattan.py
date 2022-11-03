def manhattan1(v1: list, v2: list):
    return abs(v1[0]-v2[0])+abs(v1[1]-v2[1])

def myabs(v: int or float):
    return v if v >=0 else -v

def main():
    v1,v2 = [1,2],[3,1]
    from time import time as t
    s = t()
    manhattan1(v1,v2)

