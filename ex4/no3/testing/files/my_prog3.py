# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 08:27:32 2021

@author: dani
"""
from my3Des import *
from myAes import *
from timeit import default_timer
import os
import sys

def main():
    filename = input("Enter file name to encrypt: ")
    key = os.urandom(16)
    iv = os.urandom(16)
    with open(filename, "rb") as reader:
        body = reader.read()
        with open("des3_ciphertext", "wb") as writer:
            desObject = my3Des(key[:8],"CBC",iv[:8])
            t1 = default_timer()
            ciphertext = desObject.encrypt(body)
            t2 = default_timer()
            writer.write((iv + ciphertext))
            print(f"time for triple des: {t2-t1:.3e}")
        with open("aes_ciphertext", "wb") as writer:
            aesObject = myAes(key,"CBC",iv)
            t1 = default_timer()
            ciphertext = aesObject.encrypt(body)
            t2 = default_timer()
            writer.write((iv + ciphertext))
            print(f"time for aes: {t2-t1:.3e}")

main()