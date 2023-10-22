import src
from src import transaction
from src import utils


def test_get_executed_five():
    transaction_list = utils.load_file("transaction.json")
    transaction = utils.make_transactions(transaction_list)
    assert utils.get_executed_five(transaction) == "08.12.2019 Открытие вклада\n" \
                                                   " -> Счет **5907\n" \
                                                   "41096.24 USD\n\n" \
                                                   "07.12.2019 Перевод организации\n" \
                                                   "Visa Classic 2842 87** **** 9012 -> Счет **3655\n" \
                                                   "48150.39 USD\n\n" \
                                                   "19.11.2019 Перевод организации\n" \
                                                   "Maestro 7810 84** **** 5568 -> Счет **2869\n" \
                                                   "30153.72 руб.\n\n" \
                                                   "13.11.2019 Перевод со счета на счет\n" \
                                                   "Счет **9794 -> Счет **8125\n" \
                                                   "62814.53 руб.\n\n" \
                                                   "05.11.2019 Открытие вклада\n" \
                                                   " -> Счет **8381\n" \
                                                   "21344.35 руб.\n\n"


def test_make_transactions():
    transaction_list_1 = utils.load_file("transaction.json")
    for objective in utils.make_transactions(transaction_list_1):
        assert type(objective) is src.transaction.Transaction

    transaction_list = utils.load_file("transaction_for_test.json")
    assert str(utils.make_transactions(transaction_list)[0]) == "операция 441945886"
    assert str(utils.make_transactions(transaction_list)[1]) == "операция 873106923"
    assert utils.make_transactions(transaction_list)[0].get_id() == 441945886
    assert utils.make_transactions(transaction_list)[0].get_date() == "26.08.2019"
    assert utils.make_transactions(transaction_list)[0].get_state() == "EXECUTED"
    assert utils.make_transactions(transaction_list)[0].get_information() == "26.08.2019 Перевод организации\n" \
                                                                             "Maestro 1596 83** **** 5199 -> Счет **9589\n" \
                                                                             "31957.58 руб.\n\n"


def test_load_file():
    assert type(utils.load_file("transaction.json")) is list
