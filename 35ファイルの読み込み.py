file = open('hello.txt','r',encoding='utf-8')
src = file.read()

print(src)


with open('hello.txt','r',encoding='utf-8') as file:

    src = file.read()

    print(src)


with open('hello.txt','r',encoding='utf-8') as file:
    for line in file:#開いたファイルから１行ずつ入る
        print(line,end='')#end=''で改行を防ぐ

with open('a.png','rb')as file:
    print(file.read())