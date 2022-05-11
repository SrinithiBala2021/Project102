
def MedicalStore():

    print("Hello !! Welcome to XYZ MedicalStore. ")
    print("We help you to order medicines online which will help you to save your time !!")
    a = input("Please type letter S to start the program or N to close the program:")

    if a == 'N':
        print("You have successfully closed off the program...")

    if a == 'S':
        print("Beganing the proccess ...")
        print("Which category of the medicine you want ?")
        c = input("Enter the cateogry type :")
        print("Listing the medicines in category " + c +"...")
        d = input("Enter the medicine name :")
        print("Rumagging around the stock room for " + d)
        print("Found " + d + " !!")
        e =int(input("Enter the total number of peices you want :"))
        f = input("Type A if you need another medicine if not type B for bill :")
    

    if f == 'A' :
        print("Which category of the medicine you want ?")
        c = input("Enter the cateogry type :")
        print("Listing the medicines in category " + c +"...")
        d = input("Enter the medicine name :")
        print("Rumagging around the stock room for " + d)
        print("Found " + d + "!!")
        b =int(input("Enter the total number of peices you want :"))
        f = input("Type A if you need another medicine if not type B for bill :")


    if f == 'B':
        print("Caculating the total bill ...")
        n = e + b
        g = n * 50
        print("Your total bill for medicines is Rs" )
        print(g)
        h = input("Choose your payement method NetBanking/Cash On Delivery :")


    if h == 'NetBanking':
        i = input("Enter your account user name :")
        j = input("Enter your password :")
        k = input("Enter OTP sent to your mobile :")
        print("Thanks for the transaction!! Your delivery is on the way...")


    if h == 'Cash On Delivery':
        print("Thanks for purchasing !! Your delivery is on the way !! Please pay amount on delivery ....")

MedicalStore()
