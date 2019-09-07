def get_summ (one, two, delimiter = '&'):
    one = str(one)
    two = str(two)
    delimiter = str(delimiter)
    return (f'{one} {delimiter} {two}')


print (get_summ('learn', 'python'))