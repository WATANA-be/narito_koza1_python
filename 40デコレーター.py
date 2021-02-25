def debug(function):
    def _debug(*args,**kwargs):
    #本来の関数を呼び出し結果を受け取る
        result = function(*args,**kwargs)
        #本来の関数名と引数、結果を出力
        print(function.__name__,args,kwargs,result)
        #関数の実行結果を返す
        return result
    return_debug

@debug
def say_hello():
    print('hello')
say_hello()
