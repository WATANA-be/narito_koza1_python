table = [[]for y in range(1,10)]
print(table)

table = [[x*y for x in range(1,10)]for y in range(1,10)]
print(table)

table = [[0 for x in range(5)]for y in range(5)]
print(table)

table = [[None for x in range(5)]for y in range(5)]
print(table)

sets = [x for x in range(10)]
print(sets)

dicts = {x:'デフォルト値'for x in range(10)}
print(dicts)

score = {'math':29,'eng':48}
new_score = {value:key for key,value in score.items()}
print(score)
print()
print(new_score)

numbers = [1,3,4,5,6,3]
squqare_gen = (num**2 for num in numbers)
for num in square_gen:
    print(num)

numbers = [1,3,4,5,6,3]
squqare_gen = (num**2 for num in numbers)
for num in square_gen:
    print(num)