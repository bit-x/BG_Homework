name = input('mame= ')
surname = input('surmame= ')
age = int(input('age= '))
weight = int(input('weight= '))
if age < 30 and weight > 50 and weight < 120:
    print('хорошее состояние')
elif (age > 30 and age <= 40) and (weight < 50 or weight > 120):
    print('следует заняться собой')
elif age > 40 and (weight < 50 or weight > 120):
    print('следует обратится к врачу!')
else:
    print('ХЗ, мы тут не врачи')