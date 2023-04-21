import pytest
from account import *


class TestAccount:
    def setup_method(self):
        self.p1 = Account('Fred')
        self.p2 = Account('Joel')

    def teardown_method(self):
        del self.p1
        del self.p2

    def test_init(self):
        assert self.p1.get_name() == 'Fred'
        assert self.p2.get_name() == 'Joel'
        assert self.p1.get_balance() == 0
        assert self.p2.get_balance() == 0

    def test_deposit(self):
        assert self.p1.deposit(300.49)
        assert self.p2.deposit(2873.04)
        assert self.p1.get_balance() == 300.49
        assert self.p2.get_balance() == 2873.04
        assert not self.p1.deposit(0)
        assert not self.p2.deposit(-400.78)

    def test_withdraw(self):
        self.p1.deposit(300.49)
        self.p2.deposit(2873.04)
        assert self.p1.withdraw(200.43)
        assert self.p1.get_balance() == 100.06
        assert not self.p2.withdraw(-107.32)
        assert not self.p1.withdraw(476.59)
