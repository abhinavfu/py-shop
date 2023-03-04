import re
print("Working")
fname = "Abhinav"
lname = "Anand"
email = "as@g.c"
password = "asDa12"
repassword = "asDa12"

if(email != "sd"):
    if(password == repassword):
        if(40 >= len(password) >= 8):
            print(
                "Password must contains atleast a numbers, digits, letter, uppercase letter")
            # add more authenticate

        elif(40 < len(password)):
            print("Password must be between 8 to 40 characters")
        else:
            print("Password must be more than 8 characters")
    else:
        print("Password does not match")
else:
    print("Email Id already exsits")

# Regular Expressions
z = input("enter password : ")
x = re.findall("[A-Z]", z)
print(x)
y = re.findall("\d", z)
print(y)
if len(y) >= 1 and len(x) >= 1:
    print("Password is strong")
elif len(y) >= 1 and len(x) == 0:
    print("Enter atleast one Uppercase char")
elif len(y) == 0 and len(x) >= 1:
    print("Enter atleast one digit char")
else:
    print("Enter atleast one digit char and one uppercase char")
