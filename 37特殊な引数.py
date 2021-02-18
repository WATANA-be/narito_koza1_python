#my_dict.get('キー','見つかりません(これがない場合none)')

def hello(name='匿名'):
    print(name)

hello()
hello('なめこ')


def hello(text,name='匿名'):
    print(name,text)

hello('こんにちは')
hello('こんばんは','なめこ')
print()
hello(text='こんにちは')
hello(text='こんばんは',name='なめこ')

print()
hello('こんにちは')
hello('こんばんは',name='なめこ')


def hello(*args):
    print(args)
hello()
hello('こんにちは')
hello('こんばんは','なりと','ハロー')


def hello(*args,**kwargs):
    print(args,kwargs)
hello()
hello('こんにちは',a=1)
hello('こんばんは','なりと','ハロー',a=1,b=2,c=3)

def hello(text,*,name='なりと'):
    print(text,name)

hello('こんにちは')
hello('こんにちは',name='太郎')