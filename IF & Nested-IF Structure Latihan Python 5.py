is_staff = input("Are you a staff member? (Yes/No): ")
if is_staff == "Yes":
    access_level = int(input("Enter your access level: "))

    if access_level >= 5:
        print("Access granted")
    else:
        print("Access denied: insufficient level")
else:
    print("Access denied: staff only")
