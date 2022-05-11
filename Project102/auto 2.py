def LaundryStore():

        print('Welcome to ABC Wash. We provide you this program to save your time !!')
        a = input('Type Y to start the process, or type N to terminate the process: ')
        if a == 'N':
            print("You have successfully closed off the program...")
        totalnumber = int(input('Enter laundry count: '))
        b = int(input('How many shirts/t-shirts: '))
        c = int(input('How many shorts/pants/trousers: '))
        d = int(input('How many undergarments - : '))
        e = int(input('How many dresses/skirts: '))
        f = int(input('Other articles of clothing: '))
       

        if a == 'Y':
            
            print("Soaking your clothes...")
            print("Adding detergent...")
            print('Washing your clothes...')
            print("Rinsing your clothes...")
            print("Drying your clothes...")

            w = b*10
            y  = c*10
            x = d*5
            z = e*20
            m = f*10
            totalcost = w+x+y+z+m
            
            print('We are charging you Rs',totalcost,' for ',totalnumber, ' pieces of clothing')
            paymethod = input("Choose your payement method NetBanking/Cash On Delivery :")
            
        if paymethod == 'NetBanking':
            i = input("Enter your account user name :")
            j = input("Enter your password :")
            k = input("Enter OTP sent to your mobile :")
            print("Thanks for the transaction!! Your delivery is on the way...")


        if paymethod == 'Cash On Delivery':
            print("Thanks for purchasing !! Your delivery is on the way !! Please pay amount on delivery ....")

LaundryStore()