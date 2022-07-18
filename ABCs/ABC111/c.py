from ctypes import c_short
from distutils.command.clean import clean
import sys
import numpy as np
from collections import Counter
input = sys.stdin.readline

n = int(input().rstrip('\n'))
v = list(map(int, input().rstrip('\n').split()))

m = len(v)//2

odd,even = v[0::2],v[1::2]
c_odd, c_even = [(key,val) for key, val in Counter(odd).items()],[(key,val) for key, val in Counter(even).items()]

c_odd.sort(key=lambda x: x[1], reverse=True)
c_even.sort(key=lambda x: x[1], reverse=True)

c_odd.append((0,0))
c_even.append((0,0))

if c_odd[0][0] != c_even[0][0]:
    result = n - c_odd[0][1] - c_even[0][1]
    print(result)
else:
    result = n - max(c_odd[0][1]+c_even[1][1], c_odd[1][1]+c_even[0][1])
    print(result)