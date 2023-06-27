import os.path


def array_from_file():
    if not os.path.isfile('array_from_file.txt'):
        with open('array_from_file.txt', 'w') as f:
            tmp_list = ['14', '12', '23', '13', '19', '9', '17', '25', '0', '11']
            for i in tmp_list:
                f.write(i + ' ')
    with open('array_from_file.txt', 'r') as f:
        reading = f.read()
        reading = reading.split()
        for i in range(len(reading)):
            reading[i] = float(reading[i])
        return reading