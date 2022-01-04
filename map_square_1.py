#Using map and Lambda
sam_list = [4, 5, 2, 9]

new_list = map(lambda x: x**2, sam_list)
print("Square the element of the list :\n",list(new_list))