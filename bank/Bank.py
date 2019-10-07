import argparse
import json
import sys

class BankTransaction:

       def read_event(self, json_file):
        with open(json_file) as json_data:
            data = json.load(json_data)
        return data 

        def setup_account_ststus(self):
            pass 

        def account_creation(self):
            pass 

        def transaction_authorization(self):
            pass 