print("      Welcome times Bank")
choice=int(input(" =<<"+"1"+" Open a New Account"+">>=\n"+" "+"=<<"+"2"+" Withdraw Money"+">>=\n"+" "+"=<<"+"3"+" Deposit Money"+">>=\n"+" "+"=<<"+"4"+" check custormers and Balance"+">>=\n"+" "+"=<<"+"5"+" Exit/Quit"+">>=  :"))
if choice==1:#Account opening Section
    my_dict1 = {}
    key1="Name :"
    value1=input("Pls Enter the Name :")
    key2="Password :"
    value2=int(input("Pls Enter the Password :"))
    key3="Amount :"
    value3=int(input("Pls Enter 1st Deposit Amount :"))
    if value3>=10000:
        print("Good to go u r account will be activated soon ")
        my_dict1[key1] = value1
        my_dict1[key2] = value2
        my_dict1[key3] = value3
        print(my_dict1)
    else:
        print("Sorry the Minimum amount for account opening is 10000 ")
elif choice==2:#Withdrawal section
    my_dict2 = {}
    key1 = "Name :"
    value1 = input("Pls Enter the Name :")
    key2 = "Password :"
    value2 = int(input("Pls Enter the Password :"))
    key3 = "Withdrawal_Amount :"
    value3 = int(input("Pls Enter Withdrawal Amount :"))
    if value3 <= 2000:
        print("Good to go\n","Processing\n","Pls count the money b4 u leave ")
        my_dict2[key1] = value1
        my_dict2[key2] = value2
        my_dict2[key3] = value3
        print(my_dict2)
    else:
        print("Sorry the Withdrawal limit for this account is lessthan 2000 ")
if choice==3:
    my_dict3 = {}
    key1 = "Name :"
    value1 = input("Pls Enter the Name :")
    key2 = "Password :"
    value2 = int(input("Pls Enter the Password :"))
    key3 = "Deposit_Amount :"
    value3 = int(input("Pls Enter Deposit Amount :"))
    if value3 >= 2000:
        print("Good to go\n", "Processing\n"," Your account will be updated soon ")
        my_dict3[key1] = value1
        my_dict3[key2] = value2
        my_dict3[key3] = value3
        print(my_dict3)
    else:
        print("Sorry the minimum Deposit Amount for this account is greater than 2000 ")


if choice==4:
    my_dict4 = {}
    print("Select your Name :\n","1 ramesh \n","2 suresh \n","3 Kirsh ")
    selction=int(input("Pls enter u No of your name :"))
    if selction==1:
        print("Hi Ramesh Your Account No is 1234 :\n","And Last deposit Amount is 10000",)
        print("And Last withdrawal  amount is 5000. Total Balance is 100000 ")
    elif selction==2:
        print("Hi suresh Your Account No is 1224 :\n","And Last deposit Amount is 50000",)
        print("And Last withdrawal  amount is 10000. Total Balance is 40000 ")
    elif selction==3:
        print("Hi kirsh Your Account No is 1229 :\n", "And Last deposit Amount is 90000", )
        print("And Last withdrawal  amount is 30000. Total Balance is 600000 ")
if choice==5:
    print("Exit/Quit")

