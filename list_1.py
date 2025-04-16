my_list = []
my_list2 = list()
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# print(fruits.count("apple")) 
# print(fruits.index("apple"))
fruits.append("Mango") 
fruits.reverse()
fruits.remove("kiwi")
# print(fruits)

squares = []
for x in range(10):
    squares.append(x**2)
# print(squares)
squares_two = list(map(lambda x:x**2,range(10)))
# print(squares_two)
squares_three = [x**4 for x in range(10)]
print(squares_three)
