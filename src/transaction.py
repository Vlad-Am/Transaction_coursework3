class Transaction:
        '''
        Класс создаёт экземпляр банковской операции,
        который содержит в себе всю информацию
        '''

        def __init__(
                self, id, state, date, description,
                from_, to, amount, currency
        ):
            self.id = id
            self.state = state
            self.date = date
            self.description = description
            self.from_ = from_
            self.to = to
            self.amount = amount
            self.currency = currency

        def get_id(self):
            '''
            :return: id операции
            '''
            return self.id

        def get_state(self):
            '''
            :return: статус перевода
            '''
            return self.state

        def get_date(self):
            '''
            :return: дату проведения операции
            '''
            return self.date

        def get_information(self):
            '''
            Выводит информацию о переводе
            в понятном виде
            '''
            return (f"{self.date} {self.description}\n"
                    f"{self.from_} -> {self.to}\n"
                    f"{self.amount} {self.currency}\n\n"
                    )

        def __repr__(self):
            return f"операция {self.id}"