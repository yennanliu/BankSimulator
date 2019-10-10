import argparse
import json
import sys

class BankTransaction:
    def __init__(self):
        self.active_card = False
        self.account_initialized = False
        self.available_limit = None
        self.violations = None
        self.transactions = {}
        self.status =  {"account": {"active_card": self.active_card, "account_initialized": self.account_initialized, "available_limit": self.available_limit}, "violations": [self.violations]}

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
        print (self.status)
        return self.status
    
    def account_creation(self, available_limit):
        if self.status['account']['active_card'] == True:
            self.status['account']['violations'] = "account_already_initialized"
            print(self.status)
            return self.status
        self.status['account']['active_card'] = True
        self.status['account']['account_initialized'] = True
        self.status['account']['available_limit'] = available_limit
        print(self.status)
        return self.status


    def transaction_authorization(self, amount, time):
        if self.status['account']['active_card'] == False:
            self.status['account']['violations'] = "account_not_initialized"
            print(self.status)
            return self.status

        
        elif self.status['account']['available_limit'] - amount < 0:
            self.status['account']['violations']  = "insufficient_limit"
            print(self.status)
            return self.status
    
        # to add : 1) 3 transactions in 2 mins 2) > 1 similar transactions in 2 mins
        else:
            self.status['account']['available_limit'] = self.status['account']['available_limit'] - amount
            print(self.status)
            return self.status

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
