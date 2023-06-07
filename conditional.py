# temp = eval(input("input temp:"))
# if temp < 0:
#     print("wrong input")
# else:
#     if temp > 50:
#         x = temp/2
#         print(x)
#     else:
#         print("number is less than 50")

#Boolean operations
user = "Admin"
logged_in = False

# #You can replace and with or
# if user == "Admin" and logged_in:
#     print("Admin page")
# else:
#     print("wrong credentials")

if not logged_in:
    print("Please log_in")
else:
    print("Welcome")