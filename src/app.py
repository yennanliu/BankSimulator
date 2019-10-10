import sys
sys.path.append(".")
from bank.Bank import BankTransaction 

if __name__ == '__main__':
    bank = BankTransaction()
    bank.run() 