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
    print ('json_file :', json_file)
    assert json_file == expected_output  

if __name__ == '__main__':
    pytest.main([__file__])