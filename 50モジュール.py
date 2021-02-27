import calc


result = calc.add(1,2)#モジュール名ドット属性名
print(result)

from calc import add
result = add(1,2)
print(result)




import calc as c


result = c.add(1,3)
print(result)