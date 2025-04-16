# # for i in range(1,10):
#     # print(i)


# def sayname():
#     name = str(input("Enter Your Name: "))
#     for i in range(1,10):
#         print(name)

# # sayname()
# # i = 1
# # while i<=10:
# #   if i%2==0:
# #      print("Even")
# #      i=i+1
# #   else:
# #       print(i)
# #       i=i+1


# def table():
#     num = int(input("Enter number for table: "))
#     i =1
#     while i<=10:
#         # print(num,"*",i,"=",num*i)
#         print(f"{num} X {i} = {num*i}")
#         i+=1


# res = table()
# print(res)

# for i in range(1, 11):
# print("We're on time %d" % (i))

# x=1
# while x<10:
# print("To infinity and beyond! we're getting close, on %d now!"%(x))
# x+=1

# for x in range(1, 11):
#     for y in range(1, 11):
#         print("%d * %d = %d" % (x, y, x * y))

for x in range(3):
    if x == 1:
        break

# for x in range(3):
# print(x)
# else:
# print("Final x = %d" % (x))


list_of_Lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list in list_of_Lists:
    for i in list:
        print(i)
