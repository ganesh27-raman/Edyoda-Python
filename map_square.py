def square(n):
    return n*n
sample_list = [4, 5, 2, 9]
print("Sample List :", sample_list)
new_list = map(square, sample_list)
print("Square the elements of the list :")
print(list(new_list))