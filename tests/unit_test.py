import sys
sys.path.append(".")
from bank.Bank import BankTransaction 


def test_read_file_input():
    """
    test Json2NestedJson.read_file_input method 
    """
    expected_output = [
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
    bank = BankTransaction()
    json_file = bank._read_file_input('data/input1.json')
    assert json_file == expected_output  

def test_print_status():
    bank = BankTransaction()
    expected_result = bank._print_status() 
    assert expected_result == {"account": {"active_card": False, "account_initialized": False,"available_limit": None }, "violations": [None]}

def test_account_creation():
    bank = BankTransaction()
    expected_result = bank.account_creation(available_limit=100)
    assert expected_result == {"account": {"active_card": True,"account_initialized": True, "available_limit": 100 }, "violations": [None]}

def test_transaction_authorization():
    bank = BankTransaction()
    expected_result = bank.transaction_authorization(merchant ='my_merchant', amount=100, time="2019-02-13T10:00:00.000Z")
    assert expected_result == {"account": {"active_card": False,"account_initialized": False, "available_limit": None }, "violations": ["card_not_active"]}

if __name__ == '__main__':
    pytest.main([__file__])
