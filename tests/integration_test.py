import sys
sys.path.append(".")
from io import StringIO
import json
from bank.Bank import BankTransaction 

def test_bank():
    mock_stdin = [
       {
          "account":{
             "active_card":True,
             "available_limit":100
          }
       },
       {
          "transaction":{
             "merchant":"Burger King",
             "amount":20,
             "time":"2019-02-13T10:00:00.000Z"
          }
       },
       {
          "transaction":{
             "merchant":"Habbib's",
             "amount":90,
             "time":"2019-02-13T11:00:00.000Z"
          }
       }
    ]
    sys.stdin = open('data/input1.json', 'r')
    bank = BankTransaction()
    response  = bank.run()
    assert response == [{'account': {'available_limit': 80, 'account_initialized': True, 'active_card': True}, 'violations': ['insufficient_limit']}, {'account': {'available_limit': 80, 'account_initialized': True, 'active_card': True}, 'violations': ['insufficient_limit']}, {'account': {'available_limit': 80, 'account_initialized': True, 'active_card': True}, 'violations': ['insufficient_limit']}]

if __name__ == '__main__':
    pytest.main([__file__])