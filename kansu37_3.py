def hello(*args,**kwargs):
    print(args,kwargs)

hello()
hello("こんにちは",a=1)
hello("こんばんは","なりと","ハロー",a=1,b=2,c=3)