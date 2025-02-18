## BankSimulator

### INTRO
- A simple app demo common bank functionality such as `account creation` and `transactions`, including account active check, balance check, and transactions validate.. as common bank operaitons.
- Read in the transactions information via `stdin`, parse to `account_creation`, and `transaction_authorization` and return the system output based on operation and business logic 
- Not use external component storage transactions/account `state`, so here I use `python dictionary` to save status `in-memory` and run operations with

- bank | src | tests
- Tech : python3, pytest 

### File strucure 

```
├── README.md
├── bank              : main class offering bank operaion (account_creation/transaction_authorization) methods 
├── data              : sample test data 
├── requirements.txt  : python dependency 
├── src               : main bank simulator app  (app.py)
└── tests             : unit tests 
```
### Quick start

<details>
<summary>Quick start</summary>

```bash
# quick start with OSX CLI 

$ pip install -r requirements.txt

$ cat data/input1.json | python src/app.py 

# {'violations': [None], 'account': {'active_card': True, 'available_limit': 100, 'account_initialized': True}}
# {'violations': [None], 'account': {'active_card': True, 'available_limit': 80, 'account_initialized': True}}
# {'violations': ['insufficient_limit'], 'account': {'active_card': True, 'available_limit': 80, 'account_initialized': True}}

$ cat data/input2.json | python src/app.py 

# {'account': {'account_initialized': True, 'active_card': True, 'available_limit': 100}, 'violations': [None]}
# {'account': {'account_initialized': True, 'active_card': True, 'available_limit': 100}, 'violations': ['account_already_initialized']}

$ cat data/input6.json | python src/app.py

# {'account': {'account_initialized': True, 'active_card': True, 'available_limit': 100}, 'violations': [None]}
# {'account': {'account_initialized': True, 'active_card': True, 'available_limit': 80}, 'violations': [None]}
# {'account': {'account_initialized': True, 'active_card': True, 'available_limit': 70}, 'violations': [None]}
# {'account': {'account_initialized': True, 'active_card': True, 'available_limit': 60}, 'violations': [None]}
# {'account': {'account_initialized': True, 'active_card': True, 'available_limit': 60}, 'violations': ['high_frequency_small_interval']}
# {'account': {'account_initialized': True, 'active_card': True, 'available_limit': 60}, 'violations': ['high_frequency_small_interval']}

$ cat data/input7.json | python src/app.py

# {'account': {'account_initialized': True, 'active_card': True, 'available_limit': 100}, 'violations': [None]}
# {'account': {'account_initialized': True, 'active_card': True, 'available_limit': 90}, 'violations': [None]}
# {'account': {'account_initialized': True, 'active_card': True, 'available_limit': 80}, 'violations': [None]}
# {'account': {'account_initialized': True, 'active_card': True, 'available_limit': 80}, 'violations': ['doubled_transaction']}

```

```bash
# quick start with docker 
$ docker build . -t app_env
$ docker run -i -t  app_env /bin/bash  -c "cat data/input1.json | python src/app.py"

```
</details>

### Run the test

<details>
<summary>Run the test</summary>

```bash
$ pytest -v tests/ 

# ============================================ test session starts ============================================
                                                                                      
# tests/unit_test.py::test_read_file_input PASSED                                                       [ 25%]
# tests/unit_test.py::test_print_status PASSED                                                          [ 50%]
# tests/unit_test.py::test_account_creation PASSED                                                      [ 75%]
# tests/unit_test.py::test_transaction_authorization PASSED                                             [100%]

# ========================================= 4 passed in 0.03 seconds ==========================================

```
</details>

## TODO

- Modify the process with asynchronous stream 
- Consider the API lost idempotency situation if crash with no state storage 
- write-ahead logging (WAL)  => commit status guarantee
- robustness
- build script, containerisation, dependencies
- maintainability
- clean code
