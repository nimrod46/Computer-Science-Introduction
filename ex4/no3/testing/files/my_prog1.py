# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 14:58:15 2021

@author: dani
"""
from myAes import *
import os

def encrypt():
    filename = input("Enter file name: ")
    key = os.urandom(16)
    iv = os.urandom(16)

    ifile, ofile = filename, filename[:filename.find(".")] + "_enc"+ filename[filename.find("."):]
    with open(ifile,"rb") as reader:
        with open(ofile,"wb+") as writer:
            data = reader.read()
            header, body = data[:54], data[54:]
            aesObject = myAes(key,"ECB",iv)
            writer.write(header + iv + aesObject.encrypt(data))
    with open("key.dat", "wb+") as writer:
        writer.write(key)

def decrypt():
    filename = input("Enter file name: ")
    with open("key.dat", "rb") as reader:
        key = reader.read()

    ifile, ofile = filename, filename[:filename.find("_enc")] + "_dec"+ filename[filename.find("."):]
    with open(ifile,"rb") as reader:
        with open(ofile,"wb+") as writer:
            data = reader.read()
            header, iv, body = data[:54], data[54:70], data[70:]
            aesObject = myAes(key,"ECB",iv)
            writer.write(header + aesObject.decrypt(body))
                
encrypt()            