#式A and 式B →　式Aと式Bが共にTrueならばTrue
#式A or 式B → 式Aと式Bが共にTrueならばTrue
#not 式 A → 式AがFalseならばTrue

numbers = [1,2,3,4,5]
if 1 in numbers and 2 in numbers:
    print('1と2が含まれています')

numbers = [1,2,3,4,5]
if 1 in numbers or 100 in numbers:
    print('1か100が含まれています')
elif not 200 in numbers:
    print("200は含まれていません")

elif numbers:
    print("未入力なのにTrue")

#Falseと評価されるオブジェクト
#空文字列"" 空タプル()　空リスト[] 空辞書{} 空セット set() 整数の0　浮動小数点数の0.0
#False None

names = ['佐藤','吉田','鈴木']
if len(names) != 0:
    print(names[0])

names = ['佐藤','吉田','鈴木']
if names:
    print(names[0])
else:
    print("空でした")

