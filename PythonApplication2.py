from sys import argv
import numpy as np
script, first, second, third = argv

#first la so 0 hoac 1
if (int(first) == 0):
    with open(second) as file:
        list2d = [[int(digit) for digit in line.split()] for line in file]
        vertex_n = list2d[0][0]
        print('new read array2d:', list2d)
        print('num of point', vertex_n)
        list2d.pop(0)
        B = np.array(list2d, dtype = np.int)
        print('Ma tran ke:', B)
        print('Tong so canh:', int(np.sum(B)/2))
        print('Bac cua cac dinh:',np.sum(B, axis = 0))

        #kiem tra cac tinh chat

        #output ra file o day:
        #

elif (int(first) == 1):
    with open(second) as file:
        list2d = [[int(digit) for digit in line.split()] for line in file]
        vertex_n = list2d[0][0]
        print('new read array2d:', list2d)
        print('num of point', vertex_n)
        list2d.pop(0)
        B = np.array(list2d, dtype = np.int)
        print('vallllllllll',np.sum(B, axis = 0))

def checkGraphType():
    pass

def isCompleteGraph(matrix):
    #Co n(n-1)/2 canh va moi dinh co bac: n-1
    pass

def isCGraph(matrix):
    #n>=3 va moi dinh co bac: 2
    pass

def iStarGraph(matrix):
    #co ton tai duy nhat mot dinh bac n
    #cac dinh con lai co bac 1