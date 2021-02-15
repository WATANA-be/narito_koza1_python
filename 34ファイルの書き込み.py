#書き込む内容
text = """おはよう
こんにちは
こんばんは"""

#ファイルを開き、ファイルを扱うためのオブジェクト
file = open('hello.txt','w',encoding='utf-8')

#ファイルに書き込み
file.write(text)

#ファイルを閉じる
file.close()

with open('a.png,'wb')as file:
    file.write(src)