import pytest
from zad6 import BankAccount

def test_initial_balance():
    account = BankAccount()
    assert account.get_balance() == 0

    account_with_balance = BankAccount(100)
    assert account_with_balance.get_balance() == 100

def test_deposit():
    account = BankAccount()
    account.deposit(100)
    assert account.get_balance() == 100

    with pytest.raises(ValueError):
        account.deposit(-50)

    with pytest.raises(ValueError):
        account.deposit(0)

def test_withdraw():
    account = BankAccount(100)
    account.withdraw(50)
    assert account.get_balance() == 50

    with pytest.raises(ValueError):
        account.withdraw(-50)

    with pytest.raises(ValueError):
        account.withdraw(0)

    with pytest.raises(ValueError):
        account.withdraw(100)

def test_insufficient_funds():
    account = BankAccount(50)
    with pytest.raises(ValueError):
        account.withdraw(100)

def test_deposit_withdraw_combination():
    account = BankAccount()
    account.deposit(100)
    account.withdraw(50)
    assert account.get_balance() == 50

    account.deposit(200)
    assert account.get_balance() == 250

    account.withdraw(100)
    assert account.get_balance() == 150
