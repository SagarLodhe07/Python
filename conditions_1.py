# 1. Age group Categorization
def classification():
    age = int(input("Enter your age: "))
    if age <= 12:
        print("Child")
    elif age >=13 and age <= 19:
        print("Teenager")
    elif age >= 19 and age <= 59:
        print("Adult")
    else:
        print("Senior ")

classification()