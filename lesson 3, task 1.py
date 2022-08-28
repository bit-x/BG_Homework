# def my_city(name, age, city):
#     print (name + ',', age,'год(а),','проживает в городе '+ city)
#
# name = 'Василий'
# age = 21
# city = 'Москва'
# my_city(name, age, city)



# for name, maney in zip(name, maney):
#     print(name,maney)
# a = (dict(zip(name, maney)))


# name = ['alex', 'jim', 'jon']
# maney = [200, 300, 400]
# a = (dict(zip(name, maney)))
# f = open('1.txt', 'w')
# for d, e in a.items():
#     f.write('{} - {}\n'.format(d,e))
# f.close()


a = []
b = []
c = []
d = []
e = []
f = open('1.txt')
for line in f:
    a.append(line.split())
f.close()
for i in a:
    for j in i:
        b.append(j)

for i in b:
    if i == '-':
        b.remove(i)

for j in b:
    for i in j:
        if i == '1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0':
            j = float(j)
            j = j- (j / 100 * 13)
            j = round(j)
            break
    c.append(j)
for i in c:
    if type(i) == str:
        d.append(i.upper())
    else:
        e.append(i)
a = (dict(zip(d, e)))
print(a)
for i, j in a.items():
    if j<500000:
        print(i)
        print(j)