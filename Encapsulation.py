class banking:
  def __init__(self, name, amount):
    self.__name = name
    self.__amount = amount
  
  def setBalance(self, amt):
    self.__amount += amt
  
  def readBalance(self):
    return print(f"{self.__name} yours account balance is: {self.__amount}")
  
  def withdraw(self, amt):
    self.__amount -= amt

customer1 = banking("Mange Jay", 10000)
customer2 = banking("Avinash Shiyani", 20000)
customer3 = banking("Mohan Mange", 100000)

customer1.readBalance()
customer1.withdraw(5000)
customer1.readBalance()

customer2.readBalance()
customer2.setBalance(15000)
customer2.readBalance()

customer3.readBalance()
customer3.setBalance(150000)
customer3.withdraw(20000)
customer3.readBalance()