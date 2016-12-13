
# -*- coding: utf-8 -*-
import os
from collections import defaultdict

no_op = 0
score = defaultdict(int)
file_object = open(os.getcwd() + '/countLog.txt', 'w+')

def convertToDict(fname):
    with open(fname) as f:
        idfas = f.readlines()
        a =[]
        for idfa in idfas:
            idfa = idfa.strip("\n")
            a.append(idfa)
        return a

def makeScore(key):
    global score
    score[key] += 1


def searchSameLine(fname, dic):
    count = 0
    global file_object
    with open(fname) as f:
        targetLines = f.readlines()
        for targetLine in targetLines:
            targetLine = targetLine.strip("\n")
            if count % 5000 == 1:
                file_object.write(">>>>>>>>>>>>>>>>>>>>>>line:%d\n" % count)
            if targetLine in dic:
                makeScore(targetLine)


#把小文件加入dict
dict = convertToDict(os.getcwd() + "/dataset/test.idfa.csv")

#寻找大文件中命中dict的项目
searchSameLine(os.getcwd() + "/dataset/test.000000_0.0", dict)


#把相同的项目打印到结果文件中
file_object.write("2个文件中相同的行如下:\n")
for item in score:
    file_object.write(item + "\n")

file_object.close()