# 1. Age group Categorization
def age_classification():
    age = int(input("Enter your age: "))
    if age <= 13:
        print("Child")
    # elif age >=13 and age <= 19:
    elif age < 20:
        print("Teenager")
    # elif age >= 19 and age <= 59:
    elif age < 60:
        print("Adult")
    else:
        print("Senior")


# age_classification()


def movie_ticket_princing():
    age = int(input("Enter your age: "))
    wednesday = True
    price = 12 if age >= 18 else 8
    if wednesday:
        price = price - 2
        print("Amount is: $%d" % price)
    else:
        print("Amount is: $%d" % price)

    # movie_ticket_princing()


# fruit = "Banana"
# color = "green"

# if fruit == "Banana":
#     if color == "green":
#             print("unriped")
#     elif color == "yellow":
#             print("ripe")
#     elif color == "brown":
#             print("overriped")


def transportion():
    distance = int(input("Enter Killometer: "))

    if distance < 3:
        transport = "By Walk"
    elif distance <= 15:
        transport = "By Bike"
    else:
        transport = "By Car"

    print("Transportion ", transport)


# transportion()


def password_strength():
    password = str((input("Enter your password: ")))
    password_length = len(password) # Optimized way

    # if len(password) < 6:
    if password_length < 6:
        strength = "weak"
    elif len(password) <= 10:
        strength = "Medium"
    else:
        strength = "Strong"
    print("Your password strength is ", strength)


password_strength()
