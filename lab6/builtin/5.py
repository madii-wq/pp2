def all_elements_true(tup):
    return all(tup)

my_tuple = (True, True, True)
print(all_elements_true(my_tuple))

my_tuple = (True, False, True)
print(all_elements_true(my_tuple))
