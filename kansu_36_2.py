def check_name(name):
    if len(name)>=6:
        return True
    else:
        return False

name = input("6文字以上の名前を入力")
result = check_name(name)
if result:
    print("完了")
else:
    print("名前が短すぎます")