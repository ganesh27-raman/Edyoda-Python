def reverse_string(string):
    r_string = ''
    index = len(string)
    while index > 0:
        r_string += string[ index - 1 ]
        index = index - 1
    return r_string
print(reverse_string('1234abcd'))