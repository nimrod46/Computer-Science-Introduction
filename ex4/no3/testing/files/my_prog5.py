# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 17:49:24 2021

@author: dani
"""

def some_func(s, b):
    """ True is a python word """
    if b==True:
        return s
    else:
        return s[::-1] # s backwords without a for loop
    
def some_other_func(n,k):
    """ This function has if, else, and return """
    if n%k==0:return True;
    else:return(False)
    
def super_func(lst,n):
    """ it is True that this function does nothing """
    for a in(lst): #this is a for loop with the word in in it
        if a==n:return(True)
    return(False)

def main():
    """ The main thing is to be True to yourself """
    print(some_func("False True if else return in for", False))
    print(some_other_func(20, 7))
    print(super_func([2,3,5,7,11,13], 17))
    
if __name__=='__main__':
    main()