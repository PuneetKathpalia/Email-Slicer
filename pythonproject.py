print()
print("=====================================")
print("|       Welcome to Email Slicer!!   |")
print("|      created by Puneet Kathpalia  |")
print("| of Lovely Professional University |")
print("|          Section: K22FG           |")
print("|         Roll No: RK22FGA27        |")
print("=====================================")
print()
while True:
    n=int(input("Press 1 to use Email Slicer and 2 to exit: "))
    print()
    if n==1:
        xyz=int(input("Enter the number of emails: "))
        for i in range(xyz):
            a=input("Enter your Email: ")
            if a[0].isalpha() or a[0].isnumeric():
                if a.endswith('.com') and "@" in a:
                    b=list(a)
                    c=b.index("@")
                    print("Username:",a[0:c],"and",end=" ")
                    domain=a[c+1:]
                    print(domain.upper())
                    print()
                else:
                    print("Invalid Email \n")
                    continue
            else:
                print("Invalid Email \n")
                continue
    else:
        print("Thank you for using Email Slicer!! \n")
        break
     