class Atm: #declaring class
    def __init__(self,Cash_Withdrawal,Balance_Enquiry,Cash_Deposit): #declaring constructor
        
        
            self.Cash_Withdrawal=input("Enter the amount of cash you want to withdraw from your savings account:")
            self.Balance_Enquiry=input("Enter 1 to check your bank balance:")
            self.Cash_Deposit=input("Enter the amount of cash you want to deposit to your savings account:")    


    def func():
      x= int(input())
  while (x>1):
    if x%2 == 0:
      x = x//2
      print(x)
    elif x%2 != 0:
      x= x*3+1
      print(x)

func()