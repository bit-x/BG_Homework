# fruit = ["яблоко", "банан", "киви", "арбуз"]
# # fruit = fruit.format()
# # lenfruit = len(fruit)
# right_ofset = len(max(fruit, key=len))
# for i, j in enumerate(fruit, start=1):
#     # print (i, j.format(j.rjust(right_ofset)))
#     print ('{}. {}' .format(i, j.rjust(right_ofset)))


# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [5, 6, 7, 8, 9, 10]
# # print(type(list1))
# a = set(list1)
# b = set(list2)
# list1 = (a-b)
# print (list(list1))
# # for b in list2:
# #     while b in list1:
# #         list1.remove(b)
# # print(list1)

# list1 = [1, 10, 8, 4, 5, 6]
# list2=[]
# for i in list1:
#      # print(i)
#      if i%2!=1:
#          list2.append(i/4)
#      else:
#          list2.append(i*2)
# print(list2)

# list_a = [2, -5, 8, 9, -25, 25, 4]
# # list_a = [4, 16, 25, 36, 49, 64, 81]
# list_b = []
#
# for i in list_a:
#     if i>=0:
#         b = i ** (0.5)
#         if b == int(b):
#             list_b.append(int(b))
# print(list_b)
# mounths = ('', 'yan', 'fev','mart','april', 'may', 'июня', 'июля', 'august', 'sep', 'okt', 'nove','dec')
# days = ('', 'первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое', 'одинадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое', 'семнадцатое')
# dayt = '02.07.2022'
# dey, mount, year = dayt.split('.')
# dey = int(dey)
# mount = int(mount)
# year = int(year)
# print(days[dey], mounths[mount], year, 'года')

# import random
#
# list_a = []
# n = int(input())
# for i in range(n):
#     list_a.append(random.randint(-100, 100))
# print(list_a)

# lst_1 = [1, 2, 4, 5, 6, 2, 5, 2]
# lst_1 = set(lst_1)
# print(list(lst_1))

import math

# a = [1, 2, 4, 5, 6, 2, 5, 2]
# second_a = list()
# for elem in a:
#     if a.coutn(elem) == 1:
#         second_a.append(elem)
# print(second_a)

dayt = '12.13.2022'
day, mount, yer = dayt.split('.')
day = int(day)
mount = int(mount)
yer = int(yer)
if 0 < day <= 31:
    if 0 < mount <= 12:
        if 0 < yer < 10000:
            print('yes')
else:
    print('no')