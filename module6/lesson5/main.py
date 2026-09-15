# Abstraction : Abstraction means hiding complicated data and only showing the important parts . 
import random
# class ATM : 
#     def dispense(self ,  withdrawal_cash):
#         self._accountname()
#         self._amount(withdrawal_cash)
#         print(f"Withdrawal cash = {withdrawal_cash}")
#     def start_machine(self):
#         print("Machine started . ")
#     def _amount(self , withdrawal_cash):
#         print("Counting and dispensing notes")
#     def _accountname(self):
#         print(f"Account number is {random.random()} . ")
# firstcustomer = ATM().dispense(500)
# Abstract Class : Abstract class is like a blueprint or a rulebook .
# from abc import ABC , abstractmethod
# class abc_blueprint(ABC):
#     @abstractmethod
#     def withdrawal(self , amount):
#         pass
#     @abstractmethod
#     def check_balance(self):
#         pass
# class SBI(abc_blueprint):
#     def withdrawal(self, amount):
#         print(f"ATM is dispensing {amount}")
#     def check_balance(self):
#         print(f"Your balance is {random.random()} . ")
# obj = SBI().withdrawal(900)
# Polymorphism : Polymorphism means the same action can behave differently depending upon which object does it . 
class Laptop : 
    def OS(self , os_name):
        print(f"Running on this OS : {os_name}")
class Apple(Laptop):
    def OS(self , os_name):
        print(f"Running Apple on OS : {os_name}")
class Microsoft(Laptop):
    def OS(self , os_name):
        print(f"Running Microsoft on OS : {os_name}")
obj1  = Apple().OS("MacOS")
obj2 = Microsoft().OS("Windows 11")
# Polymorphism without inheritance : 