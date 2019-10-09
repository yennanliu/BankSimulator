import argparse
import json
import sys

class BankTransaction:
    def __init__(self):
        self.active_card = False
        self.account_exist = False
        self.available_limit = None
        self.violations = None
        self.transactions = {}

    def _read_file_input(self, json_file):
        with open(json_file) as json_data:
            data = json.load(json_data)
        return data 

    def _read_stdin_input(self):
        input_data = ''
        for line in sys.stdin.readlines():
            input_data += line 
        # transform string to json for following process 
        return json.loads(input_data)

    def _print_status(self):
        print ({"account": {"active_card": self.active_card, "available_limit": self.available_limit}, "violations": [self.violations]})

    def account_creation(self, available_limit):
        if self.account_exist == True or self.available_limit is not None:
            self.violations = "account_already_initialized"
            self._print_status()
            #return {"account": {"active_card": self.active_card, "available_limit": self.available_limit}, "violations": ["account_alread_initialized"]}
        self.active_card = True
        self.account_exist = True
        self.available_limit = available_limit
        self._print_status()

    def transaction_authorization(self, amount, time):
        if self.account_exist == False:
            self.violations = "account_not_initialized"
            self._print_status()
            #return  {"account": {"active_card": self.active_card, "available_limit": self.available_limit}, "violations": ["account_not_initialized"]}

        elif self.active_card == False:
            self.violations = "card_not_active"
            self._print_status()
        
        elif self.available_limit - amount < 0:
            self.violations = "insufficient_limit"
            self._print_status()
    
        # to add : 1) 3 transactions in 2 mins 2) > 1 similar transactions in 2 mins
        else:
            self.available_limit = self.available_limit - amount
            self._print_status()

    def run(self):
        std_input = self._read_stdin_input()
        for i in range(len(std_input)):
            op_name = list(std_input[i])[0]
            if op_name == 'account':
                available_limit = std_input[i]['account']['available_limit']
                self.account_creation(available_limit)
            elif op_name == 'transaction':
                amount = std_input[i]['transaction']['amount']
                time = std_input[i]['transaction']['time']
                self.transaction_authorization(amount, time)
            else:
                raise KeyError("No such transaction type")  
