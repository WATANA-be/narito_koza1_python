num = 1

def test():
    num = 100
    print(num)
    
print(num)
test()
print(num)

print()

num = 1

def test():
    global num
    num = 100
    print(num)
    
print(num)
test()
print(num)

print()

num = [1]

def test():
    num[0]= 100
    print(num[0])
    
print(num[0])
test()
print(num[0])#この方法では変数を新しくできないので非推奨！！