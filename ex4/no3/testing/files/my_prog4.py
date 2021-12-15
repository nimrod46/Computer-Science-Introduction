# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 13:05:28 2021

@author: dani
"""


def mult_by_2(num):
    if num >> 7 == 0:
        return num<<1
    return (num<<1)^256^27 # 256 cancels the leading 1
    
def aes_product(x,y):
    if x<0 or y<0 or x>255 or y>255:
        raise ValueError("arguments to aes_product must be in Z_256")
    if y==0:
        return 0
    if y%2 == 1:
        return x^aes_product(x,y-1)
    return(aes_product(mult_by_2(x),y>>1))

def AES_inverse(n):
    if n==0: 
        return 0
    for i in range(256):
        if aes_product(n,i)==1:
            return i
    return 0

