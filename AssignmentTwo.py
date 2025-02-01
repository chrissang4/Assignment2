"""1. Initialize a variable to store the user's balance (e.g., starting with Ksh.1000).

2. Use a loop to repeatedly present the user with a menu of options:

   - Check balance

   - Deposit money

   - Withdraw money

   - Exit

3. Use `if-elif-else` statements to handle the user's menu choice:

   - If the user chooses to check the balance, display the current balance.

   - If the user chooses to deposit money, prompt for the amount to deposit and update the balance.

   - If the user chooses to withdraw money, prompt for the amount to withdraw and update the balance, ensuring the balance does not go negative.

   - If the user chooses to exit, terminate the loop and end the program.

4. Add comments to explain each part of the code."""
 
#  Initializing user balance
def atm_program():
    balance = 1000
   #Function displaying User's menu  
    while True:
     print("1. Check balance")
     print("2. Deposit money")
     print("3. Withdraw money")
     print("4. Exit")

   #   Get users choice
     choice =input(("\nEnter your choice (1-4): "))
   # option for checking balance
     if choice == "1":
        print(f"\nYour current balance is: {balance}")
   #2nd option for depositing amount
     elif choice == "2":
        deposit_amount = input(f"\nEnter amount to deposit: ")

      #  checks if the input consists only of digits
        if deposit_amount.isdigit():
           deposit_amount = float(deposit_amount)
           if deposit_amount > 0:
              balance += deposit_amount
              print(f"\nDeposit of ksh{deposit_amount} was successful. New balance: is ksh {balance}")
           else :
              print(f"Invalid amount.")
        else :
           print(f"Invalid number. Please Enter a valid number")
 # Option 3 withdraw money
     elif choice == "3":
        withdraw_amount = input(f"\nEnter amount to withdraw: ")
        if withdraw_amount.isdigit():
           withdraw_amount = float(withdraw_amount)
           if withdraw_amount > 0:
              if withdraw_amount <= balance:
                 balance -= withdraw_amount
                 print(f"Ksh.{withdraw_amount} withdrawn successfully. New balance is ksh {balance}")
              else :
                 print("You have insufficient funds")
           else :
              print("Invalid amount.")
        else :
           print("Enter a valid number: ")
   #   Option 4 Exit ATM Program
     elif choice == "4":
        print("\nThank you for using ATM services.")
     else :
        print("Invalid selection")
        break
# Running the ATM program
atm_program()
# # if __name__ == "__main__":
#    atm_program()

      
        



            

              
              


           
           
           
              



        
        
           
        
    





    
