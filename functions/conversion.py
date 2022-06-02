import numpy as np

def fromN_to10(num_rad_N, N):
    """ N進数値 => 10進数値
    Attributes:
        num_rad_N (str) : N進数値の文字列
        N (int): 変換元の基数値
    Tips:
        アルファベットと数字の混合IDを扱うときに10進数値に変換して扱うと簡単(N<=>10)
    """
    if type(num_rad_N) != str():
        num_rad_N = str(num_rad_N)
    ret = int(num_rad_N, N)

    return ret

def from10_toN(num_rad_10, N):
    """ 10進数値 => N進数値
    Attributes:
        num_rad_10 (int) => 変換元の10進数値
        N (int) => 変換先の基数
    Tips:
        アルファベットと数字の混合IDを扱うときに10進数値に変換して扱うと簡単(10<=>N)
    """
    return np.base_repr(num_rad_10, N)

