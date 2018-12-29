# Initializing blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Return the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(value, last_transaction=[1]):
    """
    Append a new value.
    Arguments:
        :value: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1]).
    """
    if last_transaction is None:
        last_transaction = [1]
    blockchain.append([last_transaction, value])


def get_transaction_value():
    """ Return input for users """
    return float(input('Your transaction amount please: '))


def get_user_choice():
    return input("Your choice: ")


def print_blockchain_elements():
    """ Output the blockchain list to the console """
    for block in blockchain:
        print('Outputting block')
        print(block)
    else:
        print('-' * 20)


def verify_chain():
    """" Verify if last value is equal next value """
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        if blockchain[block_index][0] == blockchain[block_index - 1]:
           is_valid = True
        else:
           is_valid = False
           break
    # for block in blockchain:
    #     if block_index == 0:
    #         block_index += 1
    #         continue
    #     if block[0] == blockchain[block_index - 1]:
    #        is_valid = True
    #     else:
    #        is_valid = False
    #        break
    return is_valid


waiting_for_input = True

# REPL
while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Wrong condition!')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        break
else:
    print('User left!')
