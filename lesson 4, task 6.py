ident = {'11111':'1234', '22222':'2345', '33333':'3456'}
number = input('Введите номер карты: ')
if number in ident:
    for i in ident.keys():
        if i == number:
            pin = ident.get(i)
    password = input('Введите пин-код: ')
    if password == pin:
        print('Что хочешь сделать?')
        print('Проверить счет', '   ', 'Снять деньги')
    else:
        print('неверный пин-код')

else:
    print('Номер карты не найден')