import utils


def main():
    transaction_list = utils.load_file("../json-files/transaction.json")
    transaction = utils.make_transactions(transaction_list)
    print(utils.get_executed_five(transaction))


if __name__ == "__main__":
    main()
