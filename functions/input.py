#------------------------------------------------------------------
#                            NUMBER
#------------------------------------------------------------------

"""
Nomally Input
"""

# input : N(int)
# one integer
N = int(input())

# input : N(int) M(int)
# as each vars
N, M = map(int, input().split())

# input : A(int, ..., int)
# as a list of vars
A = list(map(int, input().split()))

# input : A[[int, ..., int], ... ,[int, ..., int]] (NxM)
N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(M)]

"""
Fast Input
"""
import sys
input = sys.stdin.readline

# one integer
N = int(input().rstrip('\n'))

# mlt integer as mlt var
N, M = int(input().rstrip('\n').split())

# mlt integer as a list
A = list(map(int, input().rstrip('\n').split()))

# mlt col one integer as a list
A = [int(input().rstrip('\n')) for _ in range()]

# mlt col mlt integer as a 2-dim list
A = [list(map(int, input().rstrip('\n').split())) for _ in range()]


#------------------------------------------------------------------
#                           CHARACTER
#------------------------------------------------------------------

"""
Nomally Input
"""

# input : N(int)
# one integer
N = str(input())

# input : N(int) M(int)
# as each vars
N, M = map(str, input().split())

# input : A(int, ..., int)
# as a list of vars
A = list(map(str, input().split()))

# input : A[[int, ..., int], ... ,[int, ..., int]] (NxM)
N, M = map(str, input().split())
A = [list(map(str, input().split())) for i in range(M)]

"""
Fast Input
"""
import sys
input = sys.stdin.readline

# one integer
N = str(input().rstrip('\n'))

# mlt integer as mlt var
N, M = str(input().rstrip('\n').split())

# mlt integer as a list 
A = list(map(str, input().rstrip('\n').split()))

# mlt col one integer as a list
A = [str(input().rstrip('\n')) for _ in range()]

# mlt col mlt integer as a 2-dim list
A = [list(map(str, input().rstrip('\n').split())) for _ in range()]
