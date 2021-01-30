#for 任意の変数名in データの集まり:
#    処理A

names = ['佐藤','鈴木','田中']
for name in names:#左から順にname変数に格納
    print(name)

my_tuple=(1,2,3)
for number in my_tuple:
    print(number)#setも渡せる

for char in 'HelloWorld':
    print(char)#文字列も渡せる

names=['佐藤','鈴木','田中']
for name2 in names:
    if char in name2:
        print(char)

band_members={"ボーカル":'佐藤','ギター':'鈴木'}
for part in band_members:#辞書をそのまま渡すとキーのみ回される
    name = band_members[part]
    message='{0}は{1}さん'.format(part,name)
    print(message)
