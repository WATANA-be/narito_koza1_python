def hello():
    print("こんにちは")

hello()


def hello(name2):
    message = '{0}さん　ヤッホー'.format(name2)
    print(message)

hello('あああ')


def check_name(namedayo):
    if len(namedayo)>=6:
        return True
    else:
        return False

namedayo = input('名前を入力：')
result = check_name(namedayo)

if result:
    print('登録完了')
else:
    print('名前が短いです')