while True:
    balance=100000;
    print("  ATM   ");
    print(
        """
        1) balance
        2) Withdraw
        3) Deposit
        4) quit
        """

    );
    try:
        Option=int(input("enter the option.."));
    except Exception as e:
        print("error");
        continue
    if Option==1:
        print("Balance Rs: ",balance);

    elif Option==2:
        print("Balance Rs: ",balance);
        Withdraw=float(input("enter the withdrawal ammount Rs: "));
        if Withdraw>1:
            balance=(balance-Withdraw);
            print("Balance Rs: ",balance);
        elif Withdraw>balance:
            print("enter the correct amount.");
        else:
            print("None Withdrawal made.");

    elif Option==3:
        print("Balance Rs: ", balance);
        Deposit = float(input("enter the Deposit ammount Rs: "));
        if Deposit > 1:
            balance = (balance + Deposit);
            print("Balance Rs: ", balance);
        elif Deposit > balance:
            print("enter the correct amount.");
        else:
            print("None Deposit made.");
    elif Option==4:
        exit();


