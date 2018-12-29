# Initializing blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Return the last value of the current blockchain """
    return blockchain[-1]


def add_value(value, last_transaction=[1]):
    """
    Append a new value.
    Arguments:
        :value: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1]).
    """
    blockchain.append([last_transaction, value])


def get_user_input():
    """ Return input for users """
    return float(input('Your transaction amount please: '))


tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(value=tx_amount, last_transaction=get_last_blockchain_value())

tx_amount = get_user_input()
add_value(value=tx_amount, last_transaction=get_last_blockchain_value())

print(blockchain)
