import json
import datetime

from src.transaction import Transaction


def load_file(filename):
    '''
    Функция получает расположение JSON-файла
    с банковскими операциями и
    преобразует его в python-словарь
    :param filename: расположение JSON-файла
    :return: словарь с банковскими операциями
    '''
    with open(filename, "r", encoding="UTF-8") as file:
        transactions = json.load(file)
        return transactions


def make_transactions(transactions: list):
    '''
    Функция создаёт список экземпляров класса Transactions,
    который включает в себя всю информацию о банковской операции
    :param transactions: список с банковскими операциями
    '''
    # создаем список для экземпляров класса
    transactions_list = []

    def check_wallet(where: str):
        '''
        Функция шифрует данные кошелька, в зависимости от его типа:
        Счет или Карта
        :param where: указатель положение кошелька в счете (получатель:to или отправитель:from)
        :return: зашифрованный кошелек
        '''
        # переменная кошелёк
        wallet = ""

        try:
            card = transaction[f'{where}']
            if card[:4] == "Счет":
                wallet = f"{card[:4]} **{card[-4:]}"
            else:
                wallet = f"{card[:-12]} {card[-12:-10]}** **** {card[-4:]}"
            return wallet
        except:
            return wallet

    # добавляем в пустой список экземпляры класса Transaction
    for transaction in transactions:
        try:
            operation_id = transaction["id"]
            state = transaction["state"]
            date_full = datetime.datetime.strptime(transaction["date"], "%Y-%m-%dT%H:%M:%S.%f")
            date = datetime.datetime.strftime(date_full, "%d.%m.%Y")
            description = transaction["description"]
            sender = check_wallet("from")
            receiver = check_wallet("to")
            amount = transaction["operationAmount"]["amount"]
            currency = transaction["operationAmount"]["currency"]["name"]
            transaction = Transaction(operation_id, state, date, description, sender, receiver, amount, currency)
            transactions_list.append(transaction)
        except:
            continue

    return transactions_list


def get_executed_five(transactions: list):
    '''
    Функция выводит последние 5 выполненных операций
    :param transactions: список экземпляров класса Transactions
    :return: данные с пятью последними успешными операциями
    '''
    transactions_counter = 0
    information = ''
    transactions.sort(key=lambda x: datetime.datetime.strptime(x.get_date(), "%d.%m.%Y"), reverse=True)
    for transaction in transactions:
        if transaction.state == "EXECUTED":
            transactions_counter += 1
            information += transaction.get_information()
        if transactions_counter == 5:
            break
    return information
