import os.path


def linear():
    if not os.path.isfile('linear.txt'):
        with open('linear.txt', 'w') as f:
            tmp_list = ['2', '3']
            for i in tmp_list:
                f.write(i + '\n')
    with open('linear.txt', 'r') as f:
        reading = f.read()
        reading = reading.split('\n')
        return reading


def branched():
    if not os.path.isfile('branched.txt'):
        with open('branched.txt', 'w') as f:
            tmp_list = ['5', '3', '4']
            for i in tmp_list:
                f.write(i + '\n')
    with open('branched.txt', 'r') as f:
        reading = f.read()
        reading = reading.split('\n')
        return reading


def cyclic():
    if not os.path.isfile('cyclic.txt'):
        with open('cyclic.txt', 'w') as f:
            tmp_list = ['0', '1', '5', '5']
            for i in tmp_list:
                f.write(i + '\n')
    with open('cyclic.txt', 'r') as f:
        reading = f.read()
        reading = reading.split('\n')
        return reading
