email = input("Enter Your Email : ") #gmail@gmail.com
k,j,d = 0,0,0
if len(email) >= 6:
    if email[0].isalpha():
        pass
        if ('@' in email) and (email.count('@') == 1):
            if(email[-4] == '.') ^ (email[-3] == '.'):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == '_' or i == '@' or i == '.':
                        continue
                    else:
                        d = 1
                if k==1 or j == 1 or d == 1:
                    print("Codition 5 wrong.")
                else:
                    print("This is Right Email.")
            else:
                print("Condition 4 wrong")
        else:
            print("Condition 3 wrong.")
    else:
        print("Condition 2 wrong.")
else:
    print("Condition 1 wrong.")
#   output : 
# Enter Your Email : arjun@vssut.ac.in
# This is Right Email.
