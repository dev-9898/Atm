def Atm():
    Balance=0

    while True:
        print("\n---Atm Menu---")
        print("1.Check Balance")
        print("2.Depostit")
        print("3.Withdraw")
        print("4.Exit")

        Choice=int(input("Enter Your Choise:"))
        match Choice:
            case 1:
                print("Your Balance is:",Balance)
            case 2:
                amount =int(input("Enter Your Amount:"))
                Balance +=amount
                print("Amount Depostied Successfully")
            case 3:
                amount =int(input("Enter Your Amount:"))
                if amount <= Balance:
                    Balance -=amount
                    print("please Collect your cash")
                else:
                    print("Insufficient balance")
            case 4:
                print("Thank you for using ATM")
                break
            case _:
                print("Invalid Choise")
Atm()