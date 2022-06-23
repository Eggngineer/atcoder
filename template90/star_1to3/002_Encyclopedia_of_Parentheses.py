"""
ABC190:C Bowls and Dishes
ABC197:C ORXOR
ABC064:D Intersection
"""

import sys
input = sys.stdin.readline

def check(txt):
    score=0
    for x in txt:
        if x =="(":
            score+=1
        else:
            score-=1
        if score<0:
            return False
    if score==0:
        return True

def bit_all_search(N):
    for bit in range(2**N):
        ret = ""
        for i in range(N)[::-1]:
            if 2**i&bit == 0:
                ret+="("
            else:
                ret+=")"
        if check(ret):
            print(ret)

def main1():
    """
    Bit All Search
    """
    N = int(input().rstrip('\n'))
    if N%2==1:
        print("")
    else:
        bit_all_search(N)




def main2():
    """
    Recursion
    """
    N = int(input().rstrip('\n'))
    if N%2==0:
        rec_print_bracket("",N//2,0)
    else:
        print("")


def rec_print_bracket(txt,left,right):
    if left == right == 0:
        print(txt)
    else:
        if left > 0:
            rec_print_bracket(txt+"(",left-1,right+1)
        if right > 0:
            rec_print_bracket(txt+")",left,right-1)


if __name__=='__main__':
    """
    bit
    """
    # main1()

    
    """
    recursion
    """
    main2()