# class animal(object):
#     def run(self):
#         print("animal is running")
#
# class dog(animal):
#     def run(self):
#         print("dog is running")
#
# class cat (animal):
#     def run(self):
#         print("cat is running")
#
# def run_twice(animal):
#     animal.run()
#     animal.run()
#
# run_twice(dog())
# run_twice(cat())
# list = []
# i = 2
# for i in range(2, 101):
#     j = 2
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         list.append(i)
# print(list)
# list1 = [2, 5, 6, 9, 20]
# for i in range(len(list1)):
#     for j in range(len(list1)-i-1):
#         if list1[j] < list1[j+1]:
#             temp = list1[j]
#             list1[j] = list1[j+1]
#             list1[j+1] = temp
# print(list1)
# 九九乘法口诀
# for i in range(1,10):
#     for j in range(1, i+1):
#         print("{0}x{1}={2}".format(i, j, i*j), end=' ')
#     print()
# import os
# path = "G:/MyStudy/Python/test"
# for file1, file2, file3 in os.walk(path):
#     print(file3)
# import cv2
# vc = cv2.VideoCapture("G:/MyStudy/Python/1.mp4")
# rate = 50
# i = 0
# rval = vc.isOpened()
# while rval:
#     rval, frame = vc.read()
#     i += 1
#     if (i % rate == 0):
#         cv2.imwrite("G:/MyStudy/Python/images/"+str(i)+".jpg", frame)
# vc.release()
# list1 = [1, 2, 3, 3, 4, 4]
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# knights1 = {'b': '1', 'a': '2'}
# knights2 = sorted(knights1.items(),key= lambda i : i[0],reverse= False)
# print(knights2)
# dict1 = {"name": "zs", "age": 18, "city": "深圳", "tel": "1362626627"}
# data = sorted(dict1.items(), key=lambda i: i[0], reverse=False)
# print(data)
# # for i ,k in knights.items():
#     print(i, k)
# import numpy as np
# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])
#水平组合
# print(np.hstack((a, b)))
#垂直组合
#print(np.vstack((a, b)))
#深度组合
# print(np.dstack((a, b)))
# import time
# import requests
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.find_element_by_id("kw").send_keys("selenium2")
# time.sleep(1)
# driver.find_element_by_id("su").click()

# #关闭游标和数据库的连接
# cursor.close()
# db.close()
from collections import Counter
str = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
res = Counter(str)
print(res)
