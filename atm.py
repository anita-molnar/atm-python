print("Welcome to your local ATM")
attempts = 3
user_pin = "3456" # I used as a string as avoiding an input crash
account_balance = 6000

while attempts >0:
    pin = input("Please enter your 4-digit PIN number: ")
 
    if pin != user_pin:
        attempts -= 1
        print(f"Wrong PIN number, you have {attempts} attempts left")             

        #check if attempts reached 0 and break the loop
        if attempts ==0:
            print("Your card has been blocked!")
            break 
    else:    
        print(f"Your available balance is £{account_balance}")
        while True:
            user_withdraw = int(input("Enter the amount you would like to withdraw in £10, £20, £50, £100, other amount: "))
            if user_withdraw <= account_balance:
                account_balance -= user_withdraw
                print(f"£{user_withdraw} have been withrawn from you account")
                print(f"Your new balance is £{account_balance}")
                print("Thanks for using this ATM, see you again!")
                exit()
            else:
                print("Insufficient balance, enter a valid amount")
                continue