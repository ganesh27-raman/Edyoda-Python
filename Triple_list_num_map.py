def triple_num(n):
    return n*3
list_num = [1, 2, 3, 4, 5, 6, 7]
print("Sample List :", list_num)
new_list = map(triple_num, list_num)
print("Triple of list numbers:")
print(list(new_list))