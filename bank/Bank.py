import argparse
import json
import sys

class BankTransaction:

       def __init__(self):
            self.active_card = False
            self.available_limit = 0 
            self.account_exist = False

       def read_std_input(self, json_file):
            with open(json_file) as json_data:
                data = json.load(json_data)
            return data 

        def setup_account_status(self):
            pass 

        def account_creation(self, available_limit):
            if self.account_exist == True:
                raise ValueError("account already initialized") # to fix : std output
            self.active_card = True
            self.available_limit = available_limit

        def transaction_authorization(self, amount, time):
            self.available_limit =  self.available_limi - amount
            if  (self.account_exist == False or 
                 self.active_card == False or
                 self.available_limit < 0): 
                raise ValueError("transaction failed")   # to fix : 1) 3 transactions in 2 mins 2) > 1 similar transactions in 2 mins

            print ('transaction ok')
            return {"account": {"active_card": self.active_card, 
                                "available_limit": self.available_limit}, 
                    "violations": []}

        def get_account_status(self):
            account_status = {'active_card': self.active_card,
                              'available_limit': self.available_limit,
                              'account_exist' : self.account_exist}
            print (account_status)

        def run(self):
            pass 
