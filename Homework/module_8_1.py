def add_everything_up(num_1, num_2):
    try:
        return num_1 + num_2
    except:
        return f'{num_1}{num_2}'


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
