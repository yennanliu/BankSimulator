import argparse
import json
import sys

class BankTransaction:
    def __init__(self):
        self.active_card = False
        self.account_exist = False
        self.available_limit = None
        self.transactions = {}

    def read_std_input(self, json_file):
        with open(json_file) as json_data:
            data = json.load(json_data)
        return data 

    def account_creation(self, available_limit):
        if self.account_exist == True or self.available_limit is not None:
            return {"account": {"active_card": self.active_card, "available_limit": self.available_limit}, "violations": ["account_alread_initialized"]}
        self.active_card = True
        self.available_limit = available_limit
        return  {"account": {"active_card": self.active_card, "available_limit": self.available_limit}, "violations": []}

    def transaction_authorization(self, amount, time):
        if self.account_exist == False:
            return  {"account": {"active_card": self.active_card, "available_limit": self.available_limit}, "violations": ["account_not_initialized"]}

        if self.active_card == False:
            return  {"account": {"active_card": self.active_card, "available_limit": self.available_limit}, "violations": ["card_not_active"]}
        
        if self.available_limit - amount < 0:
            return  {"account": {"active_card": self.active_card, "available_limit": self.available_limit}, "violations": ["insufficient_limit"]}
    
         # to add : 1) 3 transactions in 2 mins 2) > 1 similar transactions in 2 mins

        return {"account": {"active_card": self.active_card, "available_limit": self.available_limit - amount}, "violations": []}

    def get_account_status(self):
        account_status = {'active_card': self.active_card,
                          'available_limit': self.available_limit,
                          'account_exist' : self.account_exist}
        print (account_status)

    def run(self, available_limit, amount, time):
        self.account_creation(available_limit)
        self.transaction_authorization(amount, time)
