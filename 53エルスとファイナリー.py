'''with open('hello.txt','x',encoding='utf-8') as file:
    file.write('hellllooooo')
'''
file = None
try:
    file = open('hello.txt','x',encoding='utf-8')
except FileExistsError:
    print('ファイルが既に存在しています')
else:
    file.write('hello')
finally:
    if file is not None:
        file.close()