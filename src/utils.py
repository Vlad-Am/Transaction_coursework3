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
        operations = json.load(file)
        return operations


def make_operations(operations: list):
    '''
    Функция создаёт список экземпляров класса Operations,
    который включает в себя всю информацию о банковской операции
    :param operations: список с банковскими операциями
    '''
    # создаем список для экземпляров класса
    operations_list = []

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
            card = inf[f'{where}']
            if card[:4] == "Счет":
                wallet = f"{card[:4]} **{card[-4:]}"
            else:
                wallet = f"{card[:-12]} {card[-12:-10]}** **** {card[-4:]}"
            return wallet
        except:
            return wallet

    for inf in operations:
        try:
            operation_id = inf["id"]
            state = inf["state"]
            date_full = datetime.datetime.strptime(inf["date"], "%Y-%m-%dT%H:%M:%S.%f")
            date = datetime.datetime.strftime(date_full, "%d.%m.%Y")
            description = inf["description"]
            sender = check_wallet("from")
            receiver = check_wallet("to")
            amount = inf["operationAmount"]["amount"]
            currency = inf["operationAmount"]["currency"]["name"]
            operation = Transaction(operation_id, state, date, description, sender, receiver, amount, currency)
            operations_list.append(operation)
        except:
            continue
    return operations_list


def get_all_operations(operations: list):
    '''
    Функция выводит все сортированные по дате операции
    :param operations: список экземпляров класса Operations
    :return: данные со всеми отсортированными операциями
    '''
    information = ''
    operations.sort(key=lambda x: datetime.datetime.strptime(x.get_date(), "%d.%m.%Y"), reverse=True)
    for operation in operations:
        information += operation.get_information()
    return information


def get_executed_five(operations: list):
    '''
    Функция выводит последние 5 выполенных операций
    :param operations: список экземпляров класса Operations
    :return: данные с пятью последними успешными операциями
    '''
    operations_counter = 0
    information = ''
    operations.sort(key=lambda x: datetime.datetime.strptime(x.get_date(), "%d.%m.%Y"), reverse=True)
    for operation in operations:
        if operation.state == "EXECUTED":
            operations_counter += 1
            information += operation.get_information()
        if operations_counter == 5:
            break
    return information
