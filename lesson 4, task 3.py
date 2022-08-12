list_nambers = [-1, -2, -3, -4, -5, -6, -7, -8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
result_list = []
for i in list_nambers:
    if i%3==0 and i>0 and i%4!=0:
        result_list.append(i)

print(result_list)