def is_valid_email(email):
    k, j, d = 0, 0, 0
    if len(email) >= 6:
        if email[0].isalpha():
            if email.count("@") == 1:
                if (email[-4] == "." or email[-3] == "."):
                    for i in email:
                        if i.isspace():
                            k = 1
                        elif i.isalpha():
                            if i.isupper():
                                j = 1
                        elif i.isdigit():
                            continue
                        elif i not in ["-", ".", "@", "_"]:
                            d = 1
                    if k == 1 or j == 1 or d == 1:
                        print("Wrong Email; Invalid characters or uppercase letters")
                        return False
                    else:
                        print("Right Email!")
                        return True
                else:
                    print("Wrong Email; Invalid position of dot")
            else:
                print("Wrong Email; More than one '@' symbol")
        else:
            print("Wrong Email; Email must start with an alphabetical character")
    else:
        print("Wrong Email; Length should be at least 6 characters")
        
    return False
# Ask the user to enter the email until a valid email is provided
while True:
    email = input("Enter your Email: ")
    if is_valid_email(email):
        break
