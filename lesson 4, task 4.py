import re
email_pattern = '[a-z1-9_]+@[a-z]+\.(ru|com|org)'
name_pattern = '([А-Я][а-я]{2,}\b)'
email = 'bitxzq@gmail.com'
name = 'Сергей'
# print(re.match(email_pattern, email).group(0))

if re.match(email_pattern, email) == None:
    print('email Err')
else:
    print('email ok')

if re.match(name_pattern, name) == None:
    print('name Err')
else:
    print('name ok')
