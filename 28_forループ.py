names = ['田中','鈴木','佐藤']
index = 0
for name in names:
    message = '{0}番目{1}'.format(index,name)
    print(message)
    index+=1

names = ['田中','鈴木','佐藤']
for index,name in enumerate(names):
    message = '{0}番目{1}'.format(index,name)
    print(message)
    #pythonらしい組み込み関数

foods = ['納豆','ヨーグルト','チャーハン']
juices = ['コーラ','コーヒー','カフェラテ']

for food,juice in zip(foods,juices):#zip関数は短い方にあわさってしまうのでチャーハンを消すとカフェラテも出てこなくなる
    print(food,juice)

for index in range(len(foods)):
    print(foods[index],juices[index])