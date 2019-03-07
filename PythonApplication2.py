from sys import argv
import numpy as np
script, option_arg, input_arg, output_arg = argv

#cac function
def tinhToanGhiFile(fileName, maTranKe):
    output_file = open(fileName, "wt")
    #Tinh tong so canh
    tong_so_canh = int(np.sum(maTranKe)/2)
    output_file.write(str(tong_so_canh))
    output_file.write('\n')

    #Tinh bac cua cac dinh
    bac_cua_cac_dinh = np.sum(maTranKe, axis = 0)
    for bac in bac_cua_cac_dinh:
        output_file.write("%s " % bac)
    output_file.write('\n')

    #kiem tra cac tinh chat
    graphType = 0
    n = len(maTranKe)
    listBacCacDinh = bac_cua_cac_dinh.tolist()
    kGraphCondition = (tong_so_canh == (n*(n-1))/2) and (listBacCacDinh.count(n-1) == n)
    cGraphCondition = (n >= 3) and (listBacCacDinh.count(2) == n)
    starGraphCondition = (listBacCacDinh.count(n-1) == 1) and (listBacCacDinh.count(1) == n-1)
    if kGraphCondition:
        graphType = 1
    elif cGraphCondition:
        graphType = 2
    elif starGraphCondition:
        graphType = 3
    output_file.write("%s" % graphType)

#doc tap tin chua danh sach ke va tra ve ma tran ke
def docTapTinDanhSachKe(inputFile):
    with open(inputFile) as file:
        danhSachKe = [[int(digit) for digit in line.split()] for line in file]
        print('danhsachKe:', danhSachKe)
        soDinh = danhSachKe[0][0]
        soCanh = danhSachKe[0][1]
        print('soDinh:', soDinh)
        print('soCanh:', soCanh)
        danhSachKe.pop(0)
        maTranKe = np.zeros(shape=(soDinh, soDinh), dtype = np.int)
        
        for dinh in danhSachKe:
            maTranKe[dinh[0]][dinh[1]] += 1
            maTranKe[dinh[1]][dinh[0]] += 1
        print('maTranKe:', maTranKe)
        return maTranKe




#first la so 0 hoac 1
if (int(option_arg) == 1):
    print('Truong hop ma tran ke!!!!!!!!!!')
    with open(input_arg) as file:
        list2d = [[int(digit) for digit in line.split()] for line in file]
        vertex_n = list2d[0][0]
        print('new read array2d:', list2d)
        print('num of point', vertex_n)
        list2d.pop(0)
        B = np.array(list2d, dtype = np.int)
        print('Ma tran ke:', B)
        tinhToanGhiFile(output_arg, B)

elif (int(option_arg) == 0):
    print('Truong hop danh sach ke!!!!!!!!!!')
    maTranKe = docTapTinDanhSachKe(input_arg)
    tinhToanGhiFile(output_arg, maTranKe)