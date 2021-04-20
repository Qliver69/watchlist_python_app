try:
    retry = input('Do you want to retry ? (y/n)  ').upper()
    for i in range(10):
        if retry == str(i):
            raise TypeError
    if len(retry) != 1:
        raise ValueError
    assert retry == 'Y' or retry == 'N'
except ValueError:
    print('Error: more than one character')
except TypeError:
    print('Error: number instead of letter')
except AssertionError:
    print('Error: the character is not y or n')