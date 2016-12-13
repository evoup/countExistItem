统计2个文件中相同的项目的行数示范代码


#把小文件加入dict
dict = convertToDict(os.getcwd() + "/dataset/test.idfa.csv")

#寻找大文件中命中dict的项目
searchSameLine(os.getcwd() + "/dataset/test.000000_0.0", dict)

根据需要自己选择对应的dataset下的文件,目前取了约1000行用来测试

返回结果
查看运行后生成的countLog.txt文件
--------------------------------------

2个文件中相同的行如下:

00000471-6EAA-48A3-9EB0-806E32CE40CA

00000417-8BFB-4931-584E-29FA207153C3
