# student_list = [10,20,30,40]

# sum_of_Marks = sum(student_list)
# lengh = len(student_list)
# # print(sum_of_Marks)
# average =  sum_of_Marks / 2 
# # print(average)

# def sum_function(a,b):
#     return a+b
    
# def sum_of_marks(listItem):
#     total = sum(listItem)
#     return f"The sum of {total}"
# res = sum_of_marks(student_list)
# # print(res)  
# # res = sum_function(10,15)
# print(res)

def odd_even():
    num  = int(input("Enter number to check= "))
    if num%2==0:
     print("Even")
    else:
        print("odd")
    return num
# print(odd_even())


def lines():
    line = int(input("Enter a number of lines = "))
    for i in range(0,line):
        for j in range(i+1):
            print("X",end=" ")
        print()
    
    return line

triangle = lines()
print(triangle)