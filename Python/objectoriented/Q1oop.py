# CREATE ACCOUNT CLASS WITH 2 ATTRINUTES - BALENCE AND ACCOUNT NO .CREATE METHOD FOR DEBIT ,CREDIT AND PRINTING THE BALENCE .



class Account:
  def __init__(self,balence,account_no):
    self.balence=balence
    self.account_no=account_no


  def Debit(self,amount):
    self.balence-=amount
    print("Rs.",amount,"Was debited")
    print("Total balence=",self.fetch_balence())


  def Credit(self,amount):
    self.balence+=amount
    print("RS.",amount,"was credited")
    print("Total balence=",self.fetch_balence())

  def fetch_balence(self):
      return self.balence

acc=Account(20000,98765) 
# print(acc.balence)  
# print(acc.account_no)  
acc.Debit(5000)
acc.Credit(2000)
