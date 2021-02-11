numbers = [1,5,6,11,3,5,7,3]
squares = []
for num in numbers:
    squares.append(num**2)
print(squares)

#リスト内包表記だと以下の通り
numbers2 = [1,4,3,444,2]
squares2 = [num2**2 for num2 in numbers2]
print(squares2)

words = ['python','django','tkinter']
upper_words = [word.upper()for word in words]
print(upper_words)

one_words = [char for word in words for char in word]
print(one_words)

even_numbers = [x for x in range(1,11)if x%2==0]
print(even_numbers)