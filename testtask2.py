quest = int(input('Сколько будет строк? '))
gls = sgl = 0
vse_gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
count = 0
while quest > count:
    ls=gl=0
    poem = input()
    for i in poem:
        if i.isalpha():
            if i in vse_gls:
                ls += 1
            else:
                gl += 1
    # print('Кол-во гласных:', ls,'Кол-во согласных:', gl)
    gls+=ls
    sgl+=gl
    count += 1

print('Кол-во гласных во всем тексте:', gls,'Кол-во согласных во всем тексте:', sgl)